<template>
  <div
    style="
      width: 98.5vw;
      height: 94.7vh;
      position: absolute;
      top:0px;
      text-align: center;
      left: 0px;
    "
  >
    <!-- <v-btn
      @click="Tutorial = !Tutorial"
      text
      style="
        position: absolute;
        top: 2vh;
        left: 1vw;
        height: 5vh;
        font-size: 2vh;
        width: 8vw;
        background: yellow;
      "
      >게임조작법</v-btn
    > -->
    <vue-p5 @setup="setup" @draw="draw" ></vue-p5>

     <v-btn
      id="gameStart"
      style="
        position: absolute;
        bottom: 0vh;
        margin-bottom: 0vh;
        left:0px;
        height: 10.7vh;
        width: 25vw;
        font-size: 5.5vh;
        border-radius: 0px;
      "
      ><span style="font-family: CookieRun-Bold;  ">게임시작</span></v-btn
    >

    <v-btn
      id="poseSave"
      style="
        position: absolute;
        bottom: 0vh;
        margin-bottom: 0vh;
        left:25vw;
        height: 10.7vh;
        width: 25vw;
        font-size: 5.5vh;
        border-radius: 0px;
      "
      ><span style="font-family: CookieRun-Bold;  ">점프화면캡처</span></v-btn
    >
    <v-btn
      id="noPoseSave"
      style="
        position: absolute;
        bottom: 0vh;
        margin-bottom: 0vh;
        left:50vw;
        height: 10.7vh;
        width: 25vw;
        font-size: 5.5vh;
        border-radius: 0px;
      "
      ><span style="font-family: CookieRun-Bold; ">런닝화면캡처</span></v-btn
    >

    <v-btn
      id="poseTrain"
      style="
        position: absolute;
        bottom: 0vh;
        margin-bottom: 0vh;
        left:75vw;
        height: 10.7vh;
        width: 25vw;
        font-size: 5.5vh;
        border-radius: 0px;
      "
      ><span style="font-family: CookieRun-Bold;  ">포즈학습</span></v-btn
    >

    <GameFinishModal @close="closeModal" v-if="modal">
      <!-- default 슬롯 콘텐츠 -->
      <p
        style="font-size: 17vh; color: white; font-weight: 500; margin-top: 7vh"
      >
        Game Over
      </p>
      <!-- /default -->
      <!-- /footer -->
      <template slot="footer" style="background-color: rgba(0, 0, 0, 1)">
        <button
          @click="doClose"
          style="
            background-color: red;
            height: 8vh;
            border-radius: 12px;
            width: 10vw;
            font-size: 4vh;
            font-weight: 600;
            color: yellow;
            margin-left: 10px;
            margin-right: 10px;
          "
        >
          다시시작
        </button>
        <button
          @click="doReTrain"
          style="
            background-color: red;
            height: 8vh;
            border-radius: 12px;
            width: 13vw;
            font-size: 4vh;
            font-weight: 600;
            color: yellow;
            margin-left: 10px;
            margin-right: 10px;
          "
        >
          다시학습하기
        </button>
      </template>
    </GameFinishModal>
    <JumpGameTutorial @close="doCloseTutorial" v-if="Tutorial">
      <p style="font-size: 7vh; color: black; font-weight: 800">게임조작법</p>
      <hooper style="margin-top: -3vh">
        <slide></slide>
        <slide></slide>
        <slide></slide>
        <slide></slide>
        <slide></slide>
        <slide></slide>

        <hooper-pagination slot="hooper-addons"></hooper-pagination>
      </hooper>

      <template slot="footer" style="background-color: rgba(0, 0, 0, 1)">
        <button
          @click="doCloseTutorial"
          style="
            background-color: red;
            border-radius: 12px;
            width: 10vw;
            font-size: 4vh;
            font-weight: 600;
            color: yellow;
          "
        >
          닫기
        </button>
      </template>
    </JumpGameTutorial>

    <Loading v-if="loading"></Loading>
  </div>
</template>

<script>
import VueP5 from "vue-p5";

// import p5_dom from "./p5_dom_min";
// import p5_sound from "./p5_sound_min";
import ml5 from "ml5";
import { Jumper } from "../../api/game/running/Jumper";
import { Train } from "../../api/game/running/Train";
// import JumpGameTutorial from "./JumpGameTutorial";
import GameFinishModal from "./GameFinishModal";
import Loading from "./loding";
import { Hooper, Slide, Pagination as HooperPagination } from "hooper";
import "../../assets/hooper.css";
import $ from "jquery";
export default {
  name: "JumpGame",
  data: function () {
    return {
      sketchObj: null,
      classifier: {},
      mobilenet: null,
      video: null,
      label: "",

      score: null,
      scroll: 15,
      scrollBg: 0,
      trains: [],
      unicorn: null,
      failsounds: [],
      restart: false,
      video: null,
      canvas: null,
      videoCanvas: null,
      canvasWidth: 1150,
      canvasHeight: 800,
      videoWidth: 1130,
      videoHeight: 800,
      countDown : 5,

      // preload
      music: null,
      ding: null,
      whistle: null,
      bg: null,
      train: null,
      jumper: null,

      // posenet
      featureExtractor: null,
      classifier: null,
      targetLabel: "jump",
      classificationResult: null,

      // js File
      unicorn: null,
      key: null,

      // train
      brain: null,
      poseSave: null,
      noPoseSave: null,
      trainButton: null,
      state: "waiting",
      jumpPoseCollecting: false,
      NojumpPoseCollecting : false,
      reCollecting : false,
      // game
      modal: false,
      score: 0,
      loading: false,
      Tutorial: false,
      gameStart: false,
      firstStart: true,

      confidence: null,

      //
      removeCanvas: false,
    };
  },
  components: {
    "vue-p5": VueP5,
    Hooper,
    Slide,
    HooperPagination,
    GameFinishModal,
    Loading,
    // JumpGameTutorial,
  },
  methods: {
    setup(sketch) {
      var that = this;
      this.sketchObj = sketch;
      sketch.createCanvas(
        this.canvasWidth + this.videoWidth,
        this.canvasHeight
      );
      this.train = sketch.createImg(
        "http://www.memozee.com/FILES/047/jinsuk.729.%ED%8F%AC%EC%BC%93%EB%AA%AC.jpg"
      );
      this.bg = sketch.createImg(
        "https://cdn.hipwallpaper.com/m/34/80/7xuaw6.jpg"
      );
      this.jumper = sketch.createImg(
        "https://user-images.githubusercontent.com/53737175/94951811-e6d86b00-051f-11eb-9edf-92b2f185bf9d.png"
      );
      this.train.hide();
      this.bg.hide();
      this.jumper.hide();

      this.unicorn = new Jumper(sketch, sketch.height, this.jumper);
      this.video = sketch.createCapture(sketch.VIDEO);
      this.video.hide();
      this.video.size(this.videoWidth, this.videoHeight);

      this.featureExtractor = ml5.featureExtractor(
        "MobileNet",
        this.modelLoaded
      );

      const options = { numLabels: 2 };
      this.classifier = this.featureExtractor.classification(
        this.video,
        options
      );

      this.setupButton(sketch);

      $("#defaultCanvas0").parent().css({
        width: "98.4vw",
        "text-align": "center",
        position: "absolute",
        top: "0px",
        left: 0,
      });

      $("#defaultCanvas0").css({ width: "98.9vw", height: "84vh" });
    },

    modelLoaded() {
      console.log("MobileNet loaded!");
    },

    videoReady() {
      console.log("webcam load... finished");
    },

    gotResults(err, result) {
      var that = this;
      if (err) {
        console.error(err);
      } else {
        that.label = result[0].label;
        that.confidence = result[0].confidence;
        that.classifier.classify(that.gotResults);
      }
    },

    setupButton(sketch) {
      var that = this;
      // left button
      // this.poseSave = sketch.select("#poseSave");
      // this.poseSave.mousePressed(function () {
      //   setTimeout(function () {
      //     that.classifier.addImage("jump");
      //     that.jumpPoseCollecting = true;

      //     setTimeout(function () {
      //       that.jumpPoseCollecting = false;
      //       console.log("점프사진 수집완료");
      //     }, 5000);
      //   }, 100);
      // });

      // this.noPoseSave = sketch.select("#noPoseSave");
      // this.noPoseSave.mousePressed(function () {
      // setTimeout(function () {
      //     that.classifier.addImage("noJump");
      //     that.NojumpPoseCollecting = true;

      //     setTimeout(function () {
      //       that.NojumpPoseCollecting = false;
      //       console.log("슬라이드사진 수집완료");
      //     }, 5000);
      //   }, 100);
      // });

      this.gameStart = sketch.select("#gameStart");
      this.gameStart.mousePressed(function () {
        that.gameState = true;
      });

      // // train button
      // this.trainButton = sketch.select("#poseTrain");
      // this.trainButton.mousePressed(function () {
      //   that.classifier.train(that.whileTraining);
      // });
    },
    finished(loss) {
      console.log("학습");
    },

    whileTraining(loss) {
      var that = this;

      if (loss == null) {
        that.classifier.classify(that.gotResults);
        // console.log(that.gotResults);
      } else {
        console.log(loss);
      }
    },
    restartGame() {
      if (this.restart) {
        this.restart = false;
        this.score = 0;
        this.scrollBg = 0;
        this.scroll = 15;
        this.trains = [];
        this.gameState = true;
        // this.sketchObj.loop();
      }
    },
    jump(sketch) {
      // if (this.restart) {
      //   this.restart = false;
      //   this.score = 0;
      //   this.scrollBg = 0;
      //   this.scroll = 10;
      //   this.trains = [];
      //   this.sketchObj.loop();
      // }
      if (event.key == " ") {
        this.unicorn.jump();
        return false;
      }
    },
    draw(sketch) {
      var that = this;

      if (this.confidence >= 0.99 && this.label == "jump") {
        this.unicorn.jump();
      }

      sketch.image(this.bg, -this.scrollBg, 0, this.canvasWidth, sketch.height);
      sketch.translate(this.canvasWidth * 2 + this.videoWidth, 0);
      sketch.scale(-1, 1);
      sketch.image(
        this.video,
        this.canvasWidth,
        0,
        this.videoWidth,
        sketch.height
      );

      sketch.translate(this.canvasWidth * 2 + this.videoWidth, 0);
      sketch.scale(-1, 1);
      if (this.jumpPoseCollecting == true) {
        sketch.textSize(80);
        sketch.textStyle(sketch.BOLD);
        sketch.fill(255, 0, 0);
        sketch.text("점프사진 수집중", 1450, 100);
      }

      if (this.NojumpPoseCollecting == true) {
        sketch.textSize(80);
        sketch.textStyle(sketch.BOLD);
        sketch.fill(255, 0, 0);
        sketch.text("슬라이드사진 수집중", 1350, 100);
      }

      if (this.gameState) {
        sketch.image(
          this.bg,
          -this.scrollBg + sketch.width,
          0,
          sketch.width,
          sketch.height
        );

        if (this.scrollBg > sketch.width) {
          this.scrollBg = 0;
        }

        if (sketch.random(1) < 0.75 && sketch.frameCount % 70 == 0) {
          this.trains.push(
            new Train(
              sketch,
              this.train,
              this.canvasWidth,
              sketch.height,
              this.scroll
            )
          );
        }

        if (sketch.frameCount % 5 == 0) {
          this.score++;
        }

        sketch.fill(255);
        sketch.textStyle(sketch.NORMAL);
        sketch.textSize(60);
        sketch.textFont("monospace");
        sketch.text(`Score: ${this.score}`, 15, 60);

        for (const t of this.trains) {
          t.move();
          t.show();

          if (this.unicorn.collide(t)) {
            // sketch.noLoop();
            // music.stop();
            // let sound = sketch.random(failSounds);
            // sound.play();

            that.modal = true;
            that.restart = true;
            that.gameState = false;
          }
        }

        this.unicorn.show();
        this.unicorn.move();
      }
    },
    closeModal() {
      this.modal = false;
    },
    CloseTutorial() {
      this.Tutorial = false;
    },

    doClose() {
      this.score = 0;
      this.closeModal();

      this.restartGame();
    },

    doReTrain() {
      this.closeModal();
      this.restart = false;
      this.score = 0;
      this.scrollBg = 0;
      this.scroll = 15;
      this.trains = [];
      this.gameState = false;

    },

    doCloseTutorial() {
      this.Tutorial = false;
      this.gameStart = true;
      // if (this.firstStart == true) {
      //   this.countDownTimer();
      // }
      this.firstStart = false;
    },

    countDownTimer() {
      if (this.countDown > 0) {
        setTimeout(() => {
          this.countDown -= 1;
          this.countDownTimer();
        }, 1000);
      }
    },
  },

  created() {
    // this.Tutorial = true;
    window.addEventListener("keydown", this.jump);
  },
  destroyed(){
    console.log("끄기");
  }
};
</script>

<style>
#defaultCanvas0 {
  display: inline-block;
}
</style>

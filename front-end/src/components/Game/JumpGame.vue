<template>
  <div
    style="
      width: 98.5vw;
      height: 94.7vh;
      position: absolute;
      top: 0px;
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
    <vue-p5 @setup="setup" @draw="draw"> </vue-p5>

    <v-btn
      id="gameStart"
      style="
        position: absolute;
        bottom: 0vh;
        margin-bottom: 0vh;
        left: 0px;
        height: 10.7vh;
        width: 25vw;
        font-size: 5vh;
        border-radius: 0px;
      "
      ><span style="font-family: CookieRun-Bold">게임시작</span></v-btn
    >

    <v-btn
      id="poseSave"
      style="
        position: absolute;
        bottom: 0vh;
        margin-bottom: 0vh;
        left: 25vw;
        height: 10.7vh;
        width: 25vw;
        font-size: 5vh;
        border-radius: 0px;
      "
      ><span style="font-family: CookieRun-Bold">점프화면캡처</span></v-btn
    >
    <v-btn
      id="noPoseSave"
      style="
        position: absolute;
        bottom: 0vh;
        margin-bottom: 0vh;
        left: 50vw;
        height: 10.7vh;
        width: 25vw;
        font-size: 5vh;
        border-radius: 0px;
      "
      ><span style="font-family: CookieRun-Bold">런닝화면캡처</span></v-btn
    >

    <v-btn
      id="poseTrain"
      style="
        position: absolute;
        bottom: 0vh;
        margin-bottom: 0vh;
        left: 75vw;
        height: 10.7vh;
        width: 25vw;
        font-size: 5vh;
        border-radius: 0px;
      "
      ><span style="font-family: CookieRun-Bold">포즈학습</span></v-btn
    >

    <GameFinishModal @close="closeModal" v-if="modal">
      <!-- default 슬롯 콘텐츠 -->
      <p
        style="
          font-size: 17vh;
          color: white;
          font-weight: 500;
          margin-top: 20vh;
        "
      >
        Game Over
      </p>
      <!-- /default -->
      <!-- /footer -->
      <template slot="footer" style="background-color: rgba(0, 0, 0, 1)">
        <button
          @click="
            doClose();
            sendGameData();
            reStartTime();
          "
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
    <!-- <JumpGameTutorial @close="doCloseTutorial" v-if="Tutorial">
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
    </JumpGameTutorial> -->

    <Loading v-if="loading"></Loading>
    <GameLevelModal v-if="levelChange">
      <p style="font-size: 15vh; color: black; font-weight: 800; color: yellow">
        {{ level }}
      </p>
    </GameLevelModal>
  </div>
</template>

<script>
import SERVER from "@/api/server.js";
import axios from "axios";

import VueP5 from "vue-p5";
import ml5 from "ml5";
import { Jumper } from "../../api/game/running/Jumper";
import { Train } from "../../api/game/running/Train";
import GameLevelModal from "./GameLevelModal";
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
      scroll: 13,
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
      countDown: 5,
      
      // record
      start_time: null,
      end_time: null,
      game_score: 0,

      // preload
      music: null,
      ding: null,
      whistle: null,
      bg: null,
      obstacle: null,
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
      NojumpPoseCollecting: false,
      reCollecting: false,
      // game
      modal: false,
      score: 0,
      loading: false,
      Tutorial: false,
      gameStart: false,
      firstStart: true,

      confidence: null,

      levelChange: false,
      removeCanvas: false,
      sound: null,
      jumpGameBGM: null,
      jumpSound : null,
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
    GameLevelModal,
  },
  methods: {
    setup(sketch) {
      var that = this;
      this.sketchObj = sketch;

      // this.p5.prototype.soundFormats('./Jump.mp3','./Jump.ogg');

      // var sound = this.p5.prototype.loadSound('./Jump.mp3');
      // var sound = p5.prototype.loadSound(['./Jump.mp3', './Jump.ogg'])
      sketch.createCanvas(
        this.canvasWidth + this.videoWidth,
        this.canvasHeight
      );

      this.obstacle = sketch.createImg(
        "https://user-images.githubusercontent.com/53737175/95007583-4d5aa780-064c-11eb-84b5-676cb9fc7ac1.png"
      );
      this.bg = sketch.createImg(
        "https://cdn.hipwallpaper.com/m/34/80/7xuaw6.jpg"
      );
      this.jumper = sketch.createImg(
        "https://user-images.githubusercontent.com/53737175/94998253-79920c00-05eb-11eb-814f-99ae41ccc470.png"
      );
      this.obstacle.hide();
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
      this.poseSave = sketch.select("#poseSave");
      this.poseSave.mousePressed(function () {
        for (var i = 0; i < 80; i++) {
          setTimeout(function () {
            that.classifier.addImage("jump");
            that.jumpPoseCollecting = true;
            console.log("점프사진 수집중");
          }, 10 * (i + 1));
        }
        setTimeout(function () {
          that.jumpPoseCollecting = false;
          console.log("점프사진 수집완료");
        }, 3000);
      });

      this.noPoseSave = sketch.select("#noPoseSave");
      this.noPoseSave.mousePressed(function () {
        // setTimeout(function () {
        //     that.classifier.addImage("noJump");
        //     that.NojumpPoseCollecting = true;

        //     setTimeout(function () {
        //       that.NojumpPoseCollecting = false;
        //       console.log("슬라이드사진 수집완료");
        //     }, 5000);
        //   }, 100);

        for (var i = 0; i < 60; i++) {
          setTimeout(function () {
            that.classifier.addImage("noJump");
            that.NojumpPoseCollecting = true;
            console.log("런닝사진 수집중");
          }, 10 * (i + 1));
        }
        setTimeout(function () {
          that.NojumpPoseCollecting = false;
          console.log("런닝사진 수집완료");
        }, 3000);
      });

      this.gameStart = sketch.select("#gameStart");
      this.gameStart.mousePressed(function () {
        that.gameState = true;
        that.start_time = that.timeNow();
      });

      // train button
      this.trainButton = sketch.select("#poseTrain");
      this.trainButton.mousePressed(function () {
        that.classifier.train(that.whileTraining);
      });
    },
    finished(loss) {
      console.log("학습");
    },

    whileTraining(loss) {
      var that = this;

      if (loss == null) {
        that.classifier.classify(that.gotResults);
        console.log("학습이 완료 되었습니다.");
      } else {
        console.log(loss);
      }
    },
    restartGame() {
      if (this.restart) {
        this.restart = false;
        this.score = 0;
        this.scrollBg = 0;
        this.scroll = 13;
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
        this.jumpSound = new Audio(require("../../assets/sound/Jump.mp3")); // path to file
        this.jumpSound.play();
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
        sketch.text("런닝사진 수집중", 1350, 100);
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
              this.obstacle,
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
        sketch.textSize(85);
        sketch.textFont("monospace");
        sketch.text(`Score: ${this.score}`, 15, 80);

        if (this.score == 500) {
            that.scroll = 18;
            that.level = "Level 2";
            that.levelChange = true;
            setTimeout(function () {
              that.levelChange = false;
          }, 600);
        }
        else if(this.score == 1000){
            that.scroll = 24;
            that.level = "Level 3";
            that.levelChange = true;
            setTimeout(function () {
              that.levelChange = false;
          }, 600);
        }

        for (const t of this.trains) {
          t.move();
          t.show();

          if (this.unicorn.collide(t)) {
            // sketch.noLoop();
            // music.stop();
            // let sound = sketch.random(failSounds);
            // sound.play();

            this.end_time = this.timeNow();
            this.game_score = this.score;
            this.modal = true;
            this.restart = true;
            this.gameState = false;
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
    timeNow() {
      var date = new Date().toISOString();
      var time = new Date().toString("ko-KR");
      return date.slice(0, 10) + " " + time.slice(16, 24);
    },
    reStartTime() {
      this.start_time = this.timeNow();
    },
    sendGameData() {
      const gameData = {
        userId: this.$store.state.userStore.userInfo.userid,
        gameNo: this.$route.query.gameNo,
        startTime: this.start_time,
        endTime: this.end_time,
        gameScore: this.game_score,
      };
      console.log(gameData)
      axios
        .post(
          SERVER.URL +
            `games/${this.$route.query.gameNo}/records/users/${this.$store.state.userStore.userInfo.userid}/`,
          gameData,
          {
            headers: { Authorization: `JWT ${this.$store.state.accessToken}` },
          }
        )
        .then((res) => {
          if (res.status === 201) {
            console.log("데이터가 생성되었습니다.");
          } else {
            console.log("201말고 뭐가 오지?");
          }
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    // this.Tutorial = true;
    window.addEventListener("keydown", this.jump);
    this.jumpGameBGM = new Audio(require("../../assets/sound/JumpGameBGM.mp3")); // path to file
    this.jumpGameBGM.volume = 0.2;
    // this.jumpGameBGM.muted =true;
    this.jumpGameBGM.loop = true;
    this.jumpGameBGM.autoplay =true;
    this.jumpGameBGM.play();
  },
  mounted(){
    // this.jumpGameBGM = new Audio(require("../../assets/sound/JumpGameBGM.mp3")); // path to file
    // this.jumpGameBGM.volume = 0.2;
    // this.jumpGameBGM.loop = true;


    console.log(this.jumpGameBGM);

  },


  destroyed() {
    let stream = this.video.elt.srcObject
    stream.getTracks()[0].stop()
    console.log("끄기");
    this.jumpGameBGM.pause();
    
    this.jumpGameBGM = null;
    this.jumpSound = null;
    // this.$forceUpdate();
  },
};
</script>

<style>
#defaultCanvas0 {
  display: inline-block;
}
</style>

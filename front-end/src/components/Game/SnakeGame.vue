<template>
  <div style="width: 100vw; height: 85vh; text-align: center">
    <v-btn
      @click="Tutorial = !Tutorial"
      text
      style="
        position: absolute;
        left: 1vw;
        height: 7vh;
        width: 8vw;
        background: yellow;
      "
    >
      <p style="font-weight: 1000; font-size: 2.5vh; margin-top: 2vh">
        게임조작법
      </p>
    </v-btn>
    <p style="font-size: 5vh; font-weight: 700">스네이크 게임</p>
    <vue-p5 @setup="setup" @draw="draw"></vue-p5>

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
          "
        >
          다시시작
        </button>
      </template>
    </GameFinishModal>

    <SnakeGameTutorial @close="doCloseTutorial" v-if="Tutorial">
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
    </SnakeGameTutorial>
    <Loading v-if="loading"></Loading>
  </div>
</template>

<script>
import VueP5 from "vue-p5";
import ml5 from "ml5";
import $ from "jquery";
import GameFinishModal from "./GameFinishModal";
import { Snake } from "../../api/game/snake/snake";
import SnakeGameTutorial from "./SnakeGameTutorial";
import { Hooper, Slide, Pagination as HooperPagination } from "hooper";
import Loading from "./loding";
import "../../assets/hooper.css";
export default {
  name: "SnakeGame",
  data: function () {
    return {
      poseNet: null,
      video: null,
      pose: null,
      skeleton: null,
      label: "",

      train: null,

      s: null,
      scl: 20,
      food: null,
      foodx: null,
      foody: null,

      snakeCanvasWidth: 400,
      snakeCanvasHeight: 400,
      height: 400,
      videoWidth: 600,
      videoHeight: 400,

      upPosition_x: 250,
      upPosition_y: 80,
      downPosition_x: 250,
      downPosition_y: 220,
      leftPosition_x: 350,
      leftPosition_y: 150,
      rightPosition_x: 150,
      rightPosition_y: 150,

      leftBuffer: null,
      rightBuffer: null,

      //컴포넌트 관련
      modal: false,
      Tutorial: false,
      loading: false,
      gameStart: false,
      firstStart: true,
      gamestatus: false,

      countDown: 20,
      score: 0,
    };
  },
  components: {
    "vue-p5": VueP5,
    GameFinishModal,
    SnakeGameTutorial,
    Loading,
    Hooper,
    Slide,
    HooperPagination,
  },
  methods: {
    setup(sketch) {
      this.sketch = sketch;
      sketch.createCanvas(this.snakeCanvasWidth + this.videoWidth, this.height);

      this.leftBuffer = sketch.createGraphics(
        this.snakeCanvasWidth,
        this.height
      );
      this.rightBuffer = sketch.createGraphics(this.videoWidth, this.height);

      this.video = sketch.createCapture(sketch.VIDEO);
      this.video.size(this.videoWidth, this.videoHeight);
      this.video.hide();

      this.poseNet = ml5.poseNet(this.video, this.modelReady());
      var that = this;
      this.poseNet.on("pose", function (results) {
        if (results.length > 0) {
          that.pose = results[0].pose;
          that.skeleton = results[0].skeleton;
        }
      });

      sketch.background(0);

      this.s = new Snake(
        sketch,
        this.scl,
        this.snakeCanvasWidth,
        this.height,
        this.food
      );

      this.pickLocation(sketch);
      //game code ends

      $("#defaultCanvas0").parent().css({
        width: "100%",
        "text-align": "center",
        position: "absolute",
        left: "1vw",
        top: "12vh",
      });
      $("#defaultCanvas0").css({ width: "85vw", height: "75vh" });
    },

    modelReady() {
      console.log("Model Loaded");
    },
    videoReady() {
      console.log("webcam load... finished");
    },

    countDownTimer() {
      if (this.countDown > 0) {
        setTimeout(() => {
          this.countDown -= 1;
          this.countDownTimer();
        }, 1000);
      }
    },

    pickLocation(sketch) {
      var cols = sketch.floor(this.snakeCanvasWidth / this.scl);
      var rows = sketch.floor(this.snakeCanvasHeight / this.scl);
      this.food = sketch.createVector(
        sketch.floor(sketch.random(cols)),
        sketch.floor(sketch.random(rows))
      );
      this.foodx = this.food.x;
      this.foody = this.food.y;
      //food.mult(scl);
    },
    draw(sketch) {
      sketch.background(0);
      sketch.fill(255);

      this.drawSnake(sketch);
      this.drawVideo(sketch);
      // Paint the off-screen buffers onto the main canvas
      sketch.translate(this.snakeCanvasWidth * 2 + this.videoWidth, 0);
      sketch.scale(-1, 1);
      sketch.image(this.leftBuffer, 0, 0);
      sketch.image(this.rightBuffer, this.snakeCanvasWidth, 0);
    },
    drawSnake(sketch) {
      var that = this;
      if (sketch.frameCount % 20 == 0) {
        this.s.update(sketch);
      }
      this.s.show(sketch);

      if (this.s.eat(this.food)) {
        that.score += 100;
        that.countDown = 20;
        that.pickLocation(sketch);
      }
      //snake
      sketch.fill(255, 0, 100);
      sketch.rect(20 * this.foodx, 20 * this.foody, this.scl, this.scl);

      if (this.label == "top") this.s.dir(0, -1);
      else if (this.label == "down") this.s.dir(0, 1);
      else if (this.label == "left") this.s.dir(-1, 0);
      else if (this.label == "right") this.s.dir(1, 0);
    },

    drawVideo(sketch) {
      this.rightBuffer.image(
        this.video,
        0,
        0,
        this.videoWidth,
        this.videoHeight
      );

      this.rightBuffer.fill(255, 0, 255);
      this.rightBuffer.rect(250, 80, 50, 50);
      this.rightBuffer.textSize(40);
      this.rightBuffer.translate(this.videoWidth, 0);
      this.rightBuffer.scale(-1, 1);
      this.rightBuffer.textStyle(this.rightBuffer.NORMAL);
      this.rightBuffer.fill(255, 255, 255);
      this.rightBuffer.text("상", 305, 120);

      this.rightBuffer.fill(255, 0, 255);
      this.rightBuffer.rect(300, 220, 50, 50);
      this.rightBuffer.textSize(40);
      this.rightBuffer.textStyle(this.rightBuffer.NORMAL);
      this.rightBuffer.fill(255, 255, 255);
      this.rightBuffer.text("하", 305, 260);

      this.rightBuffer.fill(255, 0, 255);
      this.rightBuffer.rect(200, 150, 50, 50);
      this.rightBuffer.textSize(40);
      this.rightBuffer.textStyle(this.rightBuffer.NORMAL);
      this.rightBuffer.fill(255, 255, 255);
      this.rightBuffer.text("좌", 205, 190);

      this.rightBuffer.fill(255, 0, 255);
      this.rightBuffer.rect(400, 150, 50, 50);
      this.rightBuffer.textSize(40);
      this.rightBuffer.textStyle(this.rightBuffer.NORMAL);
      this.rightBuffer.fill(255, 255, 255);
      this.rightBuffer.text("우", 405, 190);

      this.rightBuffer.translate(this.videoWidth, 0);
      this.rightBuffer.scale(-1, 1);

      var that = this;
      if (this.pose != null && this.gamestatus == true) {
        this.loading = false;
        // if (this.pose != null && this.gamestatus == true) {
        //점수판
        this.rightBuffer.translate(this.videoWidth, 0);
        this.rightBuffer.scale(-1, 1);
        this.rightBuffer.textSize(30);
        this.rightBuffer.textStyle(sketch.BOLD);
        this.rightBuffer.fill(255, 0, 0);
        this.rightBuffer.text("점수 : " + this.score, 30, 40);

        //카운트 다운
        this.rightBuffer.textSize(50);
        this.rightBuffer.textStyle(this.rightBuffer.NORMAL);
        this.rightBuffer.fill(0, 255, 255);
        this.rightBuffer.text(this.countDown, 280, 50);

        if (this.countDown == 0) {
          this.modal = true;
          this.score = 0;
          this.gamestatus = false;
        }

        this.rightBuffer.translate(this.videoWidth, 0);
        this.rightBuffer.scale(-1, 1);

        if (this.pose.score > 0.2 && this.pose != null) {
          let eyeR = that.pose.rightEye;
          let eyeL = that.pose.leftEye;
          let d = this.rightBuffer.dist(eyeR.x, eyeR.y, eyeL.x, eyeL.y);
          this.rightBuffer.fill(255, 0, 0);
          this.rightBuffer.ellipse(that.pose.nose.x, that.pose.nose.y, d - 25);
          this.rightBuffer.fill(0, 0, 255);

          if (
            (that.pose.nose.x > that.upPosition_x &&
              that.pose.nose.x < that.upPosition_x + 50 &&
              that.pose.nose.y > that.upPosition_y &&
              that.pose.nose.y < that.upPosition_y + 50) ||
            (that.pose.nose.x > that.upPosition_x &&
              that.pose.nose.x < that.upPosition_x + 50 &&
              that.pose.nose.y > that.upPosition_y &&
              that.pose.nose.y < that.upPosition_y + 50)
          ) {
            this.label = "top";
          } else if (
            (that.pose.nose.x > that.downPosition_x &&
              that.pose.nose.x < that.downPosition_x + 50 &&
              that.pose.nose.y > that.downPosition_y &&
              that.pose.nose.y < that.downPosition_y + 50) ||
            (that.pose.nose.x > that.downPosition_x &&
              that.pose.nose.x < that.downPosition_x + 50 &&
              that.pose.nose.y > that.downPosition_y &&
              that.pose.nose.y < that.downPosition_y + 50)
          ) {
            this.label = "down";
          } else if (
            (that.pose.nose.x > that.leftPosition_x &&
              that.pose.nose.x < that.leftPosition_x + 50 &&
              that.pose.nose.y > that.leftPosition_y &&
              that.pose.nose.y < that.leftPosition_y + 50) ||
            (that.pose.nose.x > that.leftPosition_x &&
              that.pose.nose.x < that.leftPosition_x + 50 &&
              that.pose.nose.y > that.leftPosition_y &&
              that.pose.nose.y < that.leftPosition_y + 50)
          ) {
            this.label = "left";
          } else if (
            (that.pose.nose.x > that.rightPosition_x &&
              that.pose.nose.x < that.rightPosition_x + 50 &&
              that.pose.nose.y > that.rightPosition_y &&
              that.pose.nose.y < that.rightPosition_y + 50) ||
            (that.pose.nose.x > that.rightPosition_x &&
              that.pose.nose.x < that.rightPosition_x + 50 &&
              that.pose.nose.y > that.rightPosition_y &&
              that.pose.nose.y < that.rightPosition_y + 50)
          ) {
            this.label = "right";
          }

          // for (let i = 0; i < that.pose.keypoints.length; i++) {
          //   let x = that.pose.keypoints[i].position.x;
          //   let y = that.pose.keypoints[i].position.y;
          //   this.rightBuffer.fill(0, 255, 0);
          //   this.rightBuffer.ellipse(x, y, 16, 16);
          // }

          // for (let i = 0; i < that.skeleton.length; i++) {
          //   let a = that.skeleton[i][0];
          //   let b = that.skeleton[i][1];
          //   this.rightBuffer.line(a.position.x, a.position.y, b.position.x, b.position.y);
          // }
        } else {
          this.rightBuffer.image(
            this.video,
            0,
            0,
            this.videoWidth,
            this.videoHeight
          );
        }
      } else {
        this.loading = true;
        console.log("로딩중");
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
      this.countDown = 20;
      this.countDownTimer();
      this.closeModal();
      this.gamestatus = true;
    },

    doCloseTutorial() {
      this.Tutorial = false;
      this.gameStart = true;
      if (this.firstStart == true) {
        this.countDownTimer();
      }
      this.gamestatus = true;
      this.firstStart = false;
    },
  },
  created() {
    this.Tutorial = true;
  },
};
</script>

<style>
#defaultCanvas0 {
  display: inline-block;
}
</style>

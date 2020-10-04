<template>
  <div
    style="
      width: 98vw;
      height: 95vh;
      position: absolute;
      top: 0px;
      left: 0px;
      text-align: center;
    "
  >
    <!-- <v-btn
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
    </v-btn> -->
    <!-- <p style="font-size: 5vh; font-weight: 700">스네이크 게임</p> -->
    <vue-p5 @setup="setup" @draw="draw"></vue-p5>

    <GameFinishModal @close="closeModal" v-if="modal">
      <!-- default 슬롯 콘텐츠 -->
      <p
        style="
          font-size: 17vh;
          color: white;
          font-weight: 500;
          margin-top: 30vh;
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
          "
        >
          다시시작
        </button>
      </template>
    </GameFinishModal>

    <!-- <SnakeGameTutorial @close="doCloseTutorial" v-if="Tutorial">
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
    </SnakeGameTutorial> -->
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
import $ from "jquery";
import GameFinishModal from "./GameFinishModal";
import { Snake } from "../../api/game/snake/snake";
import SnakeGameTutorial from "./SnakeGameTutorial";
import GameLevelModal from "./GameLevelModal";
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

      upPosition_x: -110,
      upPosition_y: 110,
      downPosition_x: -110,
      downPosition_y: 230,
      leftPosition_x: -40,
      leftPosition_y: 170,
      rightPosition_x: -180,
      rightPosition_y: 170,

      leftBuffer: null,
      rightBuffer: null,

      // record
      start_time: null,
      end_time: null,
      game_score: 0,

      // 컴포넌트 관련
      modal: false,
      Tutorial: false,
      loading: false,
      gameStart: false,
      firstStart: true,
      gamestatus: false,

      countDown: 25,
      score: 0,
      speed: 22,
      levelChange: false,
      level: "",
      snake: null,
      snakeGameBGM : null,
      failSound: null,
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
    GameLevelModal,
  },
  methods: {
    setup(sketch) {
      this.sketch = sketch;
      sketch.createCanvas(this.snakeCanvasWidth + this.videoWidth, this.height);

      this.video = sketch.createCapture(sketch.VIDEO);
      this.video.size(this.videoWidth, this.videoHeight);
      this.video.hide();

      this.snake = sketch.createImg(
        "https://user-images.githubusercontent.com/53737175/94985813-a6670480-0594-11eb-807d-6bb9303e20c4.png"
      );
      this.snake.hide();

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
      // game code ends

      $("#defaultCanvas0").parent().css({
        width: "100%",
        "text-align": "center",
        position: "absolute",
        height: "95vh",
      });
      $("#defaultCanvas0").css({ width: "100vw", height: "95vh" });
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
      // food.mult(scl);
    },
    draw(sketch) {
      sketch.background(0);
      sketch.fill(255);

      this.drawSnake(sketch);
      sketch.translate(this.snakeCanvasWidth * 2 + this.videoWidth, 0);
      sketch.scale(-1, 1);
      sketch.image(sketch, 0, 0);
      sketch.image(this.video, this.snakeCanvasWidth, 0);
      this.drawVideo(sketch);
    },
    drawSnake(sketch) {
      var that = this;
      if (sketch.frameCount % this.speed == 0) {
        this.s.update(sketch);
      }
      this.s.show(sketch);

      if (this.s.eat(this.food)) {
        that.score += 100;

        // Level2
        if (that.score >= 400 && that.score < 800) {
          that.speed = 20;
          that.countDown = 18;
          if (that.score == 400) {
            that.level = "Level 2";
            that.levelChange = true;
            setTimeout(function () {
              that.levelChange = false;
            }, 1000);
          }
        }
        // Level3
        else if (that.score >= 800 && that.score < 1200) {
          that.speed = 17;
          that.countDown = 15;
          if (that.score == 800) {
            that.level = "Level 3";
            that.levelChange = true;
            setTimeout(function () {
              that.levelChange = false;
            }, 1000);
          }
        }
        // Level4
        else if (that.score >= 1200 && that.score < 2000) {
          that.speed = 12;
          that.countDown = 13;
          if (that.score == 1200) {
            that.level = "Level 4";
            that.levelChange = true;
            setTimeout(function () {
              that.levelChange = false;
            }, 1000);
          }
        }
        // Level5
        else if (that.score >= 2000) {
          that.speed = 10;
          that.countDown = 10;
          if (that.score == 2000) {
            that.level = "Final";
            that.levelChange = true;
            setTimeout(function () {
              that.levelChange = false;
            }, 1000);
          }
        } else {
          that.countDown = 25;
        }

        that.pickLocation(sketch);
      }
      // snake
      sketch.fill(255, 0, 100);
      sketch.rect(20 * this.foodx, 20 * this.foody, this.scl, this.scl);

      if (this.label == "top") this.s.dir(0, -1);
      else if (this.label == "down") this.s.dir(0, 1);
      else if (this.label == "left") this.s.dir(-1, 0);
      else if (this.label == "right") this.s.dir(1, 0);
    },
    //비디오 화면
    drawVideo(sketch) {
      sketch.translate(this.snakeCanvasWidth * 2 + this.videoWidth, 0);
      sketch.scale(-1, 1);

      sketch.fill(255, 0, 255);
      sketch.rect(260 + this.snakeCanvasWidth, 110, 50, 50);
      sketch.textSize(40);
      sketch.textStyle(sketch.NORMAL);
      sketch.fill(255, 255, 255);
      sketch.text("상", 265 + this.snakeCanvasWidth, 150);

      sketch.fill(255, 0, 255);
      sketch.rect(260 + this.snakeCanvasWidth, 230, 50, 50);
      sketch.textSize(40);
      sketch.textStyle(sketch.NORMAL);
      sketch.fill(255, 255, 255);
      sketch.text("하", 265 + this.snakeCanvasWidth, 270);

      sketch.fill(255, 0, 255);
      sketch.rect(190 + this.snakeCanvasWidth, 170, 50, 50);
      sketch.textSize(40);
      sketch.textStyle(sketch.NORMAL);
      sketch.fill(255, 255, 255);
      sketch.text("좌", 195 + this.snakeCanvasWidth, 210);

      sketch.fill(255, 0, 255);
      sketch.rect(330 + this.snakeCanvasWidth, 170, 50, 50);
      sketch.textSize(40);
      sketch.textStyle(sketch.NORMAL);
      sketch.fill(255, 255, 255);
      sketch.text("우", 335 + this.snakeCanvasWidth, 210);

      var that = this;
      if (this.pose != null && this.gamestatus == true) {
        this.loading = false;

        // 점수판
        sketch.textSize(30);
        sketch.textStyle(sketch.BOLD);
        sketch.fill(255, 0, 0);
        sketch.text("점수 : " + this.score, 30 + this.snakeCanvasWidth, 40);

        // 카운트 다운
        sketch.textSize(50);
        sketch.textStyle(sketch.NORMAL);
        sketch.fill(0, 255, 255);
        sketch.text(this.countDown, 270 + this.snakeCanvasWidth, 50);

        if (this.countDown == 0) {
          that.end_time = this.timeNow();
          that.game_score = this.score;
          that.modal = true;
          that.score = 0;
          that.gamestatus = false;
          that.failSound = new Audio(
            require("../../assets/sound/fail.mp3")
          ); // path to file
          that.failSound.volume = 0.2;
          // this.jumpGameBGM.muted =true;
          that.snakeGameBGM.volume = 0.03;
          that.failSound.play();

        }

        sketch.translate(this.videoWidth, 0);
        sketch.scale(-1, 1);

        if (this.pose.score > 0.2 && this.pose != null) {
          const eyeR = that.pose.rightEye;
          const eyeL = that.pose.leftEye;
          const d = sketch.dist(eyeR.x, eyeR.y, eyeL.x, eyeL.y);
          sketch.fill(255, 0, 0);
          // sketch.ellipse(
          //   that.pose.nose.x - this.snakeCanvasWidth,
          //   that.pose.nose.y + 15,
          //   d - 25
          // );
          sketch.image(
            that.snake,
            that.pose.nose.x - this.snakeCanvasWidth - 0.35* d,
            that.pose.nose.y ,
            0.9*d ,
            0.9*d
          );
          sketch.fill(0, 0, 255);

          if (
            (that.pose.nose.x - this.snakeCanvasWidth > that.upPosition_x &&
              that.pose.nose.x - this.snakeCanvasWidth <
                that.upPosition_x + 50 &&
              that.pose.nose.y + 23 > that.upPosition_y &&
              that.pose.nose.y + 23 < that.upPosition_y + 50) ||
            (that.pose.nose.x - this.snakeCanvasWidth > that.upPosition_x &&
              that.pose.nose.x - this.snakeCanvasWidth <
                that.upPosition_x + 50 &&
              that.pose.nose.y + 23 > that.upPosition_y &&
              that.pose.nose.y + 23 < that.upPosition_y + 50)
          ) {
            this.label = "top";
          } else if (
            (that.pose.nose.x - this.snakeCanvasWidth > that.downPosition_x &&
              that.pose.nose.x - this.snakeCanvasWidth <
                that.downPosition_x + 50 &&
              that.pose.nose.y + 23 > that.downPosition_y &&
              that.pose.nose.y + 23 < that.downPosition_y + 50) ||
            (that.pose.nose.x - this.snakeCanvasWidth > that.downPosition_x &&
              that.pose.nose.x - this.snakeCanvasWidth <
                that.downPosition_x + 50 &&
              that.pose.nose.y + 23 > that.downPosition_y &&
              that.pose.nose.y + 23 < that.downPosition_y + 50)
          ) {
            this.label = "down";
          } else if (
            (that.pose.nose.x - this.snakeCanvasWidth > that.leftPosition_x &&
              that.pose.nose.x - this.snakeCanvasWidth <
                that.leftPosition_x + 50 &&
              that.pose.nose.y + 23 > that.leftPosition_y &&
              that.pose.nose.y + 23 < that.leftPosition_y + 50) ||
            (that.pose.nose.x - this.snakeCanvasWidth > that.leftPosition_x &&
              that.pose.nose.x - this.snakeCanvasWidth <
                that.leftPosition_x + 50 &&
              that.pose.nose.y + 23 > that.leftPosition_y &&
              that.pose.nose.y + 23 < that.leftPosition_y + 50)
          ) {
            this.label = "left";
          } else if (
            (that.pose.nose.x - this.snakeCanvasWidth > that.rightPosition_x &&
              that.pose.nose.x - this.snakeCanvasWidth <
                that.rightPosition_x + 50 &&
              that.pose.nose.y + 23 > that.rightPosition_y &&
              that.pose.nose.y + 23 < that.rightPosition_y + 50) ||
            (that.pose.nose.x - this.snakeCanvasWidth > that.rightPosition_x &&
              that.pose.nose.x - this.snakeCanvasWidth <
                that.rightPosition_x + 50 &&
              that.pose.nose.y + 23 > that.rightPosition_y &&
              that.pose.nose.y + 23 < that.rightPosition_y + 50)
          ) {
            this.label = "right";
          }
        } else {
          sketch.image(this.video, -this.snakeCanvasWidth, 0);
          sketch.textStyle(sketch.BOLD);
          sketch.translate(this.window_width, 0);
          sketch.scale(-1, 1);
          sketch.textSize(35);
          sketch.fill(255, 0, 0);
          sketch.text("포즈를 인식할 수 없습니다", -80, 200);

          //카운트다운
          sketch.textSize(50);
          sketch.textStyle(sketch.NORMAL);
          sketch.fill(0, 255, 255);
          sketch.text(that.countDown, 70, 50);

          // 점수판
          sketch.textSize(30);
          sketch.textStyle(sketch.BOLD);
          sketch.fill(255, 0, 0);
          sketch.text("점수 : " + this.score, -170, 40);
        }
      } else {
        if(this.gamestatus == true){
          this.loading = true;
        }
        else{
          this.loading = false;
        }
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
      this.speed = 22;
      this.countDown = 25;
      this.countDownTimer();
      this.closeModal();
      this.gamestatus = true;
      this.s = new Snake(
        this.sketch,
        this.scl,
        this.snakeCanvasWidth,
        this.height,
        this.food
      );
      this.snakeGameBGM.volume = 0.2;
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
    this.Tutorial = true;
    this.gamestatus = true;
    this.countDownTimer();
    this.snakeGameBGM = new Audio(
      require("../../assets/sound/SnakeGameBGM.mp3")
    ); // path to file
    this.snakeGameBGM.volume = 0.2;
    // this.jumpGameBGM.muted =true;
    this.snakeGameBGM.loop = true;
    this.snakeGameBGM.autoplay = true;
    this.snakeGameBGM.play();
  },
  mounted() {
    this.start_time = this.timeNow();
  },
  destroyed() {
    let stream = this.video.elt.srcObject
    stream.getTracks()[0].stop()
    this.sketch.remove();
    this.sketch.noLoop();
    this.sketch.clear();

    this.snakeGameBGM.pause();
    this.snakeGameBGM = null;
  },
};
</script>

<style>
#defaultCanvas0 {
  display: inline-block;
}
</style>

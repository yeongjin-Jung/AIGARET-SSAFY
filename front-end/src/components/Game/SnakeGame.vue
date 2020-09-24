<template>
  <div style="width :  100vw; height: 99%">
    <h4>스네이크 게임</h4>
    <vue-p5 @setup="setup" @draw="draw"></vue-p5>
  </div>
</template>

<script>
import VueP5 from "vue-p5";
import ml5 from "ml5";
import { Snake } from "../../api/game/snake/snake";
import $ from "jquery";
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
      upPosition_y: 100,
      downPosition_x: 250,
      downPosition_y: 200,
      leftPosition_x: 300,
      leftPosition_y: 150,
      rightPosition_x: 200,
      rightPosition_y: 150,

      leftBuffer: null,
      rightBuffer: null,
    };
  },
  components: {
    "vue-p5": VueP5,
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
      //   const options = { numLabels: 4 };
      //   this.classifier = this.mobilenet.classification(
      //     this.video,
      //     options,
      //     this.videoReady()
      //   );

      //game code starts
      this.s = new Snake(
        sketch,
        this.scl,
        this.snakeCanvasWidth,
        this.height,
        this.food
      );
      sketch.frameRate(10);
      this.pickLocation(sketch);
      //game code ends

      $("#defaultCanvas0").parent().css({
        width: "100%",
        "text-align": "center",
        position: "absolute",
        left: "1vw",
        top: "15vh",
      });
      $("#defaultCanvas0").css({ width: "80vw", height: "70vh" });
      // $("video").css({ width: "300vw;", height: "72vh" });
    },

    modelReady() {
      console.log("Model Loaded");
    },
    videoReady() {
      console.log("webcam load... finished");
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
      this.s.update(sketch);
      this.s.show(sketch);

      if (this.s.eat(this.food)) {
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
      this.rightBuffer.rect(250, 100, 50, 50);
      this.rightBuffer.textSize(40);
      this.rightBuffer.translate(this.videoWidth, 0);
      this.rightBuffer.scale(-1, 1);
      this.rightBuffer.textStyle(this.rightBuffer.NORMAL);
      this.rightBuffer.fill(255, 255, 255);
      this.rightBuffer.text("상", 305, 140);

      this.rightBuffer.fill(255, 0, 255);
      this.rightBuffer.rect(300, 200, 50, 50);
      this.rightBuffer.textSize(40);
      this.rightBuffer.textStyle(this.rightBuffer.NORMAL);
      this.rightBuffer.fill(255, 255, 255);
      this.rightBuffer.text("하", 305, 240);

      this.rightBuffer.fill(255, 0, 255);
      this.rightBuffer.rect(250, 150, 50, 50);
      this.rightBuffer.textSize(40);
      this.rightBuffer.textStyle(this.rightBuffer.NORMAL);
      this.rightBuffer.fill(255, 255, 255);
      this.rightBuffer.text("좌", 255, 190);

      this.rightBuffer.fill(255, 0, 255);
      this.rightBuffer.rect(350, 150, 50, 50);
      this.rightBuffer.textSize(40);
      this.rightBuffer.textStyle(this.rightBuffer.NORMAL);
      this.rightBuffer.fill(255, 255, 255);
      this.rightBuffer.text("우", 355, 190);

      this.rightBuffer.translate(this.videoWidth, 0);
      this.rightBuffer.scale(-1, 1);

      // this.rightBuffer.rect(300, 150, 50, 50);
      // this.rightBuffer.rect(250, 200, 50, 50);
      var that = this;
      if (this.pose != null) {
        // if (this.pose != null && this.gamestatus == true) {
        // this.loading = false;
        // //장애물
        // sketch.rect(this.position_x, this.position_y, 100, 100);
        // sketch.translate(this.window_width, 0);
        // sketch.scale(-1, 1);

        // //점수판
        // sketch.textSize(50);
        // sketch.textStyle(sketch.BOLD);
        // sketch.fill(255, 0, 0);
        // sketch.text("점수 : " + this.score, 40, 60);

        // //카운트 다운
        // sketch.textSize(100);
        // sketch.textStyle(sketch.NORMAL);
        // sketch.fill(0, 255, 255);
        // sketch.text(this.countDown, 455, 100);

        //전체 Canvas 반전
        // sketch.translate(this.window_width, 0);
        // sketch.scale(-1, 1);

        // if (this.countDown == 0) {
        //   this.modal = true;
        //   this.score = 0;
        //   this.gamestatus = false;
        // }

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
        // this.loading = true;
        console.log("로딩중");
      }
    },
  },
};
</script>

<style>
#defaultCanvas0 {
  display: inline-block;
}
</style>

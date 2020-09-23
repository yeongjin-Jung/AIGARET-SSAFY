<template>
  <div style="width:100vw; height:95vh; text-align : center;">
    <!-- <h4>손목터치게임</h4> -->
    <vue-p5 @setup="setup" @draw="draw"></vue-p5>
    <GameFinishModal @close="closeModal" v-if="modal">
      <!-- default 슬롯 콘텐츠 -->
      <p style="font-size : 17vh; color : white; font-weight:500; margin-top:7vh;">Game Over</p>
      <!-- /default -->
      <!-- /footer -->
      <template slot="footer" style="background-color : rgba(0,0,0,1);">
        <button @click="doClose" style="background-color : red; height :8vh; font-size : 4vh; font-weight: 400;">다시시작</button>
      </template>
    </GameFinishModal>
  </div>
</template>

<script>
import VueP5 from "vue-p5";
import ml5 from "ml5";
import $ from "jquery";
import GameFinishModal from "./GameFinishModal";
export default {
  name: "WristTouchGame",
  data: function () {
    return {
      video: null,
      poseNet: null,
      pose: null,
      skeleton: null,
      position_x: 900,
      position_y: 500,
      window_width: 1000,
      window_height: 700,
      countDown: 10,
      modal: false,
    };
  },
  components: {
    VueP5,
    GameFinishModal,
  },
  methods: {
    setup(sketch) {
      sketch.createCanvas(this.window_width, this.window_height);
      sketch.background(0);
      this.video = sketch.createCapture(sketch.VIDEO);
      this.video.size(this.window_width, this.window_height);
      this.video.hide();
      this.poseNet = ml5.poseNet(this.video, this.modelReady());
      var that = this;
      this.poseNet.on("pose", function (results) {
        if (results.length > 0) {
          that.pose = results[0].pose;
          that.skeleton = results[0].skeleton;
        }
      });

      $("#defaultCanvas0").parent().css({
        width: "100vw",
        "text-align": "center",
        position: "absolute",
        top: "7vh",
      });

      $("#defaultCanvas0").css({ width: "60vw", height: "85vh" });
    },
    modelReady() {
      console.log("Model Loaded");
    },
    chanege(x) {
      this.position_x = Math.floor(Math.random() * 800 + 100);
      this.position_y = Math.floor(Math.random() * 300 + 50);
      if (this.position_x >= 300 && this.position_x <= 700) {
        this.chanege(x);
      }
      this.countDown = 10;
    },
    countDownTimer() {
      if (this.countDown > 0) {
        setTimeout(() => {
          this.countDown -= 1;
          this.countDownTimer();
        }, 1000);
      }
    },

    draw(sketch) {
      sketch.translate(this.window_width, 0);
      sketch.scale(-1, 1);
      sketch.image(this.video, 0, 0, this.window_width, this.window_height);
      sketch.rect(this.position_x, this.position_y, 100, 100);
      sketch.translate(this.window_width, 0);
      sketch.scale(-1, 1);
      sketch.textSize(100);
      sketch.text(this.countDown, 450, 100);
      sketch.translate(this.window_width, 0);
      sketch.scale(-1, 1);

      if (this.countDown == 0) {
        this.modal = true;
      }
      var that = this;
      if (this.pose.score > 0.25 && this.pose != null) {
        let eyeR = that.pose.rightEye;
        let eyeL = that.pose.leftEye;
        let d = sketch.dist(eyeR.x, eyeR.y, eyeL.x, eyeL.y);
        sketch.fill(255, 0, 0);
        sketch.ellipse(that.pose.nose.x, that.pose.nose.y, d);
        sketch.fill(0, 0, 255);

        if (
          (that.pose.rightWrist.x > that.position_x &&
            that.pose.rightWrist.x < that.position_x + 100 &&
            that.pose.rightWrist.y > that.position_y &&
            that.pose.rightWrist.y < that.position_y + 100) ||
          (that.pose.leftWrist.x > that.position_x &&
            that.pose.leftWrist.x < that.position_x + 100 &&
            that.pose.leftWrist.y > that.position_y &&
            that.pose.leftWrist.y < that.position_y + 100)
        ) {
          that.chanege();
        }

        sketch.ellipse(that.pose.rightWrist.x, that.pose.rightWrist.y, 32);
        sketch.ellipse(that.pose.leftWrist.x, that.pose.leftWrist.y, 32);

        for (let i = 0; i < that.pose.keypoints.length; i++) {
          let x = that.pose.keypoints[i].position.x;
          let y = that.pose.keypoints[i].position.y;
          sketch.fill(0, 255, 0);
          sketch.ellipse(x, y, 16, 16);
        }

        for (let i = 0; i < that.skeleton.length; i++) {
          let a = that.skeleton[i][0];
          let b = that.skeleton[i][1];
          sketch.strokeWeight(2);
          sketch.stroke(255);
          sketch.line(a.position.x, a.position.y, b.position.x, b.position.y);
        }
      } else {
        sketch.image(this.video, 0, 0, this.window_width, this.window_height);
        sketch.rect(this.position_x, this.position_y, 100, 100);
        sketch.translate(this.window_width, 0);
        sketch.scale(-1, 1);
        sketch.text(this.countDown, 450, 100);
      }
    },
    closeModal() {
      this.modal = false;
    },

    

    doClose(){
      this.countDown = 10;
      this.countDownTimer();
      this.closeModal();
    }
  },
  created() {
    this.countDownTimer();
  },
};
</script>

<style>
#defaultCanvas0 {
  display: inline-block;
  height: 70vh;
}
</style>

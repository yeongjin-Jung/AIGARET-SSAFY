<template>
  <div style="width :  100vw; height: 99%">
    <!-- <h4>손목터치게임</h4> -->
    <vue-p5 @setup="setup" @draw="draw"></vue-p5>
  </div>
</template>

<script>
import VueP5 from "vue-p5";
import ml5 from "ml5";
import $ from "jquery";

export default {
  name: "WristTouchGame",
  data: function () {
    return {
      video: null,
      poseNet: null,
      pose: null,
      pose2: null,
      skeleton: null,
      position_x: 900,
      position_y: 500,
      window_width: 1500,
      window_height: 1050,
    };
  },
  components: {
    VueP5,
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
        that.pose = results[0].pose;
        that.skeleton = results[0].skeleton;
      });

      $("#defaultCanvas0")
        .parent()
        .css({ width: "100%", "text-align": "center" });
    },
    modelReady() {
      console.log("Model Loaded");
    },
    chanege() {
      this.position_x = Math.floor(Math.random() * 800 + 100);
      this.position_y = Math.floor(Math.random() * 500 + 200);
    },
    draw(sketch) {
      sketch.translate(this.window_width, 0);
      sketch.scale(-1, 1);
      sketch.image(this.video, 0, 0, this.window_width, this.window_height);
      sketch.rect(this.position_x, this.position_y, 100, 100);
      var that = this;
      if (this.pose) {
        if (
          this.pose.score > 0.1 &&
          (this.pose.rightWrist.confidence > 0.1 ||
            this.pose.leftWrist.confidence > 0.1)
        ) {
          // const eyeR = that.pose.rightEye
          // const eyeL = that.pose.leftEye;
          // const d = sketch.dist(eyeR.x, eyeR.y, eyeL.x, eyeL.y);
          // sketch.fill(255, 0, 0);
          // sketch.ellipse(that.pose.nose.x, that.pose.nose.y, d);
          if (
            (that.pose.rightWrist.x > that.position_x - 50 &&
              that.pose.rightWrist.x < that.position_x + 50 &&
              that.pose.rightWrist.y > that.position_y - 50 &&
              that.pose.rightWrist.y < that.position_y + 100) ||
            (that.pose.leftWrist.x > that.position_x - 50 &&
              that.pose.leftWrist.x < that.position_x + 75 &&
              that.pose.leftWrist.y > that.position_y - 50 &&
              that.pose.leftWrist.y < that.position_y + 75)
          ) {
            that.chanege();
          }
          sketch.fill(0, 0, 255);
          sketch.ellipse(that.pose.rightWrist.x, that.pose.rightWrist.y, 32);
          sketch.ellipse(that.pose.leftWrist.x, that.pose.leftWrist.y, 32);
          // sketch.image(this.img, that.pose.rightWrist.x, that.pose.rightWrist.y-50, 100, 100);
          // for (let i = 0; i < that.pose.keypoints.length; i++) {
          //   const x = that.pose.keypoints[i].position.x;
          //   const y = that.pose.keypoints[i].position.y;
          //   sketch.fill(0, 255, 0);
          //   sketch.textSize(50);
          //   sketch.text(i, x, y);
          //   sketch.ellipse(x, y, 16, 16);
          // }

          // for (let i = 0; i < that.skeleton.length; i++) {
          //   const a = that.skeleton[i][0];
          //   const b = that.skeleton[i][1];
          //   sketch.strokeWeight(2);
          //   sketch.stroke(255);
          //   sketch.line(a.position.x, a.position.y, b.position.x, b.position.y);
          // }
        }
      } else {
        sketch.image(this.video, 0, 0, this.window_width, this.window_height);
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

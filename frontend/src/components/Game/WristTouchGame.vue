<template>
  <div style="width :  100vw; height: 100vh">
    <!-- <h4>손목터치게임</h4> -->
    <vue-p5 @setup="setup" @draw="draw"></vue-p5>
  </div>
</template>

<script>
import VueP5 from "vue-p5";
import ml5 from "ml5";
import $ from 'jquery';

export default {
  name: "WristTouchGame",
  data: function () {
    return {
      video: null,
      poseNet: null,
      pose: null,
      skeleton: null,
      position_x: 300,
      position_y: 200,
      window_width: 1700,
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
      this.poseNet = ml5.poseNet(this.video, {
        outputStride: 16,
        multiplier: 0.75,
        quantBytes: 2,
        minPartConfidence: 0.5,
        maxPoseDetections: 5,
        minPoseConfidence: 0.15,
        nmsRadius: 30,
        detectionType: "multiple",
      });
      var that = this;
      this.poseNet.on("pose", function (results) {
        if (results.length > 0) {
          that.pose = results[0].pose;
          that.skeleton = results[0].skeleton;
        }
      });
      $("#defaultCanvas0").parent().css({"width" : "100%", "text-align" : "center"});
    },
    chanege() {
      this.position_x = Math.floor(Math.random() * 200 + 100);
      this.position_y = Math.floor(Math.random() * 150 + 100);
    },
    draw(sketch) {
      sketch.image(this.video, 0, 0, this.window_width, this.window_height);
      sketch.rect(this.position_x, this.position_y, 50, 50);
      var that = this;
      if (this.pose) {
        if (this.pose.score > 0.23) {
          const eyeR = that.pose.rightEye;
          const eyeL = that.pose.leftEye;
          const d = sketch.dist(eyeR.x, eyeR.y, eyeL.x, eyeL.y);
          sketch.fill(255, 0, 0);
          sketch.ellipse(that.pose.nose.x, that.pose.nose.y, d);
          if (
            that.pose.nose.x > that.position_x - 25 &&
            that.pose.nose.x < that.position_x + 50 &&
            that.pose.nose.y > that.position_y - 25 &&
            that.pose.nose.y < that.position_y + 50
          ) {
            that.chanege();
          }
          sketch.fill(0, 0, 255);
          sketch.ellipse(that.pose.rightWrist.x, that.pose.rightWrist.y, 32);
          sketch.ellipse(that.pose.leftWrist.x, that.pose.leftWrist.y, 32);
          if (
            that.pose.rightWrist.x > that.position_x - 50 &&
            that.pose.rightWrist.x < that.position_x + 50 &&
            that.pose.rightWrist.y - 50 > that.position_y - 50 &&
            that.pose.rightWrist.y - 50 < that.position_y + 50
          ) {
            that.chanege();
          }

          for (let i = 0; i < that.pose.keypoints.length; i++) {
            const x = that.pose.keypoints[i].position.x;
            const y = that.pose.keypoints[i].position.y;
            sketch.fill(0, 255, 0);
            sketch.textSize(50);
            sketch.text(i, x, y);
            sketch.ellipse(x, y, 16, 16);
          }

          for (let i = 0; i < that.skeleton.length; i++) {
            const a = that.skeleton[i][0];
            const b = that.skeleton[i][1];
            sketch.strokeWeight(2);
            sketch.stroke(255);
            sketch.line(a.position.x, a.position.y, b.position.x, b.position.y);
          }
        }
      } else {
        sketch.image(this.video, 0, 0);
      }
    },
  },
  created() {

      
      
  },
};
</script>

<style>
#defaultCanvas0 {
  display: inline-block;
}
</style>

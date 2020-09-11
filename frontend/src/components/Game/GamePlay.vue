<template>
  <div>
    <h4>게임 플레이 화면</h4>
    <vue-p5 @setup="setup" @draw="draw"></vue-p5>
  </div>
</template>

<script>
import VueP5 from "vue-p5";
import ml5 from "ml5";
export default {
  name: "GamePlay",
  data: function () {
    return {
      video: null,
      poseNet: null,
      pose: null,
      skeleton: null,
      position_x: 300,
      position_y: 200,
    };
  },
  components: {
    "vue-p5": VueP5,
  },
  methods: {
    setup(sketch) {
      sketch.createCanvas(640, 480);
      this.video = sketch.createCapture(sketch.VIDEO);
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
    },
    chanege() {
      this.position_x = Math.floor(Math.random() * 200 + 100);
      this.position_y = Math.floor(Math.random() * 150 + 100);
    },
    draw(sketch) {
      sketch.image(this.video, 0, 0);
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
      }else{
        sketch.image(this.video,0,0);
      }
    },
  },
};
</script>

<style>
</style>

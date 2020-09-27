<template>
  <v-dialog v-model="dialog" width="500" persistent>
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        v-bind="attrs"
        v-on="on"
        class="mr-2"
        style="padding: 20px; color: white; outline:none; background-color: #005792"
        @click="clickedFaceLoginBtn()"
      >얼굴인식으로 로그인</v-btn>
    </template>

    <v-card>
      <v-card-title class="headline justify-center" style="background: #BBBBFF">
        <p class="ma-2" style="color: white; font-family: CookieRun-Bold">얼굴인식으로 로그인</p>
      </v-card-title>

      <v-card-text style="padding-bottom: 10px">
        <div class="my-2" style="display: flex; justify-content: center; align-items: center">
          <video id="video" width="400" height="300" autoplay muted></video>
          <canvas id="canvas" width="400" height="300" style="position: absolute"></canvas>
        </div>

        <v-divider></v-divider>

        <div class="my-2" style="display: flex; justify-content: center">
          <v-btn
            class="mx-2"
            color="primary"
            @click="cancelFaceLogin()"
            style="font-family: CookieRun-Bold"
          >돌아가기</v-btn>
        </div>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import * as faceapi from "face-api.js"

export default {
  name: "FaceLogin",

  data() {
    return {
      dialog: false,
      video: null,
      canvas: null,
      videoFlag: false,
      localStream: null
    };
  },

  methods: {
    clickedFaceLoginBtn() {
      this.videoFlag = true;

      navigator.getUserMedia(
        { video: {} },
        stream => {
          video.srcObject = stream;
          this.localStream = stream;
        },
        err => console.error(err)
      );
    },

    cancel() {
      this.dialog = false;
    },

    async faceDetect() {
      console.log("this.video.width", this.video.width);
      console.log("this.video.height", this.video.height);

      let video = this.video;
      let canvas = this.canvas;

      const displaySize = { width: video.width, height: video.height };
      faceapi.matchDimensions(canvas, displaySize);

      await faceapi.nets.ssdMobilenetv1.loadFromUri("/models");
      await faceapi.nets.faceLandmark68Net.loadFromUri("/models");
      await faceapi.nets.faceRecognitionNet.loadFromUri("/models");
      await faceapi.nets.faceExpressionNet.loadFromUri("/models");

      this.timerId = setInterval(async () => {
        console.log("계속 도는 중.");
        const detections = await faceapi
          .detectAllFaces(video)
          .withFaceLandmarks()
          .withFaceExpressions();
        const resizedDetections = faceapi.resizeResults(
          detections,
          displaySize
        );
        canvas.getContext("2d").clearRect(0, 0, canvas.width, canvas.height);
        faceapi.draw.drawDetections(canvas, resizedDetections);
        faceapi.draw.drawFaceLandmarks(canvas, resizedDetections);
        faceapi.draw.drawFaceExpressions(canvas, resizedDetections);
      }, 100);
    },

    cancelFaceLogin() {
      this.isCaptured = false;
      this.localStream.getTracks()[0].stop();
      if (this.timerId != null) clearInterval(this.timerId);
      setTimeout(() => {
        this.dialog = false;
      }, 500);

      this.videoFlag = false;
    }
  },

  updated() {
    console.log("FaceLogin.vue updated.");

    if (this.videoFlag == true) {
      this.video = document.getElementById("video");
      this.canvas = document.getElementById("canvas");

      this.faceDetect();
    } else {
      this.video = null;
      this.canvas = null;

      console.log("video tag : ", this.video);
      console.log("canvas tag : ", this.canvas);
    }
  }
};
</script>

<style>
</style>
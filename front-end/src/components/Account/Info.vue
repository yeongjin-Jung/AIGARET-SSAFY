<template>
  <v-container fluid class="text-center">
    <!-- <v-row> -->
    <div>
      <div id="outer" class="row">

        <div id="inner_left" class="col-md-4" style="background: #5277de; height: 400px; display: flex; justify-content: center; flex-wrap: wrap;">
          <!-- <div style="width: 300px; height: 300px; background: #72ddf2; display: inline-block; text-align: center; padding-top: 145px; margin-bottom: 10px"> -->
          
          <!-- 사진! -->
          <div style="width: 400px; height: 300px; background: #72ddf2; text-align: center;">
            <v-img src="@/assets/ryan.png" width="400px" height="300px"></v-img>
          </div>
          
          <div style="display: inline-block">

            <!-- 비밀번호 변경 -->
            <v-dialog v-model="dialog_change_password" width="500" persistent>
              <template v-slot:activator="{ on, attrs }">
                <v-btn class="ma-2" color="red lighten-2" dark v-bind="attrs" v-on="on">
                  <!-- 비밀번호 변경 -->
                  <v-icon>mdi-account-edit</v-icon>
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="headline grey lighten-2 justify-center">비밀번호 변경</v-card-title>

                <v-card-text>
                  <v-form class="ma-4">
                    <v-text-field label="현재 비밀번호" name="password" type="password" required></v-text-field>
                    <v-text-field label="변경할 비밀번호" name="changedPassword" type="password"></v-text-field>
                    <v-text-field label="비밀번호 확인" name="changedPasswordConfirm" type="password"></v-text-field>
                  </v-form>
                </v-card-text>

                <v-card-actions>
                  <!-- <v-spacer></v-spacer> -->
                  <!-- <v-btn color="primary" text @click="dialog_change_password = false">돌아가기</v-btn> -->
                  <div style="width: 100%; margin: 0 10px; text-align: center">
                      <v-btn color="primary" style="margin: 10px 10px">수정</v-btn>
                      <v-btn color="error" style="margin: 10px 10px" @click="dialog_change_password = false">돌아가기</v-btn>
                    </div>
                </v-card-actions>
              </v-card>
            </v-dialog>

            <!-- 사진 변경 -->
            <v-dialog v-model="dialog_change_image" width="500" persistent>
              <template v-slot:activator="{ on, attrs }">
                <v-btn class="ma-2" color="red lighten-2" dark v-bind="attrs" v-on="on" @click="videoStart()">
                  <!-- 사진 변경 -->
                  <v-icon>mdi-camera-retake</v-icon>
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="headline grey lighten-2 justify-center">사진 변경</v-card-title>

                <v-card-text style="padding-bottom: 10px">
                  <div class="my-2" style="display: flex; justify-content: center; align-items: center">
                    <video id="video" width="400" autoplay muted></video>
                  </div>

                  <div class="my-2" style="display: flex; justify-content: center;">
                    <v-btn class="mx-2" fab>
                      <v-icon>mdi-camera</v-icon>
                    </v-btn>
                    <v-btn class="mx-2" fab>
                      <v-icon>mdi-refresh</v-icon>
                    </v-btn>
                  </div>
                <v-divider></v-divider>

                  <div class="my-2" style="display: flex; justify-content: center">
                    <v-btn class="mx-2" color="error" @click="update">변경</v-btn>
                    <v-btn class="mx-2" color="primary" @click="cancel">취소</v-btn>
                  </div>
                </v-card-text>
              </v-card>
            </v-dialog>
            
          </div>
        </div>
        
        <div id="inner_right" class="col-md-8" style="background: #50d9cb; height: 400px">
          <div class="ma-2" style="background: yellow;">
            <p class="text-md-left font-weight-bold" style="font-size: 2rem">관리자(이름)</p>&emsp;
            <p class="text-md-left font-weight-bold" style="font-size: 1rem; text-indent: 2rem">Administrator(아이디)</p>
          </div>
          <div class="ma-2 pa-1" style="background: purple">
            <p class="text-md-left font-weight-bold" style="font-size: 2rem;">진행 현황</p>
            <v-progress-circular class="mx-10 my-2" color="green lighten-2" :size="100" :width="15" value="60">팔</v-progress-circular>
            <v-progress-circular class="mx-10 my-2" color="blue lighten-2" :size="100" :width="15" value="30">다리</v-progress-circular>
            <v-progress-circular class="mx-10 my-2" color="pink lighten-2" :size="100" :width="15" value="80">몸</v-progress-circular>
          </div>
        </div>
      </div>

    <!-- </v-row> -->
    </div>
  </v-container>
</template>

<script>
import $ from 'jquery'

export default {
  data() {
    return {
      dialog_my_info: "",
      dialog_change_password: "",
      dialog_change_image: "",
      video: document.getElementById("video"),
      localStream: ""
    };
  },

  methods: {
    home() {
      this.$router.push({ path: "/" });
    },

    videoStart() {
      navigator.getUserMedia({ video: {} },
        stream => {
          video.srcObject = stream
          this.localStream = stream
        },
        err => console.error(err)
      )
    },

    detectLandMarkes() {
      const { Canvas, Image, ImageData } = canvas;

      // faceapi.env.monkeyPatch({ Canvas, Image, ImageData })
      faceapi.env.monkeyPatch({
        Canvas: HTMLCanvasElement,
        Image: HTMLImageElement,
        ImageData: ImageData,
        Video: HTMLVideoElement,
        createCanvasElement: () => document.createElement("canvas"),
        createImageElement: () => document.createElement("img"),
      });

      // let video = document.getElementById("video2");
      // console.log("video : ", video)
      let currentStream;
      let displaySize;

      var that = this
      navigator.getUserMedia(
      {
        video: true
      },

      stream => {
        // val.srcObject = stream;
        var video = document.getElementById("video")
        var videoEl = $("#video");

        var left = videoEl.offset().left;
        var top = videoEl.offset().top;
        
        var canvas = $("#canvas")

        var canvas_left = canvas.offset().left;

        $("#canvas").css("left", left)
        $("#canvas").css("top", top)

        video.srcObject = stream;
        video.onloadedmetadata = function(e) {
          video.play();
          displaySize = { width: this.scrollWidth, height: this.scrollHeight };
          console.log("displaySize: ", displaySize)
          console.log("hi")

          async function detect() {
            console.log("detect")
            const MODEL_URL = "/models";

            await faceapi.nets.ssdMobilenetv1.loadFromUri("/models");
            await faceapi.nets.faceLandmark68Net.loadFromUri("/models");
            await faceapi.nets.faceRecognitionNet.loadFromUri("/models");

              console.log("setInterval()")
              let fullFaceDescriptions = await faceapi
                .detectAllFaces(video)
                .withFaceLandmarks()
                .withFaceDescriptors();
              let canvasTag = $("#canvas").get(0);
              faceapi.matchDimensions(canvasTag, displaySize);

              const fullFaceDescription = faceapi.resizeResults(
                fullFaceDescriptions,
                displaySize
              );

              faceapi.draw.drawDetections(canvasTag, fullFaceDescriptions);
              faceapi.draw.drawFaceLandmarks(canvasTag, fullFaceDescriptions)

              console.log(displaySize);
          } // end method detect

          detect()
        };
        this.localStream = stream

        setTimeout(() => {
          // this.localStream.getTracks()[0].pause()
          video.pause()
        }, 5000);
      },

      err => console.error(err)
      )
      
    },

    update() {
      // 멈춰있는 사진 백에 전송.
            
    },

    cancel() {
      $("#video").get(0).pause()
      $("#video").get(0).currentTime = 0;
      
      console.log("this.localStream : ", this.localStream)
      this.localStream.getTracks()[0].stop()

      setTimeout(() => {
        this.dialog_change_image = false
      }, 1000);
    }
    
  },
};
</script>

<style>
.basil {
  background-color: #fcfeff !important;
}
.basil--text {
  color: #356859 !important;
}
</style>

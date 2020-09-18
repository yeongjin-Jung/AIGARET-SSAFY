<template>
  <v-dialog v-model="dialog" width="860px" height="1000px" persistent>
  <!-- <v-dialog v-model="dialog"  height="1000px" persistent> -->
    
    <template v-slot:activator="{ on, attrs }">
      <v-btn v-bind="attrs" v-on="on" class="mr-2" style="width: 92.88px; padding: 20px; color: white; outline:none; background-color: #324ec9" @click="clicked()">회원가입</v-btn>
    </template>

    <div id="container" style="background-color: #fcfeff; height: 530px;">
      <div style="float:left; width:50%; margin: 0 auto; text-align:center">
      
        <ValidationObserver ref="observer">
          <v-card width="448px" flat outlined style="background-color: #fcfeff; !important; border-color: white !important; float: left; height: 100%">
            <v-card-title class="justify-center" style="background-color: #005792; color: white">회원가입</v-card-title>
            <v-card-text>
              <v-form class="ma-4">
                <ValidationObserver>
                  <ValidationProvider mode="eager" v-slot="{ errors }" name="Id" rules="required">
                    <v-text-field id="id" v-model="signupData.id" :error-messages="errors" label="아이디" required>
                      <template v-slot:append-outer>
                        <v-btn outlined small rounded>중복확인</v-btn>
                      </template>
                    </v-text-field>
                  </ValidationProvider>
                </ValidationObserver>

                <!-- <v-alert dense outlined type="error">이미 가입된 아이디입니다.</v-alert> -->
                <ValidationProvider mode="eager" v-slot="{ errors }" name="Password" vid="confirmation" :rules="{ required: true, min: 8, regex: /^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]/ }">
                  <v-text-field v-model="signupData.password" :error-messages="errors" label="비밀번호" name="password" type="password"></v-text-field>
                </ValidationProvider>

                <ValidationProvider mode="eager" v-slot="{ errors }" name="PasswordConfirm" rules="required|confirmed:confirmation">
                  <v-text-field v-model="signupData.passwordConfirm" :error-messages="errors" label="비밀번호 확인" name="passwordConfirm" type="password"></v-text-field>
                </ValidationProvider>

                <ValidationProvider mode="eager" v-slot="{ errors }" name="Name" rules="required|max:10">
                  <v-text-field v-model="signupData.name" :counter="10" :error-messages="errors" label="이름" required></v-text-field>
                </ValidationProvider>

                <ValidationProvider mode="eager" v-slot="{ errors }" name="Age" rules="required|confirmed:confirmation">
                  <v-text-field v-model="signupData.age" :error-messages="errors" label="나이" name="age"></v-text-field>
                </ValidationProvider>
            <!-- <div style="width: 100%; margin: 0 10px; float: left; text-align: center"> -->
              <v-btn color="primary" style="margin: 10px 10px">회원가입</v-btn>
              <v-btn color="error" style="margin: 10px 10px" @click="close">돌아가기</v-btn>
            <!-- </div> -->
              </v-form>
            </v-card-text>
          </v-card>
        </ValidationObserver>
        
      </div>

      <!-- <div style="background: black; float: left; width: 427px; height: 425px; text-align: center;"> -->
      <div style="background: #fcfeff; height: 500px; text-align: center; float: left; vertical-align: middle;">
        <div style="margin-top: 80px; text-algin: center;">
          <!-- <span>TEST</span> -->
          <video id="video2" height="300" autoplay muted></video>
          <canvas id="canvas" class="overlay"></canvas>
          <h3 style="padding: 15px auto; font-size: 22px">얼굴이 잘 인식되도록 화면 가운데 위치시켜주세요.</h3>
          <v-btn class="mx-2" fab dark small color="primary" @click="pause">
            <v-icon dark>mdi-camera</v-icon>
          </v-btn>
          <v-btn class="mx-2" fab dark small color="error" @click="play">
            <v-icon dark>mdi-refresh</v-icon>
          </v-btn>
        </div>
      </div>

    </div>
    

  </v-dialog>
</template>

<script>
import $ from "jquery"
import * as faceapi from "face-api.js"

const canvas = require('canvas');

import { required, email, max, min, regex, confirmed } from "vee-validate/dist/rules"
import { extend, ValidationObserver, setInteractionMode, ValidationProvider } from "vee-validate"

import { mapActions } from 'vuex'

export default {
  name: "Signup",

  components: {
    ValidationProvider,
    ValidationObserver
  },

  data() {
    return {
      dialog: false,
      facedetection: "",
      video2: document.getElementById("video2"),
      localStream: "",

      signupData: {
        id: "",
        password: "",
        passwordConfirm: "",
        name: "",
        age: ""
      }
    }
  },

  props: {
    flag: false
  },

  watched() {
    if(this.flag == true) {
      this.dialog = true
    } else{
      this.dialog = false
    }
  },

  methods: {
    movePage() {
      this.$router.push({name: "Login"})
    },
    
    startVideo (val) {
      navigator.getUserMedia(
        {
          video: true
        },

        stream => {
          // val.srcObject = stream;
          var video = document.getElementById("video2")
          console.log("video : ", video)
          video.srcObject = stream;
          video.onloadedmetadata = function(e) {
           video.play();
         };
          this.localStream = stream
        },

        err => console.error(err)
      )
    },

    clicked() {
      console.log("회원가입 버튼 클릭됨.")
      // console.log("video", this.video2)
      
      // this.detectLandMarkes()
      // this.startVideo(this.video2)
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
        var video = document.getElementById("video2")
        var videoEl = $("#video2");
        var left = videoEl.offset().left;
        var top = videoEl.offset().top;
    
        // console.log("x : " + x + ", " + "y : " + y)

        // var top = video.getBoundingClientRect().top
        // var left = video.getBoundingClientRect().left
        // console.log("top : " + top + ", " + "left : " + left)

        video.srcObject = stream;
        video.onloadedmetadata = function(e) {
          video.play();
          displaySize = { width: this.scrollWidth, height: this.scrollHeight };
          console.log("displaySize: ", displaySize)
          console.log("hi")

          async function detect() {
            console.log("detect")
            const MODEL_URL = "/models";

            // await faceapi.loadSsdMobilenetv1Model(MODEL_URL);
            // await faceapi.loadFaceLandmarkModel(MODEL_URL);
            // await faceapi.loadFaceRecognitionModel(MODEL_URL);
            await faceapi.nets.ssdMobilenetv1.loadFromUri("/models");
            await faceapi.nets.faceLandmark68Net.loadFromUri("/models");
            await faceapi.nets.faceRecognitionNet.loadFromUri("/models");

            // let canvasTag = $("#canvas").get(0);
            var dia = that.dialog

            // let facedetection = setInterval(async () => {
            // this.facedetection = setInterval(async () => {
            // this.facedetection = setInterval(async () => {
              console.log("dia : ", dia)
              // if(this.dialog == false) {
              console.log("setInterval()")
              // }
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

            // }, 300);

            console.log(displaySize);
          } // end method detect

          detect()
        };
        this.localStream = stream
      },

      err => console.error(err)
      )
      
      
    },

    pause() {
      this.detectLandMarkes()

      setTimeout(() => {
        clearInterval(this.facedetection)
        console.log("타이머 종료됨.")
      }, 5000);
      
      $("#video2").get(0).pause();

      // var canvas = document.createElement("canvas");
      // canvas.width = video.videoWidth * scale;
      // canvas.height = video.videoHeight * scale;
      // canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
 
      // var img = document.createElement("img");
      // img.src = canvas.toDataURL();
      // $output.prepend(img);
    },

    play() {
      $("#video2").get(0).play()
    },

    close() {
      video2.pause()
      this.localStream.getTracks()[0].stop()
      
      this.dialog = false
    }
  },

  mounted() {
    console.log("Signup.vue mounted.")
    console.log("flag : " + this.flag)
    $("#video2").bind("loadedmetadata", function () {
        displaySize = { width: this.scrollWidth, height: this.scrollHeight };
        console.log("hi")

        async function detect() {
          console.log("detect")
          const MODEL_URL = "/models";

          // await faceapi.loadSsdMobilenetv1Model(MODEL_URL);
          // await faceapi.loadFaceLandmarkModel(MODEL_URL);
          // await faceapi.loadFaceRecognitionModel(MODEL_URL);
          await faceapi.nets.ssdMobilenetv1.loadFromUri("/models");
          await faceapi.nets.faceLandmark68Net.loadFromUri("/models");
          await faceapi.nets.faceRecognitionNet.loadFromUri("/models");

          // let canvasTag = $("#canvas").get(0);

          let facedetection = setInterval(async () => {
            console.log("detecting...")
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

            // const maxDescriptorDistance = 0.6;
            // const faceMatcher = new faceapi.FaceMatcher(
            //   labeledFaceDescriptors,
            //   maxDescriptorDistance
            // );

            // const results = fullFaceDescriptions.map((fd) =>
            //   faceMatcher.findBestMatch(fd.descriptor)
            // );

            // results.forEach((bestMatch, i) => {
            //   const box = fullFaceDescriptions[i].detection.box;
            //   const text = bestMatch.toString();
            //   const drawBox = new faceapi.draw.DrawBox(box, { label: text });
            //   drawBox.draw(canvasTag);
            // });
          }, 1000);

          console.log(displaySize);
        } // end method detect

        detect();
      });
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

#btn-signup {
  display: inline-block; 
  width: 250px;
  font-size: 16px; 
  color: rgb(255, 255, 255); 
  text-align: center; 
  line-height: 2.5em; 
  border-radius: 4px; 
  background-color: rgb(52, 152, 219);
}

#btn-home {
  display:inline-block;
  width: 250px;
  font-size: 16px;
  color: rgb(64, 64, 64);
  text-align: center;
  line-height: 2.5em;
  border-radius: 4px;
  background-color: rgb(224, 224, 224);
}

.v-dialog {
    position: absolute;
    bottom: 0;
    right: 0;
}

div {
  font-family: 'Jua', sans-serif;
  font-size: 30px;
  color: black;
  line-height: 1.5;
}

.overlay {
  position: absolute;

}

/* video#bgvid {
    position: absolute;
    z-index: 0;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
} */

</style>

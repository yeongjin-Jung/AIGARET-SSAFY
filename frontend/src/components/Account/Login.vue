<template>
  <v-main id="container" style="background-color: #fcfeff" class="fill-height">
    <v-container style="height: 100%" class="fill-height">

      <!-- <div class="fill-height" style="margin: auto;"> -->
          <v-row>
            <!-- 로그인 -->
            <v-col cols="5" height="100%">
              
              <v-spacer></v-spacer>

              <v-form>
                <h3 style="text-align: center;">AIGARET</h3>
                <h5 style="text-align: center;">AI Game Rehabilitation Trainer</h5>
                <v-text-field v-model="loginData.id" dark filled background-color="rgb(52, 63, 87)" label="ID" name="login" style="margin-top: 30px;" append-icon="mdi-account" type="text" @keypress.enter="login(loginData)"></v-text-field>
                <v-text-field v-model="loginData.password" dark filled background-color="rgb(52, 63, 87)" id="Password" label="Password" name="password" append-icon="mdi-lock" type="password" @keypress.enter="login(loginData)"></v-text-field>
              </v-form>
              
              <div class="float-left">
                <v-spacer></v-spacer>
                  <v-btn id="btn-login-id" class="mr-3" @click="login(loginData)">아이디로 로그인</v-btn>
                  <v-btn id="btn-login-face" class="mr-3" @click="login(loginData)">얼굴인식으로 로그인</v-btn>
                  <!-- <v-btn id="btn-login-face" class="mr-3" @click="signupDialog = true">회원가입</v-btn> -->
                  <Signup />
              </div>
            
            </v-col>

            <v-spacer></v-spacer>

            <v-col>
              <!-- <div style="float: left; width: 533px; height: 400px; margin: 20px auto; background: black;">
                <video id="video" height="400" autoplay muted></video>
              </div> -->
              <img src="@/assets/image1.png" width="400px" height="400px">
              <h3 style="margin-bottom: 40px; text-align: center;">자택에서도 재미있게 재활을!</h3>
            </v-col>
          </v-row>
      <!-- </div> -->

      

      <!-- <div style="width: 533px; margin: 20px auto;">
        <div style="display:inline-block; width: 250px; font-size: 16px; color: rgb(255, 255, 255); text-align: center; line-height: 2.5em; border-radius: 4px; background-color: #53cde2;">로그인</div>
        <div style="display:inline-block; width: 33px;"></div>
        <div style="display:inline-block; width: 250px; font-size: 16px; color: rgb(255, 255, 255); text-align: center; line-height: 2.5em; border-radius: 4px; background-color: #005792;" @click="signup()">회원가입</div>
        <div style="font-size:16px; color: rgb(41, 90, 221); text-decoration:underline;" @click="loginModal = !loginModal">아이디로 로그인하기</div>

        <v-dialog v-model="loginModal" persistent max-width="500px">
        <ValidationObserver ref="observer" v-slot="{invalid}">
          <v-card class="elevation-12">
            <v-toolbar dark flat>
              <v-toolbar-title>LogIn</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <v-form>

                <ValidationProvider mode="eager" v-slot="{ errors }" name="Id" rules="required">
                  <v-text-field
                    v-model="loginData.id"
                    :error-messages="errors"
                    label="ID"
                    name="id"
                    
                    prepend-icon="mdi-account"
                  ></v-text-field>
                </ValidationProvider>

                <ValidationProvider mode="eager" v-slot="{ errors }" name="Password" rules="required">
                  <v-text-field
                    v-model="loginData.password"
                    :error-messages="errors"
                    label="Password"
                    name="password"
                    type="password"
                    prepend-icon="mdi-lock"
                  ></v-text-field>
                </ValidationProvider>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" @click="loginModal = !loginModal; login(loginData)" :disabled="invalid">Login</v-btn>
              <v-btn @click="loginModal = !loginModal">Close</v-btn>
            </v-card-actions>
          </v-card>
        </ValidationObserver>
      </v-dialog>
      
      </div> -->

    </v-container>
  </v-main>
</template>

<script>
import { ValidationObserver, ValidationProvider, setInteractionMode, extend } from 'vee-validate'
import { required, email } from 'vee-validate/dist/rules';

import { mapState, mapActions } from 'vuex';

import Signup from '@/components/Account/Signup'

extend('required', {
  ...required,
  message: '{_field_} 값은 반드시 입력해야 합니다.',
})

export default {
  name: 'Login',

  components: {
    ValidationProvider,
    ValidationObserver,
    Signup
  },

  data () {
    return {
      signupDialog: false,
      video: document.getElementById('video'),
      localStream: "",
      faceapi: null,
      loginData: {
        id: "",
        password: ""
      }
    }
  },

  methods: {
    ...mapActions([
      'login'
    ]),

    startVideo (val) {
      navigator.getUserMedia(
        { video: true },
        stream => { val.srcObject = stream; this.localStream = stream },
        err => console.error(err)
      )
    },

    stopVideo(val) {
      video.pause();
      this.localStream.getTracks()[0].stop();
    },

    signup() {
      this.stopVideo(video)
      this.$router.push({name: "Signup"})
    },
  },

  mounted () {
    // const video = document.getElementById('video')
    // this.startVideo(video)

    // const recaptchaScript = document.createElement('script')
    // recaptchaScript.setAttribute('type', 'javascript')
    // recaptchaScript.setAttribute('defer', '')
    // recaptchaScript.setAttribute('src', 'face-api.min.js')
    // document.head.appendChild(recaptchaScript)

    // Promise.all([
    //   faceapi.nets.tinyFaceDetector.loadFromUri('/models'),
    //   faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
    //   faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
    //   faceapi.nets.faceExpressionNet.loadFromUri('/models')
    // ]).then(this.startVideo)

    // video.addEventListener('play', () => {
    //   const canvas = faceapi.createCanvasFromMedia(video)
    //   document.body.append(canvas)
    //   const displaySize = { width: video.width, height: video.height }
    //   faceapi.matchDimensions(canvas, displaySize)
    //   setInterval(async () => {
    //     const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
    //     const resizedDetections = faceapi.resizeResults(detections, displaySize)
    //     canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    //     faceapi.draw.drawDetections(canvas, resizedDetections)
    //     faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
    //     // faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
    //   }, 100)
    // })
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

/* html, body {
  background-color: #d1f4fa
} */

/* #container {
  margin:0 auto;
  background-color: #d1f4fa
} */

div {
  font-family: 'Jua', sans-serif;
  font-size: 30px;
  color: black;
  line-height: 1.5;
}

#btn-login-id {
  padding: 20px;
  background-color: #53cde2;
  color: white;
  outline:none;
}

#btn-login-face {
  padding: 20px;
  background-color: #005792;
  color: white;
  outline:none;
}

#btn-signup {
  padding: 20px;
  background-color: #324ec9;
  color: white;
  outline:none;
}

</style>

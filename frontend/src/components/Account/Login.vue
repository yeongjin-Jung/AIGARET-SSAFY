<template>
  <div>
    <div style="width: 400px; height: 90px; margin: auto;">
        <div style="font-weight: bold; font-size: 36px; text-align: center;" class="">AIGARET</div>
        <div style="font-weight: bold; font-size: 24px; text-align: center;" class="">AI Game Rehabilitation Trainer</div>
    </div>

    <div style="width: 533px; height: 400px; margin: 20px auto; background: black;">
      <video id="video" height="400" autoplay muted></video>
    </div>

    <div style="width: 533px; margin: 20px auto;">
      <div style="display:inline-block; width: 250px; font-size: 16px; color: rgb(255, 255, 255); text-align: center; line-height: 2.5em; border-radius: 4px; background-color: #53cde2;">로그인</div>
      <div style="display:inline-block; width: 33px;"></div>
      <div style="display:inline-block; width: 250px; font-size: 16px; color: rgb(64, 64, 64); text-align: center; line-height: 2.5em; border-radius: 4px; background-color: rgb(224, 224, 224);" @click="signup()">회원가입</div>

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
    </div>
  </div>
</template>

<script>
import { ValidationObserver, ValidationProvider, setInteractionMode, extend } from 'vee-validate'
import { required, email } from 'vee-validate/dist/rules';

import { mapState, mapActions } from 'vuex';

extend('required', {
  ...required,
  message: '{_field_} 값은 반드시 입력해야 합니다.',
})

export default {
  name: 'Login',

  components: {
    ValidationProvider,
    ValidationObserver,
  },

  data () {
    return {
      faceapi: null,
      loginModal: "",
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
        stream => { val.srcObject = stream },
        err => console.error(err)
      )
    },

    signup() {
      this.$router.push({name: "Signup"})
    },
  },

  mounted () {
    const video = document.getElementById('video')
    this.startVideo(video)

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
</style>

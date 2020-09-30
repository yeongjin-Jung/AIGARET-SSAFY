<template>
  <v-container fluid class="text-center">
    <div>
      <div id="outer" class="row">

        <div id="inner_left" class="col-md-4" style="background-color: transparent; height: 400px; display: flex; justify-content: center; flex-wrap: wrap;">

          <!-- 사진! -->
          <div style="width: 400px; height: 300px; background-color: transparent; text-align: center">
            <v-img :src="img" width="400px" height="300px"></v-img>
          </div>

          <div style="display: inline-block">
            <!-- 비밀번호 변경 -->
            <v-dialog v-model="dialog_change_password" width="500" persistent>
              <template v-slot:activator="{ on, attrs }">
                <v-btn class="ma-2" dark v-bind="attrs" v-on="on" style="background: #53cde2">
                  <v-icon>mdi-account-edit</v-icon>
                </v-btn>
              </template>

              <v-card>
                <ValidationObserver v-slot="{ invalid }">
                  <v-card-title class="headline justify-center" style="background: #BBBBFF">
                    <p class="ma-2" style="color: white; font-family: CookieRun-Bold">비밀번호 변경</p>
                  </v-card-title>

                  <v-card-text>
                    <v-form class="ma-4" ref="form" @submit.prevent>
                      <v-text-field v-model="userInfo.old_password" label="현재 비밀번호" name="password" type="password" required style="font-family: CookieRun-Bold"></v-text-field>

                      <ValidationProvider mode="eager" v-slot="{ errors }" name="NewPassword" vid="confirmation" :rules="{ required: true, min: 4 }">
                        <v-text-field v-model="userInfo.new_password" :error-messages="errors" label="변경할 비밀번호" name="newPassword" type="password" style="font-family: CookieRun-Bold"></v-text-field>
                      </ValidationProvider>

                      <ValidationProvider mode="eager" v-slot="{ errors }" name="NewPasswordConfirm" rules="required|confirmed:confirmation">
                        <v-text-field v-model="userInfo.new_passwordConfirm" :error-messages="errors" label="비밀번호 확인" name="newPasswordConfirm" type="password" style="font-family: CookieRun-Bold" @keypress.enter="changePassword(userInfo); clearForm()"></v-text-field>
                      </ValidationProvider>
                    </v-form>
                  </v-card-text>

                  <v-card-actions>  
                    <div style="width: 100%; margin: 0 10px; text-align: center">
                      <v-btn color="primary" style="margin: 10px 10px; font-family: CookieRun-Bold" @click="changePassword(userInfo); clearForm()" :disabled="invalid" >변경</v-btn>
                      <v-btn color="error" style="margin: 10px 10px font-family: CookieRun-Bold" @click="dialog_change_password = false; clearForm()">취소</v-btn>
                    </div>
                  </v-card-actions>
                </ValidationObserver>
              </v-card>
            </v-dialog>

            <!-- 사진 변경 -->
            <v-dialog v-model="dialog_change_image" width="500" persistent>
              <template v-slot:activator="{ on, attrs }">
                <v-btn class="ma-2" dark v-bind="attrs" v-on="on" @click="videoStart()" style="background: #005792">
                  <v-icon>mdi-camera-retake</v-icon>
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="headline justify-center" style="background: #BBBBFF">
                  <p class="ma-2" style="color: white; font-family: CookieRun-Bold">사진 변경</p>
                </v-card-title>

                <v-card-text style="padding-bottom: 10px">
                  <div class="my-2" style="display: flex; justify-content: center; align-items: center">
                    <video id="video" width="400" height="300" autoplay muted></video>
                    <canvas id="canvas" width="400" height="300" style="position: absolute"></canvas>
                  </div>

                  <div class="my-2" style="display: flex; justify-content: center;">
                    <v-btn class="mx-2" fab @click="videoPauseAndCapture">
                      <v-icon>mdi-camera</v-icon>
                    </v-btn>
                    <v-btn class="mx-2" fab @click="videoResume">
                      <v-icon>mdi-refresh</v-icon>
                    </v-btn>
                  </div>
                  <v-divider></v-divider>

                  <div class="my-2" style="display: flex; justify-content: center">
                    <v-btn class="mx-2" color="error" @click="changePicture" :disabled="!isCaptured" style="font-family: CookieRun-Bold">변경</v-btn>
                    <v-btn class="mx-2" color="primary" @click="cancelChangingPicture" style="font-family: CookieRun-Bold">취소</v-btn>
                  </div>
                </v-card-text>
              </v-card>
            </v-dialog>
          </div>
        </div>

        <div id="inner_right" class="col-md-8" style="background-color: transparent; height: 400px">
          <!-- 이름 및 아이디 -->
          <div class="ma-2" style="background-color: transparent;">
            <p class="text-md-left font-weight-bold" style="font-size: 2rem; font-family: CookieRun-Bold;">관리자(이름)</p>&emsp;
            <p class="text-md-left font-weight-bold" style="font-size: 1rem; text-indent: 2rem; font-family: CookieRun-Bold;">Administrator(아이디)</p>
          </div>

          <!-- 내 게임 진행 현황 -->
          <div class="ma-2 pa-1" style="background-color: transparent;">
            <p class="text-md-left font-weight-bold" style="font-size: 2rem; font-family: CookieRun-Bold;">진행 현황</p>
            <v-progress-circular class="mx-10 my-2" color="green lighten-2" :size="100" :width="15" value="60" style="font-family: CookieRun-Bold">팔</v-progress-circular>
            <v-progress-circular class="mx-10 my-2" color="blue lighten-2" :size="100" :width="15" value="30" style="font-family: CookieRun-Bold">다리</v-progress-circular>
            <v-progress-circular class="mx-10 my-2" color="pink lighten-2" :size="100" :width="15" value="80" style="font-family: CookieRun-Bold">몸</v-progress-circular>
          </div>
        </div>
      </div>

      <!-- </v-row> -->
    </div>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex'

import $ from 'jquery'
import * as faceapi from 'face-api.js'

import { extend, ValidationObserver, setInteractionMode, ValidationProvider } from 'vee-validate'
import { required, email, max, min, regex, confirmed } from 'vee-validate/dist/rules'

extend('required', {
  ...required,
  message: '{_field_} 값은 반드시 입력해야 합니다.'
})

extend('confirmed', {
  ...confirmed,
  message: '비밀번호가 같지 않습니다.'
})

extend('min', {
  ...min,
  message: '{_field_} 값은 최소 {length}자리 이상이어야 합니다.'
})

export default {
  components: {
    ValidationObserver,
    ValidationProvider
  },

  data () {
    return {
      dialog_my_info: '',
      dialog_change_password: '',
      dialog_change_image: '',

      video: document.getElementById('video'),
      canvas: document.getElementById('canvas'),
      localStream: '',

      userInfo: {
        old_password: '',
        new_password: '',
        new_passwordConfirm: ''
      },

      videoFlag: false,
      timerId: null,

      isCaptured: false,

      img: this.$store.state.userInfo.profile_image
    }
  },

  methods: {
    ...mapActions(['changePassword']),

    videoStart () {
      this.videoFlag = true

      navigator.getUserMedia(
        { video: {} },
        stream => {
          video.srcObject = stream
          this.localStream = stream
        },
        err => console.error(err)
      )
    },

    videoPauseAndCapture () {
      this.isCaptured = true
      const video = this.video
      const canvas = this.canvas

      $('#video').get(0).pause()
      var ctx = canvas.getContext('2d')

      if (this.timerId != null) { clearInterval(this.timerId) }

      ctx.drawImage(video, 0, 0, canvas.width, canvas.height)
      // console.log(canvas.toDataURL())

      const base64Encoded = canvas.toDataURL()
      // console.log(base64Encoded)
    },

    videoResume () {
      this.isCaptured = false

      if (this.timerId != null) { clearInterval(this.timerId) }

      $('#video').get(0).play()
    },

    async faceDetect () {
      console.log('this.video.width', this.video.width)
      console.log('this.video.height', this.video.height)

      const video = this.video
      const canvas = this.canvas

      const displaySize = { width: video.width, height: video.height }
      faceapi.matchDimensions(canvas, displaySize)

      await faceapi.nets.ssdMobilenetv1.loadFromUri('/models')
      await faceapi.nets.faceLandmark68Net.loadFromUri('/models')
      await faceapi.nets.faceRecognitionNet.loadFromUri('/models')
      await faceapi.nets.faceExpressionNet.loadFromUri('/models')

      this.timerId = setInterval(async () => {
        console.log('계속 도는 중.')
        const detections = await faceapi.detectAllFaces(video).withFaceLandmarks().withFaceExpressions()
        const resizedDetections = faceapi.resizeResults(detections, displaySize)
        canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
        faceapi.draw.drawDetections(canvas, resizedDetections)
        faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
        faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
      }, 100)
    },

    changePicture () {
      // 멈춰있는 사진 백에 전송.
    },

    cancelChangingPicture () {
      this.isCaptured = false
      this.localStream.getTracks()[0].stop()
      if (this.timerId != null) { clearInterval(this.timerId) }
      setTimeout(() => {
        this.dialog_change_image = false
      }, 500)

      this.videoFlag = false
    },

    clearForm() {
      this.$refs.form.reset()
    }
  },

  mounted () {
    // console.log('Info.vue mounted.')
    // console.log('this.video', this.video)
    // console.log('this.canvas', this.canvas)
    // console.log("this.img : ", this.img)
  },

  updated () {
    console.log('Info.vue updated.')
    console.log('updated - videoFlag : ', this.videoFlag)

    if (this.videoFlag == true) {
      this.video = document.getElementById('video')
      this.canvas = document.getElementById('canvas')

      this.faceDetect()
    } else {
      this.video = null
      this.canvas = null

      console.log('video tag : ', this.video)
      console.log('canvas tag : ', this.canvas)
    }
  },

  computed: {
    getUserProfileImage() {
      return this.$store.getters.getUserProfileImage;
    }
  }
}
</script>

<style>
.basil {
  background-color: #fcfeff !important;
}
.basil--text {
  color: #356859 !important;
}
</style>

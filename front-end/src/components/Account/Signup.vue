<template>
  <v-dialog v-model="dialog" width="400" height="900" persistent>
  <!-- <v-dialog v-model="dialog"  height="1000px" persistent> -->
    
    <template v-slot:activator="{ on, attrs }">
      <v-btn v-bind="attrs" v-on="on" class="ml-5" style="max-width:100%; height:6vh; padding: 20px; color: white; outline:none; background-color: #324ec9" @click="clickedSignupBtn()"><span style="font-family:NanumBarunGothic; font-size:2.5vh; font-weight:bold;">회원가입</span></v-btn>
    </template>

    <div id="outer"  style="background-color: #fcfeff; margin-left:0; margin-right:0; justify-content: center; height: 630px;">

      <div id="div_left" style="margin:auto; text-align:center">

        <ValidationObserver ref="observer" v-slot="{ invalid }">
          <v-card width="" flat outlined style="background-color: #fcfeff; !important; border-color: white !important; float: left; height: 100%">

            <v-card-title class="justify-center" style="background-color: #005792; color: white; font-family: CookieRun-Bold;">회원가입</v-card-title>

            <v-card-text>
              <v-form class="ma-4" ref="form">
                <ValidationObserver>
                  <ValidationProvider mode="eager" v-slot="{ errors }" name="아이디" rules="required">
                    <v-text-field id="id" v-model="signupData.username" :error-messages="errors" label="아이디" style="font-family: CookieRun-Regular; font-size:27px;" required>
                      <template v-slot:append-outer>
                        <v-btn outlined small rounded color="error" :disabled="signupData.username == ''" @click="checkIdDuplicate(signupData.username); isIdDuplicatedCheck = true; isIdDuplicatedCheckBtnCliked = true">중복확인</v-btn>
                      </template>
                    </v-text-field>
                  </ValidationProvider>
                </ValidationObserver>
                
                <v-alert dense outlined type="error" v-show="showAlert && isIdDuplicated" style="font-size: 20px">이미 가입된 아이디입니다.</v-alert>
                <v-alert dense outlined type="success" v-show="showAlert && !isIdDuplicated && isIdDuplicatedCheckBtnCliked" style="font-size: 20px">사용 가능한 아이디입니다.</v-alert>

                <ValidationProvider mode="eager" v-slot="{ errors }" name="비밀번호" vid="confirmation" :rules="{ required: true, min: 4 }">
                  <v-text-field v-model="signupData.password" :error-messages="errors" label="비밀번호" name="password" type="password" style="font-family: CookieRun-Regular; font-size:27px;"></v-text-field>
                </ValidationProvider>

                <ValidationProvider mode="eager" v-slot="{ errors }" name="비밀번호 확인" rules="required|confirmed:confirmation">
                  <v-text-field v-model="signupData.confirm_password" :error-messages="errors" label="비밀번호 확인" name="passwordConfirm" type="password" style="font-family: CookieRun-Regular; font-size:27px;"></v-text-field>
                </ValidationProvider>

                <ValidationProvider mode="eager" v-slot="{ errors }" name="이름" rules="required|max:10">
                  <v-text-field v-model="signupData.name" :counter="10" :error-messages="errors" label="이름" required style="font-family: CookieRun-Regular; font-size:27px;"></v-text-field>
                </ValidationProvider>

                <ValidationProvider mode="eager" v-slot="{ errors }" name="나이" rules="required|numeric|max:2">
                  <v-text-field v-model="signupData.age" :error-messages="errors" label="나이" name="age" style="font-family: CookieRun-Regular; font-size:27px;"></v-text-field>
                </ValidationProvider>
            <!-- <div style="width: 100%; margin: 0 10px; float: left; text-align: center"> -->
                
                <ValidationProvider mode="eager" v-slot="{ errors }" name="목표시간" rules="required|numeric|max:3">
                  <v-text-field v-model="signupData.goal_time" :error-messages="errors" label="일주일 목표시간" name="goal_time" style="font-family: CookieRun-Regular; font-size:27px;"></v-text-field>
                </ValidationProvider>
                
              <!-- <v-btn color="primary" style="margin: 10px 10px" :disabled="invalid || isIdDuplicated || !isIdDuplicatedCheck || !isCaptured" @click="signup(signupData); cancelChangingPicture()">회원가입</v-btn> -->
              <v-btn color="primary" style="margin: 10px 10px" :disabled="invalid || isIdDuplicated || !isIdDuplicatedCheck" @click="signup(signupData)">회원가입</v-btn>
              <v-btn color="error" style="margin: 10px 10px" @click="cancelChangingPicture">돌아가기</v-btn>
            <!-- </div> -->
              </v-form>
            </v-card-text>
          </v-card>
        </ValidationObserver>

      </div>

      <!-- 오른쪽 웹캠 div -->
      <!-- height: 717-->
      <!-- <div id="div_right" style="background: #fcfeff; text-align: center; padding-top:90px;">

        <div class="my-2" style="display: flex; justify-content: center; align-items: center;">
          <video id="video" width="400" height="300" autoplay muted style="background: black"></video>
          <canvas id="canvas" class="overlay" width="400" height="300"></canvas>
        </div>

        <div class="my-2" style="display: flex; justify-content: center;">
          <p style="padding: 15px auto; font-size: 27px; font-family: CookieRun-Bold;">얼굴이 잘 인식되도록 <br>화면 가운데 위치시켜주세요.</p>
        </div>

        <div class="my-2" style="display: flex; justify-content: center; ">
          <v-btn class="mx-2" fab dark  color="primary" @click="videoPauseAndCapture">
            <v-icon dark >mdi-camera</v-icon>
          </v-btn>
          <v-btn class="mx-2" fab dark  color="error" @click="videoResume">
            <v-icon dark>mdi-refresh</v-icon>
          </v-btn>
        </div>
      </div> -->

    </div>

  </v-dialog>
</template>

<script>
import $ from 'jquery'
import * as faceapi from './face-api-min'

import { extend, ValidationObserver, setInteractionMode, ValidationProvider } from 'vee-validate'
import { required, email, max, min, regex, confirmed, numeric } from 'vee-validate/dist/rules'

import { mapState, mapActions, mapGetters } from 'vuex'

import base64Encoded from './aigaret_logo'

const canvas = require('canvas')

extend('required', {
  ...required,
  message: '{_field_}은(는) 반드시 입력해야 합니다.'
})

extend('regex', {
  ...regex,
  message: '비밀번호는 4자리 이상이어야 합니다.'
})

extend('max', {
  ...max,
  message: '{_field_}은(는) {length}자리 이하로 입력해주세요.'
})

extend('min', {
  ...min,
  message: '{_field_}은(는) 최소 {length}자리 이상이어야 합니다.'
})

extend('confirmed', {
  ...confirmed,
  message: '비밀번호가 같지 않습니다.'
})

extend('numeric', {
  ...numeric,
  message: '{_field_}은(는) 숫자여야 합니다.'
})

const userStore = 'userStore'

export default {
  name: 'Signup',

  components: {
    ValidationProvider,
    ValidationObserver
  },

  data () {
    return {
      dialog: false,
      facedetection: '',
      video: null,
      canvas: null,
      localStream: '',

      signupData: {
        username: '',
        name: '',
        age: '',
        password: '',
        confirm_password: '',
        goal_time: '',
        profile_image: base64Encoded.key
      },

      isCaptured: false,
      timerId: null,
      videoFLag: false,

      isIdDuplicatedCheck: false,
      isIdDuplicatedCheckBtnCliked: false,
      localStream: ''
    }
  },

  props: {
    flag: false
  },

  watched () {
    if (this.flag == true) {
      this.dialog = true
    } else {
      this.dialog = false
    }
  },
  
  computed: {
    ...mapGetters(userStore, ['isIdDuplicated', 'showAlert'])
  },

  updated () {
    // console.log('Signup.vue updated.')

    // if (this.videoFlag == true) {
    //   this.video = document.getElementById('video')
    //   this.canvas = document.getElementById('canvas')

    //   this.faceDetect()
    // } else {
    //   this.video = null
    //   this.canvas = null
    // }
  },

  methods: {
    ...mapActions(userStore, ['signup', 'checkIdDuplicate']),
    
    movePage() {
      this.$router.push({name: "Login"})
    },

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
      // var canvas = document.getElementById('canvas')
      var ctx = canvas.getContext('2d')

      // if (this.timerId != null) {
      //   clearInterval(this.timerId)
      // }

      ctx.drawImage(video, 0, 0, canvas.width, canvas.height)
      // console.log(canvas.toDataURL())

      const base64Encoded = canvas.toDataURL()
      // console.log(base64Encoded)
      // this.$store.commit('SET_IMG', base64Encoded)
      this.signupData.profile_image = base64Encoded
    },

    videoResume () {
      this.isCaptured = false

      // if (this.timerId != null)
      //   clearInterval(this.timerId)

      $('#video').get(0).play()
    },

    clickedSignupBtn () {
      // console.log('회원가입 버튼 클릭됨.')

      // this.videoStart()
    },

    async faceDetect () {
      // console.log('this.video.width', this.video.width)
      // console.log('this.video.height', this.video.height)

      const video = this.video
      const canvas = this.canvas

      const displaySize = { width: video.width, height: video.height }
      faceapi.matchDimensions(canvas, displaySize)

      await faceapi.nets.ssdMobilenetv1.loadFromUri('/models')
      await faceapi.nets.faceLandmark68Net.loadFromUri('/models')
      await faceapi.nets.faceRecognitionNet.loadFromUri('/models')
      await faceapi.nets.faceExpressionNet.loadFromUri('/models')

      this.timerId = setInterval(async () => {
        // console.log('계속 도는 중.')
        const detections = await faceapi.detectAllFaces(video).withFaceLandmarks().withFaceExpressions()
        const resizedDetections = faceapi.resizeResults(detections, displaySize)
        canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
        faceapi.draw.drawDetections(canvas, resizedDetections)
        faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
        faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
      }, 100)
    },

    stopDetecting() {
      if (this.timerId != null)
        clearInterval(this.timerId)
    },

    cancelChangingPicture() {
      // this.isCaptured = false
      // this.localStream.getTracks()[0].stop()
      // if (this.timerId != null) { clearInterval(this.timerId) }
      // setTimeout(() => {
      //   this.dialog = false
      //   this.videoFlag = false
      //   this.clearForm()
      //   this.$store.state.userStore.showAlert = false
      // }, 500)

      this.dialog = false
      this.clearForm()
      this.$store.state.userStore.showAlert = false
    },

    clearForm() {
      this.$refs.form.reset()
    }
  },
}
</script>

<style scoped>
/* @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap'); */

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
  overflow: hidden;
  white-space: nowrap;
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
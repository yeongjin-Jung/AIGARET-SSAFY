<template>
  <v-dialog v-model="dialog" width="880" height="900" persistent>
  <!-- <v-dialog v-model="dialog"  height="1000px" persistent> -->

    <template v-slot:activator="{ on, attrs }">
      <v-btn v-bind="attrs" v-on="on" class="mr-2" style="max-width:100%; height:6vh; padding: 20px; color: white; outline:none; background-color: #324ec9" @click="clickedSignupBtn()"><span style="font-family:NanumBarunGothic; font-size:2.5vh; font-weight:bold;">회원가입</span></v-btn>
    </template>

    <div id="outer"  style="background-color: #fcfeff; margin-left:0; margin-right:0; justify-content: center; height:530px;">

      <div id="div_left" style="margin:auto; text-align:center">

        <ValidationObserver ref="observer" v-slot="{ invalid }">
          <v-card width="50%" flat outlined style="background-color: #fcfeff; !important; border-color: white !important; float: left; height: 100%">

            <v-card-title class="justify-center" style="background-color: #005792; color: white; font-family: CookieRun-Bold;">회원가입</v-card-title>

            <v-card-text>
              <v-form class="ma-4">
                <ValidationObserver>
                  <ValidationProvider mode="eager" v-slot="{ errors }" name="Id" rules="required">
                    <v-text-field id="id" v-model="signupData.id" :error-messages="errors" label="아이디" style="font-family: CookieRun-Regular; font-size:27px;" required>
                      <template v-slot:append-outer>
                        <v-btn outlined small rounded>중복확인</v-btn>
                      </template>
                    </v-text-field>
                  </ValidationProvider>
                </ValidationObserver>

                <!-- <v-alert dense outlined type="error">이미 가입된 아이디입니다.</v-alert> -->
                <ValidationProvider mode="eager" v-slot="{ errors }" name="Password" vid="confirmation" :rules="{ required: true, min: 8, regex: /^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]/ }">
                  <v-text-field v-model="signupData.password" :error-messages="errors" label="비밀번호" name="password" type="password" style="font-family: CookieRun-Regular; font-size:27px;"></v-text-field>
                </ValidationProvider>

                <ValidationProvider mode="eager" v-slot="{ errors }" name="PasswordConfirm" rules="required|confirmed:confirmation">
                  <v-text-field v-model="signupData.passwordConfirm" :error-messages="errors" label="비밀번호 확인" name="passwordConfirm" type="password" style="font-family: CookieRun-Regular; font-size:27px;"></v-text-field>
                </ValidationProvider>

                <ValidationProvider mode="eager" v-slot="{ errors }" name="Name" rules="required|max:10">
                  <v-text-field v-model="signupData.name" :counter="10" :error-messages="errors" label="이름" required style="font-family: CookieRun-Regular; font-size:27px;"></v-text-field>
                </ValidationProvider>

                <ValidationProvider mode="eager" v-slot="{ errors }" name="Age" rules="required">
                  <v-text-field v-model="signupData.age" :error-messages="errors" label="나이" name="age" style="font-family: CookieRun-Regular; font-size:27px;"></v-text-field>
                </ValidationProvider>
            <!-- <div style="width: 100%; margin: 0 10px; float: left; text-align: center"> -->
              <v-btn color="primary" style="margin: 10px 10px" :disabled="invalid || !isCaptured" @click="signup(signupData); stopDetecting()">회원가입</v-btn>
              <v-btn color="error" style="margin: 10px 10px" @click="cancelChangingPicture">돌아가기</v-btn>
            <!-- </div> -->
              </v-form>
            </v-card-text>
          </v-card>
        </ValidationObserver>

      </div>

      <!-- 오른쪽 웹캠 div -->
      
      <div id="div_right" style="background: #fcfeff; text-align: center; height:100%; padding-top:30px;">

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
      </div>

    </div>

  </v-dialog>
</template>

<script>
import $ from 'jquery'
import * as faceapi from './face-api-min'

import { extend, ValidationObserver, setInteractionMode, ValidationProvider } from 'vee-validate'
import { required, email, max, min, regex, confirmed } from 'vee-validate/dist/rules'

import { mapActions } from 'vuex'

const canvas = require('canvas')

extend('required', {
  ...required,
  message: '{_field_} 값은 반드시 입력해야 합니다.'
})

extend('email', {
  ...email,
  message: '{_field_} 형식이 아닙니다.'
})

extend('regex', {
  ...regex,
  message: '비밀번호는 영문, 숫자, 특수기호를 모두 포함하여야 합니다.'
})

extend('max', {
  ...max,
  message: '{_field_} 값은 {length}자리 이하로 입력해주세요.'
})

extend('min', {
  ...min,
  message: '{_field_} 값은 최소 {length}자리 이상이어야 합니다.'
})

extend('confirmed', {
  ...confirmed,
  message: '비밀번호가 같지 않습니다.'
})

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
        id: '',
        password: '',
        passwordConfirm: '',
        name: '',
        age: ''
      },

      isCaptured: false,
      timerId: null,
      videoFLag: false
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

  methods: {
    ...mapActions(['signup']),
    
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
      console.log(base64Encoded)
    },

    videoResume () {
      this.isCaptured = false

      // if (this.timerId != null)
      //   clearInterval(this.timerId)

      $('#video').get(0).play()
    },

    clickedSignupBtn () {
      console.log('회원가입 버튼 클릭됨.')

      this.videoStart()
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

    stopDetecting() {
      if (this.timerId != null)
        clearInterval(this.timerId)
    },

    cancelChangingPicture() {
      this.isCaptured = false
      this.localStream.getTracks()[0].stop()
      if (this.timerId != null) { clearInterval(this.timerId) }
      setTimeout(() => {
        this.dialog = false
      }, 500)

      this.videoFlag = false
    }
  },

  mounted() {
  },

  updated () {
    console.log('Signup.vue updated.')

    if (this.videoFlag == true) {
      this.video = document.getElementById('video')
      this.canvas = document.getElementById('canvas')

      this.faceDetect()
    } else {
      this.video = null
      this.canvas = null
    }
  }
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
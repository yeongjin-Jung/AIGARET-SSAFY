<template>
  <v-container fluid class="fill-height">
    <v-row style="text-align: center;">
      <!-- 로그인 -->
      <v-flex> 
        <v-form>
          <p style="text-align: center; font-size:11vh; font-family: CookieRun-Bold;">AIGARET</p>
          <p style="text-align: center; font-size:4vh; font-family: CookieRun-Regular; font-weight: 500;">AI Game Rehabilitation Trainer</p>
          <v-text-field v-model="loginData.username" dark filled background-color="#005792" label="ID" name="login" style="margin-top: 30px;" append-icon="mdi-account" type="text" @keypress.enter="login(loginData)"></v-text-field>
          <v-text-field v-model="loginData.password" dark filled background-color="#005792" id="Password" label="Password" name="password" append-icon="mdi-lock" type="password" @keypress.enter="login(loginData)"></v-text-field>
        </v-form>

        <div>
          <v-btn id="btn-login-id" class="mr-5" @click="login(loginData)" style="height:6vh;"><span style="font-family:NanumBarunGothic; max-width:100%; font-size:2.5vh; font-weight:bold;">로그인</span></v-btn>
          <!-- <v-btn id="btn-login-face" class="mr-3" @click="loginWithFace()">얼굴인식으로 로그인</v-btn> -->
          <!-- <v-btn id="btn-login-face" class="mr-3" @click="signupDialog = true">회원가입</v-btn> -->
          <!-- <FaceLogin /> -->
          <Signup />
        </div>
      </v-flex>
    </v-row>
  </v-container>
</template>

<script>
import { ValidationObserver, ValidationProvider, setInteractionMode, extend } from 'vee-validate'
import { required, email } from 'vee-validate/dist/rules'

import { mapState, mapActions } from 'vuex'

import Signup from './Signup'
import FaceLogin from './FaceLogin'

extend('required', {
  ...required,
  message: '{_field_} 값은 반드시 입력해야 합니다.'
})

export default {
  name: 'Login',

  components: {
    ValidationProvider,
    ValidationObserver,
    Signup,
    FaceLogin
  },

  data () {
    return {
      signupDialog: false,
      video: document.getElementById('video'),
      localStream: '',
      faceapi: null,
      loginData: {
        username: "",
        password: ""
      },

      loginWithFaceButtonClicked: false,

      icons: [
        'login-image1.png',
        'login-image2.png'
      ],

      slides: [
        'slide1',
        'slide2'
      ]
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

    stopVideo (val) {
      video.pause()
      this.localStream.getTracks()[0].stop()
    },

    signup () {
      this.stopVideo(video)
      this.$router.push({name: "Signup"})
    },

    loginWithFace() {
      this.loginWithFaceButtonClicked = true

    }
  },

  mounted () {
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
.v-text-field{
      width: 35vw;
      margin: auto;
}

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
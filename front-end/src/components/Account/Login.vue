<template>
  <v-main id="container" class="fill-height">
    <v-container style="height: 100%" class="fill-height">

      <!-- <div class="fill-height" style="margin: auto;"> -->
          <v-row>
            <!-- 로그인 -->
            <v-col cols="6" height="100%">
              
              <v-spacer></v-spacer>

              <v-form>
                <h3 style="text-align: center;">AIGARET</h3>
                <h5 style="text-align: center;">AI Game Rehabilitation Trainer</h5>
                <v-text-field v-model="loginData.username" dark filled background-color="rgb(52, 63, 87)" label="ID" name="login" style="margin-top: 30px;" append-icon="mdi-account" type="text" @keypress.enter="login(loginData)"></v-text-field>
                <v-text-field v-model="loginData.password" dark filled background-color="rgb(52, 63, 87)" id="Password" label="Password" name="password" append-icon="mdi-lock" type="password" @keypress.enter="login(loginData)"></v-text-field>
              </v-form>
              
              <div class="float-left">
                <v-spacer></v-spacer>
                  <v-btn id="btn-login-id" class="mr-3" @click="login(loginData)">아이디로 로그인</v-btn>
                  <!-- <v-btn id="btn-login-face" class="mr-3" @click="loginWithFace()">얼굴인식으로 로그인</v-btn> -->
                  <!-- <v-btn id="btn-login-face" class="mr-3" @click="signupDialog = true">회원가입</v-btn> -->
                  <FaceLogin />
                  <Signup />
              </div>
            
            </v-col>

            <v-spacer></v-spacer>

            <v-col cols="6">
              <!-- <div style="float: left; width: 533px; height: 400px; margin: 20px auto; background: black;">
                <video id="video" height="400" autoplay muted></video>
              </div> -->
              
              <v-carousel :continuous="true" :cycle="true" :show-arrows="false" hide-delimiter-background delimiter-icon="mdi-minus" height="100%">
                <v-carousel-item v-for="(slide, i) in slides" :key="i">
                  <v-row class="fill-height" style="margin: 0 15px 0 15px;" align="center" justify="center">
                    <v-img :src="require('@/assets/' + icons[i])" aspect-ratio="1" max-width="400" max-height="400"></v-img>
                    <h3 style="margin-bottom: 40px; text-align: center;">{{ slides[i] }} </h3>
                  </v-row>
                </v-carousel-item>
              </v-carousel>

              <!-- <img src="@/assets/login-pose2.png" width="400px" height="400px"> -->
              <!-- <v-img src="@/assets/login-pose2.png" width="400px" height="400px"></v-img> -->
              <!-- <v-img :src="require('@/assets/' + icons[1])" width="400px" height="400px"></v-img>
              <h3 style="margin-bottom: 40px; text-align: center;">자택에서도 재미있게 재활을!</h3> -->
            </v-col>
          </v-row>

    </v-container>
  </v-main>
</template>

<script>
import { ValidationObserver, ValidationProvider, setInteractionMode, extend } from 'vee-validate'
import { required, email } from 'vee-validate/dist/rules';

import { mapState, mapActions } from 'vuex';

import Signup from '@/components/Account/Signup'
import FaceLogin from '@/components/Account/FaceLogin'

extend('required', {
  ...required,
  message: '{_field_} 값은 반드시 입력해야 합니다.',
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
      localStream: "",
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

    stopVideo(val) {
      video.pause();
      this.localStream.getTracks()[0].stop();
    },

    signup() {
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
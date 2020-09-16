<template>
  <div id="container">
    <div style="height: 400px; background: black; float: left; width: 49%">
      <video id="video" height="400" autoplay muted></video>
    </div>
      
    <div style="float:left; width:49%">
      <ValidationObserver ref="observer">
        <v-card class="elevation-12">
          <!-- <v-toolbar dark flat>
            <v-toolbar-title class="ml-4">SignUp</v-toolbar-title>
          </v-toolbar> -->
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
            </v-form>
          </v-card-text>
          <!-- <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions> -->
        </v-card>
      </ValidationObserver>
    </div>
    <div style="width: 533px; margin: 50px auto;">
      <div id="btn-signup" @click="signup(signupData)">회원가입</div>
      <div id="btn-home" @click="movePage()">돌아가기</div>
    </div>
  </div>
</template>

<script>
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
      signupData: {
        id: "",
        password: "",
        passwordConfirm: "",
        name: "",
        age: ""
      }
    }
  },

  methods: {
    movePage() {
      this.$router.push({name: "Home"})
    }
  }
};
</script>

<style scoped>
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
</style>

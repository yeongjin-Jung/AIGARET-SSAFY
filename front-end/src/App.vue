<template>
  <v-app>
    
    <Nav />
    
    <v-container fluid class="fill-height" id="container_login" v-if="!isLoggedIn">
      <Login />
    </v-container>
    
    <!-- <v-main id="mainApp" class="pa-4 text-center" style="border: white dashed; background-color: black;"><span style="color: white">App.vue > v-main</span> -->
    <v-main id="mainApp" v-else style="padding: ;" > 
      <v-container fluid class="fill-height" style="position:absolute; top:0px; padding:0px;">
        <router-view />
        <Footer />
      </v-container>
    </v-main>

  </v-app>
</template>

<script>
import Nav from '@/components/Layout/Nav'
import Footer from '@/components/Layout/Footer'
import Login from '@/components/Account/Login'

export default {
  name: "App",
  
  components: {
    Nav,
    Footer,
    Login
  },

  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  }
};
</script>

<style lang="scss">
@font-face {
  font-family: CookieRun-Bold;
  src: url("assets/CookieRun-Bold.ttf");
}

#mainApp {
  background-image: url("assets/bluemoon.png");
  background-size : cover;

}

#container_login{
  background-image: url("assets/bluemoon.png");
  background-size : cover;

  // height: 85vh; 컴포넌트화로 무의미해진듯, 삭제예정
}

</style>

<template>
  <v-app>
    
    <Nav />
    
    <Login v-if="!isLoggedIn" id="background_cover" />
    
    <v-main v-if="isLoggedIn" id="background_cover"> 
      <v-container fluid class="fill-height">
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

@font-face {
  font-family: CookieRun-Regular;
  src: url("assets/CookieRun-Regular.ttf");
}

@font-face {
  font-family: NanumBarunGothic;
  src: url("assets/NanumBarunGothic.ttf");
}

@font-face {
  font-family: NanumBarunGothic-Bold;
  src: url("assets/NanumBarunGothicBold.ttf");
}

#background_cover {
  background-image: url("assets/bluemoon.png");
  background-size : cover;
}
</style>

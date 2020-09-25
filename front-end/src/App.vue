<template>
  <v-app style="background: #FCFCFF;">
    <Nav />

    <!-- <v-main id="mainApp" class="pa-4 text-center" style="border: white dashed; background-color: black;"><span style="color: white">App.vue > v-main</span> -->
    <v-main id="mainApp">
      <v-container fluid class="fill-height">
        <router-view />
      </v-container>
    </v-main>

    <Footer />
  </v-app>
</template>

<script>
import Nav from '@/components/Layout/Nav'
import Footer from '@/components/Layout/Footer'

export default {
  name: "App",
  components: {
    Nav,
    Footer
  },
};
</script>

<style lang="scss">
@font-face {
  font-family: CookieRun-Bold;
  src: url("assets/CookieRun-Bold.ttf");
}

#mainApp{
  background-image: url("assets/bluemoon.png");
  background-size : cover;
  // height: 85vh; 컴포넌트화로 무의미해진듯, 삭제예정
}

img{
  opacity: 1;
}
</style>


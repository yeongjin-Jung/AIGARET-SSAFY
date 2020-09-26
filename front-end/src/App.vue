<template>
  <v-app>
    <Nav />
    <!-- <v-main id="mainApp" class="pa-4 text-center" style="border: white dashed; background-color: black;"><span style="color: white">App.vue > v-main</span> -->
    <v-main id="mainApp">
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

#mainApp {
  background-image: url("assets/bluemoon.png");
  background-size : cover;
}
</style>


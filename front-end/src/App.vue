<template>
  <v-app style="background: #FCFCFF;">
    <v-main id="mainApp">
      <Nav />
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
  height: 100vh;
}

img{
  opacity: 1;
}
</style>


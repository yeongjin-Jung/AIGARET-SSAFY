<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <router-link to="/">
        <v-btn text style="">
          <span class="routerLink mr-2 ml-2">Home</span>
        </v-btn>
      </router-link>

      <router-link to="/login" style="text-decoration: none;">
        <v-btn text style="height: 99%; outline:none;">
          <span class="routerLink mr-2 ml-2">Login</span>
        </v-btn>
      </router-link>

      <router-link to="/game" style="text-decoration: none;">
        <v-btn text style="height: 99%; outline:none;">
          <span class="routerLink mr-2 ml-2">Game</span>
        </v-btn>
      </router-link>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <HelloWorld msg="Welcome to Your AIGARET"/>
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',

  components: {
    HelloWorld
  },

  data: () => ({
    //
  })
}
</script>

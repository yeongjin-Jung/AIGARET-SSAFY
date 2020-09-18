<template>
  <v-app>
    <!-- <v-app-bar app color="primary" dark>
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

      <router-link to="/" style="text-decoration: none;">
        <v-btn text>
          <span>Home</span>
        </v-btn>
      </router-link>

      <router-link to="/login" style="text-decoration: none;">
        <v-btn text>
          <span>Login</span>
        </v-btn>
      </router-link>

      <router-link to="/game" style="text-decoration: none;">
        <v-btn text>
          <span>Game</span>
        </v-btn>
      </router-link>

      <v-spacer />

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar> -->

    <v-main>
    <!-- <v-main class="pa-4 text-center" style="border: white dashed; background-color: black;"><span style="color: white">App.vue > v-main</span> -->
      <v-container fluid class="fill-height">
        <router-view />
      </v-container>
    </v-main>
  
    <v-footer app padless>
    <!-- <v-footer app style="border: white dashed; background-color: black;"> -->
      <v-bottom-navigation
        :value="activeBtn"
        color="#53cde2"
        horizontal
      >
        <v-btn
          v-for="(icon, index) in icons"
          :key="index"
          height="56"
          class="pa-0 mx-4"
        >
          <h1>{{ icon.title }}</h1>
          <v-icon x-large>{{ icon.img }}</v-icon>
        </v-btn>
      </v-bottom-navigation>
    </v-footer>
  </v-app>
</template>

<script>
// import Login from '@/components/Account/Login'

export default {
  name: 'App',

  components: {
    // Login
  },

  data: () => ({
    activeBtn: 1,
    icons: [
      {
        title: 'Recents',
        img: 'mdi-history',
      },
      {
        title: 'Favorites',
        img: 'mdi-heart',
      },
      {
        title: 'Nearby',
        img: 'mdi-map-marker',
      },
    ],
  })
}
</script>

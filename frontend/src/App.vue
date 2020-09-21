<template>
  <v-app style="background: #FCFCFF">
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
          class="pa-4"
        >
          <h2>{{ icon.title }}</h2>
          <v-icon large>{{ icon.img }}</v-icon>
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
        title: 'Profile',
        img: 'mdi-card-account-details',
      },
      {
        title: 'Report',
        img: 'mdi-history',
      },
      {
        title: 'Settings',
        img: 'mdi-application-cog',
      },
    ],
  })
}
</script>

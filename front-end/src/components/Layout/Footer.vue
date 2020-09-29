<template>
  <v-container fluid style="position: absolute; bottom: 3vh;">
    <v-row justify="center">
      <router-link v-for="(icon, index) in icons" :key="index" :to="icon.url" style="text-decoration: none;">
        <v-btn fab color="#edf9fc" class="mx-4" style="height: 9vh; width: 4.5vw;">
          <v-icon size="5vh">{{ icon.img }}</v-icon>
        </v-btn>
      </router-link>
      <v-btn fab color="#edf9fc" class="mx-4" style="height: 9vh; width: 4.5vw;" @click="logout()">
        <v-icon size="5vh">mdi-logout</v-icon>
      </v-btn>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Footer',
  
  data () {
    return {
      icons: [
        {
          title: 'Home',
          img: 'mdi-home',
          url: '/'
        },
        {
          title: 'Profile',
          img: 'mdi-card-account-details',
          url: 'info'
        },
        {
          title: 'Rank',
          img: 'mdi-trophy',
          url: 'rank'
        },
      ]
    }
  },

  methods: {
    ...mapActions(['logout']),
  }
}
</script>

<style>
</style>

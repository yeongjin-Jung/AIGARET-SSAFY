<template>
  <v-container v-if="this.$route.name == 'Home'" fluid class="text-center" style="position:absolute; bottom:3vh;">
    <v-row no-gutters align="center" justify="center">
      <v-col v-for="(icon, index) in icons" :key="index" cols="1" align="center">
        
        <v-btn v-if="index == 2" fab color="#edf9fc" @click="logout()" style="text-decoration: none; height:10vh; width:5vw;" >
          <v-icon style="font-size: 3.5vh;">mdi-login</v-icon>
        </v-btn>

        <router-link v-else :to="icon.url" style="text-decoration: none; ">
          <v-btn fab color="#edf9fc" style="height:10vh; width:5vw;"><v-icon style="font-size: 3.5vh;"  >{{ icon.img }}</v-icon></v-btn>
        </router-link>

      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Footer',

  data () {
    return {
      activeBtn: 1,
      icons: [
        {
          title: 'Profile',
          img: 'mdi-card-account-details',
          url: 'info'
        },
        {
          title: 'Rank',
          img: 'rank',
          url: 'rank'
        },
        // {
        //   title: 'Report',
        //   img: 'mdi-history',
        //   url: 'report'
        // },
        // {
        //   title: 'Settings',
        //   img: 'mdi-application-cog',
        //   url: '/'
        // },
        {}
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

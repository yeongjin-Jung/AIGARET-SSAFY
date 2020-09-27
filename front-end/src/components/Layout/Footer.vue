<template>
  <v-container v-if="this.$route.name == 'Home'" fluid class="text-center">
    <v-row no-gutters align="center" justify="center">
      <v-col v-for="(icon, index) in icons" :key="index" cols="1" align="center">
        <router-link :to="icon.url" style="text-decoration: none;">
          <v-btn fab color="#edf9fc"><v-icon>{{ icon.img }}</v-icon></v-btn>
        </router-link>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
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
          title: 'Report',
          img: 'mdi-history',
          url: 'report'
        },
        {
          title: 'Settings',
          img: 'mdi-application-cog',
          url: '/'
        }
      ]
    }
  }
}
</script>

<style>
</style>

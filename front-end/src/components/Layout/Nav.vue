<template>
  <v-system-bar app color="orange" style="height: 5vh;">
    <router-link to="/" style="text-decoration: none;">
      <v-btn icon tile style="margin-left: 10px; height:3.5vh; margin-top: 1px; margin-left: 10px;"><v-icon style="font-size: 5vh;" >mdi-home</v-icon></v-btn>
    </router-link>
    <p
      style="font-size: 4.4vh; white-space:nowrap; font-weight: 600; margin-top: 16px; margin-left: 10px; display:inline; font-family: CookieRun-Bold;"
    >AIGARET</p>
    <v-spacer></v-spacer>
    <p v-if="isLoggedIn" style="font-size: 3.5vh; white-space:nowrap; font-weight: 600; margin-right: 50px; margin-top:16px;">
      {{ $store.state.userStore.userInfo.name }}님 환영합니다.
    </p>
    <p
      style="font-size: 3.5vh; white-space:nowrap; font-weight: 600; margin-right: 50px; margin-top:16px;"
    >{{this.date}}</p>
    <p
      style="font-size: 3.5vh; white-space:nowrap; font-weight: 600; margin-right: 20px; margin-top:16px;"
    >{{this.dateTime}}</p>
  </v-system-bar>
</template>

<script>
import { mapGetters } from 'vuex'

const userStore = 'userStore'

export default {
  name: 'Nav',

  data () {
    return {
      date: null,
      dateTime: null
    }
  },
  mounted() {
    console.log('this.$store.state : ', this.$store.state)
    console.log('this.$store.state.userStore : ', this.$store.state.userStore)
    console.log('tihs.$store.state.userStore.userInfo.name : ', this.$store.state.userStore.userInfo.name)
  },

  methods: {
    getNow: function() {
      const today = new Date();

      this.date =
        today.getFullYear() +
        '-' +
        (today.getMonth() + 1) +
        '-' +
        today.getDate()

      var hour = 0
      var minute = 0
      if (today.getHours() > 12) {
        hour = today.getHours() - 12
        if (today.getMinutes() < 10) {
          minute = '0' + today.getMinutes()
        } else {
          minute = today.getMinutes()
        }
        const time = hour + ':' + minute
        const dateTime = time + ' pm'
        this.dateTime = dateTime
      } else if (today.getHours() < 12) {
        hour = today.getHours()
        if (today.getMinutes() < 10) {
          minute = '0' + today.getMinutes()
        } else {
          minute = today.getMinutes()
        }
        const time = hour + ':' + minute
        const dateTime = time + ' am'
        this.dateTime = dateTime
      } else {
        hour = today.getHours()
        if (today.getMinutes() < 10) {
          minute = '0' + today.getMinutes()
        } else {
          minute = today.getMinutes()
        }
        const time = hour + ':' + minute
        const dateTime = time + ' pm'
        this.dateTime = dateTime
      }
    }
  },

  computed: {
    ...mapGetters(userStore, ['isLoggedIn']),
    // isLoggedIn() {
    //   return this.$store.getters.isLoggedIn;
    // }
  },

  created() {
    setInterval(this.getNow, 1000);
  }
}
</script>

<style>
</style>

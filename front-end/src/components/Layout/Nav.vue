<template>
  <v-system-bar app color="orange" style="height: 5vh;">
    <!-- <router-link to="/" style="text-decoration: none;">
      <v-btn icon style="margin-left:20px;"><v-icon style="font-size : 4.5vh;" >mdi-home</v-icon></v-btn>
    </router-link> -->
    <!-- <img
      src="https://w7.pngwing.com/pngs/981/645/png-transparent-default-profile-united-states-computer-icons-desktop-free-high-quality-person-icon-miscellaneous-silhouette-symbol.png"
      style="margin-left: 40px; width: 2vw; height: 3vh;"
    /> -->
    <p
      style="font-size: 3.5vh; white-space:nowrap; font-weight: 600; margin-top: 12px; margin-left: 10px; display:inline; font-family: CookieRun-Bold;"
    >AIGARET</p>
    <v-spacer></v-spacer>
    <p v-if="isLoggedIn" style="font-size: 3.5vh; white-space:nowrap; font-weight: 600; margin-right: 50px; margin-top:16px;">
      {{ $store.state.id }}님 환영합니다.
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
export default {
  name: 'Nav',

  data () {
    return {
      date: null,
      dateTime: null
    }
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
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  },

  created() {
    setInterval(this.getNow, 1000);
  }
}
</script>

<style>
</style>

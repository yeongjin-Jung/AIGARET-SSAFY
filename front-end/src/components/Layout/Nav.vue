<template>
  <v-system-bar app color="orange" style="height: 5vh">
    <router-link to="/" style="text-decoration: none;">
      <v-btn icon><v-icon>mdi-home</v-icon></v-btn>
    </router-link>
    <img
      src="https://w7.pngwing.com/pngs/981/645/png-transparent-default-profile-united-states-computer-icons-desktop-free-high-quality-person-icon-miscellaneous-silhouette-symbol.png"
      style="margin-left: 8px; width: 4.15vw; height: 5vh;"
    />
    <p
      style="font-size: 3.5vh; white-space:nowrap; font-weight: 600; margin-top: 12px; margin-left: 30px; display:inline; font-family: CookieRun-Bold;"
    >불타는 붕어빵</p>
    <v-spacer></v-spacer>
    <p v-if="isLoggedIn">
      {{ $store.state.id}}님 환영합니다.
    </p>
    <p
      style="font-size: 3.5vh; white-space:nowrap; font-weight: 600; margin-right: 50px; margin-top:16px;"
    >{{this.date}}</p>
    <p
      style="font-size: 3.5vh; white-space:nowrap; font-weight: 600; margin-right: 20px; margin-top:16px;"
    >{{this.dateTime}}</p>
    <v-btn v-if="isLoggedIn" @click="logout()">
      로그아웃
    </v-btn>
  </v-system-bar>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  name: 'Nav',

  data () {
    return {
      date: null,
      dateTime: null
    }
  },

  methods: {
    ...mapActions(['logout']),

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

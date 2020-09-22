<template>
  <v-app style="background: #FCFCFF;">
    <v-main id="mainApp">
      <v-system-bar
        color="orange"
        
        :lights-out="lightsOut"
        :window="window"
        style="position : absolute; width:100%; height : 7vh"
      >
        <img
          src="https://w7.pngwing.com/pngs/981/645/png-transparent-default-profile-united-states-computer-icons-desktop-free-high-quality-person-icon-miscellaneous-silhouette-symbol.png"
          style="margin-left : 40px; width : 3vw; height: 5vh;"
        />
        <p
          style="font-size: 3.5vh; white-space:nowrap; font-weight: 600; margin-left: 30px; margin-top:15px; display:inline; font-family: CookieRun-Bold;"
        >불타는 붕어빵</p>
        <v-spacer></v-spacer>
        <p
          style="font-size: 3.5vh; white-space:nowrap; font-weight: 600; margin-right: 100px; margin-top:15px;"
        >{{this.date}}</p>
        <p
          style="font-size: 3.5vh; white-space:nowrap; font-weight: 600; margin-right: 20px; margin-top:15px;"
        >{{this.dateTime}}</p>
      </v-system-bar>
      <!-- <v-main class="pa-4 text-center" style="border: white dashed; background-color: black;"><span style="color: white">App.vue > v-main</span> -->
      <v-container fluid class="fill-height">
        <router-view />
      </v-container>
    </v-main>

    <v-footer app padless style="height : 10vh;">
      <!-- <v-footer app style="border: white dashed; background-color: black;"> -->
      <v-bottom-navigation :value="activeBtn" color="#53cde2" horizontal style="height : 10vh;">
        <router-link v-for="(icon, index) in icons" :key="index" :to="icon.url" style="text-decoration: none; color: #53cde2; height : 10vh;">
          <v-btn style="height: 10vh;">
            <p style="font-size: 3vh; margin-top : 10px; ">{{ icon.title }}</p>
            <v-icon style="font-size: 5vh;">{{ icon.img }}</v-icon>
          </v-btn>
        </router-link>
      </v-bottom-navigation>
    </v-footer>
  </v-app>
</template>

<script>
// import Login from '@/components/Account/Login'

export default {
  name: "App",

  components: {
    // Login
  },

  data: () => ({
    date: null,
    dateTime: null,
    height: 90,
    lightsOut: false,
    window: false,
    timestamp: "",
    activeBtn: 1,
    icons: [
      {
        title: "Profile",
        img: "mdi-card-account-details",
        url: "myinfo",
      },
      {
        title: "Report",
        img: "mdi-history",
        url: "report",
      },
      {
        title: "Settings",
        img: "mdi-application-cog",
        url: "/",
      },
    ],
  }),

  created() {
    setInterval(this.getNow, 1000);
  },

  methods: {
    getNow: function () {
      const today = new Date();

      this.date =
        today.getFullYear() +
        "-" +
        (today.getMonth() + 1) +
        "-" +
        today.getDate();

      var hour = 0;
      var minute = 0;
      if (today.getHours() > 12) {
        hour = today.getHours() - 12;
        if (today.getMinutes() < 10) {
          minute = "0" + today.getMinutes();
        } else {
          minute = today.getMinutes();
        }
        const time = hour + ":" + minute;
        const dateTime = time + " pm";
        this.dateTime = dateTime;

      } else if (today.getHours() < 12) {
        hour = today.getHours();
        if (today.getMinutes() < 10) {
          minute = "0" + today.getMinutes();
        } else {
          minute = today.getMinutes();
        }
        const time = hour + ":" + minute;
        const dateTime = time + " am";
        this.dateTime = dateTime;

      } else {
        hour = today.getHours();
        if (today.getMinutes() < 10) {
          minute = "0" + today.getMinutes();
        } else {
          minute = today.getMinutes();
        }
        const time = hour + ":" + minute;
        const dateTime = time + " pm";
        this.dateTime = dateTime;
      }
    },
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
  
}

img{
  opacity: 1;
}
</style>


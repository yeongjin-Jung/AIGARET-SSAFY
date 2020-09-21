<template>
  <v-app style="background: #FCFCFF">
    <v-main>
      <v-system-bar
        color="orange"
        :height="height"
        :lights-out="lightsOut"
        :window="window"
        style="position : absolute; width:100%;"
      >
        <img
          src="https://w7.pngwing.com/pngs/981/645/png-transparent-default-profile-united-states-computer-icons-desktop-free-high-quality-person-icon-miscellaneous-silhouette-symbol.png"
          width="75"
          height="75"
          style="margin-left : 40px;"
        />
        <p style="font-size: 50px; font-weight: 600; margin-left: 30px; margin-top:20px;">불타는 붕어빵</p>
        <v-spacer></v-spacer>
        <p style="font-size: 50px; font-weight: 600; margin-right: 100px; margin-top:15px;">{{this.date}}</p>
        <p style="font-size: 50px; font-weight: 600; margin-right: 20px; margin-top:15px;">{{this.dateTime}}</p>
      </v-system-bar>
      <!-- <v-main class="pa-4 text-center" style="border: white dashed; background-color: black;"><span style="color: white">App.vue > v-main</span> -->
      <v-container fluid class="fill-height">
        <router-view />
      </v-container>
    </v-main>

    <v-footer app padless>
      <!-- <v-footer app style="border: white dashed; background-color: black;"> -->
      <v-bottom-navigation :value="activeBtn" color="#53cde2" horizontal>
        <v-btn v-for="(icon, index) in icons" :key="index" height="56" class="pa-4">
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
      },
      {
        title: "Report",
        img: "mdi-history",
      },
      {
        title: "Settings",
        img: "mdi-application-cog",
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
      if (today.getHours() >= 12) {
        hour = today.getHours() - 12;
        const time = hour + ":" + today.getMinutes();
        const dateTime = time + " pm";
        this.dateTime = dateTime;
      } else if (today.getHours() < 12) {
        hour = today.getHours();
        const time = hour + ":" + today.getMinutes();
        const dateTime = time + " am";
        this.dateTime = dateTime;
      }
    },
  },
};
</script>


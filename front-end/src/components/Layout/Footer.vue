<template>
  <v-footer app padless style="height: 5vh; background-color: transparent;">
    <!-- <v-footer app padless style="border: white dashed; background-color: black;"> -->
    <v-bottom-navigation :value="activeBtn" color="#53cde2" horizontal style="height: 5vh; background-color: transparent;">
      <router-link v-for="(icon, index) in icons" :key="index" :to="icon.url" style="text-decoration: none; color: #005792;">
        <v-btn style="height: 5vh;">
          <p style="font-size: 3vh; margin-top : 10px; ">{{ icon.title }}</p>
          <v-icon style="font-size: 5vh;">{{ icon.img }}</v-icon>
        </v-btn>
      </router-link>
    </v-bottom-navigation>
  </v-footer>
</template>

<script>
export default {
  name: "Footer",

  data() {
    return {
      activeBtn: 1,
      icons: [
        {
          title: "Profile",
          img: "mdi-card-account-details",
          url: "info"
        },
        {
          title: "Report",
          img: "mdi-history",
          url: "report"
        },
        {
          title: "Settings",
          img: "mdi-application-cog",
          url: "/"
        }
      ]
    };
  }
};
</script>

<style>
</style>
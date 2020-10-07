<template>
  <v-container v-if="this.$route.name == 'Home'" fluid style="position: absolute; bottom: 1vh;">
    <v-row justify="center" style="height: 20vh;">
        
      <v-hover v-slot:default="{ hover }">
        <router-link id="info" to="/info" style="text-decoration: none; margin: 2vh; width: 10vw; height: 17vh;">
          <v-card class="rounded-xl" :elevation="hover ? 12 : 0" style="width: 6.5vw; height: 13vh; margin: 1vh 1.7vw;" color="transparent"></v-card>
        </router-link>
      </v-hover>

      <v-hover v-slot:default="{ hover }">
        <router-link id="rank" to="/rank" style="text-decoration: none; margin: 2vh; width: 10vw; height: 17vh;">
          <v-card class="rounded-xl" :elevation="hover ? 12 : 0" style="width: 6.5vw; height: 13vh; margin: 1vh 1.7vw;" color="transparent"></v-card>
        </router-link>
      </v-hover>

      <v-hover v-slot:default="{ hover }">
        <router-link id="logout" to="" style="text-decoration: none; margin: 2vh; width: 10vw; height: 17vh;">
          <v-card class="rounded-xl" :elevation="hover ? 12 : 0" @click="logout()" style="width: 6.5vw; height: 13vh; margin: 1vh 1.7vw;" color="transparent"></v-card>
        </router-link>
      </v-hover>

    </v-row>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex';

const userStore = 'userStore'

export default {
  name: 'Footer',
  
  data () {
    return {
      //
    }
  },

  methods: {
    ...mapActions(userStore, ['logout']),
  }
}
</script>

<style>
#logout {
background-image: url("../../assets/menuButton/logout-red.png");
background-size : contain;
background-position: center center;
}

#info {
background-image: url("../../assets/menuButton/info-blue.png");
background-size : contain;
background-position: center center;
}

#rank {
background-image: url("../../assets/menuButton/rank-green.png");
background-size : contain;
background-position: center center;
}
</style>

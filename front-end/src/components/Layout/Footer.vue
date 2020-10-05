<template>
  <v-container v-if="this.$route.name == 'Home'" fluid style="position: absolute; bottom: 1.5vh;">
    <v-row justify="center">
        
        <router-link id="info" to="/info" style="text-decoration: none; margin-left:1.8vw; margin-right:1.8vw;">
          <v-btn icon elevation="0" style="height:18vh; width:8.7vw;"></v-btn>
        </router-link>
        
        <router-link id="rank" to="/rank" style="text-decoration: none; margin-left:2vw; margin-right:1.8vw;">
          <v-btn icon elevation="0" style="height:19.4vh; width:8.9vw;"><div></div></v-btn>
        </router-link>

        <router-link id="logout" to="" style="text-decoration: none; margin-left:1.8vw; margin-right:1.8vw;">
          <v-btn icon elevation="0" @click="logout()" style="height:18vh; width:8.9vw;" ></v-btn>
        </router-link>

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
background-size : cover;
background-color: rgba( 255, 255, 255, 0 );
}

#info {
background-image: url("../../assets/menuButton/info-blue.png");
background-size : cover;
background-color: rgba( 255, 255, 255, 0 );
}

#rank {
background-image: url("../../assets/menuButton/rank-green.png");
background-size : cover;
background-color: rgba( 255, 255, 255, 0 );
}
</style>

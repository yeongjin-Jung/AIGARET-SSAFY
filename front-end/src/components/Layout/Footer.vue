<template>
  <v-container v-if="this.$route.name == 'Home'" fluid style="position: absolute; bottom: 3vh;">
    <v-row justify="center">
        
        <router-link to="/info" style="text-decoration: none; margin-left:1.5vw; margin-right:1.5vw;">
          <v-btn id="info" elevation="0" style="height:14.5vh; width:7vw;"></v-btn>
        </router-link>

        <router-link to="/rank" style="text-decoration: none; margin-left:1.5vw; margin-right:1.5vw;">
          <v-btn id="rank" elevation="0" style="height:15.4vh; width:7vw;"></v-btn>
        </router-link>

        <v-btn id="logout" elevation="0" @click="logout()" style="height:15.2vh; width:7vw; margin-left:1.5vw; margin-right:1.5vw;" ></v-btn>

    </v-row>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Footer',
  
  data () {
    return {
      //
    }
  },

  methods: {
    ...mapActions(['logout']),
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

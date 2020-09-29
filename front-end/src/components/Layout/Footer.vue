<template>
  <v-container v-if="this.$route.name == 'Home'" fluid class="text-center" style="padding: ; position:absolute; bottom:5vh;">
    <v-row no-gutters align="center" justify="center" style="height: 12vh;">
      <!-- <v-col v-for="(icon, index) in icons" :key="index" cols="1" align="center"> -->
        
        <router-link  :to="info" style="text-decoration: none; margin-left:20px; margin-right:20px;">
          <v-btn id="info" elevation="0" style="height:14vh; width:7vw;"></v-btn>
        </router-link>


        <router-link  :to="rank" style="text-decoration: none; margin-left:20px; margin-right:20px;">
          <v-btn id="rank" elevation="0" style="height:14vh; width:7vw;"></v-btn>
        </router-link>


        <v-btn id="logout" elevation="0"  @click="logout()" style="text-decoration: none; height:14vh; width:7vw; margin-left:19px; margin-right:20px;" >
          <!-- <v-icon style="font-size: 3.5vh;">mdi-login</v-icon> -->
        </v-btn>

        
        
      <!-- </v-col> -->
    </v-row>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Footer',
  
  data () {
    return {
      activeBtn: 1,
      info : 'info',
      rank : 'rank',
    }
  },

  methods: {
    ...mapActions(['logout']),
  }
}
</script>

<style>

#logout {
background-image: url("../../assets/menuButton/logout.png");
background-size : cover;
background-color: rgba( 255, 255, 255, 0 );
}

#info {
background-image: url("../../assets/menuButton/info.png");
background-size : cover;
background-color: rgba( 255, 255, 255, 0 );
}

#rank {
background-image: url("../../assets/menuButton/rank.png");
background-size : cover;
background-color: rgba( 255, 255, 255, 0 );
}
</style>

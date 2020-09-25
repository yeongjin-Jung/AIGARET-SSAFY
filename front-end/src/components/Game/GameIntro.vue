<template>
  <div class="d-inline-block mx-auto" style="width: 100%; height:48vh;">
    <v-container fluid style="max-height: 100%;">
      <v-row style="height:42.5vh; ">
        <v-col cols="6" justify="center" align="center" style="max-height: 100%;">
          <div id="imgContainer" style="max-height: 100%;">
          <v-img src="https://cdn.vuetifyjs.com/images/cards/store.jpg" style="max-width: 100%;  max-height: 40vh; display: block;"></v-img>
          </div>
        </v-col>

        <v-col cols="6" class="text-center" style="text-align: center; background-color: rgba(254,254,255,1);"> 
          <v-row class="flex-column ma-0"  style="max-width: 100%; max-height: 70%; display: inline-block; vertical-align: middle; ">
            <p style="font-size: 3vh;">{{ gameDescription }}</p>
          </v-row>
          <v-row  class="pa-4" justify="center" align="end">
            <router-link :to="{ name: gameName }" style="text-decoration: none;">
              <v-btn text style="height: 10vh; width:10vw; background:yellow;">
                <span class="routerLink mr-2 ml-2">게임시작</span>
              </v-btn>
            </router-link>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import SERVER from '../../api/server.js';
import axios from 'axios';

export default {
  name: "GameIntro",
  components: {
    //
  },
  props: {
    gameNum: Number,
  },
  data() {
    return {
      gameName: '',
      gameDescription: '',
      gameVideo: '',
    };
  },
  methods: {
    getGameInfo() {
      axios.get(SERVER.URL + 'games/' + this.gameNum)
        .then((res) => {
          this.gameName = res.data.game_name
          this.gameDescription = res.data.game_description
          this.gameVideo = res.data.game_video
        })
        .catch((err) => console.log(err.response));
    },
  },
  mounted() {
    this.getGameInfo()
  },
};
</script>

<style>
#imgContainer{
  width: 35vw;
  height: 50vh;
  display: flex;
  justify-content: center;
}

</style>

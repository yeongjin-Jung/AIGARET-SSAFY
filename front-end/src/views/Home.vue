<template>
  <v-container fluid class="text-center mb-16">
    <!-- <v-container fluid class="pa-4 text-center" style="border: white dashed"><span style="color: white">Home.vue</span> -->
    <div v-if="gameInfo[model] == null" style="font-size: 5vh; font-weight: 600; width : 35vw; height: 7.5vh">
      <MARQUEE scrollamount="15" style="width : 35vw; color: black;">게임을 선택해주세요</MARQUEE>
    </div>
    <div v-if="gameInfo[model] != null" style="font-size: 5vh; font-weight: 600; width : 35vw; height: 7.5vh">
      <MARQUEE scrollamount="15" style="width : 35vw;">{{ gameInfo[model].game_name }}</MARQUEE>
    </div>
    <v-slide-group v-model="model" show-arrows center-active>
      <v-slide-item v-for="(item, i) in items" :key="i" v-slot:default="{ active, toggle }">
        <v-col cols="4">
          <v-hover v-slot:default="{ hover }">
            <v-card
              :elevation="hover ? 12 : 2"
              :class="{ 'on-hover': hover, 'on-active': active, 'on-minimize': model != null }"
              @click="toggle"
            >
              <v-img :src="item.img" width="100vw" height="100%">
                <v-card-title class="title white--text">
                  <v-row class="fill-height flex-column" justify="space-between">

                    <!-- <div class="align-self-center">
                      <v-btn v-for="(icon, index) in icons" :key="index" :class="{ 'show-btns': hover }" color="transparent" icon>
                        <v-icon :class="{ 'show-btns': hover }" color="transparent">{{ icon }}</v-icon>
                      </v-btn>
                    </div> -->
                  </v-row>\
                </v-card-title>
              </v-img>
            </v-card>
          </v-hover>
        </v-col>
      </v-slide-item>
    </v-slide-group>

    <v-expand-transition >
      <v-sheet v-if="model != null" style="height: 50vh; background-color: rgba(0,0,0,0);">
        <GameIntro :gameInfo="gameInfo[model]" />
      </v-sheet>
    </v-expand-transition>
  </v-container>
</template>

<script>
import SERVER from '../api/server.js'
import axios from 'axios'

import GameIntro from '@/components/Game/GameIntro.vue'

export default {
  name: 'Home',
  components: {
    GameIntro
  },
  data: () => ({
    model: null,
    icons: ['mdi-rewind', 'mdi-play', 'mdi-fast-forward'],
    items: [
      {
        img: 'https://user-images.githubusercontent.com/53737175/95080191-ae6ca300-0752-11eb-96fc-6ae89915c35c.png'
      },
      {
        img:
          'https://user-images.githubusercontent.com/53737175/95080219-b88ea180-0752-11eb-8746-30dc4ed37f00.png'
      },
      {
        img: 'https://user-images.githubusercontent.com/53737175/95080228-bd535580-0752-11eb-94cb-8adee98e6abd.png'
      },
    ],
    transparent: 'rgba(255, 255, 255, 0)',
    gameInfo: {}
  }),
  methods: {
    getGameInfo () {
      axios.get(SERVER.URL + 'games/')
        .then((res) => {
          this.gameInfo = res.data
        })
        .catch((err) => console.log(err.response))
    }
  },
  mounted() {
    this.getGameInfo()
  },
}
</script>

<style scoped>
.v-card {
  transition: opacity 0.4s ease-in-out, width 0.1s ease-in-out, height 0.25s ease-in-out;
  width: 30vw;
  height: 15vh;
}

.v-card:not(.on-minimize) {
  width: 30vw;
  height: 50vh;
  margin-bottom: 50px;
}

/* -----------한세트----------- */
.v-card:not(.on-hover) {
  opacity: 0.7;
}
/* 위아래 순서 바뀌면 안됨 */
.v-card.on-active {
  opacity: 1;
  border-style: solid;
  border-color: #ffffff;
  border-width: 8px;
}
/* --------------------------- */

.show-btns {
  color: rgba(255, 255, 255, 1) !important;
}

@font-face {
  font-family: CookieRun-Bold;
  src: url("../assets/CookieRun-Bold.ttf");
}
</style>

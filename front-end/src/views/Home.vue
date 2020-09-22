<template>
  <v-container fluid class="text-center">
    <!-- <v-container class="pa-4 text-center" style="border: white dashed"><span style="color: white">Home.vue</span> -->
    <!-- <v-row align="center" justify="center"> -->
    <!-- <v-sheet class="mx-auto" elevation="8" max-width="800"> -->
     
    <p style="font-size: 5vh; font-weight: 600; position: relative; width : 40vw;  top: 30px;">
      <MARQUEE scrollamount="15" height="100%" style="width : 30vw;">게임 제목을 입력해 주세요</MARQUEE>
      <!-- 크기 조절 -->
    </p>
    <v-slide-group v-model="model" show-arrows center-active>
      <v-slide-item v-for="(item, i) in items" :key="i" v-slot:default="{ active, toggle }">
        <v-col cols="2">
          <v-hover v-slot:default="{ hover }">
            <v-card
              :elevation="hover ? 12 : 2"
              :class="{ 'on-hover': hover, 'on-active': active, 'on-minimize': model != null }"
              @click="toggle"
            >
              <v-img :src="item.img" width="100vw" height="100%">
                <v-card-title class="title white--text">
                  <v-row class="fill-height flex-column" justify="space-between">
                    <p class="mt-4 subheading text-left">{{ item.title }}</p>

                    <div>
                      <p class="ma-0 body-1 font-weight-bold font-italic text-left">{{ item.text }}</p>
                      <p class="caption font-weight-medium font-italic text-left">{{ item.subtext }}</p>
                    </div>



                    <div class="align-self-center">
                      <v-btn
                        v-for="(icon, index) in icons"
                        :key="index"
                        :class="{ 'show-btns': hover }"
                        color="transparent"
                        icon
                      >
                        <v-icon :class="{ 'show-btns': hover }" color="transparent">{{ icon }}</v-icon>
                      </v-btn>
                    </div>
                  </v-row>
                </v-card-title>
              </v-img>
            </v-card>
          </v-hover>
        </v-col>
      </v-slide-item>
    </v-slide-group>
    
    <v-expand-transition >
      <v-sheet v-if="model != null"  style="height: 55vh; background-color: rgba(0,0,0,0);" tile >
        <!-- <v-row
          class="fill-height"
          align="center"
          justify="center"
        >-->
        <p style="font-size: 4.5vh; font-weight:700; margin-bottom:0; font-family: CookieRun-Bold;">Selected {{ model+1 }}</p>
        <!-- <div style="font-size: 20px; font-weight: 600;">
          <MARQUEE scrollamount="15" width="500px">게임 제목을 입력해 주세요</MARQUEE>
        </div> -->
        <GameIntro />
        <!-- </v-row> -->
      </v-sheet>
    </v-expand-transition>
  </v-container>
</template>

<script>
import GameIntro from "../components/Game/GameIntro.vue";

export default {
  name: "Home",
  components: {
    GameIntro,
  },
  data: () => ({
    model: null,
    icons: ["mdi-rewind", "mdi-play", "mdi-fast-forward"],
    items: [
      {
        title: "New Releases",
        text: "It's New Release Friday",
        subtext: "Newly released songs. Updated daily",
        img: "http://lorempixel.com/output/nightlife-q-c-640-480-5.jpg",
      },
      {
        title: "Rock",
        text: "Greatest Rock Hits",
        subtext: "Lose yourself in rock tunes.",
        img:
          "https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80",
      },
      {
        title: "Mellow Moods",
        text: "Ambient Bass",
        subtext: "Chill beats to mellow you out.",
        img: "http://lorempixel.com/output/abstract-q-c-640-480-6.jpg",
      },
      {
        title: "New Releases",
        text: "It's New Release Friday",
        subtext: "Newly released songs. Updated daily.",
        img: "http://lorempixel.com/output/nightlife-q-c-640-480-5.jpg",
      },
      {
        title: "Rock",
        text: "Greatest Rock Hits",
        subtext: "Lose yourself in rock tunes.",
        img:
          "https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80",
      },
      {
        title: "Mellow Moods",
        text: "Ambient Bass",
        subtext: "Chill beats to mellow you out.",
        img: "http://lorempixel.com/output/abstract-q-c-640-480-6.jpg",
      },
    ],
    transparent: "rgba(255, 255, 255, 0)",
  }),
};
</script>

<style scoped>
.v-card {
  transition: opacity 0.4s ease-in-out, width 0.1s ease-in-out, height 0.2s ease-in-out;
  width: 25vw;
  height: 15vh;
}

.v-card:not(.on-minimize) {
  width: 25vw;
  height: 37vh;
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
<template>
  <div class="d-inline-block mx-auto" style="width: 100%; height:45vh;">
    <v-container fluid style="max-height: 100%;">
      <v-row style="height:42.5vh;" justify="center">
        <v-col cols="6">
          <iframe :src="`https://youtube.com/embed/${gameInfo.game_video}`" width="70%" height="100%" allowfullscreen></iframe>
        </v-col>

        <v-col cols="6">
          <v-row class="flex-column ma-0"  style="max-width: 100%; max-height: 70%; display: inline-block; vertical-align: middle; background-color: rgba(254,254,255,0.5);">
            <div style="font-size: 3vh;">{{ gameInfo.game_description }}</div>
          </v-row>
          <v-row  class="pa-4" justify="center" align="end">
            <router-link :to="{ name: gameInfo.game_name }" style="text-decoration: none;">
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
export default {
  name: 'GameIntro',
  components: {
    //
  },
  props: {
    gameInfo: Object
  }
}
</script>

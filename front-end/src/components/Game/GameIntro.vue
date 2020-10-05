<template>
  <div class="d-inline-block mx-auto" style="width: 100%; height:45vh;">
    <v-container fluid style="max-height: 100%;">
      <v-row style="height:40vh;" justify="center">
        <v-col cols="6">
          <iframe :src="`https://youtube.com/embed/${gameInfo.game_video}`" width="70%" height="100%" allowfullscreen></iframe>
        </v-col>

        <v-col cols="6">
          <v-row class="flex-column ma-0" style="max-width: 100%; max-height: 100%; display: inline-block; vertical-align: middle; background-color: rgba(254,254,255,0.5);">
            <div style="overflow: auto; height: 32vh; font-size: 3.5vh; font-family: CookieRun-Bold">
              {{ gameInfo.game_description.slice(0, 220) }}
              <br><br>
              {{ gameInfo.game_description.slice(220,) }}
            </div>
          </v-row>
          <v-row class="pt-2" justify="center" align="end">
            <router-link :to="`/game/${ gameInfo.id }`" style="text-decoration: none;">
              <v-btn style="width: 7vw; height 5vh; font-family: CookieRun-Bold; background-color: yellow;">게임시작</v-btn>
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

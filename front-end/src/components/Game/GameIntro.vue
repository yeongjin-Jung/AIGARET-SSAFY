<template>
  <v-container fluid class="pt-0">
    <v-row style="height: 45vh;" justify="center">
      <v-col cols="6">
        <iframe :src="`https://youtube.com/embed/${gameInfo.game_video}`" width="78%" height="100%" allowfullscreen></iframe>
      </v-col>

      <v-col cols="6">
        <v-row no-gutters style="background-color: rgba(254,254,255,0.5);">
          <div style="height: 32vh; font-size: 3.5vh; font-family: CookieRun-Bold">
            {{ effect }}
            <br/><br/>
            {{ indication }}
          </div>
        </v-row>
        <v-row no-gutters class="pt-2" justify="center">
          <router-link :to="{ path: `/game${ gameInfo.id }/`, query: { gameNo: gameInfo.id } }" style="text-decoration: none;">
            <v-btn outlined style="width: 10vw; height: 8.5vh; font-size: 3vh; font-family: CookieRun-Bold; background-color: yellow;">게임시작</v-btn>
          </router-link>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'GameIntro',
  components: {
    //
  },
  props: {
    gameInfo: Object
  },
  computed: {
    effect : function () {
      var descriptArr = this.gameInfo.game_description.split('[적응증]')
      return descriptArr[0]
    },
    indication : function () {
      var descriptArr = this.gameInfo.game_description.split('[적응증]')
      return '[적응증]'+ descriptArr[1]
    }
  }
}
</script>

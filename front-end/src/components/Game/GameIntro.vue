<template>
  <div class="d-inline-block mx-auto" style="width: 100%; height:45vh;">
    <v-container fluid style="max-height: 100%;">
      <v-row style="height: 40vh;" justify="center">
        <v-col cols="6">
          <iframe :src="`https://youtube.com/embed/${gameInfo.game_video}`" width="70%" height="100%" allowfullscreen></iframe>
        </v-col>

        <v-col cols="6">
          <v-row no-gutters style="display: inline-block; vertical-align: middle; background-color: rgba(254,254,255,0.5);">
            <div style="height: 27vh; font-size: 3.5vh; font-family: CookieRun-Bold">
              {{ effect }}
              <br/>
              {{ indication }}
            </div>
          </v-row>
          <v-row no-gutters class="pt-2" justify="center" align="center">
            <router-link :to="{ path: `/game${ gameInfo.id }/`, query: { gameNo: gameInfo.id } }" style="text-decoration: none;">
              <v-btn outlined style="width: 10vw; height 10vh; font-family: CookieRun-Bold; background-color: yellow;">게임시작</v-btn>
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

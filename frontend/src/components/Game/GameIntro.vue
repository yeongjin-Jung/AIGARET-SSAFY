<template>
  <div class="d-inline-block mx-auto">
    <v-container>
      <v-row>
        <v-col cols="6" justify="center" align="center">
          <v-img height="400" width="400" src="https://cdn.vuetifyjs.com/images/cards/store.jpg"></v-img>
        </v-col>

        <v-col cols="6" class="text-center">
          <v-row class="flex-column ma-0" justify="center">
            <div>청춘의 피는 끓는다 끓는 피에 뛰노는 심장은 거선의 기관과 같이 힘있다 이것이다 인류의 역사를 꾸며 내려온 동력은 바로 이것이다 이성은 투명하되 얼음과 같으며 지혜는</div>
          </v-row>
          <v-row style="height: 80%" class="pa-4" justify="center" align="end">
            <router-link to="/game/JumpGame" style="text-decoration: none;">
              <v-btn text style="height: 100px; width:100px; background:yellow;">
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
  name: "GameIntro",
  components: {
    //
  },
};
</script>

<style>
</style>

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
            <p style="font-size: 3vh;">청춘의 피는 끓는다 끓는 피에 뛰노는 심장은 거선의 기관과 같이 힘있다 이것이다 인류의 역사를 꾸며 내려온 동력은 바로 이것이다 이성은 투명하되 얼음과 같으며 지혜는</p>
          </v-row>
          <v-row  class="pa-4" justify="center" align="end">
            <router-link to="/game/WristTouchGame" style="text-decoration: none;">
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
  name: "GameIntro",
  components: {
    //
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

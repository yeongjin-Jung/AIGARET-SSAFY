<template>
  <v-container fluid>
    <!-- <v-card style="background-color: transparent;"> -->
      <v-tabs
        background-color="transparent"
        color="#53cde2"
        centered
        fixed-tabs
      >
        <v-tab style="color: white; font-family: CookieRun-Bold; font-size: 3vh;">쥐를 잡자</v-tab>
        <v-tab style="color: white; font-family: CookieRun-Bold; font-size: 3vh;">스네이크 게임</v-tab>
        <v-tab style="color: white; font-family: CookieRun-Bold; font-size: 3vh;">환상의 점프</v-tab>

        <v-tab-item
          v-for="n in 3"
          :key="n"
        >
          <RankDetail :tabIndex="n"/>
        </v-tab-item>
      </v-tabs>
    <!-- </v-card> -->
  </v-container>
</template>

<script>
import RankDetail from './RankDetail'

export default {
  name: 'Ranking',
  components: {
    RankDetail,
  }
}
</script>

<style>

</style>
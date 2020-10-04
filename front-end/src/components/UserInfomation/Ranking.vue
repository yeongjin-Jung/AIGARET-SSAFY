<template>
  <v-container fluid>
    <!-- <v-card style="background-color: transparent;"> -->
      <v-tabs
        background-color="transparent"
        color="#53cde2"
        centered
        fixed-tabs
      >
        <v-tab style="color: white;">WristTouchGame</v-tab>
        <v-tab style="color: white;">SnakeGame</v-tab>
        <v-tab style="color: white;">JumpGame</v-tab>

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
.theme--light.v-tabs-items {
  background-color: transparent;
}
</style>
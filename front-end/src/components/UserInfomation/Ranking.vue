<template>
  <v-container fluid>
    <v-card>
      <v-tabs
        background-color="white"
        color="deep-purple accent-4"
        centered
      >
        <v-tab>WristTouchGame</v-tab>
        <v-tab>SnakeGame</v-tab>
        <v-tab>JumpGame</v-tab>

        <v-tab-item
          v-for="n in 3"
          :key="n"
        >
          <RankDetail :tabIndex="n"/>
        </v-tab-item>
      </v-tabs>
    </v-card>
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

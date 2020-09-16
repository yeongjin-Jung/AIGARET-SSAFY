<template>
  <div>
    <h2>왼쪽 Navigation</h2>
    <div v-if="true">
      <GameIntro />
    </div>
    <div v-if="false">
      <GamePlay />
    </div>
  </div>
</template>

<script>
import GameIntro from './GameIntro.vue'
import GamePlay from './GamePlay.vue'

export default {
  name: 'Game',
  components: {
    GameIntro,
    GamePlay
  }
}
</script>

<style>

</style>

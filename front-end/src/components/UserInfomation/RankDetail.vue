<template>
  <v-container fluid>
    <v-row>   <!-- v-for 지우고 작업하면 될 듯 tabIndex 가 gameNo가 될 것으로 예상, 해봐야 알 듯 -->
      <v-col
      v-for="i in 6"
      :key="i"
      cols="12"
      md="4"
      >
      <v-img
          :src="`https://picsum.photos/500/300?image=${i * tabIndex * 5 + 10}`"
          :lazy-src="`https://picsum.photos/10/6?image=${i * tabIndex * 5 + 10}`"
          aspect-ratio="1"
      ></v-img>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'RankDetail',
  props: {
    tabIndex: Number,
  }
}
</script>

<style>

</style>
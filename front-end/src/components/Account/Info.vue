<template>
  <v-container id="container" style="background-color: #fcfeff">
    <v-card color="basil" height="100%" class="mx-auto" width="1000" outlined>
      <v-card-title class="text-center justify-center py-6">
        <h1 class="font-weight-bold display-3 basil--text">내 정보 수정</h1>
      </v-card-title>

      <!-- <v-tabs v-model="tab" background-color="transparent" color="basil" :transition="fade">
        <v-tab v-for="item in items" :key="item" :transition="false">{{ item }}</v-tab>
      </v-tabs>-->

      <v-btn-toggle v-model="btn">
        <v-btn value="0">
          <span class="hidden-sm-and-down">내 정보</span>
        </v-btn>
        <v-btn value="1">
          <span class="hidden-sm-and-down">비밀번호 수정</span>
        </v-btn>
        <v-btn value="2">
          <span class="hidden-sm-and-down">내 사진 변경</span>
        </v-btn>
      </v-btn-toggle>

      <!-- <v-tabs-items v-model="tab"> -->
      <!-- <v-tab-item v-for="item in items" :key="item"> -->
      <!-- <v-card v-if="tab == 0" class="mx-auto" flat outlined style="background-color: #fcfeff; !important; border-color: white !important; height: 100%"> -->
      <v-card
        v-if="btn == 0"
        class="mx-auto"
        height="100%"
        flat
        outlined
        style="background-color: #fcfeff; !important; border-color: white !important; height: 100%"
      >
        <v-card-text>
          <v-form class="ma-4">
            <v-text-field id="id" label="아이디" required></v-text-field>
            <v-text-field label="비밀번호" name="password" type="password"></v-text-field>
            <v-text-field label="비밀번호 확인" name="passwordConfirm" type="password"></v-text-field>
            <v-text-field :counter="10" label="이름" required></v-text-field>
            <v-text-field label="나이" name="age"></v-text-field>

            <div style="width: 100%; margin: 0 10px; text-align: center">
              <v-btn color="primary" style="margin: 10px 10px">수정</v-btn>
              <v-btn color="error" style="margin: 10px 10px" @click="home()">돌아가기</v-btn>
            </div>
          </v-form>
        </v-card-text>
      </v-card>

      <v-card
        v-if="btn == 1"
        class="mx-auto"
        height="100%"
        flat
        outlined
        style="background-color: #fcfeff; !important; border-color: white !important; height: 100%"
      >
        <v-card-text>
          <v-form class="ma-4">
            <v-text-field label="현재 비밀번호" name="password" type="password" required></v-text-field>
            <v-text-field label="변경할 비밀번호" name="changedPassword" type="password"></v-text-field>
            <v-text-field label="비밀번호 확인" name="changedPasswordConfirm" type="password"></v-text-field>

            <div style="width: 100%; margin: 0 10px; text-align: center">
              <v-btn color="primary" style="margin: 10px 10px">수정</v-btn>
              <v-btn color="error" style="margin: 10px 10px" @click="home()">돌아가기</v-btn>
            </div>
          </v-form>
        </v-card-text>
      </v-card>

      <v-card
        v-if="btn == 2"
        class="mx-auto"
        height="100%"
        flat
        outlined
        style="background-color: #fcfeff; !important; border-color: white !important; height: 100%"
      >
        <div class="row">
          <!-- <div class="col d-flex justify-content-center"> -->
          <div class="col col-6" justify="center" align="center">
            <v-img height="400" width="400" src="https://cdn.vuetifyjs.com/images/cards/store.jpg"></v-img>
          </div>
          <!-- <div class="col d-flex justify-content-center"> -->
          <div class="col col-6" justify="center" align="center">
            <v-img
              height="400"
              width="400"
              src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSDg6v6e1PUuSYDyCHy55lfr9l3XkzZQ102Gg&usqp=CAU"
            ></v-img>
          </div>

          <div style="width: 100%; margin: 0 10px; text-align: center">
            <v-btn color="primary" style="margin: 10px 10px">수정</v-btn>
            <v-btn color="error" style="margin: 10px 10px" @click="home()">돌아가기</v-btn>
          </div>
        </div>
      </v-card>
      <!-- </v-tab-item> -->
      <!-- </v-tabs-items> -->
    </v-card>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      btn: 0,
      tab: null,
      items: ["내 정보", "비밀번호 변경", "내 사진 변경"],
      text:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    };
  },

  methods: {
    home() {
      this.$router.push({ path: "/" });
    },
  },
};
</script>

<style>
.basil {
  background-color: #fcfeff !important;
}
.basil--text {
  color: #356859 !important;
}
</style>
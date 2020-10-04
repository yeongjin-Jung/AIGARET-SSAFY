<template>
  <v-row no-gutters class="fill-height text-center" justify="space-around">
    <!-- <v-col id="rankboard" cols="5" style="border: green 3px dashed;"> -->
    <v-col cols="5" align-self="center"> <!-- 2분할 -->
      <v-col id="rankboard" style="height: 80vh;">
        <v-col style="width: 25vw; margin: 15vh auto 0; display: flex; justify-content: flex-end;">
          <div style="font-family: CookieRun-Bold">AIGARET 최고점수: {{ gameData[0].score }}점 ({{ gameData[0].user }})</div>
        </v-col>
        <!-- <v-row no-gutters justify="center"> -->
        <v-col id="rankdiv" v-for="n in gameDataWeek.length" :key="n" style="width: 25vw; margin: 0 auto; display: flex; justify-content: space-around;">
          <!-- <v-col  cols="1"></v-col> -->
          <v-col cols="2">
            <div id="rankfont">{{ n }}위</div>
          </v-col>
          <v-col cols="5">
            <div id="rankfont">{{ gameDataWeek[n-1].user }}님</div>
          </v-col>
          <v-spacer></v-spacer>
          <v-col cols="4">
            <div id="rankfont">{{ gameDataWeek[n-1].score }}점</div>
          </v-col>
          <!-- <v-col  cols="1"></v-col> -->
        </v-col>
        <!-- </v-row> -->
      </v-col>
    </v-col>
  </v-row>
</template>

<script>
import SERVER from "@/api/server.js";
import axios from "axios";

export default {
  name: 'RankDetail',
  data() {
    return {
      gameData: [{}],
      gameDataWeek: [{}],
      myData: [{}],
      myDataWeek: [{}],
    }
  },
  props: {
    tabIndex: Number,
  },
  methods: {
    getGameData() {
      axios.get(SERVER.URL + `games/${ this.tabIndex }/records/`, {
        params: {
          sort: 'high',
          count: 1,
          week: false
        },
      }).then((res) => {
          if (res.status === 200) {
            this.gameData = res.data
          } else {
            console.log('ErrorNo: ', res.status);
          }
        })
        .catch((err) => console.log(err));
    },
    getGameDataWeek() {
      axios.get(SERVER.URL + `games/${ this.tabIndex }/records/`, {
        params: {
          sort: 'high',
          count: 5,
          week: true
        },
      }).then((res) => {
          if (res.status === 200) {
            this.gameDataWeek = res.data
          } else {
            console.log('ErrorNo: ', res.status);
          }
        })
        .catch((err) => console.log(err));
    },
    getMyGameData() {
      axios.get(SERVER.URL + `games/${ this.tabIndex }/records/users/${this.$store.state.userStore.userInfo.userid}/`, {
        params: {
          sort: 'high',
          count: 1,
          week: false,
        },
      }).then((res) => {
          if (res.status === 200) {
            this.myData = res.data
          } else {
            console.log('ErrorNo: ', res.status);
          }
        })
        .catch((err) => console.log(err));
    },
    getMyGameDataWeek() {
      axios.get(SERVER.URL + `games/${ this.tabIndex }/records/users/${this.$store.state.userStore.userInfo.userid}/`, {
        params: {
          sort: 'high',
          count: 1,
          week: true,
        },
      }).then((res) => {
          if (res.status === 200) {
            this.myDataWeek = res.data
          } else {
            console.log('ErrorNo: ', res.status);
          }
        })
        .catch((err) => console.log(err));
    }
  },
  mounted() {
    this.getGameData()
    this.getGameDataWeek()
    this.getMyGameData()
    this.getMyGameDataWeek()
  },
}
</script>

<style>
#rankboard {
  background-image: url("../../assets/rank/Rankboard.png");
  background-size : 40vw 80vh;
}

#rankdiv {
  background-image: url("../../assets/rank/Rankdiv.png");
  background-size : 25.5vw 10vh;
}

#rankfont {
  white-space: nowrap;
  font-family: CookieRun-Bold;
  font-size: 2.5vh;
}
</style>
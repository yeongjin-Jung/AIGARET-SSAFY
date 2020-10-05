<template>
  <v-row no-gutters class="fill-height text-center" justify="center">
    
    <!-- <v-spacer></v-spacer> -->
    
    <v-col cols="5" align-self="center"> <!-- 2분할 -->
      <v-col id="rankboard" style="height: 80vh;">
        <v-col style="width: 25vw; margin: 1vh auto 0; padding: 0; display: flex; justify-content: center">
          <div style="font-family: CookieRun-Bold">{{ dateNow }} ~ {{ dateNow6 }}</div>
        </v-col>
        <v-col style="width: 25vw; margin: 11vh auto 0; padding-bottom: 0; display: flex; justify-content: flex-end;">
          <div style="font-family: CookieRun-Bold">AIGARET 최고점수: {{ gameData[0].score }}점 ({{ gameData[0].user }})</div>
        </v-col>
        <div v-if="gameDataWeek.length != 0">
          <v-col id="rankdiv" v-for="n in gameDataWeek.length" :key="n" style="width: 25vw; margin: 0 auto; display: flex; justify-content: space-around;">
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
          </v-col>
          <v-col v-if="gameDataWeek.length < 5" style="margin: 0 auto; display: flex; justify-content: center;">
            <div id="rankfont" style="margin-top: 1vh;">5위까지 {{ 5 - gameDataWeek.length }}자리 남았어요!<br>남은 기록을 어서 채워주세요!</div>
          </v-col>
        </div>
        <v-col v-if="gameDataWeek.length == 0" style="height: 50vh; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: CookieRun-Bold; font-size: 4vh;">새로운 주간이 시작되었어요<br><br>기록을 측정해주세요!</div>
        </v-col>
      </v-col>
    </v-col>

    <v-col cols="5" align-self="center"> <!-- 2분할 -->
      <v-col id="myrankboard" align="center" style="height: 60vh;">
        <v-col style="display: flex; justify-content: space-around; margin: 15vh auto 8vh;">
          <!-- <v-spacer></v-spacer> -->
          <v-col cols="6">
            <div id="myrankfont">{{ myDataWeek[0].score }}점</div>
          </v-col>
          <!-- <v-spacer></v-spacer> -->
          <v-col cols="3">
            <div id="myrankfont">{{ myDataWeek[0].score/10 }}위</div>
          </v-col>
          <!-- <v-spacer></v-spacer> -->
        </v-col>
        <v-col cols="6">
          <div id="myrankfont">{{ myData[0].score }}점</div>
        </v-col>
      </v-col>
    </v-col>

    <!-- <v-spacer></v-spacer> -->

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
      dateNow: null,
      dateNow6: null,
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
    },
    timeNow() {
      const today = new Date();
      this.dateNow =
        today.getFullYear() +
        '-' +
        ( (today.getMonth() + 1) < 10 ? '0' + (today.getMonth() + 1) : (today.getMonth() + 1) ) +
        '-' +
        ( today.getDate() < 10 ? '0' + today.getDate() : today.getDate() )
      
      const today6 = new Date(today.setDate(today.getDate() + 6));
      this.dateNow6 =
        today6.getFullYear() +
        '-' +
        ( (today6.getMonth() + 1) < 10 ? '0' + (today6.getMonth() + 1) : (today6.getMonth() + 1) ) +
        '-' +
        ( today6.getDate() < 10 ? '0' + today6.getDate() : today6.getDate() )
    },
  },
  mounted() {
    this.getGameData()
    this.getGameDataWeek()
    this.getMyGameData()
    this.getMyGameDataWeek()
    this.timeNow()
  },
}
</script>

<style>
#myrankboard {
  background-image: url("../../assets/rank/Myrank.png");
  background-size : 40vw 60vh;
}

#rankboard {
  background-image: url("../../assets/rank/Rankboard.png");
  background-size : 40vw 80vh;
}

#rankdiv {
  background-image: url("../../assets/rank/Rankdiv.png");
  background-size : 25.5vw 10vh;
}

#myrankfont {
  white-space: nowrap;
  font-family: CookieRun-Bold;
  font-size: 4vh;
}

#rankfont {
  white-space: nowrap;
  font-family: CookieRun-Bold;
  font-size: 2.7vh;
}
</style>
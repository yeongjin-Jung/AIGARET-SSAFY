<template>
  <v-row no-gutters class="fill-height text-center" justify="center">
    
    <v-col cols="5" align-self="center">
      <v-col id="rankboard" style="height: 80vh;">
        <v-col style="width: 25vw; margin: 1vh auto 0; padding: 0; display: flex; justify-content: center">
          <div style="font-family: CookieRun-Bold">{{ dateNow }} ~ {{ dateNow6 }}</div>
        </v-col>
        <v-col style="width: 25vw; margin: 11vh auto 0; padding-bottom: 0; display: flex; justify-content: flex-end;">
          <div style="font-family: CookieRun-Bold">AIGARET 역대최고점수: {{ BestScore[0].score }}점 ({{ BestScore[0].user }})</div>
        </v-col>
        <div v-if="BestScoreWeek.length != 0">
          <v-col id="rankdiv" v-for="n in BestScoreWeek.length" :key="n" style="width: 25vw; margin: 0 auto; display: flex; justify-content: space-around;">
            <v-col cols="2">
              <div id="rankfont">{{ n }}위</div>
            </v-col>
            <v-col cols="5">
              <div id="rankfont">{{ BestScoreWeek[n-1].user }}님</div>
            </v-col>
            <v-spacer></v-spacer>
            <v-col cols="4">
              <div id="rankfont">{{ BestScoreWeek[n-1].score }}점</div>
            </v-col>
          </v-col>
          <v-col v-if="BestScoreWeek.length < 5" style="margin: 0 auto; display: flex; justify-content: center;">
            <div id="rankfont" style="margin-top: 1vh;">5위까지 {{ 5 - BestScoreWeek.length }}자리 남았어요!<br>남은 기록을 어서 채워주세요!</div>
          </v-col>
        </div>
        <v-col v-if="BestScoreWeek.length == 0" style="height: 50vh; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-family: CookieRun-Bold; font-size: 4vh;">새로운 주간이 시작되었어요<br><br>기록을 측정해주세요!</div>
        </v-col>
      </v-col>
    </v-col>

    <v-col cols="5" align-self="center">
      <v-col id="myrankboard" align="center" style="height: 60vh;">
        <v-row>
          <v-spacer></v-spacer>
          <v-col cols="6">
            <div style="white-space: nowrap; font-family: CookieRun-Bold; font-size: 3vh;">
              {{ this.$store.state.userStore.userInfo.username }} 님의 점수
            </div>
          </v-col>
        </v-row>

        <v-col style="display: flex; justify-content: space-around; margin: 7vh auto 8vh;">
          <v-col cols="6">
            <div id="myrankfont" v-if="myBestScoreWeek[0]">{{ myBestScoreWeek[0].score }}점</div>
            <div id="myrankfont" v-if="!myBestScoreWeek[0]">_</div>
          </v-col>
          <v-col cols="3">
            <div id="myrankfont" v-if="myWeeklyRank">{{ myWeeklyRank }} 위</div>
            <div id="myrankfont" v-if="!myWeeklyRank">_</div>
          </v-col>
        </v-col>

        <v-col cols="6">
          <div id="myrankfont" v-if="myBestScore[0]">{{ myBestScore[0].score }}점</div>
          <div id="myrankfont" v-if="!myBestScore[0]">_</div>
        </v-col>

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
      BestScore: [{}],
      BestScoreWeek: [{}],
      myBestScore: [{}],
      myBestScoreWeek: [{}],
      myWeeklyRank: null,
      dateNow: null,
      dateNow6: null,
    }
  },
  props: {
    tabIndex: Number,
  },
  methods: {
    getWeek() {
      const newDay = new Date();
      const dayDelta = newDay.getDay() - 1
      if (newDay.getDay() === 0) {  // 일요일인 경우
        const dayDelta = 6
      }
      
      const today = new Date(newDay.setDate(newDay.getDate() - dayDelta));
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


    ////////deprecated////////
    // getGameData() {  // 역대최고점수(전체)
    //   axios.get(SERVER.URL + `games/${ this.tabIndex }/records/`, {
    //     params: {
    //       week: false,
    //       distinct: true,
    //       count: 1,
    //       sort: 'high',
    //     },
    //   }).then((res) => { if (res.status === 200) { this.BestScore = res.data } })
    //     .catch((err) => console.error(err));
    // },
    // getGameDataWeek() {  // 주간랭킹5위
    //   axios.get(SERVER.URL + `games/${ this.tabIndex }/records/`, {
    //     params: {
    //       week: true,
    //       distinct: true,
    //       count: 5,
    //       sort: 'high',
    //     },
    //   }).then((res) => { if (res.status === 200) { this.BestScoreWeek = res.data } })
    //     .catch((err) => console.error(err));
    // },
    ////////deprecated////////


    getMyBestScore() {  // 역대최고점수(본인)
      axios.get(SERVER.URL + `games/${ this.tabIndex }/records/users/${this.$store.state.userStore.userInfo.userid}/`, {
        params: {
          week: false,
          distinct: false,
          count: 1,
          sort: 'high',
        },
      }).then((res) => { if (res.status === 200) { this.myBestScore = res.data } })
        .catch((err) => console.error(err));
    },
    getMyBestScoreWeek() {  // 주간최고점수(본인)
      axios.get(SERVER.URL + `games/${ this.tabIndex }/records/users/${this.$store.state.userStore.userInfo.userid}/`, {
        params: {
          week: true,
          distinct: false,
          count: 1,
          sort: 'high',
        },
      }).then((res) => { if (res.status === 200) { this.myBestScoreWeek = res.data } })
        .catch((err) => console.error(err));
    },

    // NEW
    getMyWeeklyRank() {  // 주간랭킹(나)
      axios.get(SERVER.URL + `games/${ this.tabIndex }/rank/`, {
        params: {
          week: true,
          count: 100,
        },
      }).then((res) => {
          if (res.status === 200) {
            const arr = res.data;
            const N = arr.length;

            for (let i = 0; i < N; i++) {
              if (this.$store.state.userStore.userInfo.username === arr[i].user) {
                this.myWeeklyRank = i + 1
                break
              }
            };
          }
        })
        .catch((err) => console.error(err));
    },
    getWeeklyRank5() {  // 주간랭킹5위
      axios.get(SERVER.URL + `games/${ this.tabIndex }/rank/`, {
        params: {
          week: true,
          count: 5,
        },
      }).then((res) => { if (res.status === 200) { this.BestScoreWeek = res.data } })
        .catch((err) => console.error(err));
    },
    getBestScore() {  // 역대최고점수(전체)
      axios.get(SERVER.URL + `games/${ this.tabIndex }/rank/`, {
        params: {
          week: false,
          count: 1,
        },
      }).then((res) => { if (res.status === 200) { this.BestScore = res.data } })
        .catch((err) => console.error(err));
    },
  },
  mounted() {
    this.getWeek()  // 날짜
    // this.getGameData()
    // this.getGameDataWeek()
    this.getMyWeeklyRank()  // 내 주간 순위(for문)
    this.getMyBestScore()  // 내 최고점수(역대)
    this.getMyBestScoreWeek()  // 내 최고점수(주간)
    this.getWeeklyRank5()  // 주간랭킹5위
    this.getBestScore()  // 게임최고점수
    console.log(this.myWeeklyRank)
  },
}
</script>

<style>
#myrankboard {
  background-image: url("../../assets/rank/Myrankboard.png");
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

.theme--light.v-tabs-items {
  background-color: transparent !important
}
</style>
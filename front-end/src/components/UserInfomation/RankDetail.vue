<template>
  <v-row no-gutters class="fill-height text-center" justify="space-around">
    <v-col cols="5" align-self="center" style="border: green 3px dashed;"> <!-- 2분할 -->
      <v-row no-gutters justify="center"> <!-- 4분할 -->
        <v-col cols="6" style="display: flex; align-items: center; justify-content: center; height: 40vh;">
        <!-- cols="6" 으로 가운데 정렬 효과 -->
          
          <v-col style="border: black 3px dashed;"> <!-- v-col > v-col, 횡 => 종 변화 -->
          <!-- <v-row> 주석풀어보면 횡 변화함 알 수 있음 -->

            <v-col style="border: black 3px dashed;">
              <!-- <div style="border: black 3px dashed;">주간최고점수</div> -->
              <!-- div 대신 v-col 로 써도됨(line.16 주석 풀어볼 것), 상황에따라 횡,종 변화할 수 있음 (line.10, 22 주석풀어볼 것) -->
              <v-col style="border: red 3px dashed;">
                <!-- <v-card>
                  주간최고점수(선택한게임의 이번주 나의 최고점수) -->
                  <!-- <div style="border: black 3px dashed;">{{ myDataWeek[0].score }}</div> -->
                  <!-- <div v-for="n in myDataWeek.length" :key="n" style="border: black 3px dashed;">{{ myDataWeek[n-1].score }}</div>
                </v-card> -->
                <v-card
                  color="#005792"
                  dark
                >
                  <v-card-title class="headline">
                    주간최고점수
                  </v-card-title>

                  <v-card-text>
                    <!-- <div style="font-size: 3vh; color: white;">{{ myDataWeek[0].score }}</div> -->
                  </v-card-text>
                </v-card>
              </v-col>
              <!-- <v-col style="border: black 3px dashed;">주간최고점수</v-col> -->
            </v-col>
          
          <!-- </v-row> -->
          </v-col>
        
        </v-col>
      </v-row>
      <v-row no-gutters justify="center"> <!-- 4분할 -->
        <v-col cols="6" style="display: flex; align-items: center; justify-content: center; height: 40vh;">
        <!-- cols="6" 으로 가운데 정렬 효과 -->
          <div style="border: black 3px dashed;">
            최고점수(선택한게임의 역대 나의 최고점수)
            <div style="border: black 3px dashed;">{{ myData[0].score }}</div>
          </div>
        </v-col>
      </v-row>
    </v-col>

    <!-- <v-col id="rankboard" cols="5" style="border: green 3px dashed;"> -->
    <v-col cols="5" align-self="center"> <!-- 2분할 -->
      <v-col id="rankboard" style="height: 80vh;">
        <v-col style="width: 25vw; margin: 1vh auto 0; padding: 0; display: flex; justify-content: center">
          <div style="font-family: CookieRun-Bold">{{ dateNow }} ~ {{ dateNow6 }}</div>
        </v-col>
        <v-col style="width: 25vw; margin: 10vh auto 0; padding-bottom: 0; display: flex; justify-content: flex-end;">
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
          <div style=" font-family: CookieRun-Bold; font-size: 4vh;">새로운 주간이 시작되었어요<br><br>기록을 측정해주세요!</div>
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
    getDateStr(myDate){
      return (myDate.getFullYear() + '-' + (myDate.getMonth() + 1) + '-' + myDate.getDate())
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
<template>
  <v-row no-gutters class="fill-height text-center">
    <v-col cols="5" align-self="center"> <!-- 2분할 -->
      <v-row no-gutters justify="center"> <!-- 4분할 -->
        <v-col cols="6" style="display: flex; align-items: center; justify-content: center; height: 40vh;">
        <!-- cols="6" 으로 가운데 정렬 효과 -->
          
          <v-col style="border: black 3px dashed;"> <!-- v-col > v-col, 횡 => 종 변화 -->
          <!-- <v-row> 주석풀어보면 횡 변화함 알 수 있음 -->

            <v-col style="border: black 3px dashed;">
              <!-- <div style="border: black 3px dashed;">주간최고점수</div> -->
              <!-- div 대신 v-col 로 써도됨(line.16 주석 풀어볼 것), 상황에따라 횡,종 변화할 수 있음 (line.10, 22 주석풀어볼 것) -->
              <v-col style="border: red 3px dashed;">
                주간최고점수(선택한게임의 이번주 나의 최고점수)
                <!-- <div style="border: black 3px dashed;">{{ myDataWeek[0].score }}</div> -->
                <div v-for="n in myDataWeek.length" :key="n" style="border: black 3px dashed;">{{ myDataWeek[n-1].score }}</div>
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
            <div v-for="n in myData.length" :key="n" style="border: black 3px dashed;">{{ myData[n-1].score }}</div>
          </div>
        </v-col>
      </v-row>
    </v-col>

    <v-col cols="7" align-self="center" style="border: green 3px dashed;"> <!-- 2분할 -->
          <v-col style="border: red 3px dashed; display: flex; align-items: center; justify-content: space-around;">
            전체랭킹(선택한게임의 이번주 최고점수)
            <div style="border: black 3px dashed;">이번주 최고점수: {{ gameData[0].score }}</div>
          </v-col>
      <!-- <v-row no-gutters justify="center">
        <v-col style="border: gray 3px dashed; display: flex; align-items: center; justify-content: center;"> -->
            <div v-for="n in gameData.length" :key="n" style="border: black 3px dashed; display: flex; justify-content: space-around;"><div>{{ gameData[n-1].user }}님</div> <div>Score: {{ gameData[n-1].score }}</div></div>
        <!-- </v-col>
      </v-row> -->
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
      myData: {},
      myDataWeek: {},
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
          count: 10,
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
    this.getMyGameData()
    this.getMyGameDataWeek()
  },
  updated() {
  }
}
</script>

<style>

</style>
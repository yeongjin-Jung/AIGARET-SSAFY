<template>
  <v-row no-gutters class="fill-height text-center">
    
    <v-col cols="5" align-self="center" style="border: gray 3px solid;"> <!-- 2분할 -->
      <v-row no-gutters justify="center"> <!-- 4분할 -->
        <v-col cols="6" style="border: white 3px dashed; display: flex; align-items: center; justify-content: center; height: 40vh;">
        <!-- cols="6" 으로 가운데 정렬 효과 -->
          
          <v-col style="border: black 3px dashed;"> <!-- v-col > v-col, 횡 => 종 변화 -->
          <!-- <v-row> 주석풀어보면 횡 변화함 알 수 있음 -->

            <v-col style="border: white 3px dashed;">
              <!-- <div style="border: black 3px dashed;">주간최고점수</div> -->
              <!-- div 대신 v-col 로 써도됨(line.16 주석 풀어볼 것), 상황에따라 횡,종 변화할 수 있음 (line.10, 22 주석풀어볼 것) -->
              <v-col style="border: black 3px dashed;">주간최고점수</v-col>
              <!-- <v-col style="border: black 3px dashed;">주간최고점수</v-col> -->
            </v-col>
            <!-- <v-col style="border: white 3px dashed;"> -->
              <v-col style="border: black 3px dashed;">최고점수</v-col>
            <!-- </v-col> -->
          
          <!-- </v-row> -->
          </v-col>
        
        </v-col>
      </v-row>
      <v-row no-gutters justify="center"> <!-- 4분할 -->
        <v-col cols="6" style="border: white 3px dashed; display: flex; align-items: center; justify-content: center; height: 40vh;">
        <!-- cols="6" 으로 가운데 정렬 효과 -->
          <div style="border: black 3px dashed;">
            본인점수
          </div>
        </v-col>
      </v-row>
    </v-col>

    <v-col cols="7" align-self="center" style="border: gray 3px solid;"> <!-- 2분할 -->
      <v-row no-gutters justify="center">
        <!-- <v-col cols="6" style="border: white 3px dashed; display: flex; align-items: center; justify-content: center; height: 50vh;">  -->
        <!-- line.39, line.41 차이는 cols="6", 이게 있고 없고에 따라 다르게보임 line.42의 영향이 있는데 원라를 모르겠음..-->
        <v-col style="border: white 3px dashed; display: flex; align-items: center; justify-content: center; height: 50vh;">
          <v-col style="border: black 3px dashed;">
            <v-card>
              <v-tabs
                background-color="white"
                color="deep-purple accent-4"
                centered
              >
                <v-tab>Landscape</v-tab>
                <v-tab>City</v-tab>
                <v-tab>Abstract</v-tab>

                <v-tab-item
                  v-for="n in 3"
                  :key="n"
                >
                  <RankDetail :tabIndex="n"/>
                </v-tab-item>
              </v-tabs>
            </v-card>
          </v-col>
        </v-col>
      </v-row>
    </v-col>

  </v-row>
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

<script>
//Importing Line class from the vue-chartjs wrapper
import { Line } from "vue-chartjs";
import axios from 'axios'
import SERVER from '@/api/server'
import moment from 'moment'

export default {
  extends: Line,

  data() {
    return {
      chartData: {
        labels: [],
        
        datasets: [
          {
            label: "손목 터치 게임(분)",
            data: [],
            fill: false,
            borderColor: "rgba(255, 99, 132, 1)",
            backgroundColor: "rgba(255, 99, 132, 1)",
            borderWidth: 5,
          },
          {
            label: "스네이크 게임(분)",
            data: [],
            fill: false,
            borderColor: "rgba(255, 206, 86, 1)",
            backgroundColor: "rgba(255, 206, 86, 1)",
            borderWidth: 3,
          },
          {
            label: "점프 게임(분)",
            data: [],
            fill: false,
            borderColor: "rgba(75, 192, 192, 1)",
            backgroundColor: "rgba(75, 192, 192, 1)",
            borderWidth: 3,
          },
        ],
      },
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
              gridLines: {
                display: true,
              },
            },
          ],
          xAxes: [
            {
              gridLines: {
                display: false,
              },
              fontSize: 40
            },
          ],
        },
        legend: {
          display: true,
          labels: {
            // This more specific font property overrides the global property
            fontColor: "black",
            fontSize : 15,
            fontStyle: "bold",
          },
          responsive: true,
          maintainAspectRatio: false
        }
      }
    }
  },

  mounted () {
    const today = moment().year() 
      + '-'
      + ((moment().month()+1) >= 10 ? (moment().month()+1) : ('0' + (moment().month()+1)))
      + '-'
      + ((moment().date()) >= 10 ? (moment().date()) : ('0' + (moment().date()))) 
    
    // console.log('today : ', today)
    const data = {
      'today': today
    }

    axios.post(SERVER.URL + SERVER.ROUTES.getLineData, data)
    .then(res => {
    console.log("line chart response : ", res)

    for(var idx=0; idx<12; idx++) {
      // datasets[0] : 손목
      // datasets[1] : 스네이크
      // datasets[2] : 점프
      
      // idx번째 날짜
      console.log('Date : ', res.data.records[idx].date)

      // idx번째 데이터
      console.log('WristTouchGameTime : ', res.data.records[idx].record[0].time)
      console.log('SnakeGameTime : ', res.data.records[idx].record[1].time)
      console.log('JumpGameTime : ', res.data.records[idx].record[2].time)

      console.log(typeof res.data.records[idx].date)
      console.log(typeof res.data.records[idx].record[0].time)

      // 1. 각 달을 날짜 label 배열에 추가.
      this.chartData.labels.push(res.data.records[idx].date)

      // 2. 각 달에 해당하는 게임 플레이 시간 data 배열에 추가.
      this.chartData.datasets[0].data.push(res.data.records[idx].record[0].time)
      this.chartData.datasets[1].data.push(res.data.records[idx].record[1].time)
      this.chartData.datasets[2].data.push(res.data.records[idx].record[2].time)

    }

      console.log('this.chartData.labels : ', this.chartData.labels)
      console.log('this.chartData.datasets[0].data : ', this.chartData.datasets[0].data)
      console.log('this.chartData.datasets[1].data : ', this.chartData.datasets[1].data)
      console.log('this.chartData.datasets[2].data : ', this.chartData.datasets[2].data)

      this.renderChart(this.chartData, this.options)
    })
    .catch(err => {
      console.log(err)
    })

  }
}
</script>

<style>
</style>
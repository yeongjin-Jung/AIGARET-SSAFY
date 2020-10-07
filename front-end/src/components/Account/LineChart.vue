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
            label: "쥐를 잡자(분)",
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
            label: "환상의 점프(분)",
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

      // 1. 각 달을 날짜 label 배열에 추가.
      this.chartData.labels.push(res.data.records[idx].date)

      // 2. 각 달에 해당하는 게임 플레이 시간 data 배열에 추가.
      this.chartData.datasets[0].data.push(parseInt(res.data.records[idx].record[0].time / 60))
      this.chartData.datasets[1].data.push(parseInt(res.data.records[idx].record[1].time / 60))
      this.chartData.datasets[2].data.push(parseInt(res.data.records[idx].record[2].time / 60))
    }

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
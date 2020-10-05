
<script>
//Importing Line class from the vue-chartjs wrapper
import { Line } from "vue-chartjs";
import axios from 'axios'
import SERVER from '@/api/server'
import moment from 'moment'

export default {
    extends: Line,
    data () {
      return {
        chartData: {
          labels: ["1월",	"2월",	"3월",	"4월",	"5월",	"6월",	"7월", "8월", "9월", "10월", "11월", "12월"],
          datasets: [
            {
              label: '손목 터치 게임(분)',
              data: [600,	1150,	342,	6050,	2522,	3241,	1259,	157,	1545, 9841, 3000, 6000],
              fill: false,
              borderColor: "rgba(255, 99, 132, 1)",
              backgroundColor: "rgba(255, 99, 132, 1)",
              borderWidth: 3
            },
            {
              label: '스네이크 게임(분)',
              data: [300,	100,	8008,	6247,	8544,	684,	125,	674,	1231, 154, 876, 376],
              fill: false,
              borderColor: "rgba(255, 206, 86, 1)",
              backgroundColor: "rgba(255, 206, 86, 1)",
              borderWidth: 3
            },
            {
              label: '점프 게임(분)',
              data: [457,	5685,	342,	235,	365,	697,	1259,	58,	1545, 346, 243, 156],
              fill: false,
              borderColor: "rgba(75, 192, 192, 1)",
              backgroundColor: "rgba(75, 192, 192, 1)",
              borderWidth: 3
            }
          ]
        },
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              },
              gridLines: {
                display: true
              }
            }],
            xAxes: [ {
              gridLines: {
                display: false
              }
            }]
          },
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: false
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

      // console.log("손목 터치 게임 : ", res.data.WristTouchGame.play_time__sum)
      // console.log("스네이크 게임 : ", res.data.SnakeGame.play_time__sum)
      // console.log("점프 게임 : ", res.data.JumpGame.play_time__sum)

      // this.chartData.datasets[0].data.push(parseInt(res.data.WristTouchGame.play_time__sum / 60))
      // this.chartData.datasets[0].data.push(parseInt(res.data.SnakeGame.play_time__sum / 60))
      // this.chartData.datasets[0].data.push(parseInt(res.data.JumpGame.play_time__sum / 60))

      // this.renderChart(this.chartData, this.options);
    })
    .catch(err => {
      console.log(err)
    })

      this.renderChart(this.chartData, this.options)
    }
  }
</script>

<style>
</style>
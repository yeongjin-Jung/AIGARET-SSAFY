<script>
import axios from 'axios'
import SERVER from '@/api/server.js'

import { Pie } from "vue-chartjs";
export default {
  extends: Pie,
  data() {
    return {
      chartData: {
        labels: ["손목터치 게임(분)", "스네이크 게임(분)", "점프 게임(분)"],
        datasets: [
          {
            borderWidth: 1,
            borderColor: [
              "rgba(255,99,132,1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)"
            ],
            backgroundColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)"
            ],
            data: []
          },
        ]
      },
      options: {
        legend: {
          display: true
        },
        responsive: true,
        maintainAspectRatio: false
      }
    };
  },

  mounted() {
    axios.post(SERVER.URL + SERVER.ROUTES.getPieData)
    .then(res => {
      console.log("pie chart response : ", res)

      console.log("손목 터치 게임 : ", res.data.WristTouchGame.play_time__sum)
      console.log("스네이크 게임 : ", res.data.SnakeGame.play_time__sum)
      console.log("점프 게임 : ", res.data.JumpGame.play_time__sum)

      this.chartData.datasets[0].data.push(parseInt(res.data.WristTouchGame.play_time__sum / 60))
      this.chartData.datasets[0].data.push(parseInt(res.data.SnakeGame.play_time__sum / 60))
      this.chartData.datasets[0].data.push(parseInt(res.data.JumpGame.play_time__sum / 60))

      this.renderChart(this.chartData, this.options);
    })
    .catch(err => {
      console.log(err)
    })
  }
};
</script>

<style>
</style>
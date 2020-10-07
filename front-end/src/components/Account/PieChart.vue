<script>
import axios from "axios";
import SERVER from "@/api/server.js";

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
              "rgba(75, 192, 192, 1)",
            ],
            backgroundColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
            ],
            data: [],
          },
        ],
      },
      options: {
        legend: {
          display: true,
          labels: {
            // This more specific font property overrides the global property
            fontColor: "black",
            fontSize : 15,
            fontStyle: "bold",
          },
        },
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },

  mounted() {
    axios.post(SERVER.URL + SERVER.ROUTES.getPieData)
    .then(res => {
      this.chartData.datasets[0].data.push(parseInt(res.data.records[0].time / 60))
      this.chartData.datasets[0].data.push(parseInt(res.data.records[1].time / 60))
      this.chartData.datasets[0].data.push(parseInt(res.data.records[2].time / 60))

      this.renderChart(this.chartData, this.options);
    })
    .catch(err => {
      // console.log(err)
    })
  }
};
</script>

<style>
</style>

<script>
//Importing Line class from the vue-chartjs wrapper
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  data() {
    return {
      chartData: {
        labels: [
          "1월",
          "2월",
          "3월",
          "4월",
          "5월",
          "6월",
          "7월",
          "8월",
          "9월",
          "10월",
          "11월",
          "12월",
        ],
        
        datasets: [
          {
            label: "손목 터치 게임(분)",
            data: [
              600,
              1150,
              342,
              6050,
              2522,
              3241,
              1259,
              157,
              1545,
              9841,
              3000,
              6000,
            ],
            fill: false,
            borderColor: "rgba(255, 99, 132, 1)",
            backgroundColor: "rgba(255, 99, 132, 1)",
            borderWidth: 5,
          },
          {
            label: "스네이크 게임(분)",
            data: [
              300,
              100,
              8008,
              6247,
              8544,
              684,
              125,
              674,
              1231,
              154,
              876,
              376,
            ],
            fill: false,
            borderColor: "rgba(255, 206, 86, 1)",
            backgroundColor: "rgba(255, 206, 86, 1)",
            borderWidth: 3,
          },
          {
            label: "점프 게임(분)",
            data: [
              457,
              5685,
              342,
              235,
              365,
              697,
              1259,
              58,
              1545,
              346,
              243,
              156,
            ],
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
        },
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
  mounted() {
    this.renderChart(this.chartData, this.options);
  },
};
</script>

<style>
</style>
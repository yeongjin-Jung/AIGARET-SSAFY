<template>
  <div style="width:98vw; height:94.7vh; position:absolute; top:0px; text-align : center;">
    <!-- <h4>손목터치게임</h4> -->
    <!-- <div style="text-align: center; width : 70vw; height: 70vh;  margin-top : 10vh;"></div> -->
    <vue-p5 @setup="setup" @draw="draw"></vue-p5>
    <!-- <v-btn @click="Tutorial = !Tutorial" text style="position:absolute; top:2vh;; left:1vw; margin-top:7vh; height: 7vh; width:8vw; background:yellow; ">
      <p style="font-weight:1000; font-size: 2.5vh;  margin-top: 2vh;">게임조작법</p>
    </v-btn> -->
    <GameFinishModal @close="closeModal" v-if="modal" >
      <!-- default 슬롯 콘텐츠 -->
      <p style="font-size : 17vh; color : white; font-weight:500; margin-top:30vh;">Game Over</p>
      <!-- /default -->
      <!-- /footer -->
      <template slot="footer" style="background-color : rgba(0,0,0,1);">
        <button
          @click="doClose(); sendGameData(); restart()"
          style="background-color : red; height :8vh; border-radius: 12px;  width:10vw; font-size : 4vh; font-weight: 600; color:yellow;"
        >다시시작</button>
      </template>
    </GameFinishModal>
    <!-- <WristTouchGameTutorial @close="doCloseTutorial" v-if="Tutorial">
      <p style="font-size : 7vh; color : black; font-weight:800; ">게임조작법</p>
      <hooper style="margin-top: -3vh;">
        <slide></slide>
        <slide></slide>
        <slide></slide>
        <slide></slide>
        <slide></slide>
        <slide></slide>

        <hooper-pagination slot="hooper-addons"></hooper-pagination>
      </hooper>

      <template slot="footer" style="background-color : rgba(0,0,0,1);">
        <button
          @click="doCloseTutorial"
          style="background-color : red;  border-radius: 12px;  width:10vw; font-size : 4vh; font-weight: 600; color:yellow;"
        >닫기</button>
      </template>
    </WristTouchGameTutorial> -->

    <Loading v-if="loading"></Loading>
  </div>
</template>

<script>
import SERVER from '@/api/server.js'
import axios from 'axios'

import VueP5 from 'vue-p5'
import ml5 from 'ml5'
import $ from 'jquery'
import GameFinishModal from './GameFinishModal'
// import WristTouchGameTutorial from './WristTouchGameTutorial'
import Loading from './loding'
import { Hooper, Slide, Pagination as HooperPagination } from 'hooper'

import '../../assets/hooper.css'

export default {
  name: 'WristTouchGame',
  data: function () {
    return {
      video: null,
      poseNet: null,
      pose: null,
      skeleton: null,
      position_x: 900,
      position_y: 500,
      window_width: 1000,
      window_height: 700,
      countDown: 10,
      modal: false,
      score: 0,
      mouse: null,
      loading: false,
      Tutorial: false,
      gameStart: false,
      firstStart: true,
      gamestatus: false,
      sketch : null,

      start_time: null,
      end_time: null,
      game_score: 0,
    }
  },
  components: {
    VueP5,
    GameFinishModal,
    Loading,
    // WristTouchGameTutorial,
    Hooper,
    Slide,
    HooperPagination
  },
  methods: {
    setup (sketch) {
      // sketch.remove();

      this.sketch = sketch;
      sketch.createCanvas(this.window_width, this.window_height)
      sketch.background(0)
      this.video = sketch.createCapture(sketch.VIDEO)

      this.video.size(this.window_width, this.window_height)
      this.video.hide()
      this.poseNet = ml5.poseNet(this.video, this.modelReady())
      var that = this
      this.poseNet.on('pose', function (results) {
        if (results.length > 0) {
          that.pose = results[0].pose
          that.skeleton = results[0].skeleton
        }
      })

      // this.train = sketch.createImg(
      //   "http://www.memozee.com/FILES/047/jinsuk.729.%ED%8F%AC%EC%BC%93%EB%AA%AC.jpg"
      // );
      // this.train.hide();

      $('#defaultCanvas0').parent().css({
        width: '98vw',
        'text-align': 'center',
        position: 'absolute',
        top: '0',
        height : "94.8vh"
      })

      $('#defaultCanvas0').css({ width: '64vw', height: '94.8vh' })
    },
    modelReady () {
      console.log('Model Loaded')
    },
    chanege (x) {
      this.position_x = Math.floor(Math.random() * 800 + 100)
      this.position_y = Math.floor(Math.random() * 300 + 100)
      if (this.position_x >= 300 && this.position_x <= 700) {
        this.chanege(x)
      }
      this.score += 10
      this.countDown = 10
    },
    countDownTimer () {
      if (this.countDown > 0) {
        setTimeout(() => {
          this.countDown -= 1
          this.countDownTimer()
        }, 1000)
      }
    },

    draw (sketch) {
      sketch.translate(this.window_width, 0)
      sketch.scale(-1, 1)
      sketch.image(this.video, 0, 0, this.window_width+1, this.window_height+1)

      var that = this
      if (this.pose != null && this.gamestatus == true) {
        this.loading = false
        // 장애물
        sketch.rect(this.position_x, this.position_y, 100, 100)
        sketch.translate(this.window_width, 0)
        sketch.scale(-1, 1)

        // 점수판
        sketch.textSize(50)
        sketch.textStyle(sketch.BOLD)
        sketch.fill(255, 0, 0)
        sketch.text('점수 : ' + this.score, 40, 60)

        // 카운트 다운
        sketch.textSize(100)
        sketch.textStyle(sketch.NORMAL)
        sketch.fill(0, 255, 255)
        sketch.text(this.countDown, 455, 100)

        // 전체 Canvas 반전
        sketch.translate(this.window_width, 0)
        sketch.scale(-1, 1)

        if (this.countDown == 0) {
          this.end_time = this.timeNow()
          this.game_score = this.score
          this.modal = true
          this.score = 0
          this.gamestatus = false;
          this.loading = true;
        }

        if (this.pose.score > 0.25 && this.pose != null) {
          const eyeR = that.pose.rightEye
          const eyeL = that.pose.leftEye
          const d = sketch.dist(eyeR.x, eyeR.y, eyeL.x, eyeL.y)
          sketch.fill(255, 0, 0)
          // sketch.ellipse(that.pose.nose.x, that.pose.nose.y, d);
          sketch.fill(0, 0, 255)

          if (
            (that.pose.rightWrist.x > that.position_x &&
              that.pose.rightWrist.x < that.position_x + 100 &&
              that.pose.rightWrist.y > that.position_y &&
              that.pose.rightWrist.y < that.position_y + 100) ||
            (that.pose.leftWrist.x > that.position_x &&
              that.pose.leftWrist.x < that.position_x + 100 &&
              that.pose.leftWrist.y > that.position_y &&
              that.pose.leftWrist.y < that.position_y + 100)
          ) {
            that.chanege()
          }

          sketch.ellipse(that.pose.rightWrist.x, that.pose.rightWrist.y, 32)
          sketch.ellipse(that.pose.leftWrist.x, that.pose.leftWrist.y, 32)

          for (let i = 0; i < that.pose.keypoints.length; i++) {
            const x = that.pose.keypoints[i].position.x
            const y = that.pose.keypoints[i].position.y
            sketch.fill(0, 255, 0)
            sketch.ellipse(x, y, 16, 16)
          }

          for (let i = 0; i < that.skeleton.length; i++) {
            const a = that.skeleton[i][0]
            const b = that.skeleton[i][1]
            sketch.line(a.position.x, a.position.y, b.position.x, b.position.y)
          }
        } else {
          sketch.image(this.video, 0, 0, this.window_width, this.window_height)

          sketch.textStyle(sketch.BOLD)
          sketch.translate(this.window_width, 0)
          sketch.scale(-1, 1)
          sketch.textSize(60)
          sketch.fill(255, 0, 0)
          sketch.text('포즈를 인식할 수 없습니다', 140, 400)
          sketch.textSize(100)
          sketch.textStyle(sketch.NORMAL)
          sketch.fill(0, 255, 255)
          sketch.text(this.countDown, 455, 100)
        }
      } else {
        this.loading = true;
        console.log('로딩중')
      }
    },
    closeModal () {
      this.modal = false
    },
    // CloseTutorial () {
    //   this.Tutorial = false
    // },

    doClose () {
      this.score = 0;
      this.countDown = 10;
      this.countDownTimer();
      this.closeModal();
      this.gamestatus = true;
    },
    // doCloseTutorial () {
    //   this.Tutorial = false
    //   this.gameStart = true
    //   if (this.firstStart == true) {
    //     this.countDownTimer()
    //   }
    //   this.gamestatus = true
    //   this.firstStart = false
    // }
    timeNow () {
      var date = new Date().toISOString()
      var time = new Date().toString('ko-KR')
      return date.slice(0, 10) + ' ' + time.slice(16, 24)
    },
    restart () {
      this.start_time = this.timeNow()
    },
    sendGameData () {
      const testd = {
        userId: this.$store.state.userInfo.userid,
        gameNo: this.$route.query.gameNo,
        startTime: this.start_time,
        endTime: this.end_time,
        gameScore: this.game_score,
      }
      console.log(testd)
      // axios.post(SERVER.URL + SERVER.ROUTES.sendData, testd).catch((err) => console.log(err));
      // axios.post(SERVER.URL + '?', {
      //   gameNo: this.$route.query.gameNo,
      //   startTime: this.start_time,
      //   endTime: this.end_time,
      //   gameScore: this.game_score,
      // }).catch((err) => console.log(err));
    }
  },
  created () {
    this.Tutorial = true
    this.countDownTimer();
    this.gamestatus = true;
  },
  mounted () {
    this.start_time = this.timeNow()
    // console.log(this.timeNow())
    // console.log(this.$store.state.userInfo)
  },
  destroyed(){
    this.sketch.remove();
    this.sketch.noLoop();
    this.sketch.clear();
    console.log(this.sketch);
  }
}
</script>

<style lang="scss" scoped>
#defaultCanvas0 {
  display: inline-block;
  height: 70vh;
}
</style>

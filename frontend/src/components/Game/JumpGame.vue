<template>
  <div>
    <h1>aaaaa</h1>
    <vue-p5 @setup="setup" @draw="draw"></vue-p5>
  </div>
</template>

<script>
import VueP5 from "vue-p5";
// import p5_dom from "./p5_dom_min";
// import p5_sound from "./p5_sound_min";
import ml5 from "ml5";
import { Jumper } from "../../api/game/running/Jumper";
import { Train } from "../../api/game/running/Train";
export default {
  name: "JumpGame",
  data: function () {
    return {
      sketchObj : null,
      classifier: {},
      mobilenet: null,
      video: null,
      label: "",

      score: null,
      scroll: 10,
      scrollBg: 0,
      trains: [],
      unicorn: null,
      failsounds: [],
      restart: false,
      video: null,
      height: 700,
      width: 400,

      //preload
      music: null,
      ding: null,
      whistle: null,
      bg: null,
      train: null,
      jumper: null,

      // js File
      unicorn: null,

      key: null,

      //train
      poseNet: null,
      brain : null,
    };
  },
  components: {
    "vue-p5": VueP5,
  },
  methods: {
    setup(sketch) {
      this.sketchObj = sketch;
      sketch.createCanvas(700, 400);
      this.train = sketch.createImg(
        "http://www.memozee.com/FILES/047/jinsuk.729.%ED%8F%AC%EC%BC%93%EB%AA%AC.jpg"
      );
      this.bg = sketch.createImg(
        "https://cdn.hipwallpaper.com/m/34/80/7xuaw6.jpg"
      );
      this.jumper = sketch.createImg(
        "https://supermariorun.com/assets/img/hero/hero_chara_mario_update_pc.png"
      );
      this.train.hide();
      this.bg.hide();
      this.jumper.hide();

      this.unicorn = new Jumper(sketch, sketch.height, this.jumper);
      this.video = sketch.createCapture(sketch.VIDEO);
      // this.video.hide();
      // this.poseNet = ml5.poseNet(video,modelLoaded);
      // this.poseNet.on('pose',gotPoses);


    },
    videoReady() {
      console.log("webcam load... finished");
    },
    jump(sketch){
      if(this.restart){
        this.restart = false;
        this.score = 0;
        this.scrollBg = 0;
        this.scroll =10;
        this.trains = [];
        this.sketchObj.loop();
      }
      if(event.key == ' '){
        this.unicorn.jump();
        return false;
      }
    },
    draw(sketch) {
      var that = this;
      sketch.image(this.bg, -this.scrollBg, 0, sketch.width, sketch.height);
      sketch.image(
        this.bg,
        -this.scrollBg + sketch.width,
        0,
        sketch.width,
        sketch.height
      );

      if (this.scrollBg > sketch.width) {
        this.scrollBg = 0;
      }

      if (sketch.random(1) < 0.75 && sketch.frameCount % 50 == 0) {
        this.trains.push(
          new Train(
            sketch,
            this.train,
            sketch.width,
            sketch.height,
            this.scroll
          )
        );
      }
      // if(this.score % 100 == 0 && this.score != 0){
      //   s
      // }
      if (sketch.frameCount % 5 == 0) {
        this.score++;
      }

      sketch.fill(255);
      sketch.textSize(32);
      sketch.textFont("monospace");
      sketch.text(`Score: ${this.score}`, 10, 30);

      for (let t of this.trains) {
        t.move();
        t.show();

        if (this.unicorn.collide(t)) {
          sketch.noLoop();
          // music.stop();
          // let sound = sketch.random(failSounds);
          // sound.play();

          sketch.fill(255);
          sketch.text(
            `Game Over! Press any key to restart`,
            45,
            sketch.height / 2
          );
          that.restart = true;
        }
      }

      this.unicorn.show();
      this.unicorn.move();
    },
  },
  created(){
      window.addEventListener('keydown', this.jump)
  },
};
</script>

<style>
</style>
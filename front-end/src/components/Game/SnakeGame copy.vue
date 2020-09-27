<template>
  <div style="width :  100vw; height: 99%">
    <h4>스네이크 게임</h4>
    <v-btn id="leftButton">왼쪽</v-btn>
    <span id="amountOfLeftImages">0</span>left Images
    <v-btn id="rightButton">add right button</v-btn>
    <span id="amountOfRightImages">0</span>right Images
    <v-btn id="topButton">add top button</v-btn>
    <span id="amountOfTopImages">0</span>top Images
    <v-btn id="downButton">add down button</v-btn>
    <span id="amountOfDownImages">0</span>down Images
    <v-btn id="trainButton">Train!</v-btn>
    <span id="loss"></span>

    <button id="save">Save</button>
    <vue-p5 @setup="setup" @draw="draw" @gotResults="gotResults"></vue-p5>
  </div>
</template>

<script>
import VueP5 from 'vue-p5'
import ml5 from 'ml5'
import { Snake } from '../../api/game/snake/snake'
import $ from 'jquery'
export default {
  name: 'SnakeGame',
  data: function () {
    return {
      classifier: {},
      mobilenet: null,
      video: null,
      label: '',

      // buttons for navigation
      leftButton: null,
      topButton: null,
      rightButton: null,
      downButton: null,

      leftImages: 0,
      rightImages: 0,
      topImages: 0,
      downImages: 0,

      train: null,

      s: null,
      scl: 20,
      food: null,
      foodx: null,
      foody: null,

      width: 400,
      height: 400,
      videoHeight: 950,
      videoWidth: 1270,

      loss: 0,

      error: null,
      results: null,
      sketch: null
    }
  },
  components: {
    'vue-p5': VueP5
  },
  methods: {
    setup (sketch) {
      this.sketch = sketch
      sketch.createCanvas(this.width, this.height)
      this.video = sketch.createCapture(sketch.VIDEO)
      this.video.size(this.videoWidth, this.videoHeight)
      sketch.background(0)
      this.mobilenet = ml5.featureExtractor('MobileNet')
      this.classifier = this.mobilenet.classification(
        this.video,
        4,
        this.videoReady()
      )
      //   const options = { numLabels: 4 };
      //   this.classifier = this.mobilenet.classification(
      //     this.video,
      //     options,
      //     this.videoReady()
      //   );

      this.setupButton(sketch)

      // game code starts
      this.s = new Snake(sketch, this.scl, this.width, this.height, this.food)
      sketch.frameRate(10)
      this.pickLocation(sketch)
      // game code ends

      $('#defaultCanvas0')
        .parent()
        .css({ width: '100%', 'text-align': 'center', position: 'absolute', left: '1vw', top: '15vh' })
      $('#defaultCanvas0').css({ width: '40vw', height: '72vh' })
      $('video').css({ width: '52vw', height: '72vh' })
    },
    videoReady () {
      console.log('webcam load... finished')
    },

    setupButton (sketch) {
      var that = this
      // left button
      this.leftButton = sketch.select('#leftButton')
      this.leftButton.mousePressed(function () {
        that.classifier.addImage('left')
        sketch.select('#amountOfLeftImages').html(that.leftImages++)
      })

      // right button
      this.rightButton = sketch.select('#rightButton')
      this.rightButton.mousePressed(function () {
        that.classifier.addImage('right')
        sketch.select('#amountOfRightImages').html(that.rightImages++)
      })

      // top button
      this.topButton = sketch.select('#topButton')
      this.topButton.mousePressed(function () {
        that.classifier.addImage('top')
        sketch.select('#amountOfTopImages').html(that.topImages++)
      })

      // down button
      this.downButton = sketch.select('#downButton')
      this.downButton.mousePressed(function () {
        that.classifier.addImage('down')
        sketch.select('#amountOfDownImages').html(that.downImages++)
      })

      // train button
      this.trainButton = sketch.select('#trainButton')
      this.trainButton.mousePressed(function () {
        that.classifier.train(that.whileTraining)
      })

      // Save model
      this.saveBtn = sketch.select('#save')
      this.saveBtn.mousePressed(function () {
        that.classifier.save()
      })

      //   // Load model
      //   this.loadBtn = sketch.select("#load");
      //   this.loadBtn.changed(function () {
      //     this.classifier.load("savedModel/model.json", this.customModelReady);
      //   });
    },

    whileTraining (loss) {
      var that = this

      if (loss == null) {
        that.sketch
          .select('#loss')
          .html('training done! Final loss is : ' + loss)
        that.classifier.classify(that.gotResults)
        // console.log(that.gotResults);
      } else {
        that.sketch.select('#loss').html('loss is : ' + loss)
      }
    },

    gotResults (error, results) {
      var that = this

      if (error) {
        console.error(error)
      } else {
        that.label = results[0].label
        that.classifier.classify(that.gotResults)
      }
    },

    pickLocation (sketch) {
      var cols = sketch.floor(this.width / this.scl)
      var rows = sketch.floor(this.height / this.scl)
      this.food = sketch.createVector(
        sketch.floor(sketch.random(cols)),
        sketch.floor(sketch.random(rows))
      )
      this.foodx = this.food.x
      this.foody = this.food.y
      // food.mult(scl);
    },
    draw (sketch) {
      var that = this
      sketch.background(0)
      sketch.fill(255)
      sketch.textSize(32)
      sketch.text(this.label, 10, this.height)
      // console.log(this.s.update);

      this.s.update(sketch)
      this.s.show(sketch)

      if (this.s.eat(this.food)) {
        that.pickLocation(sketch)
      }
      // snake
      sketch.fill(255, 0, 100)
      sketch.rect(20 * this.foodx, 20 * this.foody, this.scl, this.scl)

      if (this.label == 'top') this.s.dir(0, -1)
      else if (this.label == 'down') this.s.dir(0, 1)
      else if (this.label == 'left') this.s.dir(-1, 0)
      else if (this.label == 'right') this.s.dir(1, 0)
    }
  }
}
</script>

<style>
#defaultCanvas0 {
  display: inline-block;
}
</style>

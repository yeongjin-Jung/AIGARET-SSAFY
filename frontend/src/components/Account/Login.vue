<template>
  <div>
    <div style="width: 400px; height: 90px; margin: auto;">
        <div style="font-weight: bold; font-size: 36px; text-align: center;" class="">AIGARET</div>
        <div style="font-weight: bold; font-size: 24px; text-align: center;" class="">AI Game Rehabilitation Trainer</div>
    </div>

    <div style="width: 533px; height: 400px; margin: 20px auto; background: black;">
      <video id="video" height="400" autoplay muted></video>
    </div>

    <div style="width: 533px; margin: 20px auto;">
      <div style="display:inline-block; width: 250px; font-size: 16px; color: rgb(255, 255, 255); text-align: center; line-height: 2.5em; border-radius: 4px; background-color: rgb(52, 152, 219);">로그인</div>
      <div style="display:inline-block; width: 33px;"></div>
      <div style="display:inline-block; width: 250px; font-size: 16px; color: rgb(64, 64, 64); text-align: center; line-height: 2.5em; border-radius: 4px; background-color: rgb(224, 224, 224);">회원가입</div>
      <div style="font-size:16px; color: rgb(41, 90, 221); text-decoration:underline;">아이디로 로그인하기</div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'Login',
  components: {

  },
  data () {
    return {
      faceapi: null
    }
  },
  methods: {
    startVideo (val) {
      navigator.getUserMedia(
        { video: true },
        stream => { val.srcObject = stream },
        err => console.error(err)
      )
    }
  },
  mounted () {
    const video = document.getElementById('video')
    this.startVideo(video)

    // const recaptchaScript = document.createElement('script')
    // recaptchaScript.setAttribute('type', 'javascript')
    // recaptchaScript.setAttribute('defer', '')
    // recaptchaScript.setAttribute('src', 'face-api.min.js')
    // document.head.appendChild(recaptchaScript)

    // Promise.all([
    //   faceapi.nets.tinyFaceDetector.loadFromUri('/models'),
    //   faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
    //   faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
    //   faceapi.nets.faceExpressionNet.loadFromUri('/models')
    // ]).then(this.startVideo)

    // video.addEventListener('play', () => {
    //   const canvas = faceapi.createCanvasFromMedia(video)
    //   document.body.append(canvas)
    //   const displaySize = { width: video.width, height: video.height }
    //   faceapi.matchDimensions(canvas, displaySize)
    //   setInterval(async () => {
    //     const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
    //     const resizedDetections = faceapi.resizeResults(detections, displaySize)
    //     canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    //     faceapi.draw.drawDetections(canvas, resizedDetections)
    //     faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
    //     // faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
    //   }, 100)
    // })
  }
}
</script>

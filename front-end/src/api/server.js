export default {
  // URL: 'http://localhost:8000/api/',
  URL: 'https://j3b203.p.ssafy.io/api/',
  ROUTES: {
    // Account
    signup: 'rest-auth/signup/',
    login: 'rest-auth/login/',
    checkIdDuplicate: 'idDuplicateCheck/',
    changepassword: 'changepassword/',
    changeImage: 'mypages/imagechange/',

    // mypage
    getRecords: 'mypages/calendar/',
    changeGoalTime: 'mypages/goaltimechange/',
    getAchievePercent: 'mypages/achievepercent/',
    getPieData: 'mypages/totalgametime/',

    // Game
    getGameInfo: 'games/',
    // sendData: `games/${ this.$route.query.gameNo }/users/${ this.$store.state.userInfo.userid }/records/`,
  }
}

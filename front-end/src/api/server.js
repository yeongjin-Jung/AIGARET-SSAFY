export default {
  URL: 'https://aigaret.ga/api/',
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
    getLineData: 'mypages/monthlygametime/',
    getPieData: 'mypages/totalgametime/',

    // Game
    getGameInfo: 'games/',
    // sendData: `games/${ this.$route.query.gameNo }/users/${ this.$store.state.userInfo.userid }/records/`,
  }
}

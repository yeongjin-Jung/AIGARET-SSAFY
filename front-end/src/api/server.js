export default {
  // URL: 'http://localhost:5000/api/',
  URL: 'https://j3b203.p.ssafy.io/api/',
  ROUTES: {
    // Account
    signup: 'rest-auth/signup/',
    login: 'rest-auth/login/',
    checkIdDuplicate: 'rest-auth/checkIdDuplicate/',
    changepassword: 'changepassword/',
    // Game
    getGameInfo: 'games/',
    // sendData: `games/${ this.$route.query.gameNo }/users/${ this.$store.state.userInfo.userid }/records/`,
  }
}

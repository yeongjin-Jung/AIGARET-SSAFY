import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import SERVER from '@/api/server.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    id: localStorage.getItem('id'),
    accessToken: localStorage.getItem('accessToken'),
    userInfo: {
      'id': '',
      'username': '',
      'name': '',
      'age': '',
      'img': ''
    },
    img: '',
    isIdDuplicated: false,
    gameRecords: []
  },

  mutations: {
    SET_ID_DUPLICATED(state, res) {
      state.isIdDuplicated = res
    },

    SET_USER_INFO(state, userInfo) {
      state.userInfo.id = userInfo.id
      state.userInfo.username = userInfo.username
      state.userInfo.name = userInfo.name
      state.userInfo.age = userInfo.age
      state.userInfo.img = userInfo.img
    },

    SET_USER_ID (state, id) {
      state.id = id
      localStorage.setItem('id', id)
    },

    SET_TOKEN(state, token) {
      state.accessToken = token
      localStorage.setItem('accessToken', token)
    },

    LOGOUT(state) {
      state.id = ''
      state.accessToken = ''

      state.userInfo.id = ''
      state.userInfo.username = ''
      state.userInfo.name = ''
      state.userInfo.age = ''


      localStorage.removeItem('id')
      localStorage.removeItem('accessToken')
    },

    SET_IMG(state, base64Encoded) {
      state.img = base64Encoded
    },

    SET_RECORDS(state, data) {
      state.gameRecords = data
    }

  },

  getters: {
    isLoggedIn(state){
      console.log("AccessToken : ", state.accessToken)
      console.log("!!state.accessToken : ", !!state.accessToken)

      if (state.accessToken === 'null' || state.accessToken === undefined) {
        return false;
      }else{
        return !!state.accessToken;
      }
    },
  },

  actions: {
    checkIdDuplicate({ commit }, id) {
      axios.post(SERVER.URL + SERVER.ROUTES.checkIdDuplicate, id)
      .then(res => {
        console.log("res : ", res)

        if(res == true)
          commit(SET_ID_DUPLICATED, true)
        else
          commit(SET_ID_DUPLICATED, false)
      })
      .catch()
    },

    signup({ commit, dispatch }, signupData) {
      const data = {
        'username': signupData.id,
        'name': signupData.name,
        'age': signupData.age,
        'password': signupData.password,
        'confirm_password': signupData.passwordConfirm,
        'img': signupData.img
      }

      axios.post(SERVER.URL + SERVER.ROUTES.signup, data)
      .then(res => {
        const loginData = {
          'username': signupData.id,
          'password': signupData.password
        }
        dispatch('login', loginData)
        
      })
      .catch(err => console.log(err))
    },

    login({ commit }, loginData) {
      console.log("loginData : ", loginData)

      const data = {
        'username': loginData.username,
        'password': loginData.password
      }

      axios.post(SERVER.URL + SERVER.ROUTES.login, data)
      .then(res => {
        console.log("res", res)
        console.log("로그인 아이디 : ", res.data.user.username)
        console.log("받아온 토큰 : ", res.data.token)

        commit('SET_USER_INFO', res.data.user)
        commit('SET_USER_ID', res.data.user.username)
        commit('SET_TOKEN', res.data.token)
      })
      .catch(err => {
        alert("아이디, 비밀번호를 확인해주세요.")
      })
    },

    logout({ commit }) {
      commit('LOGOUT')
    },

    changePassword ({ state, commit }, userInfo) {
      const data = {
        id: state.id,
        password: userInfo.password,
        new_password: userInfo.newPassword
      }

      axios.post(SERVER.URL + SERVER.ROUTES.changePassword, data)
      .then(res => {
        console.log('비밀번호 변경 완료!')
        alert("변경된 비밀번호로 로그인 해주세요.")
        commit('LOGOUT')
      })
      .catch()
    },

    changeImage({}, new_image) {
      const data = {
        id: state.id,
        new_image: new_image
      }

      axios.post(SERVER.URL + SERVER.ROUTES.changeImage, data, {
        headers : {
          'Authorization': 'JWT ' + state.accessToken
        }
      })
      .then(res => {
      })
      .catch()
    },

    getRecords({ commit }, todayDate) {
      const data = {
        // "date": todayDate
        "date": "2020-09-30"
      }
      console.log('getRecords called.')
      console.log('todayDate : ', todayDate)
      console.log("access token : ", this.state.accessToken)
      
      axios.post(SERVER.URL + SERVER.ROUTES.getRecords, data, {
        headers: {
          'Authorization': 'JWT' + this.state.accessToken
        }
      })
      .then(res => {
        console.log(res)
        commit('SET_RECORDS', res.records)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },

  modules: {
  }
})

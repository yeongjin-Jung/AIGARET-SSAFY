import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import SERVER from '@/api/server.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    id: localStorage.getItem('id'),
    accessToken: localStorage.getItem('accessToken')
  },

  mutations: {
    SET_USER_ID (state, id) {
      state.id = id
      localStorage.setItem('id', id)
    },

    SET_TOKEN(state, token) {
      state.accessToken = token
      localStorage.setItem('accessToken', token)
      // if (!!!token.authorization) {
      //   state.authorization = token.authorization
      //   localStorage.setItem('authorization', token)
      // }
    },

    LOGOUT(state) {
      state.id = null
      state.accessToken = null

      localStorage.removeItem('id')
      localStorage.removeItem('accessToken')
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
    signup({ commit, dispatch }, signupData) {
      const data = {
        'username': signupData.id,
        'name': signupData.name,
        'age': signupData.age,
        'password': signupData.password,
        'confirm_password': signupData.passwordConfirm,
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
        newPassword: userInfo.newPassword
      }

      axios.post(SERVER.URL + SERVER.ROUTES.changePassword, data)
      .then(res => {
        console.log('비밀번호 변경 완료!')
      })
      .catch()
    },
  },

  modules: {
  }
})

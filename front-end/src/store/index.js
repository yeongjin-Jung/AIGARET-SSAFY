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
      'userid': localStorage.getItem('userid'),
      'username': localStorage.getItem('username'),
      'name': localStorage.getItem('name'),
      'age': localStorage.getItem('age'),
      'goal_time': localStorage.getItem('goal_time'),
      'profile_image': localStorage.getItem('profile_image')
    },

    isIdDuplicated: false,
    gameRecords: []
  },

  mutations: {
    SET_ID_DUPLICATED(state, res) {
      state.isIdDuplicated = res
    },

    SET_USER_INFO(state, userInfo) {
      state.userInfo.userid = userInfo.id
      state.userInfo.username = userInfo.username
      state.userInfo.name = userInfo.name
      state.userInfo.age = userInfo.age
      state.userInfo.goal_time = userInfo.goal_time
      state.userInfo.profile_image = userInfo.profile_image

      localStorage.setItem('userid', userInfo.id)
      localStorage.setItem('username', userInfo.username)
      localStorage.setItem('name', userInfo.name)
      localStorage.setItem('age', userInfo.age)
      localStorage.setItem('goal_time', userInfo.goal_time)
      localStorage.setItem('profile_image', userInfo.profile_image)
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
      state.accessToken = ''

      state.userInfo.userid = ''
      state.userInfo.username = ''
      state.userInfo.name = ''
      state.userInfo.age = ''
      state.userInfo.goal_time = ''
      state.userInfo.profile_image = ''

      localStorage.removeItem('accessToken')

      localStorage.removeItem('userid')
      localStorage.removeItem('username')
      localStorage.removeItem('name')
      localStorage.removeItem('age')
      localStorage.removeItem('goal_time')
      localStorage.removeItem('profile_image')
    },

    SET_RECORDS(state, data) {
      state.gameRecords = data
      // console.log('state.gameRecords : ', state.gameRecords)
    },

    SET_CHANGED_PROFILE_IMAGE(state, data) {
      state.userInfo.profile_image = data
      localStorage.removeItem('profile_image')
      localStorage.setItem('profile_image', data)
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

    image(state) {
      return state.userInfo.profile_image
    }
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

    changeImage({ state, commit }, newImage) {
      console.log('changePicture called.')
      console.log('new image : ', newImage)

      const data = {
        "profile_image": newImage
      }

      axios.post(SERVER.URL + SERVER.ROUTES.changeImage, data, {
        headers : {
          'Authorization': 'JWT ' + state.accessToken
        }
      })
      .then(res => {
        commit('SET_CHANGED_PROFILE_IMAGE', newImage)
      })
      .catch()
    },

    async getRecords({ commit }, todayDate) {
      const data = {
        "date": todayDate
      }

      await axios.post(SERVER.URL + SERVER.ROUTES.getRecords, data, {
        headers: {
          'Authorization': 'JWT ' + this.state.accessToken,
        }
      })
      .then(res => {
        // console.log(res)
        commit('SET_RECORDS', res.data.records)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },

  modules: {
  }
})

import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import SERVER from '@/api/server.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // id: localStorage.getItem('id'),
    // accessToken: localStroage.getItem('accessToken')
  },

  mutations: {
    SET_USER_ID(state, id) {
      state.id = id
    }
  },

  actions: {
    signup({ commit }, signupData) {
      const data = {
        'id': signupData.id,
        'password': signupData.password,
        'name': signupData.name,
        'age': signupData.age
      }

      axios.post(SERVER.URL + SERVER.ROUTES.signup, data)
      .then(res => {
      })
      .catch(err => console.log(err))
    },

    login({ commit }, loginData) {
      const data = {
        'id': loginData.id,
        "password": loginData.password
      }

      axios.post(SERVER.URL + SERVER.ROUTES.login, data)
      .then(res => {
        commit('SET_USER_ID', loginData.id)
        commit('SET_TOKEN', res.headers)
      })
      .catch()
    }
  },

  modules: {
  }
})

import axios from 'axios'
import SERVER from '@/api/server.js'

import userStore from './userStore'

const mypageStore = {
  namespaced: true,

  state: {
    gameRecords: [],
    total_time: ''
  },

  getters: {
    progressValue(state) {
      let retValue = (parseInt(state.total_time / 3600) / userStore.state.userInfo.goal_time * 100).toFixed(1)
      return retValue
    }
  },

  mutations: {
    SET_RECORDS(state, data) {
      state.gameRecords = data
      // console.log('state.gameRecords : ', state.gameRecords)
    },

    SET_TOTAL_TIME(state, data) {
      state.total_time = data
    }
  },

  actions: {
    async getRecords({ commit }, todayDate) {
      const data = {
        "date": todayDate
      }

      await axios.post(SERVER.URL + SERVER.ROUTES.getRecords, data)
      .then(res => {
        // console.log(res)
        commit('SET_RECORDS', res.data.records)
      })
      .catch(err => {
        console.log(err)
      })
    },

    async getAchievePercent({ state, commit }, data) {
      // console.log(data)
      await axios.post(SERVER.URL + SERVER.ROUTES.getAchievePercent, data)
      .then(res => {
        
        // console.log(res)
        commit('SET_TOTAL_TIME', res.data.total_time)
      })
      .catch()
    }
  }
}

export default mypageStore
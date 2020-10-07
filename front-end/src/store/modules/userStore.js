import axios from 'axios'
import router from '@/router/index'
import SERVER from '@/api/server'

const userStore = {
  namespaced: true,

  state: {
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
    showAlert: false
  },

  getters: {
    isLoggedIn(state){
      // console.log("AccessToken : ", state.accessToken)
      // console.log("!!state.accessToken : ", !!state.accessToken)

      if (state.accessToken === 'null' || state.accessToken === undefined) {
        return false;
      }else{
        return !!state.accessToken;
      }
    },

    isIdDuplicated(state) {
      return state.isIdDuplicated
    },

    image(state) {
      return state.userInfo.profile_image
    },

    goal_time(state) {
      return state.userInfo.goal_time
    },

    showAlert(state) {
      return state.showAlert
    }
  },

  mutations: {
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

    SET_CHANGED_PROFILE_IMAGE(state, data) {
      state.userInfo.profile_image = data
      localStorage.removeItem('profile_image')
      localStorage.setItem('profile_image', data)
    },

    SET_CHANGED_GOAL_TIME(state, data) {
      state.userInfo.goal_time = data
      localStorage.removeItem('goal_time')
      localStorage.setItem('goal_time', data)
    },

    SET_ID_DUPLICATED(state, data) {
      state.isIdDuplicated = data
      state.showAlert = true
    }
  },

  actions: {
    checkIdDuplicate({ commit }, id) {
      const data = {
        'username': id
      }

      axios.post(SERVER.URL + SERVER.ROUTES.checkIdDuplicate, data)
      .then(res => {
        console.log("res.data.status : ", res.data.status) // fail or success

        if(res.data.status == 'success')
          commit('SET_ID_DUPLICATED', false)
        else
          commit('SET_ID_DUPLICATED', true)
      })
      .catch()
    },

    signup({ commit, dispatch }, signupData) {
      axios.post(SERVER.URL + SERVER.ROUTES.signup, signupData)
      .then(res => {
        const loginData = {
          'username': signupData.username,
          'password': signupData.password
        }
        dispatch('login', loginData)
      })
      .catch(err => console.log(err))
    },

    login({ commit }, loginData) {
      console.log('login')
      axios.post(SERVER.URL + SERVER.ROUTES.login, loginData)
      .then(res => {
        commit('SET_USER_INFO', res.data.user)
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
      axios.patch(SERVER.URL + SERVER.ROUTES.changepassword, userInfo)
      .then(res => {
        alert("비밀번호가 변경되었습니다.\n변경된 비밀번호로 로그인 해주세요.")
        commit('LOGOUT')
        router.push('/')
      })
      .catch(err => {
        // console.log(err)
        console.log(err.response)

        if(err.response.data.message=='wrong password') {
          alert('잘못된 비밀번호를 입력했습니다. 다시 입력해주세요.')
        }
      })
    },

    changeImage({ state, commit }, newImage) {
      console.log('changePicture called.')
      console.log('new image : ', newImage)

      const data = {
        "profile_image": newImage
      }

      axios.post(SERVER.URL + SERVER.ROUTES.changeImage, data)
      .then(res => {
        commit('SET_CHANGED_PROFILE_IMAGE', newImage)
      })
      .catch()
    },
    
    changeGoalTime({ state, commit }, newGoalTime) {
      const data = {
        'goal_time': newGoalTime
      }

      axios.post(SERVER.URL + SERVER.ROUTES.changeGoalTime, data)
      .then(res => {
        commit('SET_CHANGED_GOAL_TIME', newGoalTime)
      })
      .catch()
    },
  }
}

export default userStore
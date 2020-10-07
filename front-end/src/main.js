import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import axios from 'axios'

import userStore from './store/modules/userStore'

Vue.config.productionTip = false

axios.interceptors.request.use(
  function (config) {
    // 요청을 보내기 전에 수행할 일
    if(localStorage.getItem('accessToken') == undefined)
      return config
    config.headers.Authorization = 'JWT ' + localStorage.getItem('accessToken');
    
    return config;
  },

  function (error) {
    // 오류 요청을 보내기전 수행할 일
    return Promise.reject(error);
  }
);

axios.interceptors.response.use(
  function(response) {
    return response
  },

  function(error) {
    if(error.response.status == 401) {
      // console.log('error.response.status : 401')
      store.dispatch('userStore/logout')
    }
    else
      return Promise.reject(error)
  }
)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import axios from 'axios'

Vue.config.productionTip = false

axios.interceptors.request.use(
  function (config) {
    // 요청을 보내기 전에 수행할 일
    config.headers.Authorization = 'JWT ' + localStorage.getItem('accessToken');
    
    return config;
  },
  function (error) {
    // 오류 요청을 보내기전 수행할 일
    return Promise.reject(error);
  });

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

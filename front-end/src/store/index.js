import Vue from 'vue'
import Vuex from 'vuex'

import userStore from '@/store/modules/userStore'
import mypageStore from '@/store/modules/mypageStore'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    userStore: userStore,
    mypageStore: mypageStore
  }
})

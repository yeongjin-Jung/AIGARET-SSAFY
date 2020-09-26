import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../components/Account/Login.vue')
  },
  {
    path: '/signup',
    name: 'Signup',
    component: () => import('../components/Account/Signup.vue')
  },
  {
    path: '/info',
    name: 'Info',
    component: () => import('../components/Account/Info.vue')
  },
  {
    path: '/report',
    name: 'Report',
    component: () => import('../components/UserInfomation/MyTrainingReport.vue')
  },
  {
    path: '/WristTouchGame',
    name: 'WristTouchGame',
    component: () => import('../components/Game/WristTouchGame.vue')
  },
  {
    path: '/SnakeGame',
    name: 'SnakeGame',
    component: () => import('../components/Game/SnakeGame.vue')
  },
  {
    path: '/JumpGame',
    name: 'JumpGame',
    component: () => import('../components/Game/JumpGame.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

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
    path: '/game/WristTouchGame',
    name: 'WristTouchGame',
    component: () => import('../components/Game/WristTouchGame.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

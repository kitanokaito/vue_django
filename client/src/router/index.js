import Vue from 'vue'
import Router from 'vue-router'
import Auth from '@/components/pages/Auth'
import Home from '@/components/pages/Home'
import Mypage from '@/components/pages/Mypage'
import Users from '@/components/pages/Users'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/auth',
      component: Auth
    },
    {
       path: '/mypage',
       component: Mypage
    },
    {
      path: '/users',
      component: Users
   },
  ],
  mode: 'history',
})
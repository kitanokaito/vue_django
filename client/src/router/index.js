import Vue from 'vue'
import Router from 'vue-router'

import Auth from '@/components/pages/Auth'
import Home from '@/components/pages/Home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HedgeHogs',
      component: Home
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    }
  ],
  mode: 'history',
})
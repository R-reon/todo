import Vue from 'vue'
import Router from 'vue-router'

import Auth from '@/components/pages/Auth'
import HedgeHogs from '@/components/pages/HedgeHogs'
// import Todo from '@/components/pages/Todo'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/todo',
      name: 'HedgeHogs',
      component: HedgeHogs
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    },
    // {
    //   path: '/todo',
    //   name: 'Todo',
    //   component: Todo
    // }
  ]
})

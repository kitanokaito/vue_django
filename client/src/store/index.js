import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';

import auth from './auth';
import restaurants from './restaurants';

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    restaurants,
    auth,
  },
  plugins: [createPersistedState({ storage: window.sessionStorage })],
})

export default store

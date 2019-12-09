import axios from '@/utils'

const state = {
  username: null,
  token: null,
  apiStatus: null,
};

const getters = {};

const mutations = {
  setLogin(state, payload) {
    state.username = payload.username
    state.token = payload.token
    state.apiStatus = payload.status
  },
  setLogout(state) {
    state.token = null;
  },
};

const actions = {
  async loginAction(context, form) {
    const payload = {
      token: null,
      status: true,
      username: form.username,
    };
    try {
      const { data } = await axios.post('auth/', form);
      payload.token = data.token;
    } catch(error) {
      payload.username = '';
      payload.status = false;
    }
    context.commit('setLogin', payload);
  },
  
  logoutAction(context) {
    context.commit('setLogout');
  }
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
}
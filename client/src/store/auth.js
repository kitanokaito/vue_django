import axios from '@/utils'

const state = {
  profile: null,
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
  setMyinfo(state, profile) {
    state.profile = profile;

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
  },


  async getUserInfoAction(context, token) {
    axios.defaults.headers.common['Authorization'] = `JWT ${token}`;
    const { data } = await axios.get('api/myinfo');
    [...data].forEach((_, i) => { data[i].image=axios.defaults.baseURL+data[i].image })
    context.commit('setMyinfo', data[0]);
  },  
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
}
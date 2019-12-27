import axios from '@/utils'

const state = {
  profile: {
    handle_name: null,
    icon: null,
    comment: null,
  },
  username: null,
  token: null,
  apiStatus: null,
};

const getters = {};

const mutations = {
  setRegister(state, payload) {
    state.apiStatus = payload.status
  },
  setLogin(state, payload) {
    state.username = payload.username
    state.token = payload.token
    state.apiStatus = payload.status
  },
  setLogout(state) {
    state.token = null;
  },
  setMyinfo(state, profile) {
    state.profile = Object.assign({}, profile);
  },
};

const actions = {
  async registerAction(context, form) {
    const payload = {
      status: true,
    };
    try {
      await axios.post('api/user_create', form);
    } catch(error) {
      payload.status = false;
    }
    context.commit('setRegister', payload);
  },

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
    [...data].forEach((_, i) => { 
      data[i].icon = data[i].icon ? axios.defaults.baseURL+data[i].icon
       : axios.defaults.baseURL+'/media/profile_image/no-icon.jpeg'
    })
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
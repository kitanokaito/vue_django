import axios from '@/utils'

const state = {
  list: [],
  goodNum: null,
  goodStatus:null,
  apiStatus: null,
}

const getters = {

}
const mutations = {
  setRestaurants(state, list) {
    state.list = list;
  },
  setGoodStatus(state, good) {
    state.goodStatus = good ? true : false;
  },
  setGoodNum(state, num) {
    state.goodNum = num;
  },
  setApiStatus(state, status) {
    state.apiStatus = status;
  }
}
const actions = {
  async getListAction(context, token) {
    axios.defaults.headers.common['Authorization'] = `JWT ${token}`;
    const { data } = await axios.get('api/store/');
    context.commit('setRestaurants', data);
  },


  async goodCreateAction(context, res) {
    let status = true;
    try {
      axios.defaults.headers.common['Authorization'] = `JWT ${res.token}`;
      await axios.post('api/good/create/', {
        to_store: res.storeId,
      });
    } catch (error) {
      status = false;
    }
    context.commit('setApiStatus', status);
  },


  async goodDestroyAction(context, res) {
    let status = true;
    const params = {
      to_store: res.storeId,
    }
    try {
      axios.defaults.headers.common['Authorization'] = `JWT ${res.token}`;
      await axios.delete('api/good/destroy/', { params });
    } catch (error) {
      status = false;
    }
    context.commit('setApiStatus', status);
  },


  async getGoodStatusAction(context, res) {
    let status = true;
    const params = {
      to_store: res.storeId,
    }
    try {
      axios.defaults.headers.common['Authorization'] = `JWT ${res.token}`;
      const { data } = await axios.get('api/good/status/', { params });
      context.commit('setGoodStatus', data);
    } catch (error) {
      status = false;
    }
    context.commit('setApiStatus', status);
  },


  async getGoodNumAction(context, res) {
    let status = true;
    const params = {
      to_store: res.storeId,
    }
    try {
      axios.defaults.headers.common['Authorization'] = `JWT ${res.token}`;
      const { data } = await axios.get('api/good/num/', { params });
      context.commit('setGoodNum', data);
    } catch (error) {
      status = false;
    }
    context.commit('setApiStatus', status);
  },

}


export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}

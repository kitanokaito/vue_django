import axios from '@/utils'

const state = {
  list: [],
  goodNum: null,
  apiStatus: null,
}

const getters = {

}
const mutations = {
  setRestaurants(state, list) {
    state.list = list;
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
        from_user: res.userId,
        to_store: res.storeId,
      });
    } catch (error) {
      status = false;
    }
    context.commit('setApiStatus', status);
  },
  async goodDestroyAction(context, res) {
    let status = true;
    try {
      axios.defaults.headers.common['Authorization'] = `JWT ${res.token}`;
      await axios.delete(`api/good/destroy/${res.userId}/${res.storeId}`);
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
      console.log(data);
      context.commit('setGoodNum', data);
    } catch (error) {
      status = false;
    }
    context.commit('setApiStatus', status);
  }
}


export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}

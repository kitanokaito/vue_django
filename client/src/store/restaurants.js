import axios from '@/utils'

const state = {
  list: [],
}

const getters = {

}
const mutations = {
  setRestaurants(state, list) {
    state.list = list;
  }
}
const actions = {
  async getListAction(context, token) {
    axios.defaults.headers.common['Authorization'] = `JWT ${token}`;
    const { data } = await axios.get('api/store/');
    context.commit('setRestaurants', data);
  }
}


export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}

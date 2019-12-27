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
  setLists(state, list) {
    state.list = list;
  },
  setUsers(state, list) {
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
  async getStoreListAction(context) {
    // axios.defaults.headers.common['Authorization'] = `JWT ${token}`;
    const { data } = await axios.get('api/store/');
    [...data].forEach((_, i) => { 
      data[i].icon = data[i].icon ? axios.defaults.baseURL+data[i].icon
       : axios.defaults.baseURL+'/media/profile_image/no-icon.jpeg'
       data[i].image = axios.defaults.baseURL+data[i].image
    })
    context.commit('setLists', data);
  },


  async getUsersListAction(context, res) {
    axios.defaults.headers.common['Authorization'] = `JWT ${res.token}`;
    const { data } = await axios.get('api/users/');
    context.commit('setLists', data);
  },


  async getStoreListOfUserAction(context, res) {
    const params =  {
      username: res.username,
    }
    axios.defaults.headers.common['Authorization'] = `JWT ${res.token}`;
    const { data } = await axios.get('api/store/user', { params });
    [...data].forEach((_, i) => { 
      data[i].icon = data[i].icon ? axios.defaults.baseURL+data[i].icon
       : axios.defaults.baseURL+'/media/profile_image/no-icon.jpeg'
    })
    context.commit('setLists', data);
  },


  async goodCreateAction(context, res) {
    let status = true;
    try {
      axios.defaults.headers.common['Authorization'] = `JWT ${res.token}`;
      await axios.post('api/good/', {
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
      await axios.delete(`api/good/${res.storeId}`, { params });
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
      const { data } = await axios.get(`api/good/${res.storeId}`, { params });
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
      const { data } = await axios.get('api/good/', { params });
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

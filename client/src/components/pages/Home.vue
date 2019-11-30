<template>
  <div>
    <ul>
      <li v-for="restaurant in list" :key="restaurant.id">
          <img :src="restaurant.image" alt="">
      </li>  
    </ul>
  </div>
</template>

<script>
import router from "../../router";
import { mapState } from 'vuex';
export default {
  name: "home",
  mounted() {
    // this.checkLoggedIn();
  },
  created() {
    // this.getStoreList();
  },
  data(){
    return {
    };
  },
  computed:{
    ...mapState({
      token: state => state.auth.token,
      list: state => state.restaurants.list
    })
  },
  methods: {
    checkLoggedIn() {
      if (!this.token) {
        router.push("/auth");
      }
    },
    getStoreList() {
      this.$store.dispatch('restaurants/getListAction', this.token);
    }
  }
};
</script>
<template>
  <div>
    <v-container fluid>
      <v-row dense>
        <v-col
          v-for="restaurant in list"
          :key="restaurant.name"
          :cols="restaurant.flex"
        >
          <Card
            :restaurant="restaurant"
            :username="username"
            :token="token"
          />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import router from "../../router";
import { mapState } from 'vuex';
import Card from '../molecules/Card.vue';
export default {
  name: "home",
  mounted() {
    this.checkLoggedIn();
  },
  created() {
    this.getStoreList();
  },
  data(){
    return {
      like: false,
      bookmark: false,
    };
  },
  components: {
    Card,
  },
  computed:{
    ...mapState({
      username: state => state.auth.username,
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
      this.$store.dispatch('restaurants/getStoreListAction', this.token);
    },
  }
};
</script>
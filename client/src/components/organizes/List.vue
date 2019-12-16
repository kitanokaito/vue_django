<template>
  <div>
    <v-card 
      shaped
      v-for="post in list" :key="post.id"
    >
      <Card
        :post="post"
        :token="token"
      />
    </v-card>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Card from '../molecules/Card.vue';
export default {
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
      token: state => state.auth.token,
      list: state => state.restaurants.list
    })
  },
  methods: {
    getStoreList() {
      this.$store.dispatch('restaurants/getStoreListAction', this.token);
    },
  }
};
</script>
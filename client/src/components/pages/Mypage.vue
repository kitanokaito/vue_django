<template>
  <v-container fluid>
    <v-row no-gutters class="nav">
      <Navbar/>
    </v-row>
    <v-card height="500">
      <v-img
        :src="list[0].image"
        class="white--text align-end"
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        height="300"
      >
        <v-col class="py-0">
          <v-list-item
            color="rgba(0, 0, 0, .4)"
            dark
          >
            <v-avatar size="100">
            <img
              src="https://cdn.vuetifyjs.com/images/john.jpg"
              alt="John"
            />
            </v-avatar> 
            <v-list-item-content>
              <v-list-item-title class="title">北野魁人</v-list-item-title>
              <v-list-item-subtitle>蕎麦いいよね</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-col>
      </v-img>
      <v-row
        class="mb-6"
        no-gutters
      >
        <v-col
          v-for="card in cards"
          :key="card"
          class="per"
        >
          <v-card
            class="pa-2"
            tile
            outlined
          >
            <span class="card-title">{{ card }}</span>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';

import Navbar from '../organizes/Navbar.vue'; 

export default {
  created() {
    this.getStoreList();
  },
  data() {
    return {
      cards: [
        '行ったお店',
        'ブックマーク',
        'フォロー',
        'フォロワー'
      ]
    };
  },
  components: {
    Navbar,
  },
  computed: {
    ...mapState({
      username: state => state.auth.username,
      token: state => state.auth.token,
      list: state => state.restaurants.list,
    }),
  },
  methods: {
    getStoreList() {
      this.$store.dispatch('restaurants/getStoreListOfUserAction', {
        token: this.token,
        username: this.username
      });
    }
  }
}
</script>

<style scoped>
.nav{
  height: 50px;
  /* background-color: red; */
}
.user{
  background-color:aqua;
}
.card-title {
  color: gray;
  font-size: 10px;
}
</style>


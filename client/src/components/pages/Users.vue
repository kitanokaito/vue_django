<template>
  <div>
    <v-row no-gutters>
      <Navbar/>
    </v-row>
    <v-row no-gutters>
      <v-col
        :cols="3"
        class="side"
      >
        bbb
      </v-col>
      <v-col
        :cols="9"
      >
        <v-card 
          v-for="i in 4"
          :key="i"
          shaped
        >
          <v-img
            :src="list[0].image"
            gradient="to bottom, rgba(0,0,0,.3), rgba(0,0,0,.5)"
            height="100"
          >
            <v-list-item
              color="rgba(0, 0, 0, .4)"
              dark
            >
              <v-list-item-avatar size="80">
                <img
                  src="https://cdn.vuetifyjs.com/images/john.jpg"
                  alt="John"
                />
              </v-list-item-avatar> 
              <v-list-item-content>
                <v-list-item-title>北野魁人</v-list-item-title>
                <div>
                  <v-btn x-small rounded color="secondary">フォロー</v-btn>
                </div>
                <v-list-item-subtitle>蕎麦いいよね</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-img>
        </v-card>
      </v-col>
    </v-row>
  </div>
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
.side{
  background-color:aqua;
}
.card-title {
  color: gray;
  font-size: 10px;
}
</style>


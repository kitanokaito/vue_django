<template>
  <div>
    <v-row>
      <Navbar/>
    </v-row>
    <v-row no-gutters>
      <v-card height="500">
        <v-img
          :src="list[0].image"
          class="white--text align-end"
          gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
          height="300"
        >
        <v-row no-gutters>
          <v-col class="py-0">
            <v-list-item
              color="rgba(0, 0, 0, .4)"
              dark
            >
              <v-avatar size="100">
              <img
                :src="profile.image"
                alt="John"
              />
              </v-avatar> 
              <v-list-item-content>
                <v-list-item-title class="title">{{ profile.handle_name }}</v-list-item-title>
                <v-list-item-subtitle>{{ profile.comment }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-col>
          <v-col>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn class="">
                <v-icon>mdi-credit-card-wireless</v-icon>
              </v-btn>
            </v-card-actions>
          </v-col>
        </v-row>
        </v-img>
        <v-row
          class="mb-6"
          no-gutters
        >
          <v-col
            v-for="card in cards"
            :key="card"
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
      ],
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
      profile: state => state.auth.profile,
    }),
  },
  methods: {
    async getStoreList() {
      await this.$store.dispatch('auth/getUserInfoAction', this.token);
    }
  }
}
</script>

<style scoped>
.contain {
  padding: 0px;
}
.user{
  background-color:aqua;
}
.card-title {
  color: gray;
  font-size: 10px;
}
</style>


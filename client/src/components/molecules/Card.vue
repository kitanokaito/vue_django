<template>
  <v-card>
    <v-list-item outlined class="user">
      <v-list-item-avatar>
        <v-img
          src="https://cdn.vuetifyjs.com/images/john.jpg"
        />
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title>
          {{ post.username }}
        </v-list-item-title>
        <v-list-item-subtitle>
          {{ post.email }}
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-divider class="divider"/>
    <v-list-item> 
      <v-list-item-content>
        <v-list-item-title>
          {{ post.name }}
        </v-list-item-title>
        <v-list-item-subtitle>
          {{ post.name }}
        </v-list-item-subtitle>
      </v-list-item-content>
      <v-card-actions>
        <span>{{ num }}</span>
        <v-btn icon :color="good ? 'pink' : ''" @click="goodBtn(post.id)">
          <v-icon>mdi-heart</v-icon>
        </v-btn>
        <v-btn icon :color="bookmark ? 'green' : ''" @click="bookmark=!bookmark">
          <v-icon>mdi-bookmark</v-icon>
        </v-btn>
      </v-card-actions>
    </v-list-item>
    <v-img
      :src="post.image"
      class="white--text align-end"
      gradient="to bottom, rgba(0,0,0,0), rgba(0,0,0,0.4)"
      height="300"
    >
      {{ post.body }}
    </v-img>
  </v-card>
</template>


<script>
import { mapState } from 'vuex';
export default {

  async beforeMount() {
    await this.getGoodNum();
    this.num = this.goodNum;
    await this.getGoodStatus();
    this.good = this.goodStatus;
  },
  data() {
    return{
      bookmark: false,
      good: false,
      num: null,
    };
  },
  props: {
    post: Object,
    token: String,
  },
  computed: {
    ...mapState({
      goodNum: state => state.restaurants.goodNum,
      goodStatus: state => state.restaurants.goodStatus,
      apiStatus: state => state.restaurants.apiStatus,
    }),
  },
  methods: {
    async goodBtn(id) {
      if (!this.good) {
        await this.$store.dispatch('restaurants/goodCreateAction', {
          storeId: id, 
          token: this.token
        });
        this.good = !this.good
        this.num = this.num + 1;
      } else {
        await this.$store.dispatch('restaurants/goodDestroyAction', {
          storeId: id, 
          token: this.token
        });
        this.good = !this.good
        this.num = this.num - 1;
      }
    },
    async getGoodNum() {
      await this.$store.dispatch('restaurants/getGoodNumAction', {
        storeId: this.post.id, 
        token: this.token
      });
    },
    async getGoodStatus() {
      await this.$store.dispatch('restaurants/getGoodStatusAction', {
        storeId: this.post.id, 
        token: this.token
      });
    }
  }
}
</script>

<style scoped>
.divider {
  margin: 0
}
.user {
  background-color: lightgrey;
}
</style>

<template>
  <v-card>
    <v-img
      :src="restaurant.image"
      class="white--text align-end"
      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
      height="150"
    >
      <v-card-title v-text="restaurant.name"></v-card-title>
    </v-img>
    <v-card-actions>
      <v-spacer></v-spacer>

      <span>{{ num }}</span>
      <v-btn icon :color="good ? 'pink': ''" @click="goodBtn(restaurant.id)">
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon :color="bookmark ? 'green': ''" @click="bookmark = !bookmark">
        <v-icon>mdi-bookmark</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-share-variant</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>


<script>
import { mapState } from 'vuex';
export default {

  created() {
    
    
  },
  async beforeMount() {
    await this.getGoodNum();
    this.num = this.goodNum;
    await this.getGoodStatus();
    this.good = this.goodStatus;
  },
  data() {
    return{
      userId: 0,
      bookmark: false,
      good: false,
      num: null,
    };
  },
  props: {
    restaurant: Object,
    username: String,
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
      if(this.username == "dev") {
        this.userId = 1;
      } else {
        this.userId = 2;
      }
      
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
        storeId: this.restaurant.id, 
        token: this.token
      });
    },
    async getGoodStatus() {
      await this.$store.dispatch('restaurants/getGoodStatusAction', {
        storeId: this.restaurant.id, 
        token: this.token
      });
    }
  }
}
</script>


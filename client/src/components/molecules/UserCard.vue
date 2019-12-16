<template>
  <div>
    <v-card 
      v-for="post in list" :key="post.id"
      shaped
    >
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
          <v-btn icon :color="good ? 'pink' : ''" @click="good=!good">
            <v-icon>mdi-heart</v-icon>
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
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  created() {
    this.getStoreList();
  },
  data () {
    return {
      good: false,
    }
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
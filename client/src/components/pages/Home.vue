<template>
  <v-container fluid>
    <v-row no-gutters class="nav">
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
        class="list"
      >
        <List/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import router from '../../router';
import { mapState } from 'vuex';
import List from '../organizes/List.vue';
import Navbar from '../organizes/Navbar.vue';

export default {
  created() {
    if(!this.token) {
      router.push('/auth');
    }
  },
  data() {
    return{

    };
  },
  components:{
    List,
    Navbar,
  },
  computed: {
    ...mapState({
      token: state => state.auth.token,
    }),
  },
}
</script>

<style scoped>
.nav{
  height: 50px;
  /* background-color: red; */
}
.side{
  /* height: 500px; */
  background-color: blue;
}
</style>

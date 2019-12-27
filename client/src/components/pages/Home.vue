<template>
  <div>
    <v-row no-gutters>
      <Navbar
        :token="token"
      />
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
  </div>
</template>

<script>
// import router from '../../router';
import { mapState } from 'vuex';
import List from '../organizes/List.vue';
import Navbar from '../organizes/Navbar.vue';

export default {
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
.side{
  background-color: aqua;
}
</style>

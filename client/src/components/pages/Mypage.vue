<template>
  <v-container fluid>
    <v-row no-gutters height="50">
      <Navbar/>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';

import Navbar from '../organizes/Navbar.vue'; 
export default {
  data() {
    return {

    };
  },
  components: {
    Navbar,
  },
  computed: {
    ...mapState({
      username: state => state.auth.username,
    }),
  },
}
</script>


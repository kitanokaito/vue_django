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
.list {
  /* height: 500px; */
  /* background-color: green; */
}

</style>

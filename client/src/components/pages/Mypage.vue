<template>
  <h1>
    {{ username }}
  </h1>

</template>

<script>
import { mapState } from 'vuex';

export default {
  data() {
    return {

    };
  },
  computed: {
    ...mapState({
      username: state => state.auth.username,
    }),
  },
}
</script>


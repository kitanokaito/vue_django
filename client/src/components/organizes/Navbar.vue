<template>
  <v-app-bar color="primary" dark>
    <v-btn text @click="goHome">
      <v-toolbar-title>きたログ</v-toolbar-title>
    </v-btn>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-btn text @click="goUsers">ユーザ一覧</v-btn>
      <v-menu offset-y>
        <template v-slot:activator="{on}">
        <v-btn v-on="on" text>{{ username }}</v-btn>
        </template>
        <v-list>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title @click="goMypage">マイページ</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title @click="logout">ログアウト</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-toolbar-items>
  </v-app-bar>
</template>

<script>
import { mapState } from 'vuex';
import router from '../../router'

export default {
  data() {
    return {

    };
  },
  computed:{
    ...mapState({
      token: state => state.auth.token,
      username: state => state.auth.username,
      apiStatus: state => state.auth.apiStatus,
      list: state => state.restaurants.list,
    })
  },
  methods:{
    goHome() {
      router.push('/');
    },
    goMypage() {
      router.push('/mypage')
    },
    goUsers() {
      router.push('/users')
      // await this.$store.dispatch('restaurants/getUsersListAction', {
      //   token: this.token
      // });
      // console.log(this.list);
    },
    async logout() {
      await this.$store.dispatch('auth/logoutAction');
      router.push('/auth');
    }
  }
}
</script>


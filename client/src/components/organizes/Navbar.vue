<template>
  <v-app>
    <v-app-bar color="primary" app dark>
      <v-btn text @click="goHome">
        <v-toolbar-title>きたログ</v-toolbar-title>
      </v-btn>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn text>ユーザ一覧</v-btn>
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
  </v-app>
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
      username: state => state.auth.username,
      apiStatus: state => state.auth.apiStatus,
    })
  },
  methods:{
    goHome() {
      router.push('/');
    },
    goMypage() {
      router.push('/mypage')
    },
    async logout() {
      await this.$store.dispatch('auth/logoutAction');
      router.push('/auth');
    }
  }
}
</script>


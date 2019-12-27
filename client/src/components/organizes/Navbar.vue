<template>
  <v-app-bar color="primary" dark>
    <v-btn text @click="goHome">
      <v-toolbar-title>きたログ</v-toolbar-title>
    </v-btn>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-btn text @click="goUsers">ユーザ一覧</v-btn>
      <v-menu v-if="token" offset-y>
        <template v-slot:activator="{on}">
          <v-btn v-on="on" text>
            <v-icon>mdi-account</v-icon>
            {{ username }}
          </v-btn>
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
      <v-menu v-else offset-y>
        <template v-slot:activator="{on}">
          <v-btn v-on="on" text>きたログを使う</v-btn>
        </template>
        <v-list>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title @click="goLogin">ログイン</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title @click="goRegister">新規登録</v-list-item-title>
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
      username: state => state.auth.username,
      apiStatus: state => state.auth.apiStatus,
    })
  },
  props: {
    token: String,
  },
  methods:{
    goHome() {
      router.push('/');
    },
    goLogin() {
      router.push('/auth');
    },
    goRegister() {
      router.push('/register');
    },
    goMypage() {
      router.push('/mypage')
    },
    goUsers() {
      router.push('/users')
    },
    async logout() {
      await this.$store.dispatch('auth/logoutAction');
      router.push('/auth');
    }
  }
}
</script>


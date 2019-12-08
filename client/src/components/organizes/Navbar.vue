<template>
  <v-app>
    <v-app-bar color="primary" app dark>
      <v-toolbar-title>いい店</v-toolbar-title>
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
                <v-list-item-action @click="goMypage">マイページ</v-list-item-action>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>ログアウト</v-list-item-title>
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
    })
  },
  methods:{
    goMypage() {
      router.push('/mypage')
    }
  }
}
</script>


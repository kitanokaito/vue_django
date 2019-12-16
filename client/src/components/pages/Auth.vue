<template>
	<v-container grid-list-md>
		<v-layout row wrap align-center justify-center fill-height>
			<v-flex xs12 sm8 lg4 md5>
				<v-card class="login-card">
					<v-card-title>
						<span class="headline">Login to きたログ</span>
					</v-card-title>
					<v-spacer/>
					<v-card-text>
						<v-layout
							row
							fill-height
							justify-center
							align-center
							v-if="loading"
						>
							<v-progress-circular
								:size="50"
								color="primary"
								indeterminate
							/>
						</v-layout>
						<v-form v-else ref="form" v-model="valid" lazy-validation>
							<v-container>
								<v-text-field
									v-model="credentials.username"
									:counter="70"
									label="ユーザー名"
									:rules="rules.username"
									maxlength="70"
									required
								/>
								<v-text-field
									type="password"
									v-model="credentials.password"
									:counter="20"
									label="パスワード"
									:rules="rules.password"
									maxlength="20"
									required
								/>
							</v-container>
							<v-btn class="pink white--text" :disabled="!valid" @click="login">Login</v-btn>
						</v-form>
					</v-card-text>
				</v-card>
			</v-flex>
		</v-layout>
	</v-container>
</template>

<script>
import Swal from 'sweetalert2';
import router from '../../router';
import { mapState } from 'vuex'; 
export default {
	data: () => ({
		credentials: {},
		valid:true,
		loading:false,
		rules: {
			username: [
				v => !!v || "ユーザー名は必須です",
				v => (v && v.length > 2) || "ユーザー名は3文字以上でなければなりません",
				v => /^[a-z0-9_]+$/.test(v) || "許可されていない文字が入力されています"
			],
			password: [
				v => !!v || "パスワードは必須です",
				v => (v && v.length > 4) || "パスワードは5文字以上でなければなりません"
			]
		}
	}),
	computed: {
		...mapState({
			token: state => state.auth.token,
			apiStatus: state => state.auth.apiStatus,
		})
	},
	methods: {
		async login() {
			if (this.$refs.form.validate()) {
				await this.$store.dispatch('auth/loginAction', this.credentials);
				if (this.apiStatus) {
					router.push('/');
				} else {
					Swal.fire({
						title: 'Error',
						text: 'ユーザー名もしくはパスワード、または両方が間違っています',
						showConfirmButton:false,
						showCloseButton:false,
						timer:3000
					})
					this.credentials = {}
				}
			}
		},
	}
}
</script>
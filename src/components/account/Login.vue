<template>

    <div>

        <h1 class="h1">Войти</h1>

        <form class="form"
              v-on:submit.prevent="murrenLogin">

            <input type="text"
                   v-model="murrenName"
                   placeholder="Имя Муррена">

            <br>

            <input type="password"
                   v-model="password"
                   placeholder="Пароль">

            <br><br>

            <button type="submit">
                Погнали</button>

        </form>

    </div>

</template>

<script>

    import axios from 'axios'

    export default {

        data() {

            return {

                murrenName: '',
                password: '',
            }
        },

        methods: {

            async murrenLogin() {

                let cred = {

                    username: this.murrenName,
                    password: this.password,
                };

                let tokens = await axios.post('/murren/token_create/', cred);

                if (tokens) {

                    localStorage.setItem('accessToken', tokens.data.access);
                    localStorage.setItem('refreshToken', tokens.data.refresh);
                    this.$store.commit('auth/AUTHENTICATE');
                }

                return this.$store.dispatch('auth/set_token', tokens.data)
            },
        },
    }

</script>

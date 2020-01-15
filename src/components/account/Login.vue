<template>

    <div>

        <h1 class="h1">Войти</h1>

        <div class="erorrHandling" v-if="isError">
            {{ errorText }}
        </div>

        <form class="form"
              v-on:submit.prevent="murrenLogin">

            <!-- <input type="text"
                   v-model="murrenName"
                   placeholder="Имя Муррена"> -->

            <MurrInput  
                type="text" 
                placeholder="Имя Муррена" 
                :isError="error_container.hasOwnProperty('username')"
                :errorText=" error_container.hasOwnProperty('username') ? error_container.username : null " 
                @input="val => murrenName = val" />
            <br>

            <MurrInput  
                type="password" 
                placeholder="Пароль" 
                :isError="error_container.hasOwnProperty('password')"
                :errorText=" error_container.hasOwnProperty('password') ? error_container.password : null " 
                @input="val => password = val" />

            <br>

            <button type="submit">
                Погнали</button>

        </form>

    </div>

</template>

<script>

    import axios from 'axios';
    import MurrInput from '@/components/Input';

    export default {

        components: {
            MurrInput
        },

        data() {

            return {

                murrenName: '',
                password: '',

                isError: false,
                errorText: null,

                error_container: {},
            }
        },

        methods: {

            async murrenLogin() {
                this.error_container = {};
                this.isError = false;
                this.errorText = null;

                if (this.murrenName !== '' && this.password !== '') {
                    let cred = {

                    username: this.murrenName,
                    password: this.password,
                    };

                    try {
                        let tokens = await axios.post('/murren/token_create/', cred);
                        
                        this.isError = false;
                        this.errorText = null;

                        if (tokens) {
                            localStorage.setItem('accessToken', tokens.data.access);
                            localStorage.setItem('refreshToken', tokens.data.refresh);
                            this.$store.commit('auth/AUTHENTICATE');
                        }

                        return this.$store.dispatch('auth/set_token', tokens.data)
                    } catch(e) {
                        this.isError = true;
                        this.errorText = 'Неверное имя пользователя или пароль.'
                    }
                } else {
                    if (this.murrenName === '') {
                        this.error_container.username = 'Это поле обязательно';
                    }
                    if (this.password === '') {
                        this.error_container.password = 'Это поле обязательно'
                    }
                }
            },
        },
    }

</script>

<style>
    .erorrHandling {
        color: red;
        text-align: center;

        margin-bottom: 10px;
    }
</style>
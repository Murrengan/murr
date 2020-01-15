<template>

    <div>

        <h1 class="h1">Регистрация</h1>

        <form class="form"
              v-on:submit.prevent="murrenSignup">

            <!-- <input type="text"
                   id="murren_name"
                   :class="{ error: error_container.hasOwnProperty('username') }"
                   v-model="murrenName"
                   placeholder="Имя Муррена">
            <p v-if="error_container.hasOwnProperty('username')">{{ error_container.username }}</p>
             -->
            <MurrInput  
                type="text" 
                placeholder="Имя Муррена" 
                :isError="error_container.hasOwnProperty('username')"
                :errorText=" error_container.hasOwnProperty('username') ? error_container.username : null " 
                @input="val => murrenName = val" />
            <br>

            <!-- <input type="email"
                   id="email"
                  :class="{ error: error_container.hasOwnProperty('email') }"
                   v-model="murrenEmail"
                   placeholder="Почта">
            <p v-if="error_container.hasOwnProperty('email')">{{ error_container.email }}</p>
            <br> -->

            <MurrInput  
                type="email" 
                placeholder="Почта" 
                :isError="error_container.hasOwnProperty('email')"
                :errorText=" error_container.hasOwnProperty('email') ? error_container.email : null " 
                @input="val => murrenEmail = val" />
            <br>

            <!-- <input type="password"
                   id="password"
                   :class="{ error: error_container.hasOwnProperty('password') }"
                   v-model="password"
                   placeholder="Пароль">

            <p v-if="error_container.hasOwnProperty('password')">{{ error_container.password }}</p>
             -->
            
            <MurrInput  
                type="password" 
                placeholder="Пароль" 
                :isError="error_container.hasOwnProperty('password')"
                :errorText=" error_container.hasOwnProperty('password') ? error_container.password : null " 
                @input="val => password = val" />
            <br>

            <br>

            <button type="submit"
                    class="submit_btn">
                Погнали
            </button>

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
                murrenEmail: '',
                password: '',


                murr_back_errors: '',

                error_text: [],
                error_container: {},

                murren_name_form_error: false,
                murren_email_form_error: false,
                password_form_error: false,

                input_have_error: false
            }
        },

        watch: {

            murren_name() {
                this.reset_error_class_and_text();
            },

            murrenEmail() {
                this.reset_error_class_and_text();
            },

            password() {
                this.reset_error_class_and_text();
            },
        },

        methods: {

            async murrenSignup() {

                const murr_back_response = await axios.post('/murren/register/', {

                    username: this.murrenName,
                    email: this.murrenEmail,
                    password: this.password,
                });

                if (murr_back_response.data.is_murren_created === 'true') {

                    await this.$router.push({name: 'check_email'})

                } else {

                    this.error_container = {};

                    for (let error_field in murr_back_response.data) {

                        // if (error_field === 'username') {

                        //     this.murren_name_form_error = true;
                        //     this.error_text.push(murr_back_response.data[error_field][0]);

                        // } else if (error_field === 'email') {

                        //     this.murren_email_form_error = true;
                        //     this.error_text.push(murr_back_response.data[error_field][0]);

                        // } else if (error_field === 'password') {

                        //     this.password_form_error = true;
                        //     this.error_text.push(murr_back_response.data[error_field][0]);
                        // }
                        this.error_container = {
                            ...this.error_container,
                            [error_field]: murr_back_response.data[error_field][0]
                        }
                    }

                    this.input_have_error = true;
                }
            },

            reset_error_class_and_text() {

                this.murren_name_form_error = false;
                this.murren_email_form_error = false;
                this.password_form_error = false;
                this.input_have_error = false;
            },
        },

        computed: {

            murren_name_form_class() {
                return {
                    error: this.murren_name_form_error,
                }
            },

            murren_email_form_class() {
                return {
                    error: this.murren_email_form_error,
                }
            },

            password_form_class() {
                return {
                    error: this.password_form_error,
                }
            },
        },
    }

</script>

<style>

    .error {
        border: #ff0a36 10px solid;
    }

    .container__error-text {
        margin: 0 auto;
        background-color: pink;
        max-width: 300px;
        color: #0072ff;
    }

</style>
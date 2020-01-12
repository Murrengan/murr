<template>

    <div>

        <h1 class="h1">Регистрация</h1>

        <form class="form"
              v-on:submit.prevent="murrenSignup">

            <input type="text"
                   id="murren_name"
                   v-bind:class="murren_name_form_class"
                   v-model="murrenName"
                   placeholder="Имя Муррена">

            <br>

            <input type="email"
                   id="email"
                   v-bind:class="murren_email_form_class"
                   v-model="murrenEmail"
                   placeholder="Почта">

            <br>

            <input type="password"
                   id="password"
                   v-bind:class="password_form_class"
                   v-model="password"
                   placeholder="Пароль">

            <div
                    v-if="input_have_error"
                    class="container__error-text">

                <p v-for="(error, index) in error_text"
                   :key="index">
                    {{ error }}</p>
            </div>

            <br>

            <button type="submit"
                    class="submit_btn">
                Погнали
            </button>

        </form>

    </div>

</template>

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

<script>

    import axios from 'axios'

    export default {

        data() {

            return {

                murrenName: '',
                murrenEmail: '',
                password: '',


                murr_back_errors: '',

                error_text: [],

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

                    this.error_text = [];

                    for (let error_field in murr_back_response.data) {

                        if (error_field === 'username') {

                            this.murren_name_form_error = true;
                            this.error_text.push(murr_back_response.data[error_field][0]);

                        } else if (error_field === 'email') {

                            this.murren_email_form_error = true;
                            this.error_text.push(murr_back_response.data[error_field][0]);

                        } else if (error_field === 'password') {

                            this.password_form_error = true;
                            this.error_text.push(murr_back_response.data[error_field][0]);
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
        }
    }

</script>
<template>
    <div>

        <h1 class="h1">Login</h1>

        <form class="form"
              v-on:submit.prevent="on_click">

            <label>
                <input type="text"
                       v-model="murren_name_or_email"
                       placeholder="Имя Муррена или почта">
            </label>

            <br>

            <label>
                <input type="password"
                       v-model="password"
                       placeholder="Пароль">
            </label>


            <br><br>

            <button type="submit">Погнали</button>

        </form>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                murren_name_or_email: '',
                password: '',
            }
        },
        methods: {
            on_click() {
                this.password = '';
                this.murren_name_or_email = '';
            }
        }
    }
</script>

<template>
    <div>

        <h1 class="h1">Sign up</h1>

        <form class="form"
              v-on:submit.prevent="on_click">

            <label>
                <input type="text"
                       v-model="murren_name"
                       placeholder="Имя Муррена">
            </label>

            <br>

            <label>
                <input type="email"
                       v-model="email"
                       placeholder="Почта">
            </label>

            <br>

            <label>
                <input type="password"
                       v-model="password"
                       placeholder="Пароль">
            </label>

            <br><br>

            <button type="submit" class="button">Погнали</button>

        </form>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                email: '',
                password: '',
                murren_name: '',
            }
        },
        methods: {
            on_click() {
                this.email = '';
                this.password = '';
                this.murren_name = '';
            }
        }
    }
</script>

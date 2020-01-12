<template>

    <div class="email-confirm">

        <h3>Замечательно! Почта успешно подтверждена</h3>

        <router-link
                :to="{name:'login'}">

            <button>Войти</button>

        </router-link>

    </div>

</template>


<script>

    import axios from "axios";

    export default {

        async created() {

            const murren_id = this.$route.query.activation_code;

            let data =  {murren_id: murren_id};

            await axios.post('/murren/activation/', data);
        }
    }

</script>

<style>

</style>
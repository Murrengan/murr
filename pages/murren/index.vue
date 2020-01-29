<template>
  <div>
    <h1 class="title">Страница Муррена</h1>
    <ul>
      <li v-for="murren_id in murrens_id" :key="murren_id">
        <a href="#" @click.prevent="goTo(murren_id)">Муррен с ид {{ murren_id }}</a>

      </li>
    </ul>
  </div>

</template>

<script>
    export default {
        data: () => ({
            murrens_id: [
                1, 2, 3, 4, 5
            ]
        }),
        methods: {
            goTo(murren_id) {
                this.$router.push('/murren/' + murren_id)
            }
        },
    }
</script>

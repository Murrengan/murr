<template>

    <h1>{{ msg_variable }}</h1>

</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg_variable: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

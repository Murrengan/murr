<template>
  <div class="main-container">
    <header>

    </header>

    <main>
      <nuxt/>
    </main>

    <footer>
      <Footer/>
    </footer>

  </div>
</template>

<script>

    import Footer from '~/layouts/Footer'

    export default {
        components: {
            Footer
        }
    }
</script>

<style>

  * {
    margin: 0;
    padding: 0;
    font-family: "JetBrainsMono-Regular", serif;
  }
  html {
    background-color: #37474F;
    color: #B0BEC5;
  }

  .main-container {
    min-height: 100%;
    padding-bottom: 50px;
    text-align: center;
  }

</style>

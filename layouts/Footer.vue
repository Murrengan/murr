<template>

  <div class="footer">

    <nuxt-link
      exact
      no-prefetch
      active-class="bottom_icon-active"
      class="bottom_icon"
      to="/">
      <img src="~/static/icons/murrengan.svg" alt="murr_icon"></nuxt-link>

    <nuxt-link
      no-prefetch
      active-class="bottom_icon-active"
      class="bottom_icon"
      to="/about/">
      <img src="~/static/icons/question.svg" alt="question_icon"></nuxt-link>

    <nuxt-link
      no-prefetch
      active-class="bottom_icon-active"
      class="bottom_icon"
      to="/murren/"><img src="~/static/icons/user.svg" alt="user_icon"></nuxt-link>

  </div>
</template>

<style scoped>

  .bottom_icon {
    opacity: 0.8
  }

  .bottom_icon-active {
    opacity: 1;
    filter: drop-shadow(3px 3px 3px rgba(0, 0, 0, 1));

  }

  .footer {
    background-color: #A36FFF;
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 50px;

    display: flex;
    justify-content: space-around;
    align-items: center;
  }
</style>

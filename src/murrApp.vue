<template>
    <div id="murr_app">
        <div class="container">

            <router-link to="/login">
                    <span
                            class="button"
                            v-on:click="murr_btn_clicked = false">
                        Войти</span>
            </router-link>

            <router-link to="/sign_up">
                    <span
                            class="button"
                            v-on:click="murr_btn_clicked = false">
                        Зарегистрироваться</span>
            </router-link>
        </div>


        <transition name="murr_fade">

            <div v-if="murr_btn_clicked">

                <div class="pop_up_container">
                    <router-link to="/news">
                        <span class="button"
                              v-on:click="click_murr_btn">
                            Новости</span>
                    </router-link>

                    <router-link to="/about">
                        <span
                                class="button"
                                v-on:click="click_murr_btn">
                            О мурренган</span>
                    </router-link>

                    <router-link to="/team">
                        <span
                                class="button"
                                v-on:click="click_murr_btn">
                            Команда</span>
                    </router-link>

                    <router-link to="/stack">
                        <span
                                class="button"
                                v-on:click="click_murr_btn">
                            Стек</span>
                    </router-link>

                    <div class="bottom">
                        <router-link to="/private">
                        <span
                                class="button"
                                v-on:click="click_murr_btn">
                            Личное</span>
                        </router-link>
                    </div>
                </div>
            </div>
        </transition>

        <div class="murr_menu">

            <div class="murr_button_tooltip">This is menu btn --></div>

            <a class="murr_button"
               v-on:click="click_murr_btn">
                murr
            </a>

        </div>


        <router-view/>


    </div>
</template>

<script>
    export default {

        data() {
            return {
                murr_btn_clicked: false,
            }
        },

        methods: {
            click_murr_btn() {
                return this.murr_btn_clicked = !this.murr_btn_clicked;
            }
        }
    }
</script>

<style>

    .pop_up_container {
        border: #00c6ff solid 5px;
        background-color: rgba(0, 0, 0, .3);
        border-radius: 5px;
        z-index: 1;
        padding: 10px;
        position: absolute;
        top: 50%;
        left: 50%;
        margin-right: -50%;
        transform: translate(-50%, -50%);
        width: 80%;
        height: 50%;
        text-align: center;

        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: 1fr 1fr 1fr;
        grid-template-areas: ". ." ". ." "bottom bottom";
        align-items: center;
    }

    .bottom {
        grid-area: bottom;
    }

    .murr_fade-enter-active, .murr_fade-leave-active {
        transition: opacity 0.2s;
    }

    .murr_fade-enter, .murr_fade-leave-to {
        opacity: 0;
    }

    body {
        background-color: #663399;
        color: #ffc0cb;
        font-size: 18px;
    }


    h1 {
        text-align: center;
        color: #7dffd9;
        margin: 0;
    }

    h2 {
        text-align: center;
        color: #ff0a36;
        margin: 0;
    }

    h3 {
        text-align: center;
        color: #ffc400;
    }

    .container {
        display: flex;
        max-width: 1140px;
        margin: 1.1rem auto;
        padding: 0 50px;
        justify-content: space-around
    }


    .button {
        display: inline-block;
        padding: 10px;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        outline: none;
        color: #fff;
        background-color: #4CAF50;
        border: none;
        border-radius: 5px;
        box-shadow: 0 5px #999;
        margin-right: 0.2rem;
    }

    .button:hover {
        background-color: #3e8e41
    }

    .button:active {
        background-color: #3e8e41;
        box-shadow: 0 0 #666;
        transform: translateY(4px);
    }


    .murr_button {
        background-color: #0072ff;
        border-radius: 5px;
        padding: 10px;
        position: relative;
        color: aliceblue;
        box-shadow: 0 5px #666;
        outline: 0 !important;
        cursor: pointer;
    }

    .murr_button:hover {
        background-color: #8ae8e6;
    }

    .murr_button:active {
        background-color: #00c6ff;
        transform: translateY(4px);
        box-shadow: 0 0 #666;
    }

    .murr_button_tooltip {
        margin-right: 10px;
        font-size: 1.5rem;
    }

    .murr_menu {
        z-index: 1;
        position: fixed;
        bottom: 10%;
        right: 10%;
        display: flex;
        align-items: center
    }

    .border {
        border: #999999;
        background-color: #9e69a3;
        max-width: 768px;
        margin: 0 auto;
        border-radius: 5px;
        padding: 10px;;
    }

    input {
        width: 300px;
        height: 50px;
        padding: 5px;
        margin-bottom: 5px;
        border-radius: 5px;
        font-size: 1.5rem;
    }

    .form {
        text-align: center;
    }

    button {
        width: 100px;
        height: 50px;
        border-radius: 5px;
    }

</style>

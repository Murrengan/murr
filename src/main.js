import Vue from 'vue'
import App from './MurrApp.vue'
import router from "./plugins/router";

Vue.config.productionTip = false;

new Vue({
    router,
    render: h => h(App),
}).$mount('#murr_app');

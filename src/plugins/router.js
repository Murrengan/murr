import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/sign_up',
            component: () => import('../views/account/SignUp.vue')
        },
        {
            path: '/login',
            component: () => import('../views/account/Login.vue')
        },


        {
            path: '/news',
            component: () => import('../views/popups/murr_button/News.vue')
        },
        {
            path: '/about',
            component: () => import('../views/popups/murr_button/About.vue')
        },
        {
            path: '/stack',
            component: () => import('../views/popups/murr_button/Stack.vue')
        },
        {
            path: '/team',
            component: () => import('../views/popups/murr_button/Team.vue')
        },
        {
            path: '/private',
            component: () => import('../views/popups/murr_button/Private.vue')
        },
    ]
})

import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store'

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [

        {
            path: '/sign_up',
            component: () => import('../components/account/SignUp.vue')
        },

        {
            path: '/login',
            name: 'login',
            component: () => import('../components/account/Login.vue')
        },

        {
            path: '/check_email',
            name: 'check_email',
            component: () => import('../components/account/CheckEmail.vue')
        },

        {
            path: '/murren_email_activate',
            component: () => import('../components/account/EmailConfirm.vue')
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
            name: 'team',
            component: () => import('../views/popups/murr_button/Team.vue')
        },

        {

            path: '/private',
            component: () => import('../views/popups/murr_button/Private.vue'),

            beforeEnter: (to, from, next) => {

                if (!store.getters['auth/isAuthenticatedGetter']){

                    return next({
                        name: 'login'
                    })
                }

                next()
            }
        },
    ]
})

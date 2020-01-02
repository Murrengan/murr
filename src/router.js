import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/private',
            component: () => import('./views/button_group/Private.vue')
        },
        {
            path: '/sign_up',
            component: () => import('./views/signUp.vue')
        },
        {
            path: '/login',
            component: () => import('./views/Login.vue')
        },
        {
            path: '/news',
            component: () => import('./views/button_group/News.vue')
        },
        {
            path: '/about',
            component: () => import('./views/button_group/About.vue')
        },
        {
            path: '/stack',
            component: () => import('./views/button_group/Stack.vue')
        },
        {
            path: '/team',
            component: () => import('./views/button_group/Team.vue')
        }
    ]
})

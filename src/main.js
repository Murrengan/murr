import Vue from 'vue';
import App from './MurrApp.vue';
import store from './store/index';
import router from './plugins/router';
import axios from 'axios';


axios.defaults.baseURL = 'http://127.0.0.1:8000';
Vue.config.productionTip = false;

axios.interceptors.request.use(config => {

        const accessToken = localStorage.getItem('accessToken');

        if (accessToken) {

            config.headers['Authorization'] = 'Bearer ' + accessToken;
        }

        return config;
    },

    error => {

        return Promise.reject(error);
    });


axios.interceptors.response.use((response) => {

    return response

}, function (error) {

    const originalRequest = error.config;

    if ((error.response.status === 401 || error.response.status === 400)
        &&
        originalRequest.url.includes('/murren/token_refresh/')) {

        router.push('/login');

        return Promise.reject(error);
    }

    if (error.response.status === 401
        &&
        !originalRequest._retry) {

        originalRequest._retry = true;

        const refreshToken = localStorage.getItem('refreshToken');

        const dataForPost = {refresh: refreshToken};

        return axios.post('murren/token_refresh/', dataForPost)

            .then(response => {

                if (response.status === 200) {

                    localStorage.setItem('refreshToken', response.data.refresh);
                    localStorage.setItem('accessToken', response.data.access);

                    axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('accessToken');

                    return axios(originalRequest);
                }
            })
    }

    return Promise.reject(error);

});


store.dispatch('auth/setToken', {

    access: localStorage.getItem('accessToken'),
    refresh: localStorage.getItem('refreshToken')
})
    .then(() => {
            new Vue({
                store,
                router,
                render: h => h(App),
            }).$mount('#murr_app');
        }
    );

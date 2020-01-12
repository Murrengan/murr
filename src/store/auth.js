export default {

    namespaced: true,

    state: {

        accessToken: null,
        refreshToken: null,
        murrenName: null,

        isAuthenticated: false
    },

    getters: {


        isAuthenticatedGetter(state) {

            return state.isAuthenticated
        }
    },

    mutations: {

        SET_TOKEN(state, token) {

            state.accessToken = token.access;
            state.refreshToken = token.refresh;
        },

        AUTHENTICATE(state) {

            state.isAuthenticated = true;
        },

        LOGOUT_MURREN(state) {

            state.accessToken = null;
            state.refreshToken = null;

            state.isAuthenticated = false;
        },
    },

    actions: {

        async murrenLogout({commit}) {

            commit('LOGOUT_MURREN');
        },


        async set_token({commit}, token) {

            if (token) {
                commit('SET_TOKEN', token);
            }
        }
    }
}

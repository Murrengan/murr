Vue.component('come_to_tawern_btn', {
    // template: '<button v-on:click="comeToTawern" class="btn bg-secondary">Войти в таверну</button>',
    template: '' +
        '<div>' +
        '<h3>{{ count }}</h3>' +
        '<h3>{{ text }}</h3>' +
        // '<button v-on:click="count++">Увеличить размер текста</button>' +
        '<button v-on:click="comeToTawern">Войти в таверну</button>' +
        '</div>',

    data() {
        return {
            text: 'Как дела?',
            count: 0
        }
    },

    methods: {

        comeToTawern() {
            let ws = new WebSocket('ws://127.0.0.1:8000/ws/chat/');

            ws.onopen = (data) => {
                $('.monitor').html('<iframe src="http://127.0.0.1:8000/dashboard/"  class="container border pt-3 pb-3" onload="resizeIframe(this)" scrolling="no" frameBorder="0"></iframe>\n');

                console.log("Добро пожаловать в таверну!");
            };

            ws.onmessage = (data) => {

                // console.log(event);
                let obj = JSON.parse(data.data);
                this.text = obj.data;
                // if (data.event === 'add.participiant') {
                //     my_handler_which_update_user_list(data.data);
                // }
            };
        }
    },
});

new Vue({
    el: '#ws_tawern'
});



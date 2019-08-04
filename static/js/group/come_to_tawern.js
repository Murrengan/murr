new Vue({
    el: '#come_to_tawern',
    delimiters: ['[[', ']]'],
    data: {
        name: 'Murr'
    },
    methods: {
        come_to_tawern() {
            let ws = new WebSocket('ws://127.0.0.1:8000/ws/chat/');
            ws.onopen = () => {
                console.log("Добро пожаловать в таверну!");
            };

            ws.onmessage = (data) => {

                console.log(data);
                let content = JSON.parse(data.data);
                console.log(content);
                // this.text = obj.data;
                // if (data.event === 'add.participiant') {
                //     my_handler_which_update_user_list(data.data);
                // }
            };
        }

    }
});

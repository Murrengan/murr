new Vue({
    el: '#come_to_tawern',
    delimiters: ['[[', ']]'],
    data: {
        name: 'Murr'
    },
    methods: {
        come_to_tawern() {
            let ws = new WebSocket('ws://127.0.0.1:8000/ws/chat/12414/');
            ws.onopen = () => {
                console.log("Добро пожаловать в таверну!");
                // $('.connection').html('<b>Ты в онлайне, красавчик =)</b>');
                $('.monitor').html('<iframe src="http://127.0.0.1:8000/dashboard/"' +
                                                ' class="container pt-3 pb-3 "' +
                                                ' onload="resizeIframe(this)"' +
                                                // ' scrolling="no"' +
                                                ' frameBorder="0"' +
                    '></iframe>\n');
                console.log("Соединение установлено.");
            };

            ws.onmessage = (data) => {

                console.log(data);
                // let content = JSON.parse(data.data);
                // console.log(content);
                // // this.text = obj.data;
                // if (content.event === 'group.create') {
                //     console.log('Ура!');
                //     // my_handler_which_update_user_list(data.data);
                // }
            };
        }

    }
});

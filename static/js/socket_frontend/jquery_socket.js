let socket = null;

function socket_init(url) {
    socket = new WebSocket(url);
}

function on_connect() {
    console.log("Connect");
    // let url = $('#url').val();
    let url = 'ws://127.0.0.1:8000/ws/chat/';

    // if (url === "") {
    //     url = 'ws://127.0.0.1:8000/ws/chat/';
    // }
    socket_init(url);

    socket.onopen = function () {
        $('.connection').html('<b>Ты в онлайне, красавчик =)</b>');
        $('.monitor').html('<iframe src="http://127.0.0.1:8000/dashboard/"  class="container border pt-3 pb-3" onload="resizeIframe(this)" scrolling="no" frameBorder="0"></iframe>\n');
        console.log("Соединение установлено.");
    };

    socket.onclose = function (event) {
        $('.connection').html('<b>Возвращайся скорее...</b>');
        $('.monitor').empty();
        if (event.wasClean) {
            console.log('Соединение закрыто чисто');
        } else {
            console.log('Обрыв соединения'); // например, "убит" процесс сервера
        }
        console.log('Код: ' + event.code + ' причина: ' + event.reason);
    };

    socket.onmessage = function (event) {
        data = JSON.parse(event.data);
        console.log("Получены данные " + event.data);
        console.log(data.event);

        if (data.event === 'group.create') {
            console.log('Murrengan');
            group.message = 'Murrengan';
        }

        $('.messages').append(event.data);
        $('.messages').append("<br>");
    };
}

// Парсим строку из ввода - выполняем метод event

function on_send() {
    let message = $("#message").val();
    socket.send(message);
}

function on_disconnect() {
    $('.monitor').empty();
    socket.close();
}

function clean_div() {
    $('.messages').empty();
}

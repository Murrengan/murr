new Vue({
    el: '#app',
    // vuetify: new Vuetify(),
    data: {

        murren_id: '',
        murren_avatar: '',

        base_card_img_url: '',
        base_card_text: '',
        show_btn: [],

        virgil_tell: false,


    },
    methods: {
        async come_to_tawern() {
            await axios
                .get('/murr_api/come_to_tawern/')
                .then(django_answer => {
                    this.base_card_img_url = django_answer.data.base_card_img_url;
                    this.base_card_text = django_answer.data.base_card_text;
                    this.show_btn = django_answer.data.show_btn;
                })
                .catch(error => console.log(error));
            console.log('отработал come_to_tawern/');
        },

        look_at_hell_gate() {
            axios
                .get('/murr_api/look_at_hell_gate/')
                .then(django_answer => {
                    this.base_card_img_url = django_answer.data.base_card_img_url;
                    this.base_card_text = django_answer.data.base_card_text;
                    this.show_btn = django_answer.data.show_btn;
                })
                .catch(error => console.log(error));
            console.log('отработал look_at_hell_gate/');
        },
        barmen() {
            axios
                .get('/murr_api/barmen/')
                .then(django_answer => {
                    this.base_card_img_url = django_answer.data.base_card_img_url;
                    this.base_card_text = django_answer.data.base_card_text;
                    this.show_btn = django_answer.data.show_btn;
                })
                .catch(error => console.log(error));
            console.log('отработал barmen/');
        },
        async barmen_quest_accept() {
            await axios
                .get('/murr_api/barmen_quest_accept/')
                .then(django_answer => {
                    this.base_card_img_url = django_answer.data.base_card_img_url;
                    this.base_card_text = django_answer.data.base_card_text;
                    this.show_btn = django_answer.data.show_btn;
                })
                .catch(error => console.log(error));
            console.log('отработал barmen_quest_accept/');
        },

        async come_to_basement(){
            await axios
                .get('/murr_api/come_to_basement/')
                .then(django_answer => {
                    this.base_card_img_url = django_answer.data.base_card_img_url;
                    this.base_card_text = django_answer.data.base_card_text;
                    this.show_btn = django_answer.data.show_btn;
                })
                .catch(error => console.log(error));
            console.log('отработал come_to_basement/');
        },

        v_on_click_handler(method_name) {
            this[method_name]()
        }
    },
    created() {
        axios.get('/murr_api/start/')
            .then((django_answer) => {
                // this.murren_id = django_answer.data;
                this.murren_id = django_answer.data.murren_id;
                this.base_card_text = django_answer.data.base_card_text;
                this.show_btn = django_answer.data.show_btn;

                this.murren_avatar = django_answer.data.murren_avatar;
            })
            .catch(error => console.log(error));
        console.log('отработал murr_api/start/');

    }
});

//
//         _ws: 'murr/static/img/murr_game/Tawern.png',
//
//         // switchers
//         show_tawern: false,
//         show_create_group: false,
//         show_murren_group: false,
//         show_group_members: false,
//         show_Barmen_dialog: false,
//         show_Veronika_dialog: false,
//         show_OrkVeteran_dialog: false,
//         show_quests_panel: true,
//         success_group_created: false,
//
//         scroll_btn: false,
//         bag_icon_url: '/static/img/murr_game/icon/bag.jpg',
//         skill_icon_url: '/static/img/murr_game/icon/skill.jpg',
//         murr_game_Tawern: 'http://127.0.0.1:8000/static/img/murr_game/Tawern.png',
//
//
//         // data sets
//         logs: [{type: 'action', text: 'Действие: Ты вошел в murr'},
//             {type: 'action', text: 'Действие: включен логер'}],
//         murren_in_tawern_list: [],
//         data_from_django: '',
//         available_group: false,
//         group_name_input: '',
//         murr: 'murr',
//         murren_message_input: '',
//         murren_name: '',
//         avatar_url: '',
//         hp: '',
//         mp: '',
//         user_id: ''


//         get_data_from_client_and_come_to_tawern() {
//             axios
//                 .get('http://127.0.0.1:8000/murr_game/api/return_character_info/')
//                 .then(django_answer => {
//                     this.avatar_url = django_answer.data.avatar_url;
//                     this.murren_name = django_answer.data.character.name;
//                     this.hp = django_answer.data.character.stats.hp;
//                     this.mp = django_answer.data.character.stats.mp;
//                     this.user_id = django_answer.data.user_id;
//                     this.come_to_tawern();
//                     console.log('axios отработал')
//                 })
//                 .catch(error => console.log(error));
//         },
//         come_to_tawern() {
//
//             // подключаемся к сокету tawern
//             let group_id = '1';
//             let ws = new WebSocket('ws://127.0.0.1:8000/ws/chat/' + group_id + '/');
//             this._ws = ws;
//             ws.onopen = () => {
//                 console.log("Соединение с сокетом установлено.");
//                 let command = '{"event": "add.chat.member", "data": {"user_id": "' +
//                     this.user_id +
//                     '"}}';
//                 ws.send(command);
//                 this.show_tawern = true;
//                 console.log("Добро пожаловать в таверну!");
//             };
//             ws.onmessage = (data) => {
//                 let data_from_django = JSON.parse(data.data);
//                 // Отлавливаем ответ с бекенда
//                 if (data_from_django.event === "send.message") {
//                     let new_message = data_from_django.data.message.toString();
//                     this.logs.push({type: 'message', text: new_message});
//                     this.show_btn_scroll();
//                     this.$nextTick(() => {
//                         if (this.scroll_btn === false) {
//                             this.scroll_to_new();
//                         }
//                     });
//                 }
//                 if (data_from_django.event === "murren.in.tawern.list") {
//                     console.log(data_from_django);
//                     this.murren_in_tawern_list = data_from_django.data
//
//                 }
//                 if (data_from_django.event === "leave.group") {
//                     this.logs.push({type: 'action', text: 'Вы вышли из группы'});
//                     this.show_btn_scroll();
//                     this.$nextTick(() => {
//                         if (this.scroll_btn === false) {
//                             this.scroll_to_new();
//                         }
//                     });
//                     this.show_murren_group = false;
//                 }
//             };
//             ws.onclose = () => {
//
//                 console.log('Сокет таверны закрыт');
//
//             };
//             this.show_murren_group = true;
//         },
//         send_message() {
//             let message = '{"event": "send.message", "data": {"message": "' +
//                 this.murren_message_input +
//                 '"}}';
//             this._ws.send(message);
//             this.murren_message_input = '';
//         },
//         event_leave_group() {
//
//             let command = '{"event": "leave.group", "data": {}}';
//
//             this._ws.send(command);
//             console.log('На бекенд отправлена задача' + command);
//
//             this._ws.close();
//             console.log('Активный сокет закрыт');
//
//             this.show_tawern = false;
//             console.log('Вы вышли из таверны. Ждем вас снова! =)');
//
//         },
//         show_murren_in_tawern() {
//             let command = '{"event": "murren.in.tawern.list", "data": {}}';
//             this._ws.send(command);
//
//
//             console.log('На бекенд отправлена задача' + command);
//         },
//         shakeBtn() {
//             const img = document.getElementById('onChake');
//             img.classList.add('anim-chake');
//             setTimeout(function () {
//                 img.classList.remove('anim-chake');
//             }, 250)
//         },
//         create_group_by_name() {
//
//             const ws = new WebSocket('ws://127.0.0.1:8000/ws/chat/');
//
//             let create_group_json = '{"event": "group.create", "data": {"name": "' +
//                 this.group_name_input +
//                 '"}}';
//
//             ws.onopen = function () {
//                 console.log("На бекенд отправлена задача: " + create_group_json);
//                 ws.send(create_group_json);
//             };
//
//             ws.onmessage = (data) => {
//                 console.log("С бекенда пришел ответ:");
//                 console.log(JSON.parse(data.data));
//             };
//             this.show_create_group = false;
//         },
//         scroll_to_new() {
//             let container = this.$el.querySelector(".messages");
//             let container_messages = this.$el.querySelector(".messages-content");
//             let messages = container_messages.querySelectorAll(".message");
//             container.scrollTop = messages[messages.length - 1].scrollHeight + container.scrollHeight;
//         },
//         show_btn_scroll() {
//             let container = this.$el.querySelector(".messages");
//             if (container.scrollHeight - container.offsetHeight !== 0) {
//                 const elemScroll = document.querySelector(".messages");
//                 elemScroll.addEventListener('scroll', (e) => {
//                     if (container.scrollTop + container.clientHeight >= container.scrollHeight - 40) {
//                         this.scroll_btn = false;
//                     } else {
//                         this.scroll_btn = true;
//                     }
//                 });
//             }
//         },
//         show_create_group_panel() {
//             this.show_create_group = (this.show_create_group === false);
//             console.log('Открылась панель на ввод имени группы');
//         },
//         show_available_group() {
//             const ws = new WebSocket('ws://127.0.0.1:8000/ws/chat/');
//             let show_group_list = '{"event": "group.list", "data": {}}';
//             ws.onopen = function () {
//                 ws.send(show_group_list);
//                 console.log("На бекенд отправлена задача: " + show_group_list);
//             };
//             ws.onmessage = (data) => {
//                 this.data_from_django = (JSON.parse(data.data));
//                 this.available_group = [];
//                 for (let i of this.data_from_django.data) {
//                     this.available_group.push(i);
//                 }
//                 console.log(this.available_group)
//             };
//         },
//         remove_chat_member(group_id) {
//             let group_url = 'ws://127.0.0.1:8000/ws/chat/' + group_id + '/';
//             let remove_event_json = '{"event": "remove.chat.member", "data": {}}';
//             let ws = new WebSocket(group_url);
//             ws.onopen = function () {
//                 ws.send(remove_event_json);
//                 console.log("На бекенд отправлена задача: " + remove_event_json);
//             };
//             ws.onmessage = (data) => {
//                 this.data_from_django = (JSON.parse(data.data));
//                 this.available_group.splice(this.available_group.findIndex(obj => obj.id === group_id), 1);
//             };
//             ws.onclose = () => {
//                 console.log('ws close');
//             }
//         },
//         begin_quest_barmen() {
//
//             this.show_Barmen_dialog = !this.show_Barmen_dialog;
//             this.show_quests_panel = !this.show_quests_panel;
//             this.murr_game_Tawern = 'http://127.0.0.1:8000/static/img/murr_game/Tawern_Barman.png';
//             console.log('Вы начали квест Бармена')
//
//
//         },
//
//         battle_begin() {
//             this.show_Barmen_dialog = !this.show_Barmen_dialog;
//             this.show_quests_panel = !this.show_quests_panel;
//             this.murr_game_Tawern = 'http://127.0.0.1:8000/static/img/murr_game/rat.jpg';
//         }
//
//     },
//     computed: {
//         show_create_group_menu() {
//             return this.show_create_group
//         },
//         get_user_id() {
//             return this.user_id
//         },
//     }
// });
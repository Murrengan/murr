let group = new Vue({
    el: "#group",
    data: {
        // header: 'Группа',
        // nameGroup: "<i>Dzitha</i>",
        // member: {
        //     id: 2,
        //     name: "Bill ",
        //     stat: {
        //         hp: 80,
        //         hp_link: '/static/img/murr_game/hp.svg',
        //         mp: 60,
        //         mp_link: '/static/img/murr_logo.svg',
        //     },
        //     img: '/static/img/murr_game/Magic.jpg'
        // },
        groupMembers: [],
        maxGroupMembers: 3,
        character: '',
        avatar: ''
    },
    methods: {
        addToGroup: function () {
            this.groupMembers.push(this.member.id)
        }
    },
    computed: {
        groupMemberCount: function () {
            return this.groupMembers.length || '';
        },
        canAddGroupMember: function () {
            return this.maxGroupMembers > this.groupMemberCount;
        }
    },
    mounted() {
            axios
                .get('/murr_game/api/return_character_info/')
                .then(response => {
                    // this.character = response.data;
                    this.avatar = response.data.avatar_url;
                    // this.character = response.data.character;
                    // this.opponent = response.data.opponent;
                });
            // axios
            //     .get('/murr_game/api/get_img/')
            //     .then(response => {
            //         this.character.img = response
            //     })
        }

});

// let engine = new Vue({
//         el: '#monitor',
//         data: {
//             // characters: '',
//             character: '',
//             opponent: '',
//
//         },
//         mounted() {
//             axios
//                 .get('/murr_game/api/return_members/')
//                 .then(response => {
//                     // this.characters = response.data;
//                     this.character = response.data.character;
//                     this.opponent = response.data.opponent;
//                 });
//             axios
//                 .get('/murr_game/api/get_img/')
//                 .then(response => {
//                     this.character.img = response
//                 })
//         }
// });

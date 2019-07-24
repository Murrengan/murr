let group = new Vue({
    el: "#group",
    data: {
        member: {
            id: '',
            name: 'asdf',
            groupMembers: [],
            maxGroupMembers: 3
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
                    this.characters = response.data;
                    this.member.name = response.data.name;
                });
            // axios
            //     .get('/murr_game/api/get_img/')
            //     .then(response => {
            //         this.character.img = response
            //     })
        }

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

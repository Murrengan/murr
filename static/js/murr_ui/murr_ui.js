let group = new Vue({
    delimiters: ['[[', ']]'],
    el: "#group",
    data: {
        murren: {
            id: 2,
            name: '',
            avatarUrl: ''
        },
        showGroup: true,
        groupName: '',
        groupMembers: [],
        maxGroupMembers: 3,
        private: false,
        yes: 1,
        no: 2,
        result: '',
        group_member: false,
        items: {
            'adrenalin': 1,
            'gold': 150
        }
    },
    methods: {
        addToGroup: function () {
            this.groupMembers.push(this.murren.id)
        },
        showGroupUi: function () {
            this.showGroup = (this.showGroup !== false) ? false : true;
        },
        submitForm() {
            alert('Submitted');
        },
        addGroup() {
            this.group_member = (this.group_member !== false) ? false : true;
            console.log('Все ок');
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
                this.murren.avatarUrl = response.data.avatar_url;
                this.murren.id = response.data.character.id;
                this.murren.name = response.data.character.name;
                // this.opponent = response.data.opponent;
            });
        // axios
        //     .get('/murr_game/api/get_img/')
        //     .then(response => {
        //         this.character.img = response
        //     })
    }

});

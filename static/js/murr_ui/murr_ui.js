let group = new Vue({
    el: "#group",
    data: {
        header: 'Группа',
        nameGroup: "<i>Dzitha</i>",
        member: {
            id: 2,
            name: "Bill ",
            stat: {
                hp: 80,
                hp_link: '/static/img/murr_game/hp.svg',
                mp: 60,
                mp_link: '/static/img/murr_logo.svg',
            },
            img: '/static/img/murr_game/Mage.jpg'
        },
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
    }

});
let engine = new Vue({
    el: '#monitor',
    data: {
            characters: '',
            character: '',
            opponent: '',

    },
    mounted() {
        axios
            .get('/murr_game/api/return_members/')
            .then(response => (this.characters = response.data));
            response => (this.character = response.data.character.name));
            .then(response => (this.opponent = response.data.opponent.name));
    }


// search: '',
// sitename: 'Murrengan Rulls',
// product: {
//     id: 1001,
//     price: 20,
//     title: 'murr title',
//     description: 'some <b>large</b> string',
//     cover: '/Users/egorkomarov/Documents/img/blue.png',
//     availableInventory: 5
// },
// cart: [],
// },
// methods: {
//     addToCart: function () {
//         this.cart.push(this.product.id)
//     }
// },
// computed: {
//     cartItemCount: function () {
//         return this.cart.length || 0;
//     },
//     canAddToCart: function () {
//         return this.product.availableInventory > this.cartItemCount;
//     }
// }
})
;

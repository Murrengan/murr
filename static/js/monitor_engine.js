let engine = new Vue({
    el: '#monitor',
    data: {
            // search: '',
            // heals: 123,
            characters: ''
    },
    mounted() {
        axios
            .get('http://127.0.0.1:8000/murr_game/api/return_members/')
            .then(response => (this.characters = response.data));
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

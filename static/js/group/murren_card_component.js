Vue.component('murren_card', {
    template: '' +
        '' +
        '<div class="card">' +
        '<img src="/static/img/pink_girl.png" class="img-fluid img-thumbnail" alt="...">' +
        '<div class="card-body text-center m-0 p-0">\n' +
        '<h5 class="card-title">{{ murren_name }}</h5>' +
        '</div>' +
        '</div>',
    data(){
        return{
            murren_name: 'Greg',
        }
    }
});


new Vue({
    el: '#murren_card'
});

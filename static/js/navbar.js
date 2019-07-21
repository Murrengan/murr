$(document).ready(function() {
  var wn = $(window);
  var formSearch = $('#searchForm');
  var searchInput = $('searchInput');

  wn.on('click.Bst', function(event) {
    if ( 
      formSearch.has(event.target).length == 0
      &&
      !formSearch.is(event.target)
    ) {
      formSearch.removeClass('form-search__focus').addClass('formSearch');
      searchInput.removeClass('search-input__focus').addClass('search-input');
    } else {
      formSearch.removeClass('formSearch').addClass('form-search__focus');
      searchInput.removeClass('search-input').addClass('search-input__focus');
    }
  })
});

let engine = new Vue({
        el: '#navbar',
        data: {
            username: '',

        },
        mounted() {
            axios

                .get('/murr_game/api/return_members/')

                .then(response => {
                    this.username = response;
                })
        }
    })
;

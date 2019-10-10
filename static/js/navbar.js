$(document).ready(function() {
  var wn = $(window);
  var formSearch = $('#searchForm');
  var searchInput = $('searchInput');
  var menublock = $('.menu-block');
  var contentblock = $('.content-block');
  var burger = $('#burger');
  var search = $('#search');

  burger.on('click', function(event) {
    if (burger.hasClass('show')) {
      menublock.removeClass('show-side-nav');
      contentblock.removeClass('show-side-body');
      burger.removeClass('show');
      $('body').css('overflow-x', 'auto');
    }else{
      menublock.addClass('show-side-nav');
      contentblock.addClass('show-side-body');
      burger.addClass('show');
      $('body').css('overflow-x', 'hidden');
    }
    
  });

  search.on('click', function(event) {
    if (search.hasClass('show')) {
      $('#searchForm').css('display', 'none');
      $('.navbar-brand').css('display', 'block');
      search.removeClass('show');
    }else{
      $('#searchForm').css('display', 'flex');
      $('.navbar-brand').css('display', 'none');
      search.addClass('show');
    }
    
  });

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

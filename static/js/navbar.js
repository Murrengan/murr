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
  
  $('#myModal').on('show.bs.modal', function (e) {
	  $.ajax({
		  url: 'https://api.ufs-online.ru/api/v1/aviator/airport/autocomplete?q=vj',
		  dataType: 'json',
		  success: function(data) {
			var result = "";
			data.forEach(function(item, i, arr) {
				result += "<p style='color: black'>" + item.cityName + "</p>";
			});
			$('#murreyContent').html(result);
		  }
	  });

	})
});

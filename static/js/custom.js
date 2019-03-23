// Добавляем плавную прокрутку к элементу
$('.nav-link, .navbar-brand').click(function() {
  $('.navbar-collapse').collapse('toggle'); // При нажатии на ссылку, меню сворачивается
  var sectionTo = $(this).attr('href');
  $('html, body').animate({
    scrollTop: $(sectionTo).offset().top -56 // Отступ от блока (Обычно задается высота nav-bar)
  }, 1000); // Время прокрутки до элемента в секундах
});
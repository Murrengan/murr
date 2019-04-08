// Добавляем плавную прокрутку к элементу
$('.nav-link, .navbar-brand').click(function() {
  $('.navbar-collapse').collapse('toggle'); // При нажатии на ссылку, меню сворачивается
  var sectionTo = $(this).attr('href');
  $('html, body').animate({
    scrollTop: $(sectionTo).offset().top -56 // Отступ от блока (Обычно задается высота nav-bar)
  }, 1000); // Время прокрутки до элемента в секундах
});


// Для работы с ajax
//
// <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
// Установка csrf_token
// (function () {
//     let csrftoken = Cookies.get('csrftoken');
//     $.ajaxSetup({
//         headers: {"X-CSRFToken": csrftoken}
//     });
// })();
//
//
// // Поставить лайк
// let comment_for_murr = function (id) {
//     $.ajax({
//         url: "murrs/murr_detail/" + id + "/",
//         type: "POST",
//         // type: "GET",
//         data: $("form[name='comment_form']").serialize(),
//
//
//         success: (response) => {
//             window.location = response
//         },
//         error: (response) => {
//             console.log("False")
//         }
//     })
// };
//
//   $("form[name='comment_form']").submit(function (e) {
//
//         e.preventDefault();
//
//         let data = $(this).serialize();
//
//         $.ajax({
//             url: $(this).attr('action'),
//             type: "POST",
//
//             data,
//
//             success: (response) => {
//                 alert('Комментарий отправлен! +)')
//             },
//             error: (response) => {
//                 console.log("False")
//             }
//         })
//     });

// Установка csrf_token
(function () {
    let csrftoken = Cookies.get('csrftoken');
    $.ajaxSetup({
        headers: {"X-CSRFToken": csrftoken}
    });
})();

// Добавляем плавную прокрутку к элементу
$('.nav-link, .navbar-brand').click(function() {
  $('.navbar-collapse').collapse('toggle'); // При нажатии на ссылку, меню сворачивается
  var sectionTo = $(this).attr('href');
  $('html, body').animate({
    scrollTop: $(sectionTo).offset().top -56 // Отступ от блока (Обычно задается высота nav-bar)
  }, 1000); // Время прокрутки до элемента в секундах
});


// Показать форму комментария
let openForm = function (id) {
    $(`#${id}`).show()
};
// Скрыить форму комментария
let closeForm = function (id) {
    $(`#${id}`).hide()
};
// Поставить лайк
let like = function (id) {
    $.ajax({
        url: "http://127.0.0.1:8000/like/",
        type: "POST",
        data: {
            pk: id,
        },
        success: (response) => {
            window.location = response
        },
        (response) =;> {
            console.log("False")
        }
    })
};
// Подписаться
let follow = function (id) {
    $.ajax({
        url: "http://127.0.0.1:8000/profile/follow/",
        type: "POST",
        data: {
            pk: id,
        },
        success: (response) => {
            window.location = response
        },
        (response) =;> {
            console.log("False")
        }
    })
};
// обработать форму авторизации с помощью ajax request.
$(".need_auth").submit(function (e) {
    e.preventDefault();
    var url = $(this).attr('action');
    var data = $(this).serialize();
    $.post(
        url,
        data,
        function (response) {
            window.location = response.location;
        },
    );
});


$(".edt-comment").on('click', function () {
    // console.log('reply');
    msg = ($(this).parents("div.media-body").find('p').html());
    if ( $('#id_content').val() ) {
      $('#id_content').val("");
    }
    $('#id_content').val(msg);
    $('#id_content').focus();

    console.log(msg);
    return false;});

$('.del-comment').on('click', function () {
    BootstrapDialog.alert('I want banana!');
    return false;
});


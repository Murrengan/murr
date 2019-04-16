// Установка csrf_token
(function () {
    let csrftoken = Cookies.get('csrftoken');
    $.ajaxSetup({
        headers: {"X-CSRFToken": csrftoken}
    });
})();

// Добавляем плавную прокрутку к элементу
$('.nav-link, .navbar-brand').click(function () {
    $('.navbar-collapse').collapse('toggle'); // При нажатии на ссылку, меню сворачивается
    var sectionTo = $(this).attr('href');
    $('html, body').animate({
        scrollTop: $(sectionTo).offset().top - 56 // Отступ от блока (Обычно задается высота nav-bar)
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
    error: (response)=> {
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
    errorr: (response)=>{
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
    msg = $(this).parents("div.media-body").find('p').html();
    if ($('#id_content').val()) {
        $('#id_content').val("");
    }
    $('#id_content').val(msg);
    $('#id_content').focus();

    console.log(msg, $(this).parent('.comment-control.small').data('id'));
    return false;
});

$('.del-comment').on('click', function () {
    id = $(this).parent('.comment-control.small').data('id');
    var commentRow = $(this).parent('.media.m-2');
    console.log('will be delete comment id -' + id);
    BootstrapDialog.show({
        title: 'Подтвердите действие',
        type: 'type-danger',
        message: 'Вы уверены, что хотите удалить этот комментарий?',
        buttons: [{
            label: 'Удалить',
            cssClass: 'btn-primary btn-sm',
            action: function (dialog) {
                $.ajax({
                    type: 'POST',
                    dataType: 'json',
                    url: '/murrs/murr_detail/comment_cut/' + a + '/',
                    data: {id_comment: id},
                    success: function (response) {
                        if (response.success) {
                            //актуализируем кол-во комментариев
                            var commentCount = parseInt($('#commentsCounter').html());
                            $('#commentsCounter').html(commentCount - 1);

                            commentRow.animate({
                                opacity: 1,
                                height: 0,
                                padding: 0
                            }, 'fast', function () {
                                commentRow.remove();
                            });
                        } else {
                            alert('Внимание ' + response.message);
                        }
                    },
                    error: function () {
                        alerrt('Сервер не отвечает. Попробуйте повторить позднее.');
                    }
                });
                dialog.close();
            }
        }, {
            label: 'Отмена',
            cssClass: 'btn-sm',
            action: function (dialog) {
                dialog.close();
            }
        }]
    });
    return false;
});

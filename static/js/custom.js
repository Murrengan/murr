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
        errorr: (response) => {
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
        errorr: (response) => {
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

//dipper
function create_post() {
    console.log("create post is working!"); // sanity check
    let slug = $("form#add-comment-form").prop('action').split('/').pop(); // get slug from URL of form.action property
    $.ajax({
        url: slug, // the endpoint
        type: "POST", // http method
        data: {content: $('#id_content').val()}, // data from textarea sent with the post request

        // handle a successful response
        success: function (response) {
            // $('#post-text').val(''); // remove the value from the input
            tinymce.get('id_content').setContent(''); // remove the value from the editor
            tinymce.get('id_content').save(); // transfer empty val to the textarea input
            console.log(response); // log the returned json to the console
            if (response.success) {
                $(".comment-list").replaceWith(response.comments_list);
                console.log("success"); // another sanity check
                $('html, body').animate({
                    scrollTop: $(".comment").first().offset().top - 56 // Отступ от блока (Обычно задается высота nav-bar)
                    }, 1000);
            }
        },
        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#alerts').html("<div class='alert alert-danger alert-dismissible mt-2' data-alert>Oops! We have encountered an error: " + errmsg +
                "<button type='button' class='close' data-dismiss='alert' aria-label='Close'>&times;</button></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

$('#add-comment-form').on('submit', function (event) {
    event.preventDefault();

    var editorContent = tinyMCE.get('id_content').getContent();
    if (editorContent == '' || editorContent == null) // alerts on comment is epmty
    {
        // Add error message if not already present
        if (!$('#editor-error-message').length)
        {
            $('<div id="editor-error-message" class="alert alert-danger alert-dismissible fade font-weight-bold ' +
              '   invalid-feedback show small">\n' +
              '       Comment content is empty.' +
              '       <button type="button" class="close" data-dismiss="alert" aria-label="Close">\n' +
              '           <span aria-hidden="true">&times;</span>\n' +
              '       </button>\n' +
              '</div>'
            ).insertAfter($(tinyMCE.get('id_content').getContainer()));
        }
        $('#id_content').toggleClass('is-invalid');
        $('#editor-error-message').slideDown();
        return false;
    } else {
        // Hide error message
        if ($('#editor-error-message'))
            $('#editor-error-message').fadeOut();

        console.log("add-comment-form submitted!");  // sanity check
        tinymce.get('id_content').save();
        create_post();
    }
});

// prevent DOM remove alert
    $('#editor-error-message').on('close.bs.alert', function (e) {
        $('#editor-error-message').fadeOut(function () {
            $('#id_content').toggleClass('is-invalid');
        });
        $('#editor-error-message').show();
        e.preventDefault();
    });


$(".container").on('click', ".edt-comment", function () {
    // console.log('reply');
    let commentContent = $('#id_content')
    msg = $(this).parents("div.media-body").find('div.mb-1.comm-content').html();
    if (commentContent.val()) {
        commentContent.val("");
        tinymce.get('id_content').load();
    }
    commentContent.val(msg);
    tinymce.get('id_content').load();
    $(".mce-container").focus();
    tinyMCE.get('id_content').selection.select(tinyMCE.get('id_content').getBody(), true);
    tinyMCE.get('id_content').selection.collapse(false);
    // commentContent.focus();
    tinymce.execCommand('mceFocus',false,'id_content');

    console.log(msg, $(this).parent('.comment-control.small').data('id'));
    return false;
});

$('.container').on('click', ".del-comment", function () {
    var commentRow = '';
    var slug = $("form#add-comment-form").prop('action').split('/').pop();
    id = $(this).parent('.comment-control.small').data('id');
    if ($('.comment-list .media').length > 1) {
        commentRow = $(this).parents('.media');
    } else {
        commentRow = $('.comment-list');
    }
    console.log('will be delete comment id -' + id);
    BootstrapDialog.show({
        title: '<i class="fas fa-exclamation-circle"></i>&nbsp; Подтвердите действие',
        type: 'type-danger',
        cssClass: 'text-danger lead',
        message: 'Вы уверены, что хотите удалить этот комментарий?',
        buttons: [{
            label: 'Удалить',
            cssClass: 'btn-primary btn-sm',
            action: function (dialog) {
                $.ajax({
                    type: 'POST',
                    dataType: 'json',
                    url: slug + '/comment_cut.ajax/' + id + '/',
                    data: {id_comment: id},
                    success: function (response) {
                        console.log('success:');
                        console.log(response);
                        if (response.success) {
                            //актуализируем кол-во комментариев
                            var commentCount = parseInt($('.commentsCounter').html());
                            $('.commentsCounter').html(commentCount - 1);

                            commentRow.animate({
                                opacity: 0,
                                height: 0,
                                padding: 0
                            }, 'slow', function () {
                                commentRow.remove();
                            });
                        } else {
                            alert('Внимание ' + response.message);
                        }
                    },
                    error: function (errorData) {
                        console.log('error:');
                        console.log(errorData);
                        alert('Сервер не отвечает. Попробуйте повторить позднее.');
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
// dipper
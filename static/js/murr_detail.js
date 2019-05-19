;(function($) {
    let $name = 'murrDetail',
        methods = {
            init: function() {
                return this.each(function() {
                    let $this = $(this), data = {
                        csrfmiddlewaretoken: $this.data('csrf'),
                        murr_slug: $this.data('murr_slug')
                    };
                    $this.data($name, data);

                    $this[$name]('bindEvent')
                })
            },
            bindEvent: function() {
                let $this = $(this), data = $this.data($name);

                $('.comment-add', $this).click(function(event) {
                    event.preventDefault();
                    $this[$name]('addComment');
                });

                $('.comment-update', $this).click(function(event) {
                    event.preventDefault();
                    $this[$name]('updateComment');
                });

                $('.comment-list', $this).click(function(event) {

                    if (event.target.classList.contains('del-comment')) {
                        event.preventDefault();
                        $this[$name]('deleteWithConfirm', $(event.target));
                    } else if (event.target.classList.contains('edt-comment')) {
                        event.preventDefault();
                        $this[$name]('editComment', $(event.target));
                    }
                });
            },
            editComment: function($target) {
                let $this = $(this), data = $this.data($name),
                    $comment = $target.closest('.comment'),
                    $comment_input = $('#id_content'),
                    comment_content = $('.comment-content', $comment);

                $comment_input.val(comment_content.html());
                $.extend(data, $comment.data(), {content: $comment_input.val()});
                $('.comment-add', $this).addClass('hide');
                $('.comment-update', $this).removeClass('hide');
            },
            updateComment: function() {
                let $this = $(this), data = $this.data($name),
                    $comment_input = $('#id_content'),
                    ajax_data = $.extend(data, {content: $comment_input.val()});

                $.ajax({
                    url: '/murrs/comment_update/', data: ajax_data,
                    type: 'POST', dataType: 'json',
                    success: function(response) {
                        $('#id_content').val('');
                        $(".comment-list").html(response['comments']);
                        $('.comment-add', $this).removeClass('hide');
                        $('.comment-update', $this).addClass('hide');
                    }
                })
            },
            addComment: function() {
                let $this = $(this), data = $this.data($name),
                    content = $('#id_content').val(),
                    ajax_data = $.extend(data, {content: content});

                $.ajax({
                    url: '/murrs/comment_add/', data: ajax_data,
                    type: 'POST', dataType: 'json',
                    success: function(response) {
                        $('#id_content').val('');
                        $(".comment-list").html(response['comments']);
                        $('html, body').animate(
                            {scrollTop: $(".comment").first().offset().top - 56},
                            1000
                        );
                    }
                })
            },
            deleteComment: function($comment) {
                let $this = $(this), data = $this.data($name);

                $.extend($comment.data(), data);
                $.ajax({
                    url: '/murrs/comment_delete/', data: $comment.data(),
                    type: 'POST', dataType: 'json',
                    success: function (response) {
                        $comment.animate({
                            opacity: 0,
                            height: 0,
                            padding: 0
                        }, 'slow', function () {
                            $comment.remove();
                        });
                    }
                });

            },
            deleteWithConfirm: function($target) {
                let $this = $(this), data = $this.data($name),
                    $comment = $target.closest('.comment');

                BootstrapDialog.show({
                    title: '<div class="fas fa-exclamation-circle"></div>&nbsp; Подтвердите действие',
                    type: 'type-danger',
                    cssClass: 'text-danger lead',
                    message: 'Вы уверены, что хотите удалить этот комментарий?',
                    buttons: [{
                        label: 'Удалить',
                        cssClass: 'btn-primary btn-sm',
                        action: function(dialog) {
                            $this[$name]('deleteComment', $comment);
                            dialog.close();
                        }
                    }, {
                        label: 'Отмена',
                        cssClass: 'btn-sm',
                        action: function(dialog) {
                            dialog.close();
                        }
                    }]
                })
            }
        };
    $.fn[$name] = $.namespace(methods)
})(jQuery);
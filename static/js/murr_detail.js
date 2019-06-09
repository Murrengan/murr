;(function($) {
    let $name = 'murrDetail',
        methods = {
            init: function() {
                return this.each(function() {
                    let $this = $(this), data = {
                        csrfmiddlewaretoken: $this.data('csrf_token'),
                        murr_slug: $this.data('murr_slug')
                    };
                    $this.data($name, data);

                    $this[$name]('bindEvent');
                    $('#id_content').emojioneArea({
                        pickerPosition: "bottom",
                        search: false,
                        recentEmojis: false
                    })
                })
            },
            bindEvent: function() {
                let $this = $(this), data = $this.data($name);
                $('.js-comment-add', $this).unbind('click').click(function(event) {
                    event.preventDefault();
                    $this[$name]('addComment');
                });

                $('.js-comments', $this).unbind('click').click(function(event) {
                    if (event.target.classList.contains('js-delete')) {
                        event.preventDefault();
                        $this[$name]('deleteComment', $(event.target));
                    } else if (event.target.classList.contains('js-edit')) {
                        event.preventDefault();
                        $this[$name]('editComment', $(event.target));
                    } else if (event.target.classList.contains('js-cancel')) {
                        event.preventDefault();
                        $this[$name]('cancelEdit', $(event.target));
                    } else if (event.target.classList.contains('js-save')) {
                        event.preventDefault();
                        $this[$name]('updateComment', $(event.target));
                    }
                });
            },
            addComment: function() {
                let $this = $(this), data = $this.data($name),
                    content = $('#id_content').val();
                $.extend(data, {content: content, 'g-recaptcha-response': grecaptcha.getResponse()});
                $.ajax({
                    url: '/murrs/comment_add/', data: data,
                    type: 'POST', dataType: 'json',
                    success: function(response) {
                        $('#id_content').data("emojioneArea").setText('');
                        $('.emojionearea-editor').empty();
                        $(".js-comments").html(response['comments']);
                    }
                })
            },
            editComment: function($target) {
                let $this = $(this), data = $this.data($name),
                    $comment = $target.closest('.js-comment'),
                    $content = $('.js-content', $comment);

                $('.js-cancel').click();

                $('#comment-edit-content').emojioneArea({pickerPosition: "right"
                });
                $comment.data('comment', $content.html());
                $.extend(data, $comment.data(), {'content': $content.html()});
                $.ajax({
                    url: '/murrs/comment_edit/', data: data,
                    type: 'POST', dataType: 'json',
                    success: function(response) {
                        $content.html(response.html);
                        $('#comment-edit-content').emojioneArea({ pickerPosition: "bottom" });
                    }
                })
            },
            cancelEdit: function($target) {
                let $this = $(this), data = $this.data($name),
                    $comment = $target.closest('.js-comment'),
                    $content = $('.js-content', $comment);

                $content.html($comment.data('comment'));
            },
            updateComment: function($target) {
                let $this = $(this), data = $this.data($name),
                    $comment = $target.closest('.js-comment'),
                    content = $('#comment-edit-content').val();

                $.extend(data, $comment.data(), {'content': content});
                $.ajax({
                    url: '/murrs/comment_update/', data: data,
                    type: 'POST', dataType: 'json',
                    success: function(response) {
                        $(".js-comments").html(response['comments']);
                    }
                })
            },
            deleteComment: function($target) {
                let $this = $(this), data = $this.data($name),
                    $comment = $target.closest('.js-comment'),
                    $commentList = $(".js-comments");

                $.extend(data, $comment.data());
                $.ajax({
                    url: '/murrs/comment_delete/', data: data,
                    type: 'POST', dataType: 'json',
                    success: function (response) {
                        $comment.animate({
                            opacity: 0,
                            height: 0,
                            padding: 0
                        }, 'slow', function () {
                            $comment.remove();
                            if (!$commentList.html().trim()) { $commentList.html('') }
                        });
                    }
                });
            },
        };
    $.fn[$name] = $.namespace(methods)
})(jQuery);

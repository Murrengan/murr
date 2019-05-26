;(function($) {
    let $name = 'murrPage',
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

                $('.js-comment-add', $this).click(function(event) {
                    event.preventDefault();
                    $this[$name]('addComment');
                });

                $('.js-comments', $this).click(function(event) {
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

                $.extend(data, {content: content});
                $.ajax({
                    url: '/murrs/comment_add/', data: data,
                    type: 'POST', dataType: 'json',
                    success: function(response) {
                        $('#id_content').val('');
                        $(".js-comments").html(response['comments']);
                    }
                })
            },
            editComment: function($target) {
                let $this = $(this), data = $this.data($name),
                    $comment = $target.closest('.js-comment'),
                    $content = $('.js-content', $comment);

                $('.js-cancel').click();
                $comment.data('comment', $content.html());
                $.extend(data, $comment.data(), {'content': $content.html()});
                $.ajax({
                    url: '/murrs/comment_edit/', data: data,
                    type: 'POST', dataType: 'json',
                    success: function(response) {
                        $content.html(response.html)
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
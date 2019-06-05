;(function($) {
    let $name = 'murrList',
        methods = {
            init: function() {
                return this.each(function() {
                    let $this = $(this), data = {
                        csrfmiddlewaretoken: $this.data('csrf_token'),
                        murren: $this.data('murren')
                    };
                    $this.data($name, data);

                    $this[$name]('bindEvent');
                })
            },
            bindEvent: function() {
                let $this = $(this), data = $this.data($name),
                    $murrDetailModal = $('.js-murr-detail');

                $('.js-murr-card-like', $this).click(function() {
                    if (data.murren) { $this[$name]('like', $(this)) }
                    else { $this[$name]('signUp') }
                });

                $('.js-murr-card-unlike', $this).click(function() {
                    if (data.murren) { $this[$name]('unlike', $(this)) }
                    else { $this[$name]('signUp') }
                });

                $('.js-murr-card', $this).click(function(event) {
                    if (event.target.classList.contains('js-murr-card-open')) {
                        event.preventDefault();
                        $this[$name]('slideIn', $(this))
                    }
                });

                $('.js-murr-detail-overlay').click(function() {
                    $this[$name]('slideOut')
                });
            },
            slideOut: function() {
                let $this = $(this), data = $this.data($name),
                    $slideIn = $('.js-murr-detail'),
                    $slideInOverlay = $('.js-murr-detail-overlay');

                $slideIn.addClass('modal-box_closed');
                $slideInOverlay.addClass('modal-overlay_closed');
                window.location.reload(true);

            },
            slideIn: function($card) {
                let $this = $(this), data = $this.data($name),
                    slug = $card.data('murr'), $slideIn = $('.js-murr-detail'),
                    $slideInOverlay = $('.js-murr-detail-overlay');

                $slideIn.removeClass('modal-box_closed');
                $slideInOverlay.removeClass('modal-overlay_closed');
                $.ajax({
                    url: '/murrs/murr_detail/' + slug, data: data,
                    type: 'POST', dataType: 'json',
                    success: function(response) {
                        $('.js-murr-detail-body', $slideIn).html(response.html);
                        $('.js-murr-detail')['murrDetail']();
                    }
                })
            },
            signUp: function() {
                window.location.href = '/accounts/signup/';
            },
            like: function($target) {
                let $this = $(this), data = $this.data($name),
                $murr = $target.closest('.js-murr-card');

                $.extend($murr.data(), data);
                $.ajax({
                    url: '/murrs/like/', data: $murr.data(),
                    type: 'POST', dataType: 'json',
                    success: function(response) {
                        if (response.error) { alert(response.error); return; }

                        $('.js-murr-card-like', $murr).addClass('is-hidden');
                        $('.js-murr-card-unlike', $murr).removeClass('is-hidden');
                        $('.js-murr-card-like-counter', $murr).html(response['likes']);
                    }
                })
            },
            unlike: function($target) {
                let $this = $(this), data = $this.data($name),
                $murr = $target.closest('.js-murr-card');

                $.extend($murr.data(), data);
                $.ajax({
                    url: '/murrs/unlike/', data: $murr.data(),
                    type: 'POST', dataType: 'json',
                    success: function(response) {
                        if (response.error) { alert(response.error); return; }

                        $('.js-murr-card-like', $murr).removeClass('is-hidden');
                        $('.js-murr-card-unlike', $murr).addClass('is-hidden');
                        $('.js-murr-card-like-counter', $murr).html(response['likes']);
                    }
                })
            },
        };
    $.fn[$name] = $.namespace(methods)
})(jQuery);
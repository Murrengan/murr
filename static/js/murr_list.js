;(function ($) {
    let $name = 'murrList',
        methods = {
            init: function () {
                return this.each(function () {
                    let $this = $(this), data = {
                        csrfmiddlewaretoken: $this.data('csrf_token'),
                        murren: $this.data('murren')
                    };
                    $this.data($name, data);

                    $this[$name]('bindEvent');
                })
            },
            bindEvent: function () {
                let $this = $(this), data = $this.data($name),
                    $murrDetailModal = $('.js-murr-detail');

                $('.js-murr-card-like', $this).click(function () {
                    if (data.murren) {
                        $this[$name]('like', $(this))
                    }
                    else {
                        $this[$name]('signUp')
                    }
                });

                $('.js-murr-card__action', $this).click(function () {
                    if (data.murren) {
                        $this[$name]('listActions', $(this))
                    }
                    else {
                        $this[$name]('signUp')
                    }
                });
                $('.js-murr-card__overlay-close', $this).click(function () {
                    if (data.murren) {
                        $this[$name]('closeActions', $(this))
                    }
                    else {
                        $this[$name]('signUp')
                    }
                });
                $('.js-report_murr', $this).click(function () {
                    if (data.murren) {
                        $this[$name]('reportMurr', $(this))
                    }
                    else {
                        $this[$name]('signUp')
                    }
                });
                $('.js-hide_murr', $this).click(function () {
                    if (data.murren) {
                        $this[$name]('hideMurr', $(this))
                    }
                    else {
                        $this[$name]('signUp')
                    }
                });

                $('.js-murr-card-unlike', $this).click(function () {
                    if (data.murren) {
                        $this[$name]('unlike', $(this))
                    }
                    else {
                        $this[$name]('signUp')
                    }
                });

                $('.js-murr-card', $this).click(function (event) {
                    if (event.target.classList.contains('js-murr-card-open')) {
                        event.preventDefault();
                        $this[$name]('slideIn', $(this))
                    }
                });

                $('.js-murr-detail-overlay').click(function () {
                    $this[$name]('slideOut')
                });
            },
            slideOut: function () {
                let $this = $(this), data = $this.data($name),
                    $slideIn = $('.js-murr-detail'),
                    $slideInOverlay = $('.js-murr-detail-overlay');

                $slideIn.addClass('modal-box_closed');
                $slideInOverlay.addClass('modal-overlay_closed');
                window.location.reload(true);


            },
            slideIn: function ($card) {
                let $this = $(this), data = $this.data($name),
                    slug = $card.data('murr'), $slideIn = $('.js-murr-detail'),
                    $slideInOverlay = $('.js-murr-detail-overlay');

                $slideIn.removeClass('modal-box_closed');
                $slideInOverlay.removeClass('modal-overlay_closed');
                $.ajax({
                    url: '/murrs/murr_detail/' + slug, data: data,
                    type: 'POST', dataType: 'json',
                    success: function (response) {
                        $('.js-murr-detail-body', $slideIn).html(response.html);
                        $('.js-murr-detail')['murrDetail']();
                    }
                })
            },
            signUp: function () {
                window.location.href = '/accounts/signup/';
            },
            like: function ($target) {
                let $this = $(this), data = $this.data($name),
                    $murr = $target.closest('.js-murr-card');

                $.extend($murr.data(), data);
                $.ajax({
                    url: '/murrs/like/', data: $murr.data(),
                    type: 'POST', dataType: 'json',
                    success: function (response) {
                        if (response.error) {
                            alert(response.error);
                            return;
                        }

                        $('.js-murr-card-like', $murr).addClass('is-hidden');
                        $('.js-murr-card-unlike', $murr).removeClass('is-hidden');
                        $('.js-murr-card-like-counter', $murr).html(response['likes']);
                    }
                })
            },
            unlike: function ($target) {
                let $this = $(this), data = $this.data($name),
                    $murr = $target.closest('.js-murr-card');

                $.extend($murr.data(), data);
                $.ajax({
                    url: '/murrs/unlike/', data: $murr.data(),
                    type: 'POST', dataType: 'json',
                    success: function (response) {
                        if (response.error) {
                            alert(response.error);
                            return;
                        }

                        $('.js-murr-card-like', $murr).removeClass('is-hidden');
                        $('.js-murr-card-unlike', $murr).addClass('is-hidden');
                        $('.js-murr-card-like-counter', $murr).html(response['likes']);
                    }
                })
            },
            listActions: function ($card) {
                let $murr = $card.closest('.js-murr-card');
                $('.murr-card__body__overlay', $murr).css('display', 'block');
            },
            closeActions : function ($card) {
                let $murr = $card.closest('.js-murr-card');
                $('.murr-card__body__overlay', $murr).css('display', 'none');
            },
            hideMurr : function ($card) {
                let $this = $(this), data = $this.data($name),
                    $murr = $card.closest('.js-murr-card'),
                    murr_pk = $murr.data('murr-pk'),
                    $murrList = $('.murr-list');
                $.extend(data, {pk: murr_pk});
                $.ajax({
                    url: '/murrs/hide_murr/', data: data,
                    type: 'POST', dataType: 'json',
                    success: function (response) {
                        $murr.animate({
                            opacity: 0

                        }, 'slow', function () {
                            $murr.remove();
                            if (!$murrList.html().trim()) { $murrList.html('') }
                        });
                    }
                });
            },
            reportMurr : function ($card) {
                let $this = $(this), data = $this.data($name),
                    $murr = $card.closest('.js-murr-card'),
                    murr_pk = $murr.data('murr-pk'),
                    $murrList = $('.murr-list');
                $.extend(data, {pk: murr_pk});
                $.ajax({
                    url: '/murrs/report_murr/', data: data,
                    type: 'POST', dataType: 'json',
                    success: function (response) {
                        $murr.animate({
                            opacity: 0

                        }, 'slow', function () {
                            $murr.remove();
                            if (!$murrList.html().trim()) { $murrList.html('') }
                        });
                    }
                });
            }
        };
    $.fn[$name] = $.namespace(methods)
})(jQuery);


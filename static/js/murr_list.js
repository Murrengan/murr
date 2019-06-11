;(function ($) {
    let $name = 'murrList',
        methods = {
            init: function () {
                let $this = $(this), data = {
                    csrfmiddlewaretoken: $this.data('csrf_token'),
                    murren: $this.data('murren')
                };

                $this.data($name, data);
                $this[$name]('bindEvent');
            },
            bindEvent: function () {
                let $this = $(this), data = $this.data($name),
                    $murrDetailModal = $('.js-murr-detail');

                $($this).click(function () {
                    if ($(event.target).hasClass('js-murr-card-like')) {
                        if (data.murren) {
                            $this[$name]('like', $(event.target))
                        } else {
                            $this[$name]('signUp')
                        }
                    } else if ($(event.target).hasClass('js-murr-card__action')) {
                        if (data.murren) {
                            $this[$name]('listActions', $(event.target))
                        }
                        else {
                            $this[$name]('signUp')
                        }
                    } else if ($(event.target).hasClass('js-murr-card__overlay-close')) {
                        if (data.murren) {
                            $this[$name]('closeActions', $(event.target))
                        }
                        else {
                            $this[$name]('signUp')
                        }
                    } else if ($(event.target).hasClass('js-report_murr')) {
                        if (data.murren) {
                            $this[$name]('reportMurr', $(event.target))
                        }
                        else {
                            $this[$name]('signUp')
                        }
                    } else if ($(event.target).hasClass('js-hide_murr')) {
                        if (data.murren) {
                            $this[$name]('hideMurr', $(event.target))
                        }
                        else {
                            $this[$name]('signUp')
                        }
                    } else if ($(event.target).hasClass('js-murr-card-unlike')) {
                        if (data.murren) {
                            $this[$name]('unlike', $(event.target))
                        }
                        else {
                            $this[$name]('signUp')
                        }
                    } else if (event.target.classList.contains('js-murr-card-open')) {
                        event.preventDefault();
                        $this[$name]('slideIn', $(event.target))
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
            slideIn: function ($target) {
                let $this = $(this), data = $this.data($name),
                    $murr = $target.closest('.js-murr-card'),
                    slug = $murr.data('murr'), $slideIn = $('.js-murr-detail'),
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
            listActions: function ($target) {
                let $murr = $target.closest('.js-murr-card');

                $('.murr-card__body__overlay', $murr).removeClass('is-hidden');
            },
            closeActions: function ($target) {
                let $murr = $target.closest('.js-murr-card');

                $('.murr-card__body__overlay', $murr).addClass('is-hidden');
            },
            hideMurr: function ($target) {
                let $this = $(this), data = $this.data($name),
                    $murr = $target.closest('.js-murr-card'),
                    murr_slug = $murr.data('murr'),
                    $murrList = $('.murr-list');

                $.extend(data, {murr: murr_slug, action: 'hide'});
                $.ajax({
                    url: '/murrs/murr_action/', data: data,
                    type: 'POST', dataType: 'json',
                    success: function (response) {
                        $murr.animate(
                            {opacity: 0},
                            'slow',
                            function () {
                                $murr.remove();
                                if (!$murrList.html().trim()) {
                                    $murrList.html('')
                                }
                            });
                    }
                });
            },
            reportMurr: function ($target) {
                let $this = $(this), data = $this.data($name),
                    $murr = $target.closest('.js-murr-card'),
                    murr_slug = $murr.data('murr'),
                    $murrList = $('.murr-list');

                $.extend(data, {murr: murr_slug, action: 'report'});
                $.ajax({
                    url: '/murrs/murr_action/', data: data,
                    type: 'POST', dataType: 'json',
                    success: function (response) {
                        $murr.animate(
                            {opacity: 0},
                            'slow',
                            function () {
                                $murr.remove();
                                if (!$murrList.html().trim()) {
                                    $murrList.html('')
                                }
                            });
                    }
                });
            }
        },
        infinite = new Waypoint.Infinite({
            element: $('.murr-list')[0],
            items: '.js-murr-card',
            onBeforePageLoad: function () {
                $('.loading').show();
            },
            onAfterPageLoad: function ($items) {
                $('.loading').hide();
            },
        });
    $.fn[$name] = $.namespace(methods);
})(jQuery);



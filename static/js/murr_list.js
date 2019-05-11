;(function($) {
    let $name = 'murrList',
        methods = {
            init: function() {
                return this.each(function() {
                    let $this = $(this), data = {
                        csrfmiddlewaretoken: $this.data('csrf'),
                        murren: $this.data('murren')
                    };
                    $this.data($name, data);

                    $this[$name]('bindEvent')
                })
            },
            bindEvent: function() {
                let $this = $(this), data = $this.data($name);

                $('.card-like', $this).click(function() {
                    if (data.murren) { $this[$name]('like', $(this)) }
                    else { $this[$name]('signUp') }
                });

                $('.card-unlike', $this).click(function() {
                    if (data.murren) { $this[$name]('unlike', $(this)) }
                    else { $this[$name]('signUp') }
                })
            },
            signUp: function() {
                window.location.href = '/accounts/signup/';
            },
            like: function($target) {
                let $this = $(this), data = $this.data($name),
                $murr = $target.closest('.card');

                $.extend($murr.data(), data);
                $.ajax({
                    url: '/murrs/like/', data: $murr.data(),
                    type: 'POST', dataType: 'json',
                    success: function(response) {
                        if (response.error) { alert(response.error); return; }

                        $('.card-like', $murr).addClass('hide');
                        $('.card-unlike', $murr).removeClass('hide');
                        $('.card-likes-count', $murr).html(response.likes);
                    }
                })
            },
            unlike: function($target) {
                let $this = $(this), data = $this.data($name),
                $murr = $target.closest('.card');

                $.extend($murr.data(), data);
                $.ajax({
                    url: '/murrs/unlike/', data: $murr.data(),
                    type: 'POST', dataType: 'json',
                    success: function(response) {
                        if (response.error) { alert(response.error); return; }

                        $('.card-like', $murr).removeClass('hide');
                        $('.card-unlike', $murr).addClass('hide');
                        $('.card-likes-count', $murr).html(response.likes);
                    }
                })
            },
        };
    $.fn[$name] = $.namespace(methods)
})(jQuery);
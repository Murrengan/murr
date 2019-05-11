;(function($) {
    let $name = 'murrList',
        methods = {
            init: function() {
                return this.each(function() {
                    let $this = $(this), data = {
                        csrfmiddlewaretoken: $this.data('csrf')
                    };
                    $this.data($name, data);

                    $this[$name]('bindEvent')
                })
            },
            bindEvent: function() {
                let $this = $(this);

                $('.card-like', $this).click(function() {
                    $this[$name]('like', $(this))
                });

                $('.card-unlike', $this).click(function() {
                    $this[$name]('unlike', $(this))
                })
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
                    }
                })
            },
        };
    $.fn[$name] = $.namespace(methods)
})(jQuery);
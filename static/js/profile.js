;(function($) {
    let $name = 'murrenProfile',
        methods = {
            init: function() {
                return this.each(function() {
                    let $this = $(this), data = {
                        csrfmiddlewaretoken: $this.data('csrf'),
                        following: $this.data('murren')
                    };
                    $this.data($name, data);

                    $this[$name]('bindEvent')
                })
            },
            bindEvent: function() {
                let $this = $(this);

                $('.profile-follow', $this).click(function() {
                    $this[$name]('follow')
                });

                $('.profile-unfollow', $this).click(function() {
                    $this[$name]('unfollow')
                })
            },
            follow: function() {
                let $this = $(this), data = $this.data($name);

                $.ajax({
                    url: '/murren/follow/', data: data,
                    type: 'POST', dataType: 'json',
                    success: function(response) {
                        if (response.error) { alert(response.error); return; }

                        $('.profile-follow', $this).addClass('hide');
                        $('.profile-unfollow', $this).removeClass('hide');
                    }
                })
            },
            unfollow: function() {
                let $this = $(this), data = $this.data($name);

                $.ajax({
                    url: '/murren/unfollow/', data: data,
                    type: 'POST', dataType: 'json',
                    success: function(response) {
                        if (response.error) { alert(response.error); return; }

                        $('.profile-follow', $this).removeClass('hide');
                        $('.profile-unfollow', $this).addClass('hide');
                    }
                })
            },
        };
    $.fn[$name] = $.namespace(methods)
})(jQuery);
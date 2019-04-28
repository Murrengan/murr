(function() {
    $.namespace = function(methods) {
        return function(method) {
            if (methods[method]) {
                return methods[method].apply(this, Array.prototype.slice.call(arguments, 1))
            } else if (typeof method === 'object' || !method) {
                return methods.init.apply(this, arguments)
            }
        }
    };
})();

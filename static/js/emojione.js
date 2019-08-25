$(document).ready(function() {
    $(".js-content").each(function() {
        var original = $(this).html();
        // use .shortnameToImage if only converting shortnames (for slightly better performance)
        var converted = emojione.toImage(original);
        $(this).html(converted);
    });
});

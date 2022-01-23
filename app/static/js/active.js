$(document).ready(function () {

    var url = window.location.href;
    console.log(url);
    url = url.split('/');
    prefix = url[3];

    var current_html = '<span class="sr-only">(current)</span>';

    if (prefix == '' || prefix == 'index') {
        $('#homeNav a').css({
            'opacity': '1',
            'color': 'black'
        });
        $('#homeNav a').append(' ' + current_html);
    } else if (prefix == 'brands') {
        $('#brandsNav a:first').css({
            'opacity': '1',
            'color': 'black'
        });
        $('#brandsNav a:first').append(' ' + current_html);
    } else if (prefix == 'categories') {
        $('#categoriesNav a:first').css({
            'opacity': '1',
            'color': 'black'
        });
        $('#categoriesNav a:first').append(' ' + current_html);
    }
});
$(function() {
    $('.tile').on('click', function() {
        $('.tile').removeClass('tile-selected');
        tile = $(this).data('tile');
        html_input = '<input name="tile" type="hidden" value="' + tile + '" />';
        $('#input_hidden_area').html(html_input);
        $(this).addClass('tile-selected');
    });
});
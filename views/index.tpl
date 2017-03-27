% rebase('base.tpl')
<style>
button {
    background-color: transparent;
    border: none;
}
</style>
<script>
$(function() {
    $('.tile').on('click', function() {
        tile = $(this).val();
        html_input = '<input name="tile" type="hidden" value="' + tile + '" />';
        $('#input_hidden_area').html(html_input);
    });
});
</script>
<div style="text-align: center; width: 100%;">
    <div class="well well-lg" style="text-align: left;">
        何切る？
    </div>
    <div style="width: 100%;">
        <table>
            <tr>
                % for hand in random_hand:
                    <td>
                        <button class="tile" value="{{hand}}">
                            <img src="img/{{hand}}.gif">
                        </button>
                    </td>
                % end
            </tr>
        </table>
    </div>
    <hr>
    <form action="show_result" method="post">
        <input type="hidden" name="hand" value="{{random_hand}}" />
        <div id="input_hidden_area"></div>
        <input class="btn btn-info" type="submit" value="決定" />
    </form>
</div>

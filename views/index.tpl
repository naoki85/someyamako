% rebase('base.tpl')
<div style="text-align: center; width: 100%;">
    <div class="well well-lg" style="text-align: left;">
        何切る？
    </div>
    <div class="main">
        <ul class="majan_container clearfix">
            % for hand in random_hand:
                <li>
                     <div class="tile" data-tile="{{hand}}">
                        <img src="img/{{hand}}.gif">
                    </div>
                </li>
            % end
        </ul>
    </div>
    <hr>
    <form action="show_result" method="post">
        <input type="hidden" name="hand" value="{{random_hand}}" />
        <div id="input_hidden_area"></div>
        <input class="btn btn-info" type="submit" value="決定" />
    </form>
</div>

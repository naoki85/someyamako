% rebase('base.tpl')
<div class="h-align-center" style="width: 100%;">
    <div class="well well-lg h-align-left">
        何切る？
    </div>
    <div class="main">
        <div class="dora h-align-left mb-default">
            ドラ
            <img src="img/{{dora}}.gif">
        </div>
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
        <input type="hidden" name="dora" value="{{dora}}" />
        <input type="hidden" name="hand" value="{{random_hand}}" />
        <div id="input_hidden_area"></div>
        <input class="btn btn-info" type="submit" value="決定" />
    </form>
    <div>{{predict_list}}</div>
</div>

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
    <hr>
    <table class="table">
            % tiles = [[11,12,13,14,15,16,17,18,19], [21,22,23,24,25,26,27,28,29], [31,32,33,34,35,36,37,38,39], [41,42,43,44,45,46,47]]
            % for i in range(0, 4):
            <tr>
            % for j in range(0, len(tiles[i])):
            <td>
                <div class="tile">
                    <img src="img/{{tiles[i][j]}}.gif">
                </div>
                <p>{{round(predict_list[tiles[i][j]] * 100,2)}} %</p>
            </td>
            % end
            </tr>
            % end
    </table>
</div>

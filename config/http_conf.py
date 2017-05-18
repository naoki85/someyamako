import os
from bottle import run
def bottle_run():
    if os.getenv("HONBAN_FLG"):
        # 本番用の設定
        run(host="163.44.175.59", port=8080, debug=True, reloader=True)
    else:
        # ローカル用の設定
        run(host='localhost', port=8080, debug=True, reloader=True)


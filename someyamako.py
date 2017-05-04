# モジュールの読み込み
import os
from bottle import route, get, post, run, template, request, static_file, redirect
from classes.mahjang import *
from classes.output import *
from config.http_conf import *

@get('/')
@get('/index')
def index():
    mahjang = Mahjang()
    dora = mahjang.get_dora()
    random_hand = mahjang.random_set_hand()
    return template('index', random_hand=random_hand, dora=dora)

@post('/show_result')
def show_result():
    hand = request.forms.get('hand')
    tile = request.forms.get('tile')
    dora = request.forms.get('dora')
    hand_convert_to_list = hand.replace('[', '').replace(']', '').split(', ')
    Output().write_in_csv(hand_convert_to_list, tile, dora)
    redirect('/')

@route('/<filename:path>')
def static(filename):
    path = os.getcwd() + '/static'
    return static_file(filename, root=path)

if __name__ == '__main__':
    bottle_run()


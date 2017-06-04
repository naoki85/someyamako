# -*- coding:utf-8 -*-
import numpy as np
from classes.mahjang  import *
from classes.network  import *
from classes.output   import *

# 設定値
learning_rate = 0.01
loop_count    = 100

# 配牌を読み込んで、4×9の行列にする
mahjang = Mahjang()
matrix_hands, matrix_results, matrix_dora = mahjang.load_csv_data()

# 学習処理
network       = Network()
learning_rate = 0.01
loop_count    = 100

for loop in range(0, loop_count):
    tmp_total_loss = 0

    for i in range(0, len(matrix_hands)):
        matrix_hand      = matrix_hands[i]
        matrix_result    = matrix_results[i]
        matrix_each_dora = matrix_dora[i]

        loss = network.loss(matrix_hand, matrix_each_dora, matrix_result)
        tmp_total_loss += loss
        # 勾配を求める
        grads = network.return_gradient(matrix_hand, matrix_each_dora, matrix_result)
        network.params['W1'] -= learning_rate * grads['W1']
        network.params['W2'] -= learning_rate * grads['W2']
        network.params['b']  -= learning_rate * grads['b']
        print(network.params)

output = Output()
output.write_in_pickle(network.params['W1'], network.params['W2'], network.params['b'])

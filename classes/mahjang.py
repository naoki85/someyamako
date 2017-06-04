# -*- coding:utf-8 -*-
import sys, os, random, csv
import numpy as np

class Mahjang:
    u"""
    麻雀のルールに関する定義を行うクラスです
    """

    def __init__(self):
        # 牌の初期化
        # 萬子
        self.characters = [11, 12, 13, 14, 15, 16, 17, 18, 19]
        # 筒子
        self.circles = [21, 22, 23, 24, 25, 26, 27, 28, 29]
        # 索子
        self.bamboos = [31, 32, 33, 34, 35, 36, 37, 38, 39]
        # 字牌
        self.honours = [41, 42, 43, 44, 45, 46, 47]
        # 全ての牌
        self.tiles = (self.characters + self.circles + self.bamboos + self.honours)
        # 山
        self.wall = self.tiles * 4
        # CSVディレクトリ
        self.csv_dirpath = os.getcwd() + '/csv'

    def random_set_hand(self):
        u"""
        配牌をランダムにセットします
        """
        my_hand = random.sample(self.wall, 14)
        my_hand.sort()
        return my_hand

    def load_csv_data(self):
        u"""
        CSVファイルから手牌と結果をロードします
        """
        hands, results, dora = self.set_params_from_csv_file()
        return self.params_convert_to_matrix(hands, results, dora)

    def get_dora(self):
        u"""
        ドラをランダムにセットします
        """
        list_dora = random.sample(self.tiles, 1)
        return list_dora[0]

    def set_params_from_csv_file(self):
        u"""
        CSVファイルからサンプルデータを読み込み、データを返します
        @return hands
        @return results
        @return dora
        """
        # CSVファイルのパスを追加
        csv_filepath = self.csv_dirpath + '/results.csv'

        with open(csv_filepath, 'r', newline='') as csvfile:
            reader  = csv.reader(csvfile)
            header  = next(reader)
            hands   = []
            results = []
            dora    = []

            for row in reader:
                tmp_hand = [int(row[index]) for index in range(0, 14)]
                tmp_dora = int(row[14])
                result   = int(row[15])

                hands.append(tmp_hand)
                results.append(result)
                dora.append(tmp_dora)

        return hands, results, dora

    def list_convert_matrix(self, my_hand, dora):
        matrix_hand = np.zeros((4, 9))
        matrix_dora = np.zeros((4, 9))

        result_color_matrix, result_number_matrix = self.convert_matrix_index(dora)
        matrix_dora[result_color_matrix][result_number_matrix] += 1

        for i in range(0, len(my_hand)):
            color_matrix, number_matrix = self.convert_matrix_index(my_hand[i])
            matrix_hand[color_matrix][number_matrix] += 1

        return matrix_hand, matrix_dora


    def params_convert_to_matrix(self, my_hands, results, dora):
        u"""
        TODO 上のメソッドとまとめる
        引数で渡された配牌を4×9の行列に変換する
        @return matrix_hands
        @return matrix_results
        @return matrix_dora
        """
        matrix_hands   = []
        matrix_results = []
        matrix_dora    = []

        for j in range(0, len(my_hands)):
            tmp_my_hand     = my_hands[j]
            matrix_hand     = np.zeros((4, 9))
            matrix_result   = np.zeros((4, 9))
            matrix_dora_tmp = np.zeros((4, 9))

            result_color_matrix, result_number_matrix = self.convert_matrix_index(results[j])
            matrix_result[result_color_matrix][result_number_matrix] += 1
            result_color_matrix, result_number_matrix = self.convert_matrix_index(dora[j])
            matrix_dora_tmp[result_color_matrix][result_number_matrix] += 1

            for i in range(0, len(tmp_my_hand)):
                color_matrix, number_matrix = self.convert_matrix_index(tmp_my_hand[i])
                matrix_hand[color_matrix][number_matrix] += 1

            matrix_hands.append(matrix_hand)
            matrix_results.append(matrix_result)
            matrix_dora.append(matrix_dora_tmp)

        return matrix_hands, matrix_results, matrix_dora

    def convert_matrix_index(self, input):
        u"""
        行列のインデックスを返します
        """
        if input < 20:
            color_matrix  = 0
            number_matrix = input - 11
        elif input >= 20 and input < 30:
            color_matrix  = 1
            number_matrix = input - 21
        elif input >= 30 and input < 40:
            color_matrix  = 2
            number_matrix = input - 31
        elif input >= 40:
            color_matrix  = 3
            number_matrix = input - 41

        return color_matrix, number_matrix


import sys, os, random

class Mahjang:
    u"""
    麻雀のルールに関する定義を行うクラスです。
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

    def random_set_hand(self):
        u"""
        配牌をランダムにセットします。
        """
        my_hand = random.sample(self.wall, 14)
        return my_hand


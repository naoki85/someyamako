# -*- coding:utf-8 -*-
import numpy as np
import os, pickle

class Network:
    u"""
    配牌からあがりを予測するモデルです。
    """

    def __init__(self, weight_init_std=0.01):
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(9, 9)
        self.params['W2'] = weight_init_std * np.random.randn(9, 9)
        self.params['b'] = np.zeros((4, 9))

    def load_parameters_from_pickle(self):
        u"""
        前回の重み、バイアスの学習結果をpickleファイルから取得する
        """
        pickle_filepath = os.getcwd() + '/pickle/output_results.pickle'
        with open(pickle_filepath, 'rb') as f:
            params = pickle.load(f)

        self.params['W1'] = params['W1']
        self.params['W2'] = params['W2']
        self.params['b'] = params['b']

    def loss(self, hand, dora, t):
        u"""
        損失関数の値を返します
        """
        y = self.predict(hand, dora)

        return self.cross_entropy_error(y, t)

    def predict(self, hand, dora):
        u"""
        予測値を返します
        @param hand 手牌
        @param dora ドラ
        """
        W1, W2, b = self.params['W1'], self.params['W2'], self.params['b']

        a = np.dot(hand, W1) + np.dot(dora, W2) + b
        y = self.softmax(a)

        return y

    def return_gradient(self, hand, dora, t):
        loss_W = lambda W: self.loss(hand, dora, t)
        
        grads = {}
        grads['W1'] = self.numerical_gradient(loss_W, self.params['W1'])
        grads['W2'] = self.numerical_gradient(loss_W, self.params['W2'])
        grads['b']  = self.numerical_gradient(loss_W, self.params['b'])
        
        return grads

    def softmax(self, x):
        u"""
        正規化する関数です
        """
        x = x - np.max(x)
        return np.exp(x) / np.sum(np.exp(x))

    def cross_entropy_error(self, y, t):
        u"""
        損失関数には交差エントロピーを用います
        """
        delta = 1e-7
        return -np.sum(t * np.log(y + delta))

    def numerical_gradient(self, f, x):
        h = 1e-4
        grad = np.zeros_like(x)
        
        it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
        while not it.finished:
            idx = it.multi_index
            tmp_val = x[idx]
            x[idx] = float(tmp_val) + h
            fxh1 = f(x)
            
            x[idx] = tmp_val - h
            fxh2 = f(x)
            grad[idx] = (fxh1 - fxh2) / (2*h)
            
            x[idx] = tmp_val # 値を元に戻す
            it.iternext()
            
        return grad

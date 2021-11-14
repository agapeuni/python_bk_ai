import numpy as np
import math
import random
import matplotlib.pyplot as plt    # from matplotlib import pyplot
# 자세한 내용은 일반화 수식부분을 참조할 것

class Neural:    # 뉴럴넷 클래스를 정의

    # constructor
    def __init__(self, n_input, n_hidden, n_output):
        self.hidden_weight = np.random.random_sample((n_hidden, n_input + 1))  # 1이 더해진 것은 bios를 의미함
        self.output_weight = np.random.random_sample((n_output, n_hidden + 1)) # 1이 더해진 것은 bios를 의미함
        self.hidden_momentum = np.zeros((n_hidden, n_input + 1))    # 1이 더해진 것은 bios를 의미함
        self.output_momentum = np.zeros((n_output, n_hidden + 1))   # 1이 더해진 것은 bios를 의미함
# momentum은 수렴속도를 향상시키기 위한 방법의 하나로, "가중치의 수정량+ (계수 X 지난회의 가중치 수정량)"으로 계산
# v = delta*v - alpha*dx,  x += v  

# public method
    def train(self, X, T, alpha, delta, epoch):  # X: input, T:output, alpha:learning rate, delta:unit error
        self.error = np.zeros(epoch)
        N = X.shape[0]                          # N:입력 갯수
        for epo in range(epoch):
            for i in range(N):
                x = X[i, :]                     # x: 입력값 처음부터 끝까지
                t = T[i, :]                     # t: 출력값 처음부터 끝까지

                self.__update_weight(x, t, alpha, delta)

            self.error[epo] = self.__calc_error(X, T)

    def predict(self, X):
        N = X.shape[0]
        Y = np.zeros((N, X.shape[1]))
        for i in range(N):
            x = X[i, :]
            z, y = self.__forward(x)

            Y[i] = y

        return Y

    def error_graph(self):
        plt.ylim(0.0, 2.0)
        plt.ylim(0.0, 2.0)
        plt.plot(np.arange(0, self.error.shape[0]), self.error)
        plt.show()

# 시그모이드 활성화 함수의 정의
    def __sigmoid(self, arr):
        return np.vectorize(lambda x: 1.0 / (1.0 + math.exp(-x)))(arr)

    def __forward(self, x):
        # z: 은닉층 출력값, y: 출력층 출력값, #dot는 행렬의 곱셈(백터의 내적) 
        z = self.__sigmoid(self.hidden_weight.dot(np.r_[np.array([1]), x]))  
        y = self.__sigmoid(self.output_weight.dot(np.r_[np.array([1]), z]))

        return (z, y)

    def __update_weight(self, x, t, alpha, delta):
        z, y = self.__forward(x)

        # 출력층 가중치 업데이트
        output_delta = (y - t) * y * (1.0 - y)                          # 델타 = 오차 X 미분
        _output_weight = self.output_weight                             # r_는 2개의 배열을 옆 또는 위아래로 붙이는 것 
        self.output_weight -= alpha * output_delta.reshape((-1, 1)) * np.r_[np.array([1]), z] - delta * self.output_momentum
        self.output_momentum = self.output_weight - _output_weight

        # 은닉층 가중치 업데이트
        hidden_delta = (self.output_weight[:, 1:].T.dot(output_delta)) * z * (1.0 - z)
        _hidden_weight = self.hidden_weight

        # reshape((-1, 2))는 2개의 열을 가진 배열로 재배치(-1) 함을 의미
        self.hidden_weight -= alpha * hidden_delta.reshape((-1, 1)) * np.r_[np.array([1]), x]
        self.hidden_momentum = self.hidden_weight - _hidden_weight
        
    def __calc_error(self, X, T):     # 손실함수 계산 부분
        N = X.shape[0]
        err = 0.0
        for i in range(N):
            x = X[i, :]
            t = T[i, :]

            z, y = self.__forward(x)
            err += (y - t).dot((y - t).reshape((-1, 1))) / 2.0     
            
        return err
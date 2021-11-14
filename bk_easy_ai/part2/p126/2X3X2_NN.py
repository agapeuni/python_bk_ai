# 2X3X2의 뉴럴 네트워크를 만들어 보자. 
# 임의의 논리연산을 하는 신경망
# 시그모이드 함수로 활성화 되었으므로 output은 0과 1사이로 나와야만 한다. 

import numpy as np
from random import random

alpha = 1.0   # learning rate(학습률)
epoch = 5000  # 학습 횟수

# 가중치 및 기준치의 초깃값 설정 initializing of weight and bias 
wt = []    # vacant array for weights
bs = []    # vacant array for bias
for i in range(12):  # 2X3X2에서는 총 12개의 가중치값이 필요
    w = np.random.rand()
    wt.append(w)
for i in range(5):   # 2X3X2에서는 총 5개의 bias값이 필요
    w = np.random.rand()
    bs.append(w)

# 시그모이드 활성화 함수 sigmoid activation function 
def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    return y

# 입력 및 정답(교시) 데이터셋 input and teaching data
input_data = np.array([[0,0], [0,1], [1,0], [1,1]])     # 입력 데이터
teaching_data = np.array([[0,0], [0,1], [0,1], [1,0]])  # 앞은 AND, 뒤는 XOR

# 데이터셋에 의한 학습 train with input and teaching data
for n in range(1, epoch+1): # 1부터 epoch까지 반복
    for i in range(len(input_data)): 
        x1 = input_data[i][0]   # i번쨰 행의 첫번째 숫자
        x2 = input_data[i][1]   # i번쨰 행의 두번째 숫자
        t1 = teaching_data[i][0]
        t2 = teaching_data[i][1]
        ########## forward(순방향) #########
        u1 = sigmoid(wt[0]*x1 + wt[1]*x2 + bs[0])  # 은닉층 첫번째 출력
        u2 = sigmoid(wt[2]*x1 + wt[3]*x2 + bs[1])  # 은닉층 두번째 출력
        u3 = sigmoid(wt[4]*x1 + wt[5]*x2 + bs[2])  # 은닉층 세번째 출력
        y1 = sigmoid(wt[6]*u1 + wt[7]*u2 + wt[8]*u3 + bs[3])   # 출력층 첫번째 출력
        y2 = sigmoid(wt[9]*u1 + wt[10]*u2 + wt[11]*u3 + bs[4]) # 출력층 두번째 출력
        ########## backward(역방향) ########
        E = 0.5 * (y1 - t1)**2 + 0.5 * (y2 - t2)**2  # 손실함수
        dE_dw_0 = ((y1-t1)*(1-y1)*y1*wt[6] + (y2-t2)*(1-y2)*y2*wt[9])* (1-u1)*u1*x1
        #           (오        메      가   +    오      메     가)        미     입  
        dE_dw_1 = ((y1-t1)*(1-y1)*y1*wt[7] + (y2-t2)*(1-y2)*y2*wt[10])*(1-u2)*u2*x1
        dE_dw_2 = ((y1-t1)*(1-y1)*y1*wt[8] + (y2-t2)*(1-y2)*y2*wt[11])*(1-u3)*u3*x1
        dE_dw_3 = ((y1-t1)*(1-y1)*y1*wt[6] + (y2-t2)*(1-y2)*y2*wt[9])* (1-u1)*u1*x2
        dE_dw_4 = ((y1-t1)*(1-y1)*y1*wt[7] + (y2-t2)*(1-y2)*y2*wt[10])*(1-u2)*u2*x2
        dE_dw_5 = ((y1-t1)*(1-y1)*y1*wt[8] + (y2-t2)*(1-y2)*y2*wt[11])*(1-u3)*u3*x2
        dE_dw_6 =  (y1-t1)*(1-y1)*y1*u1
        #             오       미    입
        dE_dw_7 =  (y1-t1)*(1-y1)*y1*u2
        dE_dw_8 =  (y1-t1)*(1-y1)*y1*u3
        dE_dw_9 =  (y2-t2)*(1-y2)*y2*u1 
        dE_dw_10 = (y2-t2)*(1-y2)*y2*u2 
        dE_dw_11 = (y2-t2)*(1-y2)*y2*u3

        dE_db_0 = ((y1-t1)*(1-y1)*y1*wt[6] + (y2-t2)*(1-y2)*y2*wt[9])*  (1-u1)*u1*1
        #             오       메     가         오       메     가          미    입(1) 
        dE_db_1 = ((y1-t1)*(1-y1)*y1*wt[7] + (y2-t2)*(1-y2)*y2*wt[10])* (1-u2)*u2*1
        dE_db_2 = ((y1-t1)*(1-y1)*y1*wt[8] + (y2-t2)*(1-y2)*y2*wt[11])* (1-u3)*u3*1
        dE_db_3 = (y1-t1)*(1-y1)*y1*1
        #            오       미    입(1)
        dE_db_4 = (y2-t2)*(1-y2)*y2*1
        ########## 최적화(경사하강법) #########
        wt[0] = wt[0] - alpha * dE_dw_0
        wt[1] = wt[1] - alpha * dE_dw_1
        wt[2] = wt[2] - alpha * dE_dw_2
        wt[3] = wt[3] - alpha * dE_dw_3
        wt[4] = wt[4] - alpha * dE_dw_4
        wt[5] = wt[5] - alpha * dE_dw_5
        wt[6] = wt[6] - alpha * dE_dw_6
        wt[7] = wt[7] - alpha * dE_dw_7
        wt[8] = wt[8] - alpha * dE_dw_8
        wt[9] = wt[9] - alpha * dE_dw_9
        wt[10] = wt[10] - alpha * dE_dw_10
        wt[11] = wt[11] - alpha * dE_dw_11
        bs[0] = bs[0] - alpha * dE_db_0
        bs[1] = bs[1] - alpha * dE_db_1
        bs[2] = bs[2] - alpha * dE_db_2
        bs[3] = bs[3] - alpha * dE_db_3
        bs[4] = bs[4] - alpha * dE_db_4

    print("{} EPOCH-ERROR: {}".format(n, E))

# Test: 입력값 x1, x2에 대하여 본 뉴럴넷으로 예측. 앞은 AND, 뒤는 XOR
x1 = 1                   # x1과 x2값을 바꿔가며 테스트해 볼 것
x2 = 0
u1 = sigmoid(wt[0]*x1 + wt[1]*x2 + bs[0])
u2 = sigmoid(wt[2]*x1 + wt[3]*x2 + bs[1])
u3 = sigmoid(wt[4]*x1 + wt[5]*x2 + bs[2])
y1 = sigmoid(wt[6]*u1 + wt[7]*u2 + wt[8]*u3 + bs[3])
y2 = sigmoid(wt[9]*u1 + wt[10]*u2 + wt[11]*u3 + bs[4])
print("AND - XOR")
print("Input:[{}, {}] --> Output: [{:.1f}, {:.1f}]".format(x1, x2, y1, y2))
print("")
# 1X2X1의 가장 간단한 신경망 만들기 
# 시그모이드 함수 값을 추측하는 신경망 만들기
# 시그모이드 함수로 활성화되었으므로 출력값은 0과 1사이의 수로 나와야만 함.

import numpy as np   # py -m pip install numpy로 인스톨, numpy는 수학처리용 모듈

alpha = 1.0   # learning rate(학습률)
epoch = 5000  # 몇 번을 반복하여 학습할 것인가? 여기서는 5000번 반복 학습

# 가중치 및 기준치의 초기값 설정 
w1 = 1.0    # 은닉층 첫 번째 가중치 초깃값
w2 = -1.0   # 은닉층 두 번째 가중치 초깃값
w3 = 2.0    # 출력층 첫 번째 가중치 초깃값
w4 = -2.0   # 출력층 두 번째 가중치 초깃값
b1 = -1.0   # 은닉층 첫 번째 기준치 초깃값
b2 = 1.0    # 은닉층 두 번째 기준치 초깃값
b3 = 2.0    # 출력층 기준치 초깃값

# 시그모이드 활성화 함수 
def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    return y

# 입력 및 학습 데이터 만들기
input_data = np.array([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5])  # 입력 데이터 10개를 배열에 저장하기
teaching_data = []   # 빈 학습 데이터를 만들고
for i in input_data: # 입력 데이터 수만큼 반복하기
    teaching_data.append(sigmoid(i))  # 각각의 입력값으로 시그모이드 함수 호출하여 계산하기

# 입력값과 학습 데이터로 5000번 반복 학습하기
for n in range(1, epoch+1): # 1부터 epoch까지 반복하기
    for i in range(len(input_data)): 
        x = input_data[i]    # 입력값 input_data[0]~[9]까지를 x로 변환하기
        t = teaching_data[i] # 학습 데이터도 각각 교시값 t로 변환

        ########## 순방향 계산(출력값) #########
        u1 = sigmoid(w1 * x + b1)
        u2 = sigmoid(w2 * x + b2)
        y = sigmoid(w3 * u1 + w4 * u2 + b3)
        
        ########## 역방향 계산(오차역전파법) ########
        E = 0.5 * (y - t)**2              # 손실함수
        dE_dw_3 = (y-t) * (1-y) * y * u1  # 출력층 가중치
        dE_dw_4 = (y-t) * (1-y) * y * u2  # 출력층 가중치
        dE_db_3 = (y-t) * (1-y) * y       # 출력층 기준치
        dE_dw_1 = (y-t) * (1-y) * y * w3 * (1-u1) * u1 * x # 은닉층 가중치
        dE_dw_2 = (y-t) * (1-y) * y * w4 * (1-u2) * u2 * x # 은닉층 가중치
        dE_db_1 = (y-t) * (1-y) * y * w3 * (1-u1) * u1     # 은닉층 기준치
        dE_db_2 = (y-t) * (1-y) * y * w4 * (1-u2) * u2     # 은닉층 기준치
        
        ########## 가중치 및 기준치 업데이트(경사하강법) #########
        w1 = w1 - alpha * dE_dw_1
        w2 = w2 - alpha * dE_dw_2
        w3 = w3 - alpha * dE_dw_3
        w4 = w4 - alpha * dE_dw_4
        b1 = b1 - alpha * dE_db_1
        b2 = b2 - alpha * dE_db_2
        b3 = b3 - alpha * dE_db_3

    print("{} EPOCH-ERROR: {}".format(n, E))   # 손실함수 값(오차) 출력

# Test: 입력값 x에 대하여 본 신경망으로 예측된 값과 정답값 출력하기
x = 0.5                              
u1 = sigmoid(w1 * x + b1)            # 입력에 대한 출력값 계산(순방향 계산)
u2 = sigmoid(w2 * x + b2)            # 입력에 대한 출력값 계산(순방향 계산)
y = sigmoid(w3 * u1 + w4 * u2 + b3)  # 입력에 대한 출력값 계산(순방향 계산)

print("")
print("신경망의 예측값: {}".format(y))
print("계산된 값(정답): {}".format(sigmoid(x)))
print("")

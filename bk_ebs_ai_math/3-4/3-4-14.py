import librosa
import librosa.display
import numpy as np


#import matplotlib.pyplot as plt

# 입력변수와 출력변수 생성하기

X_train = np.zeros((40, 20))                # 입력변수 생성
y_train = np.zeros(40)                     # 출력변수 생성

# 인덱스번호 0~19번까지는 레이블 1(배고픔), 21~40번까지는 레이블 0(웃음)
y_train[0:20] = 1

# hungry_특징추출
for i in range(20):
    audio_path = 'bk_ebs_ai/3-4/hungry/hungry_'+str(i+1)+'.wav'
    y, sr = librosa.load(audio_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    temp = mfcc.mean(axis=1)
    X_train[i] = temp                       # 인덱스번호 0~19번까지

# laugh_특징추출
for i in range(20):
    audio_path = 'bk_ebs_ai/3-4/laugh/laugh_'+str(i+1)+'.wav'
    y, sr = librosa.load(audio_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    temp = mfcc.mean(axis=1)
    X_train[i+20] = temp                   # 인덱스번호 20~39번까지

# 추출한 특성 값들을 데이터 셋으로 묶기

# 데이터 셋
data_sets = np.zeros((40, 21))
data_sets[:, 0:20] = X_train
data_sets[:, 20] = y_train

# csv 모듈을 이용하여 파일로 추출하기

# 로지스틱 회귀로 접근 가능한지 확인하는 중
# 시도2_기울기의 변화량 만을 수집


def AccumAscentCurv(A):
    accVal = 0
    for i in range(len(A)-1):
        accVal = accVal + abs(A[i+1]-A[i])
    return accVal


X = [AccumAscentCurv(X_train[i]) for i in range(40)]
y = y_train


X = np.array(X).reshape(40, 1)
y = y.reshape(40, 1)


def sigmoid(X):
    return 1 / (1+np.exp(-X))


def cost_func(X, a):

    delta = 1e-7    # log 무한대 발산 방지
    temp = beta0 + np.dot(X, beta1)
    Y_pred = sigmoid(temp)

    # likelihood
    return -np.sum(a*np.log(Y_pred + delta) + (1-a)*np.log((1 - Y_pred)+delta))

# 에포크(Epoch) 마다 손실(비용)값을 계산하는 Error 함수 정의하기


def Error(X, a):
    delta = 1e-7    # log 무한대 발산 방지

    #temp = beta0 + X*beta1
    temp = beta0 + np.dot(X, beta1)
    Y_pred = sigmoid(temp)

    # likelihood
    return -np.sum(a*np.log(Y_pred + delta) + (1-a)*np.log((1 - Y_pred)+delta))

# 학습을 마친 후, 임의의 데이터에 대해 미래 값 예측 함수


def predict(X):

    #temp = beta0 + beta1*X
    temp = np.dot(X, beta1) + beta0
    Y_pred = sigmoid(temp)

    if Y_pred >= 0.79:
        result = 1  # hungry
    else:
        result = 0  # laugh

    return Y_pred, result


def numerical_derivative(f, x):
    delta_x = 1e-4  # 0.0001
    grad = np.zeros_like(x)

    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])

    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + delta_x
        fx1 = f(x)  # f(x+delta_x)

        x[idx] = tmp_val - delta_x
        fx2 = f(x)  # f(x-delta_x)
        grad[idx] = (fx1 - fx2) / (2*delta_x)

        x[idx] = tmp_val
        it.iternext()

    return grad

# 파라미터 업데이트하기


learning_rate = 1e-3
beta1 = np.random.rand(1, 1)
beta0 = np.random.rand(1)


def F(X): return cost_func(X, y)


for step in range(10000001):

    beta1 -= learning_rate * numerical_derivative(F, beta1)

    beta0 -= learning_rate * numerical_derivative(F, beta0)

    if (step % 100000 == 0):
        print("Epoch = ", step, "error value = ", Error(X, y))

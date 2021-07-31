# 데이터 불러오기
import pandas as pd

df_train = pd.read_csv('fashion-mnist_train.csv') #훈련 데이터 파일 열기
df_test = pd.read_csv('fashion-mnist_test.csv')   #테스트 데이터 파일 열기

#데이터 다루기
import numpy as np

#데이터 프레임을 배열 형태로 저장하기
data_train = np.array(df_train,dtype=np.float32) # 훈련 데이터를 배열로 저장
x_train = data_train[:, 1:]     # 훈련 데이터의 각 행별 픽셀 값 저장
y_train = data_train[:, 0]      # 훈련 데이터의 각 행별 레이블 저장

data_test = np.array(df_test)   # 테스트 데이터를 배열로 저장
x_test = data_test[:, 1:]       # 테스트 데이터의 각 행별 픽셀 값 저장
y_test = data_test[:, 0]        # 테스트 데이터의 각 행별 레이블 저장

print(df_test)
print(data_test)

# 데이터를 학습, 평가 데이터로 분리하기

# 데이터 준비하기
import numpy as np
import pandas as pd               # 모듈 추가하기
df = pd.read_csv('bk_ebs_ai/3-3/temp_ice.csv', encoding='euc-kr')
df.head(5)

# 학습(train) 데이터를 입력변수와 출력변수로 나누기
data = np.array(df)
X = data[:, 1]     # 평균기온 열의 데이터를 출력변수로 지정
Y = data[:, -1]    # 아이스크림/빙수 열의 데이터를 출력변수로 지정

# 비용을 계산하고 업데이트하기

# 입력변수와 출력변수 각각의 평균(mean) 구하기
mean_x = np.mean(X)
mean_y = np.mean(Y)

# X변수의 개수 구하기
n = len(X)

# 최소제곱법을 이용하여 beta0과 beta1 구하기
temp1 = 0
temp2 = 0
for i in range(n):
    temp1 += (X[i] - mean_x) * (Y[i] - mean_y)
    temp2 += (X[i] - mean_x) ** 2
beta1 = temp1 / temp2
beta0 = mean_y - (beta1 * mean_x)

# 문제 해결하기 -----------------------------------------------------------


def Regression(beta0, beta1, X):
    y_pred = beta0+beta1*X
    return y_pred


my_temp = float(input("안녕하세요. 오늘의 기온을 입력해 주세요. : "))

predicted_value = Regression(beta0, beta1, my_temp)
print("오늘의 아이스크림 쇼핑 클릭량은 100점을 기준으로 {0} 만큼 예상됩니다.".format(predicted_value))

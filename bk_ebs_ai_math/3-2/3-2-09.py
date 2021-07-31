# 데이터 불러오기
import numpy as np
import pandas as pd
iris = pd.read_csv('bk_ebs_ai/3-2/Iris.csv')    # 붖꽃 데이터 불러오기

# 150개 데이터의 특성 데이터와 종류 데이터를 나누어 저장하기

# 계산의 편의를 위해 데이터셋의 형식을 numpy로 변환
xy = np.array(iris)
# 테이블의 1~4 열벡터 를 features에 저장
features = xy[:, 1:-1]
# 테이블의 마지막 열벡터를 target_values에 저장
target_value = xy[:, [-1]]

# [Step3] 유클리드 거리법을 이용하여 두 데이터 간의 거리를 구하는 함수 선언하기
# Distance 함수 만들기


def Distance(A, B):
    return np.sqrt(np.sum(np.power((A-B), 2)))


# [Step 4] 붓꽃 분류기 함수 작성하기
# 마지막 행벡터와 거리가 가까운 K개의 데이터의 라벨 중 빈도가 가장 높은 라벨을 반환하는 함수 정의하기
def K_NN(Unknown, features, K):
    # ①_데이터간의 거리 계산
    distance_result = np.zeros(150)
    for i in range(150):
        distance_result[i] = Distance(Unknown, features[i])
    # ②_분류하려는 데이터와 가까운 순서대로 나열
    index = distance_result.argsort()
    # ③_K개의 라벨 확인
    target_result = []
    result = [0, 0, 0]
    for i in range(K):
        target_result.append(target_value[index[i]])
        if target_result[i] == 'Iris-setosa':
            result[0] += 1
        elif target_result[i] == 'Iris-versicolor':
            result[1] += 1
        else:
            result[2] += 1
    # ④_라벨의 빈도가 가장 높은 값 반환
    max_label = result.index(max(result))
    species = {0: "setosa", 1: "versicolor", 2: "virginica"}
    species_result = species[max_label]
    return species_result


# 고흐가 그린 붓꽃 그림의 데이터 분류하기

# 그림에서 수집한 데이터
ID_1 = np.array([2.7, 2.4, 1.65, 0.67])
ID_2 = np.array([5.84, 5.48, 3, 2.16])
ID_3 = np.array([3.97, 4.01, 1.7, 0.67])


# K_NN 분류기 함수를 이용하여 분류하기
result_1 = K_NN(ID_1, features, 5)
result_2 = K_NN(ID_2, features, 5)
result_3 = K_NN(ID_3, features, 5)

# 분류 결과 출력하기
print(result_1, result_2, result_3)

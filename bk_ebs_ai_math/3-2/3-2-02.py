# 여러 개의 자료형 변환하기

import csv

f = open('bk_ebs_ai/3-2/iris.csv')               # iris.csv 파일 열기
data = csv.reader(f)               # iris.csv 속 데이터를 data에 저장하기
header = next(data)                # 제목을 따로 저장하기
result = []                         # 빈 리스트 result 만들기

# 전체 데이터를 행별로 result 리스트에 저장 및 출력하기
for row in data:
    result.append(row)             # 행별로 데이터 저장하기

# result에 저장된 값 중 꽃받침과 꽃잎의 길이, 너비 값을 숫자로 바꾼 후 출력하기
for i in result:
    for j in range(1, 5):          # 두 번째 값부터 다섯 번째 값까지 실수형으로 바꾸기
        i[j] = float(i[j])
    print(i)                      # 실수형으로 바꾼 결과 출력하기

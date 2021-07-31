# 붓꽃 데이터를 불러와 출력하기

import csv

f = open('bk_ebs_ai/3-2/iris.csv')               # iris.csv 파일 열기
data = csv.reader(f)               # iris.csv 속 데이터를 data에 저장하기
result = []                         # 빈 리스트 result 만들기

# 전체 데이터를 행별로 result 리스트에 저장 및 출력하기
for row in data:
    result.append(row)             # 행별로 데이터 저장하기
    print(row)                     # 행별로 데이터 출력하기

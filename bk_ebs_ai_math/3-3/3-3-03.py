import numpy as np  # numpy 불러오기
import csv

f = open('bk_ebs_ai/3-3/temp_ice.csv',
         encoding='euc-kr')     # temp_ice.csv 파일 열기
data = csv.reader(f)         # temp_ice.csv 파일 속 데이터를 data로 저장하기
header = next(data)          # 헤더 처리
temp = []                    # 평균 기온 데이터 저장을 위한 리스트 생성하기
ice = []                     # 아이스크림 쇼핑 데이터 저장을 위한 리스트 생성하기

# 전체 데이터를 행별로 temp 리스트, ice 리스트에 저장 및 출력하기
for row in data:
    temp.append(float(row[1]))     # 행별로 평균 기온 데이터 저장하기
    ice.append(int(row[4]))        # 행별로 아이스크림/빙수 데이터 저장하기


# 평균 기온 값을 기준으로 도수분포 구간 설정하기

bins = np.arange(min(temp), max(temp), 5)
print(bins)

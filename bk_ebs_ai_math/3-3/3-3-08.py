import matplotlib.pyplot as plt
import numpy as np
import csv

f = open('bk_ebs_ai/3-3/temp_ice.csv',
         encoding='euc-kr')     # temp_ice.csv 파일 열기
data = csv.reader(f)         # temp_ice.csv 파일 속 데이터를 data로 저장하기
header = next(data)          # 헤더 처리
temp = []                    # 평균 기온 데이터 저장을 위한 리스트 생성하기
ice = []                     # 아이스크림 쇼핑 데이터 저장을 위한 리스트 생성하기

# 전체 데이터를 행별로 temp 리스트, ice 리스트에 저장 및 출력하기
for row in data:
    temp.append(float(row[1]))     # 행별로 데이터 저장하기
    ice.append(int(row[4]))        # 행별로 데이터 저장하기

# 평균 기온 값을 기준으로 도수 분포 구간 설정
bins = np.arange(min(temp), max(temp)+5, 5)     # 끝나는 값에 계급 간격만큼 더하기

# 각 계급에 해당하는 도수값 확인 후 출력하기
hist, bins = np.histogram(temp, bins)         # 히스토그램 값 계산하기


# 평균 기온값을 기준으로 아이스크림 쇼핑 클릭량을 구분하여 저장하기
ice_buy = np.zeros(7)                      # 아이스크림 쇼핑 클릭량의 합 저장할 배열 생성하기

for i in range(0, len(temp)):              # 평균 기온 데이터 전체 탐색하기
    if bins[0] <= temp[i] and temp[i] < bins[1]:       # 첫 번째 계급에 해당한다면
        # 첫 번째 배열 값에 해당 날짜 아이스크림 쇼핑 클릭량 저장하기
        ice_buy[0] = ice_buy[0] + ice[i]

    elif bins[1] <= temp[i] and temp[i] < bins[2]:     # 두 번째 계급에 해당한다면
        # 두 번째 배열 값에 해당 날짜 아이스크림 쇼핑 클릭량 저장하기
        ice_buy[1] = ice_buy[1] + ice[i]

    elif bins[2] <= temp[i] and temp[i] < bins[3]:     # 세 번째 계급에 해당한다면
        # 세 번째 배열 값에 해당 날짜 아이스크림 클릭량 저장하기
        ice_buy[2] = ice_buy[2] + ice[i]

    elif bins[3] <= temp[i] and temp[i] < bins[4]:     # 네 번째 계급에 해당한다면
        # 네 번째 배열 값에 해당 날짜 아이스크림 클릭량 저장하기
        ice_buy[3] = ice_buy[3] + ice[i]

    elif bins[4] <= temp[i] and temp[i] < bins[5]:     # 다섯 번째 계급에 해당한다면
        # 다섯 번째 배열 값에 해당 날짜 아이스크림 클릭량 저장하기
        ice_buy[4] = ice_buy[4] + ice[i]

    elif bins[5] <= temp[i] and temp[i] < bins[6]:     # 여섯 번째 계급에 해당한다면
        # 여섯 번째 배열 값에 해당 날짜 아이스크림 클릭수 저장하기
        ice_buy[5] = ice_buy[5] + ice[i]

    # 일곱 번째 계급에 해당한다면(이외의 값에 해당한다면
    else:
        # 일곱 번째 배열 값에 해당 날짜 아이스크림 클릭량 저장하기
        ice_buy[6] = ice_buy[6] + ice[i]

# 계급별 아이스크림 쇼핑 클릭량의 평균을 구하기 ------------------------------------------------------------------
# 평균 기온값 계급별 아이스크림 쇼핑 클릭량의 평균 구하기
ice_buy_a = np.zeros(7)                  # 아이스크림 쇼핑 클릭량의 합 저장할 배열 생성하기
for i in range(0, len(ice_buy)):
    ice_buy_a[i] = ice_buy[i] / hist[i]  # 계급별 아이스크림 쇼핑 클릭량 평균 구하기


# 평균 기온에 따른 아이스크림 쇼핑 클릭량의 평균을 막대그래프로 표현하기 ------------------

plt.xlabel('Average temperature')                      # x축 레이블 이름 정하기
plt.ylabel('Number of ice cream shopping')             # y축 레이블 이름 정하기
plt.bar(bins[0:7], ice_buy_a, width=2, align='edge')   # 막대 그래프 그리기
plt.xticks(bins[0:7])                                  # x축 눈금 레이블 설정하기
plt.show()

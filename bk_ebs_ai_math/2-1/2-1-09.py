import csv

a = [[], [], [], [], [], [], []]  # 7 x 24 크기의 list 이 필요

# a[i] = dictionary {num, wnum, ynum} : 요일별로 각 시간대에 저장해야 할 데이터
# csv 파일에서 데이터를 읽어서 2차원 배열 a[][] 에 넣는다.
with open('passby_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    i = j = 0
    for row in reader:
        a[i].append(row)
        j = j + 1
        if(j % 24 == 0):  # 24개 데이터 읽었으면 다음 요일로 넘어가기
            i = i + 1

# 시간대별로 주간 평균값 구하기
avgh, avghw, avghy = [], [], []
for j in range(0, 24):
    day_sum = 0
    day_wsum = 0
    day_ysum = 0

    # j번째 시간대 주간 총합
    for i in range(0, 7):
        # i번째 요일에 j번째 시간대 행인수
        day_sum = day_sum + int(a[i][j]['num'])
        # (실습) i번째 요일에 j번째 시간대 여성 행인수('wnum')
        day_wsum = day_wsum + int(a[i][j]['wnum'])
        # (실습) i번째 요일에 j번째 시간대 30대이하 행인수('ynum')
        day_ysum = day_ysum + int(a[i][j]['ynum'])

    avgh.append(day_sum/7)  # j번째 시간대 주간 행인수 평균
    # (실습) j번째 시간대 주간 여성 평균(avghw)
    avghw.append(day_wsum/7)
    # (실습) j번째 시간대 주간 30대 이하 평균 (avghy)
    avghy.append(day_ysum/7)


# 시간대별 평균 유동인구 출력하기
day_title = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
hour_title = ['01', '02', '03', '04', '05', '06',
              '07', '08', '09', '10', '11', '12',
              '13', '14', '15', '16', '17', '18',
              '19', '20', '21', '22', '23', '24', ]

print("시간대  행인수  여성  30대이하")
for j in range(0, 24):
    print("[~{0}:00]: {1:4} {2:6} {3:7}".format(
        hour_title[j], int(avgh[j]), int(avghw[j]), int(avghy[j])))

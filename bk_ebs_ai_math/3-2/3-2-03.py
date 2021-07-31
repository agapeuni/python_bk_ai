import csv

f = open('bk_ebs_ai/3-2/iris.csv')          # Iris.csv 파일 열기
data = csv.reader(f)          # Iris.csv 파일 속 데이터를 data에 저장하기
header = next(data)           # 제목을 따로 저장하기
result = []                    # 빈 리스트 result 만들기

# 전체 데이터를 행별로 result 리스트에 저장
for row in data:
    result.append(row)

# result에 저장된 값 중 꽃받침과 꽃잎의 길이, 너비 값을 숫자로 바꾸기
for i in result:
    for j in range(1, 5):     # 두 번째 값부터 다섯 번째 값까지 실수형으로 바꾸기
        i[j] = float(i[j])

# ----------------------------------------------------------------------------
# 꽃 종류별 데이터 저장하기
a = []                         # Iris-setosa 정보를 저장할 리스트 만들기
b = []                         # Iris-versicolor 정보를 저장할 리스트 만들기
c = []                         # Iris-verginica 정보를 저장할 리스트 만들기

for i in result:
    if i[5] == 'Iris-setosa':
        a.append(i[0:5])
    if i[5] == 'Iris-versicolor':
        b.append(i[0:5])
    if i[5] == 'Iris-virginica':
        c.append(i[0:5])

# iris-setosa의 꽃잎과 꽃받침 너비, 길이에 따른 평균값 구해보기
SL = []                       # 꽃받침 길이 값 저장할 리스트 만들기
SW = []                       # 꽃받침 너비 값 저장할 리스트 만들기
PL = []                       # 꽃잎 길이 값 저장할 리스트 만들기
PW = []                       # 꽃잎 너비 값 저장할 리스트 만들기

for i in a:
    SL.append(i[1])           # 꽃받침 길이의 합 구하기
    SW.append(i[2])           # 꽃받침 너비의 합 구하기
    PL.append(i[3])           # 꽃잎 길이의 합 구하기
    PW.append(i[4])           # 꽃잎 너비의 합 구하기

print('<Iris-setosa의 특성별 평균값>')          # 제목 출력
print('꽃받침 길이 평균:', round(sum(SL)/len(SL), 3), '\n꽃받침 너비 평균:', round(sum(SW)/len(SW), 3),
      '\n꽃잎 길이 평균:', round(sum(PL)/len(PL), 3), '\n꽃잎 너비 평균:', round(sum(PW)/len(PW), 3))

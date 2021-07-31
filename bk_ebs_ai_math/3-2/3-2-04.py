import csv

f = open('bk_ebs_ai/3-2/iris.csv')
data = csv.reader(f)
header = next(data)
result =[]

# 전체 데이터를 행별로 result 리스트에 저장
for row in data :
    result.append(row)

# result에 저장된 값 중 꽃받침과 꽃잎의 길이, 너비 값을 숫자로 바꾸기
for i in result :
    for j in range(1,5) :
        i[j] = float(i[j])

# 꽃 종류별 데이터 저장하기
a = []                         # Iris-setosa 정보를 저장할 리스트 만들기
b = []                         # Iris-versicolor 정보를 저장할 리스트 만들기
c = []                         # Iris-verginica 정보를 저장할 리스트 만들기

for i in result :
    if i[5]=='Iris-setosa' :
        a.append(i[0:5])
    if i[5]=='Iris-versicolor' :
        b.append(i[0:5])
    if i[5]=='Iris-virginica' :
        c.append(i[0:5])

#setosa의 꽃잎과 꽃받침 너비, 길이에 따른 평균값 구해보기
SL = []                       # 꽃받침 길이 값 저장할 리스트 만들기
SW = []                       # 꽃받침 너비 값 저장할 리스트 만들기
PL = []                       # 꽃잎 길이 값 저장할 리스트 만들기
PW = []                       # 꽃잎 너비 값 저장할 리스트 만들기

for i in a :
    SL.append(i[1])
    SW.append(i[2])
    PL.append(i[3])
    PW.append(i[4])
#---------------------------------------------------------------------
# Iris-setosa의 꽃잎과 꽃받침 길이, 너비에 따른 중앙값 구하기    

SL.sort( ) # 꽃받침 길이 정렬하기
SW.sort( ) # 꽃받침 너비 정렬하기
PL.sort( ) # 꽃잎 길이 정렬하기
PW.sort( ) # 꽃잎 너비 정렬하기
m = int(len(a)/2) # Iris-setosa의 전체 개수를 2로 나누어 중앙값 구하기

print('<Iris-setosa의 특성별 중앙값>') # 제목 출력하기
print('꽃받침 길이 중앙값:', SL[m], '\n꽃받침 너비 중앙값:', SW[m], '\n꽃잎 길이 중앙값:', PL[m], '\n꽃잎 너비 중앙값:', PW[m])
    

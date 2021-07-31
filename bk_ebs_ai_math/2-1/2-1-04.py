# 주중 유동 인구만으로 합과 평균을 구해 그래프와 함께 출력하기
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

# 은재가 조사한 일주일 간 유동 인구 데이터 (월요일 ~ 일요일)
a = [242, 256, 237, 223, 263, 81, 46]

# 한글을 출력하기 위한 폰트 로딩
rc('font', family="Malgun Gothic")

x_data = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']

# -----------------------------------------------------------
# 주중 데이터만으로 합과 평균 구하기
weekday_size = 5                           # 주중이므로 5
weekday_sum = 0                            # 합이 저장될 변수 초기화
weekday_avg = 0                            # 평균이 저장될 변수 초기화

for i in range(0, weekday_size):           # 인덱스 i는 0부터 시작하여 weekday_size번 반복하기
    weekday_sum = weekday_sum + a[i]       # 주중 유동 인구 총합 구하기

weekday_avg = weekday_sum / weekday_size   # 주중 유동 인구 평균 구하기

# 계산한 총합과 평균 출력하기
print("weekday Data = ", a[0:5])           # 주중 데이터 출력하기
print("weekday Sum : ", weekday_sum)       # 합 출력
print("weekday Average : ", weekday_avg)   # 평균 출력

# 그래프의 제목 붙이기
plt.title("주중 유동 인구수 데이터", fontsize=16)
plt.xlabel("요일", fontsize=12)
plt.ylabel("유동 인구수", fontsize=12)

# 꺽은선 그래프 그리기
plt.plot(x_data, a)
plt.scatter(x_data[0:weekday_size], a[0:weekday_size],
            c='red', edgecolor='none', s=50)

plt.show()

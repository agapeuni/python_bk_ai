# 은재가 조사한 일주일 간 유동인구 데이터 (월요일 ~ 일요일)
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

# 은재가 조사한 일주일 간 유동 인구 데이터 (월요일 ~ 일요일)
a = [242, 256, 237, 223, 263, 81, 46]

rc('font', family="Malgun Gothic")

x_data = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']

plt.title("일주일간 유동 인구수 데이터", fontsize=16)
plt.xlabel("요일", fontsize=12)
plt.ylabel("유동 인구수", fontsize=12)

plt.scatter(x_data, a)
plt.plot(x_data, a)
plt.show()

# y=f(x)형태의 함수 그려보기
# 증분을 위한 매개변수 t를 사용하여 프로그래밍함.

from matplotlib import pyplot as plt
from math import pi, sin, cos, sqrt, exp, tanh

def draw_graph(x, y, title, color, marker, linewidth):
  plt.title(title)
  plt.plot(x, y, color=color, marker=marker, linewidth=linewidth)
  plt.grid(True)          # 그래프에 격자(Grid)를 넣어 표현
  plt.show()

# frange()는 range()함수의 부동소수점수 버젼
def frange(start, final, increment=0.1):  # increament를 0.01로 하면 촘촘히 표현
  numbers = []

  while start < final:    # start:x축 최소치, final: x축 최대치
    numbers.append(start)
    start = start + increment  # 최소치에서 increment 설정치 만큼씩 증가시킴.
  return numbers

x_min = -10           # x축 최소치 설정
x_max = 10            # x축 최대치 설정
def draw_function():
  intervals = frange(x_min, x_max)
  x = []             # x축 데이터를 위한 빈 리스트를 만듦.
  y = []             # y축 데이터를 위한 빈 리스트를 만듦.

  for t in intervals:  # 아래의 두 줄이 tanh 도함수를 나타내는 방정식
    x.append(t)
    # y.append(tanh(t))  # tanh함수 그리기
    y.append((1+tanh(t))*(1-tanh(t)))  # tanh함수의 도함수 그리기

  draw_graph(x, y, title='Graph', color='red', marker='*', linewidth=2)

if __name__ == '__main__':
  try:
    draw_function()
  except KeyboardInterrupt:  # Ctr+C 를 누르면 중단
    pass
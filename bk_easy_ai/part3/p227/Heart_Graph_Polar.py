# 극좌표로 표현된 하트 방정식을 그래프로 그려보자. 
# x=16sin(t)**3, y=13cos(t)-5cos(2t)-2cos(3t)-cos(4t)
# 그래프 상에서는 옆으로 좀 퍼져있으니, 옆쪽을 좁게 하여 형태를 조절해야 한다. 

from matplotlib import pyplot as plt
from math import pi, sin, cos

def draw_graph(x, y, title, color):
  plt.title(title)
  plt.plot(x, y, color=color)
  plt.show()

# frange()는 range()함수의 부동소수점 버전
def frange(start, final, increment=0.01):
  numbers = []

  while start < final:
    numbers.append(start)
    start = start + increment

  return numbers

def draw_heart():
  intervals = frange(0, 2 * pi)
  x = []
  y = []

  for t in intervals:  # 아래의 두줄이 하트 모양을 나태내는 방정식
    x.append(16 * sin(t) ** 3)
    y.append(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))

  draw_graph(x, y, title='HEART', color='#FF6597')

if __name__ == '__main__':
  try:
    draw_heart()
  except KeyboardInterrupt:
    pass
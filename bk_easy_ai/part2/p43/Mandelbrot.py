import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize              # color map 조작을 위해 필요
from numba import jit                                # 계산시간 단축을 위해 필요
import time                                          # 계산시간을 보기 위해 필요
 
t0 = time.time()
 
@jit                                                 # Numba에 의한 Just In Time Compile을 실행
def mandelbrot(c_real, c_imag, n_max):
    Re, Im = np.meshgrid(c_real, c_imag)             # Re(실수부)과 Im(허수부)의 조합을 계산
    n_grid = len(Re.ravel())                         # 조합의 총수
    z = np.zeros(n_grid)                             # 망델브로 집합 데이터의 저장용 빈 배열
 
    # z가 망델브로 집합에 속하는지 속하지 않는지를 판별하고, 결과 데이터를 저장하기 위한 반복문
    for i in range(n_grid):
        c = complex(Re.ravel()[i], Im.ravel()[i])    # 복소수c를 정의
 
        # 반복회수n과 복소수z0을 초기화
        n = 0
        z0 = complex(0, 0)
 
        # z0가 무한대 또는 최대 반복횟수가 될 때까지 루프를 반복
        while np.abs(z0) < np.inf and not n == n_max:
            z0 = z0 ** 2 + c                         # 점화식(수열) 계산
            n += 1                                   # 반복 횟수를 1씩 늘려감
 
        # z0가 무한대로 발산하는 경우는 n, 수렴하는 경우는 0을 저장
        if n == n_max:
            z[i] = 0
        else:
            z[i] = n
 
        # 계산 진척도를 모니터링(매번 보여주면 계산이 느려지기 때문)
        if i % 100000 == 0:
            print(i, '/',n_grid, (i/n_grid)*100)
    z = np.reshape(z, Re.shape)      # 2차원 배열(이미지 표시용)으로 reshape
    z = z[::-1]                      # imshow() 실행시 이미지가 뒤집히므로, 미리 상하 반전시켜 놓음
    return z
 
# 수평방향 h(실수부 Re)와 수직방향 v(허수부 Im)의 범위를 정함
h1 = -2               # 망델브로 집합 전체를 보여줌
h2 = 0.5              # 망델브로 집합 전체를 보여줌
v1 = -1.2             # 망델브로 집합 전체를 보여줌
v2 = 1.2              # 망델브로 집합 전체를 보여줌

# h1 = -1.8   # 망델브로 집합의 왼쪽 가운데 부분(작은 망델브로가 보이는 부분)을 zoom up하여 보여줌
# h2 = -1.6   # 망델브로 집합의 왼쪽 가운데 부분(작은 망델브로가 보이는 부분)을 zoom up하여 보여줌
# v1 = -0.1   # 망델브로 집합의 왼쪽 가운데 부분(작은 망델브로가 보이는 부분)을 zoom up하여 보여줌
# v2 = 0.1    # 망델브로 집합의 왼쪽 가운데 부분(작은 망델브로가 보이는 부분)을 zoom up하여 보여줌

# h1 = -1.78373        # 위의 일부분을 더욱 확대하여 보여줌
# h2 = -1.77685        # 위의 일부분을 더욱 확대하여 보여줌
# v1 = -0.00334008     # 위의 일부분을 더욱 확대하여 보여줌
# v2 = 0.0040149       # 위의 일부분을 더욱 확대하여 보여줌
 
# 분해능(resolution) 설정
resolution = 4000
 
# 실수부와 허수부의 축 데이터 배열 및 최대 반복 횟수를 설정
c_real = np.linspace(h1, h2, resolution)
c_imag = np.linspace(v1, v2, resolution)
n_max = 100
 
# 함수를 실행하여 이미지를 획득
z = mandelbrot(c_real, c_imag, n_max)
 
t1 = time.time()
print('Calculation time=', float(t1 - t0), '[s]')
 
 
##########  여기부터는 그래프 이미지 표시 부분 ##########
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Re')
ax1.set_ylabel('Im')
 
mappable = ax1.imshow(z, cmap='jet',
                      norm=Normalize(vmin=0, vmax=n_max),
                      extent=[h1, h2, v1, v2])
 
cbar = plt.colorbar(mappable=mappable, ax=ax1)
cbar.set_label('Iteration until divergence')
cbar.set_clim(0, n_max)
plt.tight_layout()
plt.show()
plt.close()
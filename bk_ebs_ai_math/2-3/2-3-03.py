# 생성한 소리 데이터를 wav 형식의 파일로 저장하기

import numpy as np                             # 행렬 및 벡터 데이터 관리를 위한 numpy 모듈
import matplotlib.pyplot as plt                # 소리 데이터의 그래프 표현을 위한 모듈
from scipy.io.wavfile import write             # wav 형식으로 소리 데이터를 저장하기 위한 모듈
import os                                      # wav 파일을 시스템 명령어로 재생하기 위한 모듈

# sampling rate
# 정보 샘플링 주기, 1초에 44100개의 샘플링, 단위는 Hz(주파수)
Fs = 44100.0

# 1초 데이터 생성을 위한 환경 변수 설정
tlen = 1                                       # 1초로 초기화
Ts = 1/Fs                                      # 샘플링 사이의 간격(시간) 계산
t = np.arange(0, tlen, Ts)                     # 소리 데이터를 생성할 시간 성분으로 구성된 배열로
# [0, 1] 사이를 TimeStamp의 간격으로 분할하여
# Fs 개의 데이터를 담을 수 있는 배열 t를 생성

# 시그널 생성하기
sin_freq = 440                                 # sin 곡선의 주기
# t 배열의 각 성분값에 sin 주기를 라디안 단위로 변환한 src 배열을 준비
src = 2*np.pi*sin_freq*t
# timestamp를 각으로 변환한 src 배열에 맞게 sin 데이터를 변환
signal = np.sin(src)

# -------------------------------------------------------------------------------
# sin 함수로 생성한 음성 데이터를 wav 형식의 파일로 저장
scaled = np.int16(signal/np.max(np.abs(signal)) * 32767)
write('bk_ebs_ai/2-3/snd_signal2.wav', 44100, scaled)

import librosa
import librosa.display
import numpy as np

# 입력변수와 출력변수 생성하기

X_train=np.zeros((40,20))                # 입력변수 생성
y_train=np.zeros(40)                     # 출력변수 생성

#인덱스번호 0~19번까지는 레이블 1(배고픔), 21~40번까지는 레이블 0(웃음)
y_train[0:20] = 1

# hungry_특징추출  
for i in range(20):
  audio_path = 'hungry/hungry_'+str(i+1)+'.wav'
  y, sr = librosa.load(audio_path)
  mfcc= librosa.feature.mfcc(y=y, sr=sr)
  temp=mfcc.mean(axis=1)
  X_train[i]=temp                       # 인덱스번호 0~19번까지 

# laugh_특징추출  
for i in range(20):
  audio_path = 'laugh/laugh_'+str(i+1)+'.wav'
  y, sr = librosa.load(audio_path)
  mfcc= librosa.feature.mfcc(y=y, sr=sr)
  temp=mfcc.mean(axis=1) 
  X_train[i+20]=temp                   # 인덱스번호 20~39번까지

# 추출한 특성 값들을 데이터 셋으로 묶기

# 데이터 셋
data_sets=np.zeros((40,21))
data_sets[:,0:20]=X_train
data_sets[:,20]=y_train


# 5-2. 학습 데이터 특성 시각화하기
# 시도2_기울기의 변화량만을 수집
def AccumAscentCurv(A):
  accVal=0
  for i in range(len(A)-1):
    accVal = accVal + abs(A[i+1]-A[i])
  return accVal

X = [AccumAscentCurv(X_train[i]) for i in range(40)]
y = y_train

import matplotlib.pyplot as plt
plt.scatter(X, y)
plt.show()


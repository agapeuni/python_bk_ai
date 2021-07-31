import librosa
import librosa.display
import numpy as np


#import matplotlib.pyplot as plt

# 입력변수와 출력변수 생성하기

X_train=np.zeros((40,20))                # 입력변수 생성
y_train=np.zeros(40)                     # 출력변수 생성

#인덱스번호 0~19번까지는 레이블 1(배고픔), 21~40번까지는 레이블 0(웃음)
y_train[0:20] = 1

# hungry_특징추출  
for i in range(20):
  audio_path = 'bk_ebs_ai/3-4/hungry/hungry_'+str(i+1)+'.wav'
  y, sr = librosa.load(audio_path)
  mfcc= librosa.feature.mfcc(y=y, sr=sr)
  temp=mfcc.mean(axis=1)
  X_train[i]=temp                       # 인덱스번호 0~19번까지 

# laugh_특징추출  
for i in range(20):
  audio_path = 'bk_ebs_ai/3-4/laugh/laugh_'+str(i+1)+'.wav'
  y, sr = librosa.load(audio_path)
  mfcc= librosa.feature.mfcc(y=y, sr=sr)
  temp=mfcc.mean(axis=1) 
  X_train[i+20]=temp                   # 인덱스번호 20~39번까지

# 추출한 특성 값들을 데이터 셋으로 묶기

# 데이터 셋
data_sets=np.zeros((40,21))
data_sets[:,0:20]=X_train
data_sets[:,20]=y_train


def AccumAscentCurv(A):
  accVal=0
  for i in range(len(A)-1):
    accVal = accVal + abs(A[i+1]-A[i])
  return accVal

X = [AccumAscentCurv(X_train[i]) for i in range(40)]
y = y_train

# 데이터 준비하기
X=np.array(X).reshape(40,1)
y=y.reshape(40,1)

print(X[:5])
print(y[:5])

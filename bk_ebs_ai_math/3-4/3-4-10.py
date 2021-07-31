import librosa
import librosa.display
import numpy as np


# 입력 변수와 출력 변수 생성하기
 
X_train=np.zeros((40,20))                # 입력 변수 생성
y_train=np.zeros(40)                     # 출력 변수 생성

#인덱스 번호 0~19번까지는 레이블 1(배고픔), 21~40번까지는 레이블 0(웃음)
y_train[0:20] = 1

# hungry_특징 추출  
for i in range(20):
  audio_path = 'bk_ebs_ai/3-4/hungry/hungry_'+str(i+1)+'.wav'
  y, sr = librosa.load(audio_path)
  mfcc= librosa.feature.mfcc(y=y, sr=sr)
  temp=mfcc.mean(axis=1)
  X_train[i]=temp                       # 인덱스 번호 0~19번까지 

# laugh_특징 추출  
for i in range(20):
  audio_path = 'bk_ebs_ai/3-4/laugh/laugh_'+str(i+1)+'.wav'
  y, sr = librosa.load(audio_path)
  mfcc= librosa.feature.mfcc(y=y, sr=sr)
  temp=mfcc.mean(axis=1) 
  X_train[i+20]=temp                   # 인덱스 번호 20~39번까지

# 추출한 특성 값들을 데이터 셋으로 묶기

#데이터 셋
data_sets=np.zeros((40,21))
data_sets[:,0:20]=X_train
data_sets[:,20]=y_train

# csv 모듈을 이용하여 파일로 추출하기

#데이터 셋 csv로 추출
import csv
with open('baby_cry.csv', 'w') as f:
    writer = csv.writer(f)
    for i in range(40):
        writer.writerow(data_sets[i,:])

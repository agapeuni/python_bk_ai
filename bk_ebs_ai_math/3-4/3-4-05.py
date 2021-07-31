import librosa
import librosa.display
import matplotlib.pyplot as plt

# 하나의 그래프에 여러 개의 소리 데이터 표현_discomfort
folder = ['discomfort', 'hungry', 'laugh', 'tired']   # 폴더 이름 저장하기
set_label=[]                                          # 레이블 이름을 folder 리스트에 저장하기

for i in range(1,11):
    a = folder[0]+'/'+folder[0]+'_'+str(i)+'.wav'
    y, sr = librosa.load(a)
    librosa.display.waveplot(y, sr=sr, alpha=0.5)   # 그래프로 표현하기
    set_label.append(i)                             # 라벨 이름 저장하기  
    
plt.legend(set_label)                               # 그래프 범례 생성하기
plt.title(folder[0])                                # 그래프 제목 설정하기
plt.xlabel("Time(ms)")                              # 그래프 x축 라벨 설정하기
plt.ylabel("Sound(dB)")                             # 그래프 y축 라벨 설정하기
plt.show()                                          # 그래프 출력

import librosa
import librosa.display
import matplotlib.pyplot as plt

# 하나의 그래프에 여러 개의 소리 데이터 표현-4가지 상황
folder = ['discomfort', 'hungry', 'laugh', 'tired']
set_label=[]

# 하나의 그래프에 여러 개의 소리 데이터 표현-4가지 상황
for i in range(0,4):
    plt.subplot(4,1,i+1)
    a = folder[i]+'/'+folder[i]+'_1.wav'
    y, sr = librosa.load(a)
    librosa.display.waveplot(y, sr=sr)
    plt.title(folder[i])
plt.tight_layout()
plt.show() 

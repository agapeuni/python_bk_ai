import librosa
import librosa.display
import matplotlib.pyplot as plt

folder = ['discomfort', 'hungry', 'laugh', 'tired']    #하나의 plot 생성_waveplot_discomfort
set_label=[]

# 하나의 그래프에 여러 개의 소리 데이터 표현-discomfort-화면 분할
for i in range(1,10):
    plt.subplot(3,3,i)
    a = folder[0]+'/'+folder[0]+'_'+str(i)+'.wav'
    y, sr = librosa.load(a)
    librosa.display.waveplot(y, sr=sr)
    plt.title(folder[0]+str(i))
plt.tight_layout()
plt.show() 

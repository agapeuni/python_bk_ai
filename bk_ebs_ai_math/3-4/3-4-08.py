import librosa
import librosa.display
import matplotlib.pyplot as plt


folder = ['discomfort', 'hungry', 'laugh', 'tired']
set_label=[]


# 하나의 그래프에 여러 개의 소리 데이터 표현-4가지 상황, 동일 시간
for i in range(0,4):
    plt.subplot(4,1,i+1)
    a = folder[i]+'/'+folder[i]+'_1.wav'
    y, sr = librosa.load(a)
    librosa.display.waveplot(y[:100000], sr=sr) # 그래프로 표현하기
    plt.title(folder[i])                        # 개별 그래프 제목 설정하기
plt.tight_layout()
plt.show()


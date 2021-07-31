import librosa
import librosa.display
import matplotlib.pyplot as plt         # 그래프를 출력하기 위한 모듈

# waveplot
audio = 'bk_ebs_ai/3-4/discomfort/discomfort_1.wav'   # 소리 파일 경로 지정하기
y, sr = librosa.load(audio)             # 소리 파일 불러오기

librosa.display.waveplot(y, sr=sr)      # 소리 데이터를 그래프로 표현하기
plt.title('Waveplot')                   # 그래프 제목 설정하기
plt.show()                              # 그래프 출력

import librosa
import librosa.display

audio = 'bk_ebs_ai/3-4/discomfort/discomfort_1.wav'    #소리 파일 경로 지정하기
y, sr = librosa.load(audio)                 #소리 파일 불러오기
print(y)
print(sr)

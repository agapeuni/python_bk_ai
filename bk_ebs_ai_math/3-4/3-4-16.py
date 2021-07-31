import librosa

# test data 준비하기
audio_path = 'bk_ebs_ai/3-4/test01.wav'
y, sr = librosa.load(audio_path)
mfcc = librosa.feature.mfcc(y=y, sr=sr)
X_test = mfcc.mean(axis=1)

print(X_test)

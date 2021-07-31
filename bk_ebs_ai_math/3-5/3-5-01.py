# 데이터 불러오기
import pandas as pd

df_train = pd.read_csv('fashion-mnist_train.csv') #훈련 데이터 파일 열기
df_test = pd.read_csv('fashion-mnist_test.csv')   #테스트 데이터 파일 열기

print(df_train.info(),'\n')
print(df_test.info(),'\n')
print(df_train.shape,'\n')
print(df_test.shape,'\n')


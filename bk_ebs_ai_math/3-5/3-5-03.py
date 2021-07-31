# 데이터 불러오기
import pandas as pd

df_train = pd.read_csv('fashion-mnist_train.csv') #훈련 데이터 파일 열기
df_test = pd.read_csv('fashion-mnist_test.csv')   #테스트 데이터 파일 열기


# 데이터 다루기
import numpy as np

# 데이터 프레임을 배열 형태로 저장하기
data_train = np.array(df_train,dtype=np.float32) # 훈련 데이터를 배열로 저장
x_train = data_train[:, 1:]     # 훈련 데이터의 각 행별 픽셀 값 저장
y_train = data_train[:, 0]      # 훈련 데이터의 각 행별 레이블 저장


# 데이터를 활용하여 바지 이미지 출력하기
import matplotlib.pyplot as plt
# 의류 종류 레이블을 딕셔너리로 저장
label_dictionary = {0:'T-shirt/top', 1:'Trouser', 2:'Pullover',\
                    3:'Dress', 4:'Coat', 5:'Sandal', 6:'Shirt',\
                    7:'Sneaker', 8:'Bag', 9:'Ankle boot' }
i = 109
plt.imshow(x_train[i].reshape(28,28), cmap='gray')
plt.colorbar()
plt.title("Label {}, {}".format(y_train[i], label_dictionary[y_train[i]]))
plt.show()

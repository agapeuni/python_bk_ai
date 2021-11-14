import tensorflow as tf                    # tensorflow를 tf라는 이름으로 import함.
from keras import datasets, layers, models # 신경망 구성을 위해 keras를 import함.
import matplotlib.pyplot as plt            # 이미지를 보여주거나 그래프를 그리기 위한 모듈
import numpy as np                         # 다양한 수학적 처리를 위해 import

(train_images, train_labels), (test_images, test_labels)=datasets.mnist.load_data() 
# MNIST 데이터셋을 가지고 와서 (학습 이미지, 정답), (테스트 이미지, 정답)으로 나누어 줌.
train_images=train_images.reshape((60000, 28, 28, 1))  
# 학습용 : 6만 장을 batch size로 묶어 한꺼번에 처리, 28x28 크기, channel은 1이므로 흑백 이미지
test_images=test_images.reshape((10000, 28, 28, 1))
# 테스트용 : # 만 장을 batch size로 묶어 한꺼번에 처리, 28x28 크기, channel은 1이므로 흑백 이미지  
train_images, test_images=train_images/255, test_images/255 
# RGB값 0~255를 0과 1사이로 표현해야 되므로 255로 나누어 정규화를 함.  

################ Feature Extraction <Convolution Block> #################
model=models.Sequential()  # 신경망 모델을 만들고, 신경망을 순차적으로 연결해 줌.
model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)))
# 32는 필터의 개수, (3,3)은 필터(마스크) 사이즈, 활성 함수는 reLU 사용, 이미지의 사이즈는 28x28, 흑백(1)
model.add(layers.MaxPooling2D((2,2)))  # 풀링 계층을 추가해 줌. (2,2) 사이즈마다 최대치 추출
model.add(layers.Dropout(0.25))     # dropout을 통해 25% 이내의 범위에서 연결을 끊음.
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.Dropout(0.25))     # 25% 이내에서 연결을 끊음.  

################## Fully Connected NN <Neual Net Block> ###################
model.add(layers.Flatten())         # 최종 출력된 이미지 배열을 평탄화해 입력해 줌.
model.add(layers.Dense(64, activation='relu'))     # 은닉층, 노드 개수는 64
model.add(layers.Dense(10, activation='softmax'))  # softmax를 써서 확률값으로 출력

##########################  <Optimization Block>  ##########################
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']) 
# 최적화를 위해 adam을 사용. 손실함수로 cross entropy를 사용, 평가지표는 Accuracy(정확도)
model.fit(train_images, train_labels, epochs=1)   # dropout을 안하고 epoch를 1번만 했음
# fit 함수를 통해 훈련(이미지 학습)을 시킴, epoch는 일단 1회로 설정

##########################  Image Test #####################
test_image=test_images[463, :, :, 0]   # 테스트 이미지의 번호 (463은 464번째 이미지)
plt.title("Number of the Image: {}".format(test_labels[463]))
plt.imshow(test_image)  # 테스트 이미지(여기서는 464번째 이미지)를 보여줌. 
plt.show()   # 464번째 수가 6이라는 것과 정답이 6이라는 것을 확인할 수 있음

##########################  Prediction with Probability ######################
pred=model.predict(test_image.reshape(1, 28, 28, 1)) # 예측을 위해 (batch size, height, width, channel)형태로 바꾸어 줌.
pred.shape
print(pred)   # 0-9까지의 확율이 list배열 형태로 표시, 7번째(숫자 6을 의미)의 확률이 가장 높음.
num=np.argmax(pred) # numpy모듈의 argmax함수를 통해 가장 확률이 높은 번호를 가지고 옴.
print("예측값: {}".format(num))  # 예측된 숫자를 표시해 줌.
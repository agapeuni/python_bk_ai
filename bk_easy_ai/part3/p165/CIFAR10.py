import tensorflow as tf
from keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
(train_images, train_labels), (test_images,
                               test_labels) = datasets.cifar10.load_data()
# train_images=train_images.reshape((60000, 32, 32, 3))
# test_images=test_images.reshape((10000, 32, 32, 3))
train_images, test_images = train_images/255, test_images/255
################ Feature Extraction <Convolution Block> #################
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.25))     # 25%의 연결을 끊음.
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Dropout(0.25))     # 25%의 연결을 끊음.
################## Fully Connected NN <Neual Net Block> ###################
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
##########################  <Optimization Block>  ##########################
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=3)
##########################  Batch Image Test #####################
test_batch = test_images[:31]   # 0에서 31까지의 총 32개의 이미지를 한꺼번에 테스트
print(test_batch.shape)       # shape이 (31, 32, 32, 3)임을 확인
##########################  Prediction with Probability ######################
pred = model.predict(test_batch)
print(pred.shape)    # 32개의 테스트 이미지와 10개의 정답(출력)으로 구성됨.
numbers = np.argmax(pred, -1)  # -1은 여러 개의 예측을 동시에 표시하기 위한 것
print("패널들의 그림번호 예측: {}".format(numbers))
# 0:비행기(plane)   1:자동차(car)    2:새(bird)   3:고양이(cat)  4:사슴(deer)
# 5:개(dog)     6:개구리(frog)   7:말(horse)  8:배(boat)     9:트럭(truck)

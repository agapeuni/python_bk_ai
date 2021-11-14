# CNN을 쓰지 않고 일반 Neural Net만으로 학습, 학습 속도는 빠르나 정확도가 떨어지므로 여러 번 학습해야 함.
# from __future__ import absolute_import, division, print_function, unicode_literals, unicode_literals
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
 
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# plt.figure()              # 주석문 해제하여 0번 이미지 확인
# plt.imshow(train_images[0])
# plt.colorbar()
# plt.grid(True)
# plt.show()
train_images = train_images / 255.0   # train_images, test_images=train_images/255, test_images/255 으로 표현해도 됨.
test_images = test_images / 255.0
# plt.figure(figsize=(10,10))         # 주석문 해제하여 0-25번 까지의 이미지 확인
# for i in range(25):        
#     plt.subplot(5,5,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[i], cmap=plt.cm.binary)
#     plt.xlabel(class_names[train_labels[i]])
# plt.show()

model = keras.Sequential([                 # 숫자 MINIST 코드와 비교 바람, 같은 것인데 표현이 조금 다름.
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5)

# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)  # 주석 해제하여 학습 정확도 확인
# print('\n테스트 정확도:', test_acc)

predictions = model.predict(test_images)
test_no=3
print(predictions[test_no])                                                   # 예측치를 확률로 표시
print("예측 이미지의 번호: {}".format(np.argmax(predictions[test_no])))         # 예측치를 숫자로 표시
print("실제 이미지의 번호: {}".format(test_labels[test_no]))

# 그래프로 표현하여 가시화 작업 해보기
def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')
# 0번째 이미지의 예측 신뢰도 점수 배열, 레이블이 올바르게 에측되면 파랑, 아니면 빨강
i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)
plt.show()
# 12번째 이미지의 예측 신뢰도 점수 배열
i = 12
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)
plt.show()

# 처음 X 개의 테스트 이미지와 예측 레이블, 진짜 레이블을 출력
# 올바른 예측은 파랑색으로 잘못된 예측은 빨강색으로 나타남
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions, test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions, test_labels)
plt.show()

# 훈련된 모델을 이용한 이미지 예측 (테스트 세트에서 이미지 하나를 선택)
# img = test_images[0]      # 0번 이미지
# img = (np.expand_dims(img,0))  # (28,28)에서 (1, 28, 28)로 배치 사이지의 차원을 추가
# predictions_single = model.predict(img)
# print(predictions_single)
# plot_value_array(0, predictions_single, test_labels)
# _ = plt.xticks(range(10), class_names, rotation=45)
# np.argmax(predictions_single[0])
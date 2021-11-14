# 국화, 민들레, 장미, 해바라기, 튤립 훈련(사진의 크기, 이름 상관없음)
from keras.callbacks import ModelCheckpoint, EarlyStopping, CSVLogger
import os
from glob import glob
import numpy as np
import tensorflow as tf
from keras import datasets, layers, models
from PIL import Image
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator

train_dir = 'D:/github/python_bk_ai/bk_easy_ai/dataset/train'   # 자신의 PC상의 폴더 경로로 변경하기
test_dir = 'D:/github/python_bk_ai/bk_easy_ai/dataset/test'     # 자신의 PC상의 폴더 경로로 변경하기

###################### Hyperparameter Tuning ####################
num_epoch = 30                           # 훈련 학습 횟수
batch_size = 16                          # 이미지의 묶음, 고해상도 사진일수록 작게 하기
learning_rate = 0.001                    # 학습률, 작을수록 학습 정확도 올라감.
dropout_rate = 0.3                       # 30%의 신경망 연결을 의도적으로 끊음. 과적합 방지용
input_shape = (50, 50, 3)                # 원하는 크기를 입력하면 모든 입력 이미지가 resize됨.
num_class = 5                            # 분류를 위한 정답의 개수 지정

########################## Preprocess ############################
train_datagen = ImageDataGenerator(       # Datagenerator로 이미지를 변환시킴.
    rescale=1./255.,                      # 이미지 데이터의 정규화
    width_shift_range=0.3,                # 이미지 폭을 30%이내에서 임으로 변경
    zoom_range=0.2,                       # 20% 이내에서 임의로 축소/확대
    horizontal_flip=True,                 # 이미지를 위 아래로 뒤집음.
    validation_split=0.2                  # train을 8대2로 나누어 train과 val로 사용
)
test_datagen = ImageDataGenerator(        # 테스트 이미지의 스케일에 맞추어 줄 것
    rescale=1./255.,
)

train_generator = train_datagen.flow_from_directory(     # DataGenerator를 통해 데이터를 Load할 수도 있음.
    train_dir,
    target_size=input_shape[:2],      # 이미지의 크기만 가지고 옴(50, 50, 3)->(50,50)
    batch_size=batch_size,
    color_mode='rgb',
    class_mode='categorical',         # 다분류의 경우, 2진 분류의 경우는 Binary로 설정
    subset='training',                # train 데이터
)                                     # Found 60000 images belonging to 10 classes.라 표시됨을 확인

validation_generator = train_datagen.flow_from_directory(   # DataGenerator를 통해 데이터를 Load할 수도 있음.
    train_dir,
    target_size=input_shape[:2],
    batch_size=batch_size,
    color_mode='rgb',
    class_mode='categorical',
    subset='validation'  # val 데이터
)                        # validation_Generator는 학습이 잘되고 있는지 확인을 위해 필요, 생략 가능

############### Feature Extraction <Convolution Block> ##############
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(dropout_rate))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(dropout_rate))

################ Fully Connected NN <Neual Net Block> ################
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dropout(dropout_rate))
model.add(layers.Dense(num_class, activation='softmax'))

########################  Optimization Block  ########################
model.compile(optimizer=tf.optimizers.Adam(learning_rate),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

##############################  Callback  #############################

checkpoint = ModelCheckpoint(
    'weights/best.h5', monitor='val_accuracy', save_best_only=True)
# 학습 중 모델을 저장하기. acc가 향상된 경우만 저장하기

earlystopping = EarlyStopping(monitor='val_accuracy', patience=20)
# 학습 도중 val_acc가 향상되지 않으면 종료하기

logger = CSVLogger('bk_easy_ai/weights/history.csv')
# 학습 과정 loss, acc 등을 저장하기

os.makedirs('bk_easy_ai/weights/', exist_ok=True)
callbacks = [checkpoint, earlystopping, logger]

###########################  Training Block  ##########################
hist = model.fit_generator(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=num_epoch,
    callbacks=callbacks,
    validation_data=validation_generator,      # Label된 testset이 없는 경우 생략하는 것이 맞음
    # Label된 testset이 없는 경우 생략하는 것이 맞음
    validation_steps=len(validation_generator)
)

model.save('bk_easy_ai/weights/last.h5')  # 학습된 모델 저장하기

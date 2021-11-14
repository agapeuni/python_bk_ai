from keras.models import load_model
import tensorflow as tf
from glob import glob
import numpy as np
import matplotlib.pyplot as plt

# 테스트 이미지 경로, 자신의 PC에 맞추어 변경하기
data_path = glob('D:/github/python_bk_ai/bk_easy_ai/dataset/test/*.jpg')

########################  load trained model ####################
path_model = 'bk_easy_ai/weights/best.h5'  # 학습된 모델이 저장된 경로
model = load_model(path_model)  # 학습된 모델 불러오기

########################  Prediction with Probability ####################
np.random.shuffle(data_path)        # shuffle을 이용하여 이미지 경로를 임의로 섞기
input_shape = (50, 50, 3)


def read_image(path):               # 이미지를 읽어 오기 위한 함수 만들기
    gfile = tf.io.read_file(path)     # 경로상의 하나의 이미지를 읽어 들여 gfile 변수에 보관
    image = tf.io.decode_image(
        gfile, dtype=tf.float32)  # 읽은 이미지를 디코딩 -> 이미지 배열
    return image


for test_no in range(5):       # 테스트할 이미지의 번호
    path = data_path[test_no]     # test_no+1번째 파일의 경로

    img = read_image(path)
    img = tf.image.resize(img, input_shape[:2])  # 이미지의 크기를 입력 이미지에 맞춤.

    image = np.array(img)          # imshow를 통한 이미지 확인을 위해, 저장된 이미지를 배열 형태로 바꿈.
    # print(image.shape)         # 배열 형태로 만들어 졌기 떄문에 형태 확인 가능. shape이 (50,50,3)임을 확인
    plt.imshow(image)
    plt.title('Check the Image and Predict Together!')
    plt.show()

    # 테스트 이미지 shape을 (50, 50) -> (1, 50, 50, 3) 로 만들어 줌
    test_image = image[tf.newaxis, ...]
    pred = model.predict(test_image)

    print(pred)                           # test_no번째의 이미지를 예측하여 확률분포로 보여줌
    num = np.argmax(pred)                   # 확률분포중 가장 큰 값을 찾아 숫자로 표시

    if num == 0:
        print("국화..인것 같네요^^")
    elif num == 1:
        print("민들레..인것 같네요^^")
    elif num == 2:
        print("장미..인것 같네요^^")
    elif num == 3:
        print("해바라기..인것 같네요^^")
    elif num == 4:
        print("튤립..인것 같네요^^")
    else:
        print("전혀 모르겠어요 ㅠㅠ")

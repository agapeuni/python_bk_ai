import matplotlib.pyplot as plt
from keras import datasets
cf=datasets.cifar10
(x_train, y_train), (x_test, y_test)=cf.load_data()

start_no_pannel=0   # CIFAR10.py에서 추측한 숫자들을 no_pannel숫자를 바꾸어 가며 확인해 볼것
finish_no_pannel=5
for i in range(start_no_pannel, finish_no_pannel):
    plt.title("<Number:{}>".format(y_test[i]))
    plt.imshow(x_test[i])
    plt.show()
    
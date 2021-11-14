# python 3.7.7
# py -m pip install pyserial
# py -m pip install PyQt5

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QStackedWidget
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import Qt, QSize

from modules import communication, widget, neuralNetwork, xylobot

class MainWindow(QMainWindow):

    def __init__(self, title_name, icon_path, size):
        super().__init__()
        self.title = title_name
        self.icon = QIcon(icon_path)
        self.size = size

        self.xylobot = communication.ComPort()
        self.parameter = xylobot.Parameters()
        self.ann = neuralNetwork.ANN(input_node=2, hidden_node=4, output_node=2, axis=4)

        self.input_data = [[50, 350], [350, 350], [350, 50], [50, 50]]  # 13_view.png 이미지 내의 목표점 좌표 픽셀
        self.target_data = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.target_original_data = [[12.00, 51.00], [-12.00, 51.00], [-12.00, 25.00], [12.00, 25.00]]
        self.normalize_input_data = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.normalize_target_data = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.MAIN11 = 0
        self.MAIN12 = 1
        self.MAIN13 = 2
        self.MAIN14 = 3

        self.initUI()
        self.openXylobot()

    
    def initUI(self):
        self.stack_widget = QStackedWidget(self)
        self.stack_widget.addWidget(widget.Main11(self))
        self.stack_widget.addWidget(widget.Main12(self))
        self.stack_widget.addWidget(widget.Main13(self))
        self.stack_widget.addWidget(widget.Main14(self))
        self.setCentralWidget(self.stack_widget)
        
        back_img = QImage('image/main_background.png')
        background = QPalette()
        background.setBrush(10, QBrush(back_img))
        self.setPalette(background)

        self.statusBar().showMessage('Ready')
        self.statusBar().setStyleSheet(
            'color: black;'
            'font: bold 20px Tahoma;'
            )

        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)
        self.setGeometry(150, 60, self.size[0], self.size[1])
    
    def openXylobot(self):
        self.xylobot.open()
        if self.xylobot.is_connected == True:
            self.statusBar().setStyleSheet(
                'color: black;'
                'font: bold 20px Tahoma;'
                )
            self.statusBar().showMessage('Com port : Connected')
        else:
            self.statusBar().setStyleSheet(
                'color: red;'
                'font: bold 20px Tahoma;'
                )
            self.statusBar().showMessage('Com port : Connection failure')

    def closeEvent(self, event):
        self.xylobot.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow('ANN', 'icon/xylobot_16x16.png', (1600, 900))    
    form.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QRect, Qt, QMetaObject, QCoreApplication, QSize, pyqtSignal, QObject
from PyQt5.QtGui import QImage, QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QCheckBox, QMenuBar, QApplication, \
    QTextEdit, QPlainTextEdit, QMenu, QAction
import cv2


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        self.camera_on = False
        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer(self)

        MainWindow.resize(1059, 550)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.question_title = QLabel(self.centralwidget)

        self.question_title.setObjectName(u"question_title")
        self.question_title.setGeometry(QRect(40, 50, 271, 61))
        font = QFont()
        font.setPointSize(17)
        self.question_title.setFont(font)
        self.question_title.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.question_title.setAlignment(Qt.AlignCenter)
        self.question_text = QTextEdit(self.centralwidget)
        self.question_text.setObjectName(u"question_text")
        self.question_text.setGeometry(QRect(40, 120, 271, 141))
        font1 = QFont()
        font1.setPointSize(14)
        self.question_text.setFont(font1)
        self.question_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.camera_label = QLabel(self.centralwidget)
        self.camera_label.setObjectName(u"camera_label")
        self.camera_label.setGeometry(QRect(330, 180, 471, 271))
        self.camera_label.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.save_answers = QPushButton(self.centralwidget)
        self.save_answers.setObjectName(u"next_btn")
        self.save_answers.setGeometry(QRect(40, 460, 271, 51))
        self.save_answers.clicked.connect(self.set_right_answers)
        font2 = QFont()
        font2.setPointSize(12)
        self.save_answers.setFont(font2)

        self.use_camera_text = QLabel(self.centralwidget)
        self.use_camera_text.setObjectName(u"use_camera_text")
        self.use_camera_text.setGeometry(QRect(330, 50, 471, 121))
        self.use_camera_text.setFont(font)
        self.use_camera_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.use_camera_text.setAlignment(Qt.AlignCenter)
        self.use_camera_text.setWordWrap(True)

        self.turn_on_camera = QPushButton(self.centralwidget)
        self.turn_on_camera.setObjectName(u"check_answer_btn")
        self.turn_on_camera.setGeometry(QRect(330, 460, 471, 51))
        self.turn_on_camera.setFont(font2)
        self.turn_on_camera.clicked.connect(self.use_camera)

        self.results_text = QLabel(self.centralwidget)
        self.results_text.setObjectName(u"results_text")
        self.results_text.setGeometry(QRect(820, 50, 191, 61))
        self.results_text.setFont(font)
        self.results_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.results_text.setAlignment(Qt.AlignCenter)
        self.results_text.setWordWrap(True)
        self.results_label = QLabel(self.centralwidget)
        self.results_label.setObjectName(u"results_label")
        self.results_label.setGeometry(QRect(820, 120, 191, 191))
        self.results_label.setFont(font)
        self.results_label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.results_label.setAlignment(Qt.AlignCenter)
        self.results_label.setWordWrap(True)

        self.get_res_btn = QPushButton(self.centralwidget)
        self.get_res_btn.setObjectName(u"right_answers")
        self.get_res_btn.setGeometry(QRect(820, 320, 191, 191))
        self.get_res_btn.setFont(font)
        self.get_res_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.get_res_btn.clicked.connect(self.calculate_results)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 300, 211, 131))

        self.answers_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.answers_layout.setObjectName(u"answers_layout")
        self.answers_layout.setContentsMargins(0, 0, 0, 0)

        self.answer_text_1 = QPlainTextEdit(self.centralwidget)
        self.answer_text_1.setObjectName(u"answer_text_1")
        self.answer_text_1.setGeometry(QRect(90, 290, 161, 31))

        self.answer_text_4 = QPlainTextEdit(self.centralwidget)
        self.answer_text_4.setObjectName(u"answer_text_4")
        self.answer_text_4.setGeometry(QRect(90, 410, 161, 31))

        self.answer_text_3 = QPlainTextEdit(self.centralwidget)
        self.answer_text_3.setObjectName(u"answer_text_3")
        self.answer_text_3.setGeometry(QRect(90, 370, 161, 31))

        self.answer_text_2 = QPlainTextEdit(self.centralwidget)
        self.answer_text_2.setObjectName(u"answer_text_2")
        self.answer_text_2.setGeometry(QRect(90, 330, 161, 31))

        self.answer_btn_1 = QCheckBox(self.centralwidget)
        self.answer_btn_1.setObjectName(u"answer_btn__1")
        self.answer_btn_1.setGeometry(QRect(60, 300, 14, 13))

        self.answer_btn_2 = QCheckBox(self.centralwidget)
        self.answer_btn_2.setObjectName(u"answer_btn__2")
        self.answer_btn_2.setGeometry(QRect(60, 340, 14, 13))

        self.answer_btn_3 = QCheckBox(self.centralwidget)
        self.answer_btn_3.setObjectName(u"answer_btn__3")
        self.answer_btn_3.setGeometry(QRect(60, 380, 14, 13))

        self.answer_btn_4 = QCheckBox(self.centralwidget)
        self.answer_btn_4.setObjectName(u"answer_btn__4")
        self.answer_btn_4.setGeometry(QRect(60, 420, 14, 13))

        self.num_1 = QLabel(self.centralwidget)
        self.num_1.setObjectName(u"num_1")
        self.num_1.setGeometry(QRect(840, 150, 31, 21))
        font3 = QFont()
        font3.setPointSize(20)
        self.num_1.setFont(font3)
        self.num_1.setScaledContents(False)
        self.num_1.setAlignment(Qt.AlignCenter)

        self.num_3 = QLabel(self.centralwidget)
        self.num_3.setObjectName(u"num_3")
        self.num_3.setGeometry(QRect(840, 230, 31, 21))
        self.num_3.setFont(font3)
        self.num_3.setScaledContents(False)
        self.num_3.setAlignment(Qt.AlignCenter)

        self.num_2 = QLabel(self.centralwidget)
        self.num_2.setObjectName(u"num_2")
        self.num_2.setGeometry(QRect(840, 190, 31, 21))
        self.num_2.setFont(font3)
        self.num_2.setScaledContents(False)
        self.num_2.setAlignment(Qt.AlignCenter)

        self.num_4 = QLabel(self.centralwidget)
        self.num_4.setObjectName(u"num_4")
        self.num_4.setGeometry(QRect(840, 270, 31, 21))
        self.num_4.setFont(font3)
        self.num_4.setScaledContents(False)
        self.num_4.setAlignment(Qt.AlignCenter)

        self.answer_count_1 = QLabel(self.centralwidget)
        self.answer_count_1.setObjectName(u"answer_count_1")
        self.answer_count_1.setGeometry(QRect(880, 150, 61, 21))
        self.answer_count_1.setFont(font1)

        self.answer_count_2 = QLabel(self.centralwidget)
        self.answer_count_2.setObjectName(u"answer_count_2")
        self.answer_count_2.setGeometry(QRect(880, 190, 61, 21))
        self.answer_count_2.setFont(font1)

        self.answer_count_3 = QLabel(self.centralwidget)
        self.answer_count_3.setObjectName(u"answer_count_3")
        self.answer_count_3.setGeometry(QRect(880, 230, 61, 21))
        self.answer_count_3.setFont(font1)

        self.answer_count_4 = QLabel(self.centralwidget)
        self.answer_count_4.setObjectName(u"answer_count_4")
        self.answer_count_4.setGeometry(QRect(880, 270, 61, 21))
        self.answer_count_4.setFont(font1)

        self.results = {}

        self.answers_back = QLabel(self.centralwidget)
        self.answers_back.setObjectName(u"answers_back")
        self.answers_back.setGeometry(QRect(40, 270, 271, 181))
        self.answers_back.setFont(font1)
        self.answers_back.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.answers_back.raise_()
        self.question_title.raise_()
        self.question_text.raise_()
        self.camera_label.raise_()
        self.save_answers.raise_()
        self.use_camera_text.raise_()
        self.turn_on_camera.raise_()
        self.results_text.raise_()
        self.results_label.raise_()
        self.get_res_btn.raise_()
        self.verticalLayoutWidget.raise_()
        self.answer_text_1.raise_()
        self.answer_text_4.raise_()
        self.answer_text_3.raise_()
        self.answer_text_2.raise_()
        self.answer_btn_1.raise_()
        self.answer_btn_2.raise_()
        self.answer_btn_3.raise_()
        self.answer_btn_4.raise_()
        self.num_1.raise_()
        self.num_3.raise_()
        self.num_2.raise_()
        self.num_4.raise_()
        self.answer_count_1.raise_()
        self.answer_count_2.raise_()
        self.answer_count_3.raise_()
        self.answer_count_4.raise_()

        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu1 = QMenu(self.menubar)
        self.menu1.setObjectName(u"menu1")

        guitaract = QAction("&Exit", self)
        guitaract.setShortcut("Ctrl+Q")
        guitaract.setStatusTip("Exit application")
        guitaract.triggered.connect(self.open_set_id_window)

        self.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu1.menuAction())
        self.menu1.addAction(guitaract)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.question_title.setText(
            QCoreApplication.translate("MainWindow", u"Your question:",
                                       None))
        self.question_text.setText("")
        self.camera_label.setText("")
        self.save_answers.setText(QCoreApplication.translate("MainWindow", u"Сохранить", None))
        self.use_camera_text.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u041d\u0430\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u0430\u043c\u0435\u0440\u0443 \u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u044c\u0442\u0435 \u043e\u0442\u0432\u0435\u0442\u044b",
                                                                None))
        self.turn_on_camera.setText(QCoreApplication.translate("MainWindow", u"Включить камеру", None))
        self.results_text.setText(
            QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b",
                                       None))
        self.results_label.setText("")
        self.get_res_btn.setText("Че по ответам")

        self.num_1.setText(QCoreApplication.translate("MainWindow", u"1:", None))
        self.num_3.setText(QCoreApplication.translate("MainWindow", u"3:", None))
        self.num_2.setText(QCoreApplication.translate("MainWindow", u"2:", None))
        self.num_4.setText(QCoreApplication.translate("MainWindow", u"4:", None))
        self.answer_count_1.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.answer_count_2.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.answer_count_3.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.answer_count_4.setText(QCoreApplication.translate("MainWindow", "0", None))

        self.answer_btn_1.setText("")
        self.answer_btn_2.setText("")
        self.answer_btn_3.setText("")
        self.answer_btn_4.setText("")

        self.menu1.setTitle(QCoreApplication.translate("MainWindow", u"1", None))

        self.answers_back.setText("")

    # retranslateUi

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            image = image.scaled(471, 271, aspectRatioMode=Qt.IgnoreAspectRatio)
            self.camera_label.setPixmap(QPixmap.fromImage(image))

    def use_camera(self):
        if not self.camera_on:
            self.camera_on = True
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(100)
        else:
            self.camera_label.clear()
            self.camera_on = False
            self.timer.stop()

    def set_right_answers(self):
        self.right_answers = []
        for btn in self.answer_btn_1, self.answer_btn_2, self.answer_btn_3, self.answer_btn_4:
            if btn.checkState():
                self.right_answers.append(btn.objectName()[-1])
        print(self.right_answers)

    def add_answer(self, aruco_id: int, side: str):
        if aruco_id not in self.results:
            if side == "up":
                self.results[aruco_id] = "1"
            elif side == "left":
                self.results[aruco_id] = "2"
            elif side == "right":
                self.results[aruco_id] = "3"
            else:
                self.results[aruco_id] = "4"

    def calculate_results(self):
        print(self.results.values())
        for answer in self.results.values():
            if answer == "1":
                self.answer_count_1.setText(str(int(self.answer_count_1.text()) + 1))
            elif answer == "2":
                self.answer_count_2.setText(str(int(self.answer_count_2.text()) + 1))
            elif answer == "3":
                self.answer_count_3.setText(str(int(self.answer_count_3.text()) + 1))
            else:
                self.answer_count_4.setText(str(int(self.answer_count_4.text()) + 1))

    def open_set_id_window(self):
        self.guitar = Guitar()
        self.guitar.show()

class Guitar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(250, 55, 1200, 800)
        self.setWindowTitle('Гитара')

        self.First_button = QPushButton('Первая струна(клавиша 1)', self)
        self.First_button.resize(170, 50)
        self.First_button.move(40, 100)

        self.Second_button = QPushButton('Вторая струна(клавиша 2)', self)
        self.Second_button.resize(170, 50)
        self.Second_button.move(40, 200)


import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.setupUi(window)

    window.add_answer(123, "left")
    window.add_answer(456, "left")
    window.add_answer(789, "up")

    window.show()
    sys.exit(app.exec_())

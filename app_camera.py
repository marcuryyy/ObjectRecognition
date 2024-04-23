from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QRect, Qt, QMetaObject, QCoreApplication, QSize
from PyQt5.QtGui import QImage, QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QCheckBox, QMenuBar, QApplication, \
    QTextEdit

import cv2


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1059, 550)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.question_title = QLabel(self.centralwidget)

        self.capture = cv2.VideoCapture(0)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)

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
        self.next_btn = QPushButton(self.centralwidget)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setGeometry(QRect(40, 460, 271, 51))
        font2 = QFont()
        font2.setPointSize(12)
        self.next_btn.setFont(font2)
        self.use_camera_text = QLabel(self.centralwidget)
        self.use_camera_text.setObjectName(u"use_camera_text")
        self.use_camera_text.setGeometry(QRect(330, 50, 471, 121))
        self.use_camera_text.setFont(font)
        self.use_camera_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.use_camera_text.setAlignment(Qt.AlignCenter)
        self.use_camera_text.setWordWrap(True)
        self.check_answer_btn = QPushButton(self.centralwidget)
        self.check_answer_btn.setObjectName(u"check_answer_btn")
        self.check_answer_btn.setGeometry(QRect(330, 460, 471, 51))
        self.check_answer_btn.setFont(font2)
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
        self.right_answers = QLabel(self.centralwidget)
        self.right_answers.setObjectName(u"right_answers")
        self.right_answers.setGeometry(QRect(820, 320, 191, 51))
        self.right_answers.setFont(font)
        self.right_answers.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.right_answers.setAlignment(Qt.AlignCenter)
        self.right_answers.setWordWrap(True)
        self.right_answers_percent = QLabel(self.centralwidget)
        self.right_answers_percent.setObjectName(u"right_answers_percent")
        self.right_answers_percent.setGeometry(QRect(820, 380, 191, 71))
        self.right_answers_percent.setFont(font)
        self.right_answers_percent.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.right_answers_percent.setAlignment(Qt.AlignCenter)
        self.right_answers_percent.setWordWrap(True)
        self.check_answer_btn_2 = QPushButton(self.centralwidget)
        self.check_answer_btn_2.setObjectName(u"check_answer_btn_2")
        self.check_answer_btn_2.setGeometry(QRect(820, 460, 191, 51))
        self.check_answer_btn_2.setFont(font2)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 300, 211, 131))
        self.answers_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.answers_layout.setObjectName(u"answers_layout")
        self.answers_layout.setContentsMargins(0, 0, 0, 0)
        self.answer_1 = QCheckBox(self.verticalLayoutWidget)
        self.answer_1.setObjectName(u"answer_1")
        # self.answer_1.clicked.connect()

        self.answers_layout.addWidget(self.answer_1)

        self.answer_2 = QCheckBox(self.verticalLayoutWidget)
        self.answer_2.setObjectName(u"answer_2")

        self.answers_layout.addWidget(self.answer_2)

        self.answer_3 = QCheckBox(self.verticalLayoutWidget)
        self.answer_3.setObjectName(u"answer_3")

        self.answers_layout.addWidget(self.answer_3)

        self.answer_4 = QCheckBox(self.verticalLayoutWidget)
        self.answer_4.setObjectName(u"answer_4")

        self.answers_layout.addWidget(self.answer_4)

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
        self.next_btn.raise_()
        self.use_camera_text.raise_()
        self.check_answer_btn.raise_()
        self.results_text.raise_()
        self.results_label.raise_()
        self.right_answers.raise_()
        self.right_answers_percent.raise_()
        self.check_answer_btn_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1059, 21))
        MainWindow.setMenuBar(self.menubar)

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
        self.next_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.use_camera_text.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u041d\u0430\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u0430\u043c\u0435\u0440\u0443 \u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u044c\u0442\u0435 \u043e\u0442\u0432\u0435\u0442\u044b",
                                                                None))
        self.check_answer_btn.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043e\u0442\u0432\u0435\u0442",
                                                                 None))
        self.results_text.setText(
            QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b",
                                       None))
        self.results_label.setText("")
        self.right_answers.setText("")
        self.right_answers_percent.setText("")
        self.check_answer_btn_2.setText(QCoreApplication.translate("MainWindow",
                                                                   u"\u0417\u0430\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0432\u043e\u043f\u0440\u043e\u0441",
                                                                   None))
        self.answer_1.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.answer_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.answer_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.answer_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.answers_back.setText("")

    # retranslateUi

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            image = image.scaled(471,271,aspectRatioMode=Qt.IgnoreAspectRatio)
            self.camera_label.setPixmap(QPixmap.fromImage(image))

    def change_text(self: QCheckBox):
        self.setText()

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.setupUi(window)
    window.show()
    sys.exit(app.exec_())

import cv2
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, Qt, QTimer)
from PySide2.QtGui import (QBrush, QColor, QFont,
                           QPalette, QPixmap,
                           QImage)
from PySide2.QtWidgets import *
import ltr


class CollectAnsApp(QMainWindow):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        self.setWindowIcon(QtGui.QIcon("mind_is_bam.png"))

        self.right_answers = None
        self.set_student_window = None
        self.answers_window = None

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

        # self.get_res_btn = QPushButton(self.centralwidget)
        # self.get_res_btn.setObjectName(u"right_answers")
        # self.get_res_btn.setGeometry(QRect(820, 320, 191, 191))
        # self.get_res_btn.setFont(font)
        # self.get_res_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        # self.get_res_btn.clicked.connect(self.calculate_results)

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
        # self.get_res_btn.raise_()
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

        add_student_act = QAction("Добавить студентов", self)
        add_student_act.triggered.connect(self.open_set_id_window)

        show_answers_act = QAction("Сгруппировать ответы студентов", self)
        show_answers_act.triggered.connect(self.open_answers_window)

        self.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu1.menuAction())
        self.menu1.addAction(add_student_act)
        self.menu1.addAction(show_answers_act)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Сбор ответов", None))
        self.question_title.setText(QCoreApplication.translate("MainWindow", u"Ваш вопрос:", None))
        self.save_answers.setText(QCoreApplication.translate("MainWindow", u"Сохранить", None))
        self.use_camera_text.setText(QCoreApplication.translate("MainWindow", u"Включить камеру", None))
        self.turn_on_camera.setText(QCoreApplication.translate("MainWindow", u"Включить камеру", None))
        self.results_text.setText(QCoreApplication.translate("MainWindow", u"Результаты", None))
        # self.get_res_btn.setText("Посчитать ответы")

        self.num_1.setText(QCoreApplication.translate("MainWindow", u"1:", None))
        self.num_3.setText(QCoreApplication.translate("MainWindow", u"3:", None))
        self.num_2.setText(QCoreApplication.translate("MainWindow", u"2:", None))
        self.num_4.setText(QCoreApplication.translate("MainWindow", u"4:", None))

        self.answer_count_1.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.answer_count_2.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.answer_count_3.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.answer_count_4.setText(QCoreApplication.translate("MainWindow", "0", None))

        self.menu1.setTitle(QCoreApplication.translate("MainWindow", u"Действия", None))
    # retranslateUi

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame, answers = ltr.main(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            if answers:
                for i in range(len(answers)):
                    self.add_answer(answers[i][0], answers[i][1])
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
            self.calculate_results()
            self.results = {}

    def set_right_answers(self):
        self.right_answers = []
        for btn in self.answer_btn_1, self.answer_btn_2, self.answer_btn_3, self.answer_btn_4:
            if btn.checkState():
                self.right_answers.append(btn.objectName()[-1])
        print(self.right_answers)

    def add_answer(self, aruco_id: str, side: str):
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
        print(self.results)
        for answer in self.results.values():
            if answer == "1":
                self.answer_count_1.setText(str(int(self.answer_count_1.text()) + 1))
            elif answer == "2":
                self.answer_count_2.setText(str(int(self.answer_count_2.text()) + 1))
            elif answer == "3":
                self.answer_count_3.setText(str(int(self.answer_count_3.text()) + 1))
            else:
                self.answer_count_4.setText(str(int(self.answer_count_4.text()) + 1))
        # self.results = {}

    def open_set_id_window(self):
        if self.set_student_window is None:
            self.set_student_window = SetStudentsWindow()
            self.set_student_window.setupUi(self.set_student_window)
        self.set_student_window.show()

    def open_answers_window(self):
        self.answers_window = AnswersWindow()
        self.answers_window.setupUi(self.answers_window)

        if self.set_student_window is None or len(self.set_student_window.student_list_dict) == 0:
            message = QMessageBox()
            message.setText("Вы не добавили ни одного студента")
            message.setWindowTitle("Что-то пошло не так")
            message.setWindowIcon(QtGui.QIcon("question.png"))
            message.setStandardButtons(QMessageBox.Close)
            message.exec_()
            return True
        elif len(self.results) == 0:
            message = QMessageBox()
            message.setText("Вы ещё не собрали ни одного ответа")
            message.setWindowTitle("Что-то пошло не так")
            message.setWindowIcon(QtGui.QIcon("question.png"))
            message.setStandardButtons(QMessageBox.Close)
            message.exec_()
            return True
        elif self.right_answers is None:
            message = QMessageBox()
            message.setText("Вы не установили правильные ответы")
            message.setWindowTitle("Что-то пошло не так")
            message.setWindowIcon(QtGui.QIcon("question.png"))
            message.setStandardButtons(QMessageBox.Close)
            message.exec_()
            return True
        self.answers_window.generate_tables(self.set_student_window.student_list_dict, self.results, self.right_answers)
        self.answers_window.show()


class AnswersWindow(QWidget):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")

        Form.resize(909, 633)
        Form.setContextMenuPolicy(Qt.NoContextMenu)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.setWindowIcon(QtGui.QIcon("congratz.png"))

        self.title_answered_correctly = QLabel(Form)
        self.title_answered_correctly.setObjectName(u"title_answered_correctly")
        self.title_answered_correctly.setGeometry(QRect(270, 10, 301, 51))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(21)
        self.title_answered_correctly.setFont(font)
        self.title_answered_correctly.setFrameShape(QFrame.Box)
        self.title_answered_correctly.setLineWidth(2)
        self.title_answered_correctly.setAlignment(Qt.AlignCenter)

        self.title_answered_incorrectly = QLabel(Form)
        self.title_answered_incorrectly.setObjectName(u"title_answered_incorrectly")
        self.title_answered_incorrectly.setGeometry(QRect(270, 310, 301, 51))
        self.title_answered_incorrectly.setFont(font)
        self.title_answered_incorrectly.setFrameShape(QFrame.Box)
        self.title_answered_incorrectly.setLineWidth(2)
        self.title_answered_incorrectly.setAlignment(Qt.AlignCenter)

        self.correct_ans_table = QScrollArea(Form)
        self.correct_ans_table.setObjectName(u"correctly_ans_table")
        self.correct_ans_table.setGeometry(QRect(50, 70, 791, 231))

        self.incorrect_ans_table = QScrollArea(Form)
        self.incorrect_ans_table.setObjectName(u"incorrectly_ans_table")
        self.incorrect_ans_table.setGeometry(QRect(50, 370, 791, 231))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Результаты с учениками", None))
        self.title_answered_correctly.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0432\u0435\u0442\u0438\u043b\u0438 \u0432\u0435\u0440\u043d\u043e", None))
        self.title_answered_incorrectly.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0432\u0435\u0442\u0438\u043b\u0438 \u043d\u0435\u0432\u0435\u0440\u043d\u043e", None))
    # retranslateUi

    def generate_tables(self, student_list_dict, results, right_answers):
        widget_for_correct_ans = QWidget()
        layout_for_correct_ans = QVBoxLayout(widget_for_correct_ans)

        widget_for_incorrect_ans = QWidget()
        layout_for_incorrect_ans = QVBoxLayout(widget_for_incorrect_ans)

        print(student_list_dict)
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(21)
        for name in student_list_dict.keys():
            student_id = student_list_dict[name]
            if student_id in results.keys():
                temp_label = QLabel()
                if results[student_id] in right_answers:
                    temp_label.setStyleSheet(u"background-color: rgb(170, 255, 127);")
                    temp_label.setText(name)
                    temp_label.setFont(font)
                    layout_for_correct_ans.addWidget(temp_label)
                else:
                    temp_label.setStyleSheet(u"background-color: rgba(179, 8, 8, 100);")
                    temp_label.setText(name)
                    temp_label.setFont(font)
                    layout_for_incorrect_ans.addWidget(temp_label)

        self.correct_ans_table.setWidget(widget_for_correct_ans)
        self.incorrect_ans_table.setWidget(widget_for_incorrect_ans)
        # self.answers_window.correctly_ans_table.setAlignment(Qt.AlignCenter)



class SetStudentsWindow(QWidget):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(763, 597)

        self.setWindowIcon(QtGui.QIcon("plus.png"))

        self.student_list_dict = {}

        self.students_list_name = QLabel(Form)
        self.students_list_name.setObjectName(u"students_list_name")
        self.students_list_name.setGeometry(QRect(460, 10, 299, 61))

        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
        # endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
        # endif

        self.students_list_name.setPalette(palette)
        font = QFont()
        font.setPointSize(18)
        self.students_list_name.setFont(font)
        self.students_list_name.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.students_list_name.setTextFormat(Qt.AutoText)
        self.students_list_name.setScaledContents(False)
        self.students_list_name.setAlignment(Qt.AlignCenter)

        self.aruco_label_name = QLabel(Form)
        self.aruco_label_name.setObjectName(u"aruco_label_name")
        self.aruco_label_name.setGeometry(QRect(10, 60, 441, 41))
        font1 = QFont()
        font1.setPointSize(16)
        self.aruco_label_name.setFont(font1)
        self.aruco_label_name.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.aruco_label_name.setAlignment(Qt.AlignCenter)

        self.student_name = QLabel(Form)
        self.student_name.setObjectName(u"student_name")
        self.student_name.setGeometry(QRect(10, 10, 71, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.student_name.setFont(font2)
        self.student_name.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.student_name.setAlignment(Qt.AlignCenter)

        self.student_name_input = QTextEdit(Form)
        self.student_name_input.setObjectName(u"student_name_input")
        self.student_name_input.setGeometry(QRect(90, 10, 261, 41))
        self.student_name_input.setLineWrapMode(QTextEdit.NoWrap)

        self.id_number = QLabel(Form)
        self.id_number.setObjectName(u"id_number")
        self.id_number.setGeometry(QRect(360, 10, 41, 41))
        font3 = QFont()
        font3.setPointSize(10)
        self.id_number.setFont(font3)
        self.id_number.setFocusPolicy(Qt.WheelFocus)
        self.id_number.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.id_number.setAlignment(Qt.AlignCenter)

        self.id_number_input = QTextEdit(Form)
        self.id_number_input.setObjectName(u"id_number_input")
        self.id_number_input.setGeometry(QRect(410, 10, 41, 41))

        self.add_student_button = QPushButton(Form)
        self.add_student_button.setObjectName(u"add_student")
        self.add_student_button.setGeometry(QRect(10, 510, 441, 81))
        font4 = QFont()
        font4.setPointSize(22)
        self.add_student_button.setFont(font4)
        self.add_student_button.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.add_student_button.clicked.connect(self.add_student)

        self.student_list = QTableWidget(Form)
        self.student_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        if (self.student_list.columnCount() < 2):
            self.student_list.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.student_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.student_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.student_list.setObjectName(u"student_list")
        self.student_list.setGeometry(QRect(460, 80, 301, 511))
        self.student_list.horizontalHeader().setDefaultSectionSize(40)
        self.student_list.setColumnWidth(0, 239)
        self.student_list.setColumnWidth(1, 10)

        self.aruco_label = QLabel(Form)
        self.aruco_label.setObjectName(u"aruco_label")
        self.aruco_label.setGeometry(QRect(10, 110, 441, 391))
        self.aruco_label.setFont(font1)
        self.aruco_label.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.aruco_label.setAlignment(Qt.AlignCenter)

        # if QT_CONFIG(shortcut)
        # endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Добавление учеников", None))
        self.students_list_name.setText(QCoreApplication.translate("Form", u"Ваши ученики", None))
        self.aruco_label_name.setText(QCoreApplication.translate("Form", u"Аруко Маркер:", None))
        self.student_name.setText(QCoreApplication.translate("Form", u"Ученик:", None))
        self.id_number.setText(QCoreApplication.translate("Form", u"Номер:", None))
        self.add_student_button.setText(QCoreApplication.translate("Form",  u"Добавить ученика", None))
        ___qtablewidgetitem = self.student_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Ученик", None));
        ___qtablewidgetitem1 = self.student_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"ID", None));
        self.aruco_label.setText(QCoreApplication.translate("Form", u"Аруко мркр", None))

    # retranslateUi

    def add_student(self):
        id_is_not_number = any(not i.isnumeric() for i in self.id_number_input.toPlainText())
        if id_is_not_number:
            message = QMessageBox()
            message.setText("Номер ученика должен быть числом от 0 до 59")
            message.setWindowTitle("Что-то пошло не так")
            message.setWindowIcon(QtGui.QIcon("question.png"))
            message.setStandardButtons(QMessageBox.Close)
            message.exec_()
            return True

        id_between_0_59 = 0 <= int(self.id_number_input.toPlainText()) <= 59
        if not id_between_0_59:
            message = QMessageBox()
            message.setText("Номер ученика должен быть числом от 0 до 59")
            message.setWindowTitle("Что-то пошло не так")
            message.setWindowIcon(QtGui.QIcon("question.png"))
            message.setIcon(QMessageBox.Warning)
            message.setStandardButtons(QMessageBox.Close)
            message.exec_()
            return True

        if self.id_number_input.toPlainText() in self.student_list_dict.values():
            message = QMessageBox()
            message.setText("Ученик с таким номером уже существует")
            message.setWindowTitle("Что-то пошло не так")
            message.setWindowIcon(QtGui.QIcon("question.png"))
            message.setIcon(QMessageBox.Warning)
            message.setStandardButtons(QMessageBox.Close)
            message.exec_()
            return True

        self.student_list_dict[self.student_name_input.toPlainText()] = self.id_number_input.toPlainText()
        self.student_list.setRowCount(len(self.student_list_dict))
        student = list(self.student_list_dict.keys())
        for person in range(len(self.student_list_dict)):
            person_name = QtWidgets.QTableWidgetItem(student[person])
            person_id = QtWidgets.QTableWidgetItem(self.student_list_dict[student[person]])
            self.student_list.setItem(person, 0, person_name)
            self.student_list.setItem(person, 1, person_id)
        self.student_name_input.clear()
        self.id_number_input.clear()


import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CollectAnsApp()
    window.setupUi(window)
    window.add_answer("12", "up")
    window.add_answer("13", "left")
    window.add_answer("14", "left")
    window.show()
    sys.exit(app.exec_())

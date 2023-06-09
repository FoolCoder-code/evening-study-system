# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Projects\evening-study-system\res\design\window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1401, 901)
        MainWindow.setMinimumSize(QtCore.QSize(1400, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphic_roll_call_tab = QtWidgets.QFrame(self.centralwidget)
        self.graphic_roll_call_tab.setGeometry(QtCore.QRect(0, 0, 700, 900))
        self.graphic_roll_call_tab.setStyleSheet("background-color: #282c34;\n"
"\n"
"border: 3px solid #2f333d;")
        self.graphic_roll_call_tab.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphic_roll_call_tab.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphic_roll_call_tab.setObjectName("graphic_roll_call_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.graphic_roll_call_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mode_select_layout = QtWidgets.QFrame(self.graphic_roll_call_tab)
        self.mode_select_layout.setMaximumSize(QtCore.QSize(16777215, 60))
        self.mode_select_layout.setObjectName("mode_select_layout")
        self.mode_layout = QtWidgets.QHBoxLayout(self.mode_select_layout)
        self.mode_layout.setObjectName("mode_layout")
        self.check_mode = QtWidgets.QPushButton(self.mode_select_layout)
        self.check_mode.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.check_mode.setFont(font)
        self.check_mode.setStyleSheet("color: #fff;\n"
"background-color: #323842;\n"
"\n"
"border-radius: 8px")
        self.check_mode.setObjectName("check_mode")
        self.mode_layout.addWidget(self.check_mode)
        self.late_mode = QtWidgets.QPushButton(self.mode_select_layout)
        self.late_mode.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.late_mode.setFont(font)
        self.late_mode.setStyleSheet("color: #fff;\n"
"background-color: #323842;\n"
"\n"
"border-radius: 8px")
        self.late_mode.setObjectName("late_mode")
        self.mode_layout.addWidget(self.late_mode)
        self.missing_mode = QtWidgets.QPushButton(self.mode_select_layout)
        self.missing_mode.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.missing_mode.setFont(font)
        self.missing_mode.setStyleSheet("color: #fff;\n"
"background-color: #323842;\n"
"\n"
"border-radius: 8px")
        self.missing_mode.setObjectName("missing_mode")
        self.mode_layout.addWidget(self.missing_mode)
        self.verticalLayout.addWidget(self.mode_select_layout)
        self.normal_seat_layout = QtWidgets.QFrame(self.graphic_roll_call_tab)
        self.normal_seat_layout.setObjectName("normal_seat_layout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.normal_seat_layout)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addWidget(self.normal_seat_layout)
        self.information_tab = QtWidgets.QFrame(self.centralwidget)
        self.information_tab.setGeometry(QtCore.QRect(700, 0, 701, 900))
        self.information_tab.setStyleSheet("background-color: #21252b;\n"
"\n"
"border: 3px solid #2f333d;")
        self.information_tab.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.information_tab.setFrameShadow(QtWidgets.QFrame.Raised)
        self.information_tab.setObjectName("information_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.information_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalFrame = QtWidgets.QFrame(self.information_tab)
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.info_copy_layout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.info_copy_layout.setObjectName("info_copy_layout")
        self.infos_btns_layout = QtWidgets.QFrame(self.horizontalFrame)
        self.infos_btns_layout.setMinimumSize(QtCore.QSize(0, 120))
        self.infos_btns_layout.setObjectName("infos_btns_layout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.infos_btns_layout)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.infos_layout = QtWidgets.QHBoxLayout()
        self.infos_layout.setObjectName("infos_layout")
        self.target_count = QtWidgets.QLabel(self.infos_btns_layout)
        self.target_count.setMaximumSize(QtCore.QSize(130, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.target_count.setFont(font)
        self.target_count.setStyleSheet("color: #fff;\n"
"background-color: #323842;\n"
"\n"
"border-radius: 8px")
        self.target_count.setAlignment(QtCore.Qt.AlignCenter)
        self.target_count.setObjectName("target_count")
        self.infos_layout.addWidget(self.target_count)
        self.actual_count = QtWidgets.QLabel(self.infos_btns_layout)
        self.actual_count.setMaximumSize(QtCore.QSize(130, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.actual_count.setFont(font)
        self.actual_count.setStyleSheet("color: #fff;\n"
"background-color: #323842;\n"
"\n"
"border-radius: 8px")
        self.actual_count.setAlignment(QtCore.Qt.AlignCenter)
        self.actual_count.setObjectName("actual_count")
        self.infos_layout.addWidget(self.actual_count)
        self.missing_count = QtWidgets.QLabel(self.infos_btns_layout)
        self.missing_count.setMaximumSize(QtCore.QSize(130, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.missing_count.setFont(font)
        self.missing_count.setStyleSheet("color: #fff;\n"
"background-color: #323842;\n"
"\n"
"border-radius: 8px")
        self.missing_count.setAlignment(QtCore.Qt.AlignCenter)
        self.missing_count.setObjectName("missing_count")
        self.infos_layout.addWidget(self.missing_count)
        self.verticalLayout_3.addLayout(self.infos_layout)
        self.btns_layout = QtWidgets.QHBoxLayout()
        self.btns_layout.setObjectName("btns_layout")
        self.confirm_output = QtWidgets.QPushButton(self.infos_btns_layout)
        self.confirm_output.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.confirm_output.setFont(font)
        self.confirm_output.setStyleSheet("color: #fff;\n"
"background-color: #323842;\n"
"\n"
"border-radius: 8px")
        self.confirm_output.setObjectName("confirm_output")
        self.btns_layout.addWidget(self.confirm_output)
        self.clear_output = QtWidgets.QPushButton(self.infos_btns_layout)
        self.clear_output.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.clear_output.setFont(font)
        self.clear_output.setStyleSheet("color: #fff;\n"
"background-color: #323842;\n"
"\n"
"border-radius: 8px")
        self.clear_output.setObjectName("clear_output")
        self.btns_layout.addWidget(self.clear_output)
        self.datetime_btn = QtWidgets.QPushButton(self.infos_btns_layout)
        self.datetime_btn.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.datetime_btn.setFont(font)
        self.datetime_btn.setStyleSheet("color: #fff;\n"
"background-color: #323842;\n"
"\n"
"border-radius: 8px")
        self.datetime_btn.setObjectName("datetime_btn")
        self.btns_layout.addWidget(self.datetime_btn)
        self.verticalLayout_3.addLayout(self.btns_layout)
        self.info_copy_layout.addWidget(self.infos_btns_layout)
        self.copy_edit = QtWidgets.QPlainTextEdit(self.horizontalFrame)
        self.copy_edit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.copy_edit.setStyleSheet("color: #fff")
        self.copy_edit.setReadOnly(True)
        self.copy_edit.setObjectName("copy_edit")
        self.info_copy_layout.addWidget(self.copy_edit)
        self.verticalLayout_4.addWidget(self.horizontalFrame)
        self.student_table = QtWidgets.QTableWidget(self.information_tab)
        self.student_table.setStyleSheet("background-color: #323842;\n"
"border-radius: 5px;")
        self.student_table.setObjectName("student_table")
        self.student_table.setColumnCount(0)
        self.student_table.setRowCount(0)
        self.verticalLayout_4.addWidget(self.student_table)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.check_mode.setText(_translate("MainWindow", "Q 已到"))
        self.late_mode.setText(_translate("MainWindow", "W 遲到"))
        self.missing_mode.setText(_translate("MainWindow", "E 曠課"))
        self.target_count.setText(_translate("MainWindow", "應到人數：0"))
        self.actual_count.setText(_translate("MainWindow", "實到人數：0"))
        self.missing_count.setText(_translate("MainWindow", "未到人數：0"))
        self.confirm_output.setText(_translate("MainWindow", "確認"))
        self.clear_output.setText(_translate("MainWindow", "清空"))
        self.datetime_btn.setText(_translate("MainWindow", "選擇日期"))

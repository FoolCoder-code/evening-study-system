import os, sys
import pandas as pd
from datetime import datetime
from pathlib import Path

# 8 x 3 x 4 + 6

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QDateEdit, QTableWidgetItem, QSpacerItem, QSizePolicy, QShortcut
from PyQt5.QtGui import QFont, QBrush, QColor, QKeySequence

from design.Ui_window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    resized = QtCore.pyqtSignal()
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()

        self.font = QFont()
        self.font.setFamily("微軟正黑體")
        self.font.setPointSize(12)

        self.ui.setupUi(self)
        self.resized.connect(self.onWindowResize)

        self.ui.student_table.horizontalHeader().setFixedHeight(40)
        self.ui.student_table.setFont(self.font)

        self.student_datas = self.excel_to_data()
        self.check_datas = []

        self.all_students_btn = []
        self.dynamic_seats()
        self.datetimeedit_setup()

        self.selected_mode = "check"
        self.function_setup()
        self.ui.check_mode.click()

        self.ui.copy_edit.setFont(self.font)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(MainWindow, self).resizeEvent(event)

    def onWindowResize(self):
        size = self.size()
        width = size.width()
        height = size.height()
        print(f"resizing {width=} {height=}")

        self.ui.graphic_roll_call_tab.setGeometry(0, 0, width//2, height)
        self.ui.information_tab.setGeometry(width//2, 0, width - width//2, height)

    def excel_to_data(self):
        student_datas = pd.read_excel(Path("data.xlsx"))
        fixed_students = {}
        self.ui.student_table.setColumnCount(len(student_datas.columns))
        self.ui.student_table.setHorizontalHeaderLabels([i for i in student_datas.columns])
        for i, (index, row) in enumerate(student_datas.iterrows()):
            #self.ui.student_table.horizontalHeaderItem(i).setFont(self.font)
            now_student = {}
            for row_name in ["班級", "座號", "姓名", "姓名(公布)", "編號", "自習時間"]:
                try:
                    now_student[row_name] = str(int(row[row_name]))
                except ValueError:
                    now_student[row_name] = str(row[row_name])
            fixed_students[str(row["編號"])] = now_student
        print(fixed_students)

        """for i, column_name in enumerate(student_datas.columns):
            #self.ui.student_table.horizontalHeaderItem(i).setFont(self.font)
            for j, data in enumerate(student_datas[str(column_name)].tolist()):
                try:
                    fixed_students[j][column_name] = str(int(data))
                except ValueError:
                    fixed_students[j][column_name] = str(data)"""
        #fixed_students.sort(key=lambda x: int(x["編號"]))

        for student_num in range(0, 103):
            now_student = fixed_students.get(str(student_num), False)
            if not now_student:
                continue
            rowPos = self.ui.student_table.rowCount()
            self.ui.student_table.insertRow(rowPos)
            for i, key in enumerate(student_datas.columns):
                self.ui.student_table.setItem(rowPos, i, QTableWidgetItem(str(now_student[key])))
                self.ui.student_table.item(rowPos, i).setForeground(QBrush(QColor("#fff")))
        return fixed_students

    def dynamic_seats(self):
        def callback(*args):
            return lambda: self.student_select(*args)
        for i in range(1, 9):
            now_l_layout = QVBoxLayout()
            now_l_layout.setObjectName(f"seat_layout_l_{i}")
            for j in range(1, 3):
                now_layout = QHBoxLayout()
                now_layout.setObjectName(f"seat_layout_{i}_{j}")
                spacer_count = 0
                for k in range(1, 7):
                    now_btn = QPushButton()
                    num = (8-i)*2*6 + ((3-j)*6) - (6-k)
                    if j == 1 and k in [1, 2]:
                        num = num - 4
                    elif j == 1 and k in [3, 4]:
                        num = num - 2
                    elif j == 2 and k in [3, 4]:
                        num = num + 2
                    elif j == 2 and k in [5, 6]:
                        num = num + 4
                    _now_student = self.student_datas.get(str(num), False)
                    if not _now_student:
                        now_btn.setText(f"{num}")
                    else:
                        _now_num = _now_student.get("編號", "")
                        _now_name = _now_student.get("姓名", "")
                        now_btn.setText(f"{num} {_now_name}")
                        now_btn.clicked.connect(callback(_now_num, now_btn))
                    now_btn.setFont(self.font)
                    now_btn.setStyleSheet("color: #fff;\n")
                    if spacer_count == 2:
                        spacerItem = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
                        spacer_count = 0
                        now_layout.addSpacerItem(spacerItem)
                    self.all_students_btn.append([str(num), now_btn])
                    spacer_count = spacer_count + 1
                    now_layout.addWidget(now_btn)
                now_l_layout.addLayout(now_layout)
            self.ui.verticalLayout_2.addLayout(now_l_layout)
        now_layout = QHBoxLayout()
        now_layout.setObjectName(f"seat_layout_front")
        for i in range(102, 96, -1):
            now_btn = QPushButton()
            _now_student = self.student_datas.get(str(i), False)
            if not _now_student:
                now_btn.setText(f"{i}")
            else:
                _now_num = _now_student.get("編號", "")
                _now_name = _now_student.get("姓名", "")
                now_btn.setText(f"{i} {_now_name}")
                now_btn.clicked.connect(callback(_now_num, now_btn))
            now_btn.setFont(self.font)
            now_btn.setStyleSheet("color: #fff;\n")
            self.all_students_btn.append([str(i), now_btn])
            now_layout.addWidget(now_btn)
        self.ui.verticalLayout_2.addLayout(now_layout)
        self.btn_datetime_today()

    def datetimeedit_setup(self):
        self.dateform = QWidget()
        self.dateform.setWindowTitle("選擇日期")
        self.dateform.resize(250, 100)
        self.dateform.setMinimumSize(QtCore.QSize(250, 100))
        self.dateform.setMaximumSize(QtCore.QSize(250, 100))
        dateedit = QDateEdit(self.dateform)
        dateedit.setGeometry(20, 20, 210, 30)
        dateedit.setDateTime(QtCore.QDateTime.currentDateTime())
        dateedit.setCalendarPopup(True)
        dateedit.setDisplayFormat("yyyy/MM/dd")

        confirm_btn = QPushButton(self.dateform)
        confirm_btn.setText("使用今日日期")
        confirm_btn.setGeometry(20, 60, 100, 30)
        confirm_btn.clicked.connect(self.btn_datetime_today)

        confirm_btn = QPushButton(self.dateform)
        confirm_btn.setText("確認")
        confirm_btn.setGeometry(130, 60, 60, 30)
        confirm_btn.clicked.connect(self.btn_datetime_selected)
        self.getSelectedTime = lambda: dateedit.dateTime().toString(dateedit.displayFormat())

    def function_setup(self):
        self.ui.confirm_output.clicked.connect(self.btn_confirm)
        self.ui.clear_output.clicked.connect(self.btn_clear)
        self.ui.datetime_btn.clicked.connect(self.btn_datetime_show)

        self.check_mode_shortcut = QShortcut(QKeySequence("Q"), self.ui.centralwidget)
        self.check_mode_shortcut.activated.connect(lambda: self.mode_select("check"))
        self.late_mode_shortcut = QShortcut(QKeySequence("W"), self.ui.centralwidget)
        self.late_mode_shortcut.activated.connect(lambda: self.mode_select("late"))
        self.missing_mode_shortcut = QShortcut(QKeySequence("E"), self.ui.centralwidget)
        self.missing_mode_shortcut.activated.connect(lambda: self.mode_select("missing"))

        self.ui.check_mode.clicked.connect(lambda: self.mode_select("check"))
        self.ui.late_mode.clicked.connect(lambda: self.mode_select("late"))
        self.ui.missing_mode.clicked.connect(lambda: self.mode_select("missing"))

    def btn_confirm(self):
        print("confirm")
        text = ""
        for target in ["check", "late", "missing"]:
            #.get('姓名(公開)') .get('班級') .get('座號')
            result = [f"{student.get('班級')}-{student.get('座號')} {student.get('姓名(公布)')}" for student in [self.student_datas.get(student[0]) for student in self.check_datas if student[1] == target]]
            if target == "check":
                pass
            elif target == "late":
                text = text + "遲：\n" + "\n".join(result)
            elif target == "missing":
                text = text + "曠：\n" + "\n".join(result)
        self.ui.copy_edit.setPlainText(text)

    def btn_clear(self):
        print("clear")
        self.btn_datetime_today()

    def btn_datetime_show(self):
        print("datetime")
        self.dateform.show()

    def mode_select(self, target:str):
        self.selected_mode = target
        for btn_name in ["check", "late", "missing"]:
            btn = getattr(self.ui, f"{btn_name}_mode")
            print(f"{btn_name=} {target=}")
            if btn_name == target:
                btn.setStyleSheet("color: #fff;\nbackground-color: #4e5868;\nborder-radius: 8px")
            else:
                btn.setStyleSheet("color: #fff;\nbackground-color: #323842;\nborder-radius: 8px")
            # D#323842 B#4e5868

    def student_select(self, target_num, target_btn):
        print(target_num, target_btn)
        target_student = self.student_datas.get(str(target_num), {})
        if not target_student:
            return
        if self.weekday not in target_student.get("自習時間", "0"):
            return
        is_checked = target_num in [n[0] for n in self.check_datas]
        if self.selected_mode == "check":
            target_btn.setStyleSheet("color: #98c379;\n")
        elif self.selected_mode == "late":
            target_btn.setStyleSheet("color: #e5b55f;\n")
        elif self.selected_mode == "missing":
            target_btn.setStyleSheet("color: #e05a55;\n")
        if not is_checked:
            self.check_datas.append([str(target_num), self.selected_mode])
        else:
            self.check_datas[[n[0] for n in self.check_datas].index(target_num)][1] = self.selected_mode
        self.set_count(len([n[1] for n in self.check_datas if n[1] in ["check", "late"]]))
        print(self.check_datas)

    def btn_datetime_today(self):
        try:
            self.dateform.close()
        except AttributeError:
            pass
        weekday = datetime.now().weekday()
        print(weekday)
        self.datetime_get_namelist(weekday)

    def btn_datetime_selected(self):
        self.dateform.close()
        dt = datetime.strptime(self.getSelectedTime(), "%Y/%m/%d")
        weekday = dt.weekday()
        print(weekday)
        self.datetime_get_namelist(weekday)

    def datetime_get_namelist(self, _weekday:int):
        self.coming_scount = 0
        self.check_datas = []
        weekday = _weekday + 1
        self.weekday = str(weekday)
        if weekday <= 0 or weekday >= 6:
            return
        for student_btn in self.all_students_btn:
            num = student_btn[0]
            now_student = self.student_datas.get(str(num), False)
            if not now_student:
                coming = False
            else:
                coming = str(weekday) in now_student.get("自習時間", "")
            if coming:
                student_btn[1].setStyleSheet("color: #fff;\n")
                self.coming_scount = self.coming_scount + 1
            else:
                student_btn[1].setStyleSheet("color: #575757;\n")
        self.set_count(0)

    def set_count(self, come:int=0):
        should = self.coming_scount
        self.ui.target_count.setText(f"應到人數：{should}")
        self.ui.actual_count.setText(f"實到人數：{come}")
        self.ui.missing_count.setText(f"未到人數：{should-come}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
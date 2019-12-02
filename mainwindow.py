# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dylanpc/Documents/soundboard.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from playsound import playsound


class Ui_Soundboard(QWidget):
    def setupUi(self, Soundboard):
        Soundboard.setObjectName("Soundboard")
        Soundboard.resize(1125, 620)
        Soundboard.setMinimumSize(QtCore.QSize(0, 620))
        Soundboard.setMaximumSize(QtCore.QSize(16777215, 620))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Soundboard.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(Soundboard)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.file_window = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_window.sizePolicy().hasHeightForWidth())
        self.file_window.setSizePolicy(sizePolicy)
        self.file_window.setMinimumSize(QtCore.QSize(0, 600))
        self.file_window.setMaximumSize(QtCore.QSize(200, 780))
        self.file_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.file_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file_window.setLineWidth(3)
        self.file_window.setMidLineWidth(5)
        self.file_window.setObjectName("file_window")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.file_window)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.browse_button = QtWidgets.QPushButton(self.file_window)
        self.browse_button.setObjectName("browse_button")
        self.gridLayout_3.addWidget(self.browse_button, 1, 0, 1, 1)
        self.file_line = QtWidgets.QLabel(self.file_window)
        self.file_line.setAlignment(QtCore.Qt.AlignCenter)
        self.file_line.setObjectName("file_line")
        self.gridLayout_3.addWidget(self.file_line, 0, 0, 1, 1)
        self.list_layout = QtWidgets.QListWidget(self.file_window)
        self.list_layout.setObjectName("list_layout")
        self.gridLayout_3.addWidget(self.list_layout, 2, 0, 1, 1)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.file_window)
        self.button_window = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_window.sizePolicy().hasHeightForWidth())
        self.button_window.setSizePolicy(sizePolicy)
        self.button_window.setMinimumSize(QtCore.QSize(0, 600))
        self.button_window.setMaximumSize(QtCore.QSize(16777215, 780))
        self.button_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_window.setLineWidth(3)
        self.button_window.setMidLineWidth(5)
        self.button_window.setObjectName("button_window")
        self.gridLayout = QtWidgets.QGridLayout(self.button_window)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.button_window)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.button_scroll_area = QtWidgets.QScrollArea(self.button_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_scroll_area.sizePolicy().hasHeightForWidth())
        self.button_scroll_area.setSizePolicy(sizePolicy)
        self.button_scroll_area.setMinimumSize(QtCore.QSize(0, 0))
        self.button_scroll_area.setWidgetResizable(True)
        self.button_scroll_area.setObjectName("button_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 803, 555))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.grid_layout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.grid_layout.setObjectName("grid_layout")
        self.button_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.button_scroll_area, 1, 0, 1, 1)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.button_window)
        Soundboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(Soundboard)
        QtCore.QMetaObject.connectSlotsByName(Soundboard)

        self.browse_button.clicked.connect(self.update_file_selection)

    def update_file_selection(self):

        self.check_boxes = {}

        self.sound_buttons = {}

        self.sound_signal_tracker = {}

        self.list_layout.clear()

        self.remove_all_list_items()

        selected_files = self.get_files()

        for f_ in selected_files:
            self.check_boxes.update({f"{f_}": QtWidgets.QListWidgetItem()})
            self.check_boxes[f_].setText(f"{f_}")
            self.check_boxes[f_].setCheckState(QtCore.Qt.Unchecked)
            self.list_layout.addItem(self.check_boxes[f_])

        self.list_layout.sortItems()
        self.list_layout.itemClicked.connect(self.create_button_signal)
        self.list_layout.itemClicked.connect(self.remove_button_signal)
        self.list_layout.itemDoubleClicked.connect(self.double_click_signal)

    def create_button_signal(self):

        for k in self.check_boxes.keys():
            if self.check_boxes[k].checkState() == QtCore.Qt.Checked:
                if k not in self.sound_buttons.keys():
                    self.sound_buttons.update({f"{k}": QtWidgets.QPushButton()})
                    self.sound_buttons[k].setText(f"{k}")
                    self.grid_layout.addWidget(self.sound_buttons[k])
                    self.sound_buttons[k].setFixedSize(125, 100)
                    """To Do: Re-adjust buttons and add signal"""

        for k in self.sound_buttons.keys():
            if k not in self.sound_signal_tracker.keys():
                self.sound_signal_tracker[f"{k}"] = "Created"
                self.sound_buttons[k].clicked.connect(lambda: playsound(self.parent_path + k))

    def remove_button_signal(self):

        for k in self.check_boxes.keys():
            if self.check_boxes[k].checkState() == QtCore.Qt.Unchecked:
                if k in self.sound_buttons.keys():
                    self.sound_buttons[k].deleteLater()
                    del self.sound_buttons[k]
                    del self.sound_signal_tracker[k]

    def double_click_signal(self):

        selected_item = self.list_layout.selectedItems()[0]

        if selected_item in self.check_boxes.values():
            if selected_item.checkState() == QtCore.Qt.Unchecked:
                selected_item.setCheckState(QtCore.Qt.Checked)
            else:
                selected_item.setCheckState(QtCore.Qt.Unchecked)

    def remove_all_list_items(self):

        for i in range(self.grid_layout.count()):
            self.grid_layout.itemAt(i).widget().deleteLater()

    def get_files(self):

        file_names = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select files',
                    '/', "Sound files (*.wav *.mp3py)")

        selected_files = [f_.split("/")[-1] for f_ in file_names[0]]

        try:
            parent_dir = file_names[0][0].split("/")[-2] + "/"
            self.parent_path = '/'.join([folder for folder in file_names[0][0].split("/")[:-1]]) + "/"

        except IndexError:
            parent_dir = "No Files Selected"

        self.update_file_line(parent_dir)

        return selected_files

    def update_file_line(self, directory):

        _translate = QtCore.QCoreApplication.translate
        self.file_line.setText(_translate("Soundboard", directory))

    def retranslateUi(self, Soundboard):

        _translate = QtCore.QCoreApplication.translate
        Soundboard.setWindowTitle(_translate("Soundboard", "Soundboard"))
        self.browse_button.setText(_translate("Soundboard", "Browse..."))
        self.file_line.setText(_translate("Soundboard", "Choose Files"))
        self.label.setText(_translate("Soundboard", "Soundboard Buttons"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Soundboard = QtWidgets.QMainWindow()
    ui = Ui_Soundboard()
    ui.setupUi(Soundboard)
    Soundboard.show()
    sys.exit(app.exec_())

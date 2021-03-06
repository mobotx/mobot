# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pid_tune.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pid_tune(object):
    def setupUi(self, pid_tune):
        pid_tune.setObjectName("pid_tune")
        pid_tune.resize(538, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pid_tune.sizePolicy().hasHeightForWidth())
        pid_tune.setSizePolicy(sizePolicy)
        pid_tune.setMinimumSize(QtCore.QSize(538, 150))
        pid_tune.setMaximumSize(QtCore.QSize(538, 150))
        pid_tune.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(pid_tune)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.p_slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.p_slider.setMaximum(1000)
        self.p_slider.setOrientation(QtCore.Qt.Horizontal)
        self.p_slider.setObjectName("p_slider")
        self.gridLayout.addWidget(self.p_slider, 0, 1, 1, 1)
        self.w_value = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.w_value.setObjectName("w_value")
        self.gridLayout.addWidget(self.w_value, 2, 2, 1, 1)
        self.i_value = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.i_value.setObjectName("i_value")
        self.gridLayout.addWidget(self.i_value, 1, 2, 1, 1)
        self.w_slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.w_slider.setMinimum(-1000)
        self.w_slider.setMaximum(1000)
        self.w_slider.setProperty("value", 0)
        self.w_slider.setOrientation(QtCore.Qt.Horizontal)
        self.w_slider.setObjectName("w_slider")
        self.gridLayout.addWidget(self.w_slider, 2, 1, 1, 1)
        self.i_slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.i_slider.setMaximum(1000)
        self.i_slider.setOrientation(QtCore.Qt.Horizontal)
        self.i_slider.setObjectName("i_slider")
        self.gridLayout.addWidget(self.i_slider, 1, 1, 1, 1)
        self.i_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.i_label.setObjectName("i_label")
        self.gridLayout.addWidget(self.i_label, 1, 0, 1, 1)
        self.p_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.p_label.setObjectName("p_label")
        self.gridLayout.addWidget(self.p_label, 0, 0, 1, 1)
        self.w_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.w_label.setObjectName("w_label")
        self.gridLayout.addWidget(self.w_label, 2, 0, 1, 1)
        self.p_value = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.p_value.setMinimumSize(QtCore.QSize(0, 0))
        self.p_value.setBaseSize(QtCore.QSize(0, 0))
        self.p_value.setTextFormat(QtCore.Qt.PlainText)
        self.p_value.setScaledContents(False)
        self.p_value.setWordWrap(False)
        self.p_value.setIndent(0)
        self.p_value.setObjectName("p_value")
        self.gridLayout.addWidget(self.p_value, 0, 2, 1, 1)
        self.gridLayout.setColumnMinimumWidth(2, 100)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stop_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout.addWidget(self.stop_button)
        self.w_present_value = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.w_present_value.setObjectName("w_present_value")
        self.horizontalLayout.addWidget(self.w_present_value)
        self.verticalLayout.addLayout(self.horizontalLayout)
        pid_tune.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(pid_tune)
        self.statusbar.setObjectName("statusbar")
        pid_tune.setStatusBar(self.statusbar)

        self.retranslateUi(pid_tune)
        QtCore.QMetaObject.connectSlotsByName(pid_tune)

    def retranslateUi(self, pid_tune):
        _translate = QtCore.QCoreApplication.translate
        pid_tune.setWindowTitle(_translate("pid_tune", "PID Tuning"))
        self.w_value.setText(_translate("pid_tune", "0.0"))
        self.i_value.setText(_translate("pid_tune", "0.0"))
        self.i_label.setText(_translate("pid_tune", "I"))
        self.p_label.setText(_translate("pid_tune", "P"))
        self.w_label.setText(_translate("pid_tune", "W"))
        self.p_value.setText(_translate("pid_tune", "0.0"))
        self.stop_button.setText(_translate("pid_tune", "Stop"))
        self.w_present_value.setText(_translate("pid_tune", "abs(W): 0.0 rad/sec"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pid_tune = QtWidgets.QMainWindow()
    ui = Ui_pid_tune()
    ui.setupUi(pid_tune)
    pid_tune.show()
    sys.exit(app.exec_())

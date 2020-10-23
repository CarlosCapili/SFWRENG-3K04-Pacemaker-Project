# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\dcm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1003, 656)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.paceButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paceButton.sizePolicy().hasHeightForWidth())
        self.paceButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.paceButton.setFont(font)
        self.paceButton.setObjectName("paceButton")
        self.verticalLayout_5.addWidget(self.paceButton)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.aaiButton = QtWidgets.QRadioButton(self.centralwidget)
        self.aaiButton.setObjectName("aaiButton")
        self.gridLayout.addWidget(self.aaiButton, 1, 0, 1, 1)
        self.aooButton = QtWidgets.QRadioButton(self.centralwidget)
        self.aooButton.setObjectName("aooButton")
        self.gridLayout.addWidget(self.aooButton, 0, 0, 1, 1)
        self.vooButton = QtWidgets.QRadioButton(self.centralwidget)
        self.vooButton.setObjectName("vooButton")
        self.gridLayout.addWidget(self.vooButton, 0, 1, 1, 1)
        self.vviButton = QtWidgets.QRadioButton(self.centralwidget)
        self.vviButton.setObjectName("vviButton")
        self.gridLayout.addWidget(self.vviButton, 1, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EGRAMLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.EGRAMLabel.setFont(font)
        self.EGRAMLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EGRAMLabel.setObjectName("EGRAMLabel")
        self.horizontalLayout.addWidget(self.EGRAMLabel)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.paceCheck = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paceCheck.sizePolicy().hasHeightForWidth())
        self.paceCheck.setSizePolicy(sizePolicy)
        self.paceCheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.paceCheck.setObjectName("paceCheck")
        self.verticalLayout_4.addWidget(self.paceCheck)
        self.senseCheck = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senseCheck.sizePolicy().hasHeightForWidth())
        self.senseCheck.setSizePolicy(sizePolicy)
        self.senseCheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.senseCheck.setObjectName("senseCheck")
        self.verticalLayout_4.addWidget(self.senseCheck)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.atrialGraphics = QtWidgets.QGraphicsView(self.centralwidget)
        self.atrialGraphics.setObjectName("atrialGraphics")
        self.verticalLayout_2.addWidget(self.atrialGraphics)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.ventricularGraphics = QtWidgets.QGraphicsView(self.centralwidget)
        self.ventricularGraphics.setObjectName("ventricularGraphics")
        self.verticalLayout_2.addWidget(self.ventricularGraphics)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 3, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.reportsButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reportsButton.sizePolicy().hasHeightForWidth())
        self.reportsButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reportsButton.setFont(font)
        self.reportsButton.setObjectName("reportsButton")
        self.verticalLayout.addWidget(self.reportsButton)
        self.parametersButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parametersButton.sizePolicy().hasHeightForWidth())
        self.parametersButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parametersButton.setFont(font)
        self.parametersButton.setObjectName("parametersButton")
        self.verticalLayout.addWidget(self.parametersButton)
        self.aboutButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutButton.sizePolicy().hasHeightForWidth())
        self.aboutButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aboutButton.setFont(font)
        self.aboutButton.setObjectName("aboutButton")
        self.verticalLayout.addWidget(self.aboutButton)
        self.setClockButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setClockButton.sizePolicy().hasHeightForWidth())
        self.setClockButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setClockButton.setFont(font)
        self.setClockButton.setObjectName("setClockButton")
        self.verticalLayout.addWidget(self.setClockButton)
        self.newPatientButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newPatientButton.sizePolicy().hasHeightForWidth())
        self.newPatientButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newPatientButton.setFont(font)
        self.newPatientButton.setObjectName("newPatientButton")
        self.verticalLayout.addWidget(self.newPatientButton)
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quitButton.setFont(font)
        self.quitButton.setObjectName("quitButton")
        self.verticalLayout.addWidget(self.quitButton)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1003, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReview = QtWidgets.QAction(MainWindow)
        self.actionReview.setObjectName("actionReview")
        self.actionModify = QtWidgets.QAction(MainWindow)
        self.actionModify.setObjectName("actionModify")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.paceButton.setText(_translate("MainWindow", "Pace Now"))
        self.aaiButton.setText(_translate("MainWindow", "AAI"))
        self.aooButton.setText(_translate("MainWindow", "AOO"))
        self.vooButton.setText(_translate("MainWindow", "VOO"))
        self.vviButton.setText(_translate("MainWindow", "VVI"))
        self.EGRAMLabel.setText(_translate("MainWindow", "ELECTROGRAM"))
        self.paceCheck.setText(_translate("MainWindow", "Pace Leads"))
        self.senseCheck.setText(_translate("MainWindow", "Sense Leads"))
        self.label.setText(_translate("MainWindow", "Atrial"))
        self.label_2.setText(_translate("MainWindow", "Ventricular"))
        self.reportsButton.setText(_translate("MainWindow", "Reports"))
        self.parametersButton.setText(_translate("MainWindow", "Parameters"))
        self.aboutButton.setText(_translate("MainWindow", "About"))
        self.setClockButton.setText(_translate("MainWindow", "Set Clock"))
        self.newPatientButton.setText(_translate("MainWindow", "New Patient"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.actionReview.setText(_translate("MainWindow", "Review"))
        self.actionModify.setText(_translate("MainWindow", "Modify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

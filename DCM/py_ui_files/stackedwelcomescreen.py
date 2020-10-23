# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\stackedwelcomescreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Welcome(object):
    def setupUi(self, Welcome):
        Welcome.setObjectName("Welcome")
        Welcome.resize(640, 269)
        self.welcomeScreen = QtWidgets.QWidget()
        self.welcomeScreen.setObjectName("welcomeScreen")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.welcomeScreen)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 80, 261, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.registerButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.registerButton.setFont(font)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.registerButton)
        self.loginButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.label = QtWidgets.QLabel(self.welcomeScreen)
        self.label.setGeometry(QtCore.QRect(10, 10, 621, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        Welcome.addWidget(self.welcomeScreen)
        self.registerScreen = QtWidgets.QWidget()
        self.registerScreen.setObjectName("registerScreen")
        self.gridLayoutWidget = QtWidgets.QWidget(self.registerScreen)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 80, 531, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.userTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userTextEdit.sizePolicy().hasHeightForWidth())
        self.userTextEdit.setSizePolicy(sizePolicy)
        self.userTextEdit.setMaximumSize(QtCore.QSize(500, 26))
        self.userTextEdit.setObjectName("userTextEdit")
        self.gridLayout.addWidget(self.userTextEdit, 0, 1, 1, 1)
        self.passTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passTextEdit.sizePolicy().hasHeightForWidth())
        self.passTextEdit.setSizePolicy(sizePolicy)
        self.passTextEdit.setMaximumSize(QtCore.QSize(500, 26))
        self.passTextEdit.setObjectName("passTextEdit")
        self.gridLayout.addWidget(self.passTextEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.registerScreen)
        self.pushButton.setGeometry(QtCore.QRect(240, 200, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.registerScreen)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 621, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        Welcome.addWidget(self.registerScreen)
        self.loginScreen = QtWidgets.QWidget()
        self.loginScreen.setObjectName("loginScreen")
        self.pushButton_2 = QtWidgets.QPushButton(self.loginScreen)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 200, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.loginScreen)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 621, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.loginScreen)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 80, 531, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.userTextEdit_2 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userTextEdit_2.sizePolicy().hasHeightForWidth())
        self.userTextEdit_2.setSizePolicy(sizePolicy)
        self.userTextEdit_2.setMaximumSize(QtCore.QSize(500, 26))
        self.userTextEdit_2.setObjectName("userTextEdit_2")
        self.gridLayout_2.addWidget(self.userTextEdit_2, 0, 1, 1, 1)
        self.passTextEdit_2 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passTextEdit_2.sizePolicy().hasHeightForWidth())
        self.passTextEdit_2.setSizePolicy(sizePolicy)
        self.passTextEdit_2.setMaximumSize(QtCore.QSize(500, 26))
        self.passTextEdit_2.setObjectName("passTextEdit_2")
        self.gridLayout_2.addWidget(self.passTextEdit_2, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        Welcome.addWidget(self.loginScreen)

        self.retranslateUi(Welcome)
        Welcome.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Welcome)

    def retranslateUi(self, Welcome):
        _translate = QtCore.QCoreApplication.translate
        Welcome.setWindowTitle(_translate("Welcome", "Welcome!"))
        self.registerButton.setText(_translate("Welcome", "Register a new user"))
        self.loginButton.setText(_translate("Welcome", "Login as an existing user"))
        self.label.setText(_translate("Welcome", "Welcome to the SFWRENG 3K04 DCM Interface"))
        self.label_3.setText(_translate("Welcome", "Password:"))
        self.label_2.setText(_translate("Welcome", "Username:"))
        self.pushButton.setText(_translate("Welcome", "Register"))
        self.label_4.setText(_translate("Welcome", "Register new user"))
        self.pushButton_2.setText(_translate("Welcome", "Login"))
        self.label_5.setText(_translate("Welcome", "Login as an existing user"))
        self.label_6.setText(_translate("Welcome", "Password:"))
        self.label_7.setText(_translate("Welcome", "Username:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Welcome = QtWidgets.QStackedWidget()
    ui = Ui_Welcome()
    ui.setupUi(Welcome)
    Welcome.show()
    sys.exit(app.exec_())

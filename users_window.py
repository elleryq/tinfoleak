# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'users_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s


try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)


except AttributeError:

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1031, 634)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8("Output_Reports/img/tinfoleak-logo-o.jpg")),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 2)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tbl_users = QtWidgets.QTableWidget(self.frame)
        self.tbl_users.setEnabled(True)
        self.tbl_users.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tbl_users.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tbl_users.setAlternatingRowColors(False)
        self.tbl_users.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tbl_users.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_users.setRowCount(0)
        self.tbl_users.setColumnCount(10)
        self.tbl_users.setObjectName(_fromUtf8("tbl_users"))
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter
        )
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_users.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter
        )
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_users.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter
        )
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_users.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_users.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_users.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_users.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter
        )
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_users.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_users.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter
        )
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_users.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter
        )
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_users.setHorizontalHeaderItem(9, item)
        self.tbl_users.horizontalHeader().setDefaultSectionSize(150)
        self.gridLayout.addWidget(self.tbl_users, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 2)
        self.cb_all = QtWidgets.QCheckBox(Dialog)
        self.cb_all.setObjectName(_fromUtf8("cb_all"))
        self.gridLayout_2.addWidget(self.cb_all, 3, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 3, 1, 1, 1)
        self.lb_file = QtWidgets.QLabel(Dialog)
        self.lb_file.setGeometry(QtCore.QRect(140, 40, 871, 16))
        self.lb_file.setText(_fromUtf8(""))
        self.lb_file.setObjectName(_fromUtf8("lb_file"))
        self.lb_valid_users = QtWidgets.QLabel(Dialog)
        self.lb_valid_users.setGeometry(QtCore.QRect(140, 60, 57, 15))
        self.lb_valid_users.setText(_fromUtf8(""))
        self.lb_valid_users.setObjectName(_fromUtf8("lb_valid_users"))
        self.lb_invalid_users = QtWidgets.QLabel(Dialog)
        self.lb_invalid_users.setGeometry(QtCore.QRect(140, 80, 57, 15))
        self.lb_invalid_users.setObjectName(_fromUtf8("lb_invalid_users"))
        self.frame_2.raise_()
        self.buttonBox.raise_()
        self.label.raise_()
        self.lb_file.raise_()
        self.lb_valid_users.raise_()
        self.lb_invalid_users.raise_()
        self.cb_all.raise_()
        self.frame.raise_()

        self.retranslateUi(Dialog)
        # QtCore.QObject.connect(
        #     self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept
        # )
        self.buttonBox.accepted.connect(Dialog.accept)
        # QtCore.QObject.connect(
        #     self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject
        # )
        self.buttonBox.accepted.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "tinfoleak", None))
        self.label.setText(_translate("Dialog", "Select Target of Analysis", None))
        self.label_2.setText(_translate("Dialog", "File:", None))
        self.label_3.setText(_translate("Dialog", "Valid users:", None))
        self.label_4.setText(_translate("Dialog", "Invalid users:", None))
        item = self.tbl_users.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Select", None))
        item = self.tbl_users.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Profile image", None))
        item = self.tbl_users.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Background image", None))
        item = self.tbl_users.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Created at", None))
        item = self.tbl_users.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Screen name", None))
        item = self.tbl_users.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Name", None))
        item = self.tbl_users.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Protected", None))
        item = self.tbl_users.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Description", None))
        item = self.tbl_users.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "Followers", None))
        item = self.tbl_users.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "Friends", None))
        self.cb_all.setText(_translate("Dialog", "All", None))
        self.lb_invalid_users.setText(
            _translate("Dialog", "<html><head/><body><p><br/></p></body></html>", None)
        )

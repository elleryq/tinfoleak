# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'relations_window.ui'
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
        Dialog.resize(931, 563)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Output_Reports/img/tinfoleak-logo-o.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 11, 1, 1)
        self.cb_relations = QtWidgets.QCheckBox(self.frame)
        self.cb_relations.setChecked(False)
        self.cb_relations.setObjectName(_fromUtf8("cb_relations"))
        self.gridLayout.addWidget(self.cb_relations, 4, 13, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 8, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 10, 1, 1)
        self.cb_profile_images = QtWidgets.QCheckBox(self.frame)
        self.cb_profile_images.setChecked(True)
        self.cb_profile_images.setObjectName(_fromUtf8("cb_profile_images"))
        self.gridLayout.addWidget(self.cb_profile_images, 3, 13, 1, 1)
        self.pb_select_file_user2 = QtWidgets.QPushButton(self.frame)
        self.pb_select_file_user2.setObjectName(_fromUtf8("pb_select_file_user2"))
        self.gridLayout.addWidget(self.pb_select_file_user2, 4, 7, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout.addWidget(self.label_28, 4, 3, 1, 1)
        self.tb_username_2 = QtWidgets.QLineEdit(self.frame)
        self.tb_username_2.setStyleSheet(_fromUtf8(""))
        self.tb_username_2.setObjectName(_fromUtf8("tb_username_2"))
        self.gridLayout.addWidget(self.tb_username_2, 4, 6, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout.addWidget(self.label_30, 4, 5, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout.addWidget(self.label_29, 3, 5, 1, 1)
        self.tb_username = QtWidgets.QLineEdit(self.frame)
        self.tb_username.setStyleSheet(_fromUtf8(""))
        self.tb_username.setText(_fromUtf8(""))
        self.tb_username.setObjectName(_fromUtf8("tb_username"))
        self.gridLayout.addWidget(self.tb_username, 3, 6, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout.addWidget(self.label_27, 3, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 12, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 8, 1, 1)
        self.lb_file_user2 = QtWidgets.QLabel(self.frame)
        self.lb_file_user2.setText(_fromUtf8(""))
        self.lb_file_user2.setObjectName(_fromUtf8("lb_file_user2"))
        self.gridLayout.addWidget(self.lb_file_user2, 4, 9, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 2)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 3)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.tbl_relations = QtWidgets.QTableWidget(self.groupBox)
        self.tbl_relations.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tbl_relations.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tbl_relations.setObjectName(_fromUtf8("tbl_relations"))
        self.tbl_relations.setColumnCount(10)
        self.tbl_relations.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_relations.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_relations.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_relations.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_relations.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_relations.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_relations.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_relations.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_relations.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_relations.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_relations.setHorizontalHeaderItem(9, item)
        self.gridLayout_3.addWidget(self.tbl_relations, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 3)
        self.cb_all_user1 = QtWidgets.QCheckBox(Dialog)
        self.cb_all_user1.setObjectName(_fromUtf8("cb_all_user1"))
        self.gridLayout_4.addWidget(self.cb_all_user1, 2, 0, 1, 1)
        self.cb_all_user2 = QtWidgets.QCheckBox(Dialog)
        self.cb_all_user2.setObjectName(_fromUtf8("cb_all_user2"))
        self.gridLayout_4.addWidget(self.cb_all_user2, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_4.addWidget(self.buttonBox, 2, 2, 1, 1)

        self.retranslateUi(Dialog)
        # QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        self.buttonBox.accepted.connect(Dialog.accept)
        # QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "tinfoleak", None))
        self.cb_relations.setText(_translate("Dialog", "Relations", None))
        self.label_4.setText(_translate("Dialog", "File:", None))
        self.cb_profile_images.setText(_translate("Dialog", "Profile images", None))
        self.pb_select_file_user2.setText(_translate("Dialog", "Select file", None))
        self.label_28.setText(_translate("Dialog", "User 2", None))
        self.label_30.setText(_translate("Dialog", "@", None))
        self.label_29.setText(_translate("Dialog", "@", None))
        self.label_27.setText(_translate("Dialog", "User 1", None))
        self.label_3.setText(_translate("Dialog", "Users", None))
        self.label_2.setText(_translate("Dialog", "Relations", None))
        item = self.tbl_relations.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Select", None))
        item = self.tbl_relations.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Profile Image", None))
        item = self.tbl_relations.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Screen name", None))
        item = self.tbl_relations.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Name", None))
        item = self.tbl_relations.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Relation", None))
        item = self.tbl_relations.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Select", None))
        item = self.tbl_relations.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Profile Image", None))
        item = self.tbl_relations.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Screen name", None))
        item = self.tbl_relations.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "Name", None))
        item = self.tbl_relations.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "Hidden Relations Code", None))
        self.cb_all_user1.setText(_translate("Dialog", "All User 1", None))
        self.cb_all_user2.setText(_translate("Dialog", "All User 2", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/relations_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(931, 563)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./UI/Output_Reports/img/tinfoleak-logo-o.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 11, 1, 1)
        self.cb_relations = QtWidgets.QCheckBox(self.frame)
        self.cb_relations.setChecked(False)
        self.cb_relations.setObjectName("cb_relations")
        self.gridLayout.addWidget(self.cb_relations, 4, 13, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 8, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 10, 1, 1)
        self.cb_profile_images = QtWidgets.QCheckBox(self.frame)
        self.cb_profile_images.setChecked(True)
        self.cb_profile_images.setObjectName("cb_profile_images")
        self.gridLayout.addWidget(self.cb_profile_images, 3, 13, 1, 1)
        self.pb_select_file_user2 = QtWidgets.QPushButton(self.frame)
        self.pb_select_file_user2.setObjectName("pb_select_file_user2")
        self.gridLayout.addWidget(self.pb_select_file_user2, 4, 7, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 4, 3, 1, 1)
        self.tb_username_2 = QtWidgets.QLineEdit(self.frame)
        self.tb_username_2.setStyleSheet("")
        self.tb_username_2.setObjectName("tb_username_2")
        self.gridLayout.addWidget(self.tb_username_2, 4, 6, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 4, 5, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 3, 5, 1, 1)
        self.tb_username = QtWidgets.QLineEdit(self.frame)
        self.tb_username.setStyleSheet("")
        self.tb_username.setText("")
        self.tb_username.setObjectName("tb_username")
        self.gridLayout.addWidget(self.tb_username, 3, 6, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 3, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 12, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 8, 1, 1)
        self.lb_file_user2 = QtWidgets.QLabel(self.frame)
        self.lb_file_user2.setText("")
        self.lb_file_user2.setObjectName("lb_file_user2")
        self.gridLayout.addWidget(self.lb_file_user2, 4, 9, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 2)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 3)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.tbl_relations = QtWidgets.QTableWidget(self.groupBox)
        self.tbl_relations.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tbl_relations.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tbl_relations.setObjectName("tbl_relations")
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
        self.cb_all_user1.setObjectName("cb_all_user1")
        self.gridLayout_4.addWidget(self.cb_all_user1, 2, 0, 1, 1)
        self.cb_all_user2 = QtWidgets.QCheckBox(Dialog)
        self.cb_all_user2.setObjectName("cb_all_user2")
        self.gridLayout_4.addWidget(self.cb_all_user2, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_4.addWidget(self.buttonBox, 2, 2, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "tinfoleak"))
        self.cb_relations.setText(_translate("Dialog", "Relations"))
        self.label_4.setText(_translate("Dialog", "File:"))
        self.cb_profile_images.setText(_translate("Dialog", "Profile images"))
        self.pb_select_file_user2.setText(_translate("Dialog", "Select file"))
        self.label_28.setText(_translate("Dialog", "User 2"))
        self.label_30.setText(_translate("Dialog", "@"))
        self.label_29.setText(_translate("Dialog", "@"))
        self.label_27.setText(_translate("Dialog", "User 1"))
        self.label_3.setText(_translate("Dialog", "Users"))
        self.label_2.setText(_translate("Dialog", "Relations"))
        item = self.tbl_relations.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Select"))
        item = self.tbl_relations.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Profile Image"))
        item = self.tbl_relations.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Screen name"))
        item = self.tbl_relations.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Name"))
        item = self.tbl_relations.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Relation"))
        item = self.tbl_relations.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Select"))
        item = self.tbl_relations.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Profile Image"))
        item = self.tbl_relations.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Screen name"))
        item = self.tbl_relations.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "Name"))
        item = self.tbl_relations.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "Hidden Relations Code"))
        self.cb_all_user1.setText(_translate("Dialog", "All User 1"))
        self.cb_all_user2.setText(_translate("Dialog", "All User 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

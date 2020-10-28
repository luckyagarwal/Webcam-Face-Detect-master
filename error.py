# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_e(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.direct = QtWidgets.QLabel(Dialog)
        self.direct.setGeometry(QtCore.QRect(50, 140, 311, 111))
        self.direct.setObjectName("direct")
        self.error_msg = QtWidgets.QLabel(Dialog)
        self.error_msg.setGeometry(QtCore.QRect(57, 60, 291, 61))
        self.error_msg.setObjectName("error_msg")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.direct.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#aa0000;\">Name</span>:  without capslock</p><p><span style=\" font-weight:600; color:#aa0000;\">Coer_id</span>:  only numeric</p><p><span style=\" font-weight:600; color:#aa0000;\">Branch</span>:  short in capital wthout special character</p></body></html>"))
        self.error_msg.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0055ff;\">INVALID ENTRY!!</span></p></body></html>"))



"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
"""
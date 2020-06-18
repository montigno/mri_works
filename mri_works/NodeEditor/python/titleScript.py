##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################


from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel,\
    QPushButton, QCheckBox, QLineEdit


class changeTitle(QDialog):
    def __init__(self, nameBlock, unit, parent=None):
        super(changeTitle, self).__init__(parent)
        self.setWindowTitle('Title change')
        self.setWindowFlags(self.windowFlags() &
                            QtCore.Qt.WindowCloseButtonHint)
        self.adjustSize()

        self.vbox = QVBoxLayout(self)

        hbox = QHBoxLayout()
        label = QLabel("Script Name : ")
        hbox.addWidget(label)
        self.title = QLineEdit(nameBlock)
        self.title.setAlignment(QtCore.Qt.AlignTop)
        hbox.addWidget(self.title)
        hbox2 = QHBoxLayout()
        label = QLabel("Script Unit : ")
        hbox2.addWidget(label)
        label = QLineEdit(unit)
        label.setDisabled(True)
        label.setAlignment(QtCore.Qt.AlignTop)
        hbox2.addWidget(label)
        self.vbox.addLayout(hbox)
        self.vbox.addLayout(hbox2)

        buttonOk = QPushButton('Ok', self)
        buttonCancel = QPushButton('Cancel', self)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(buttonOk)
        hbox4.addWidget(buttonCancel)

        self.vbox.addLayout(hbox4)

        self.setLayout(self.vbox)

        buttonOk.clicked.connect(self.OK)
        buttonCancel.clicked.connect(self.CANCEL)

    def CANCEL(self):
        self.close()

    def OK(self):
        self.close()

    def getNewValues(self):
        return self.title.text()

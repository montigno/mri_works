##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################


from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, \
    QPushButton, QComboBox, QLineEdit


class errorHandler(QDialog):
    def __init__(self, nameBlock, unit, parent=None):
        super(errorHandler, self).__init__(parent)
        self.setWindowTitle('Error handling')

        self.vbox = QVBoxLayout(self)

        hbox = QHBoxLayout(self)
        label = QLabel("Block Name : ")
        hbox.addWidget(label)
        label = QLineEdit(nameBlock)
        label.setDisabled(True)
        label.setAlignment(QtCore.Qt.AlignTop)
        hbox.addWidget(label)

        hbox2 = QHBoxLayout(self)
        label = QLabel("Block Unit : ")
        hbox2.addWidget(label)
        label = QLineEdit(unit)
        label.setDisabled(True)
        label.setAlignment(QtCore.Qt.AlignTop)
        hbox2.addWidget(label)

        hbox3 = QHBoxLayout(self)
        label = QLabel("What to do ? : ")
        hbox3.addWidget(label)
        self.cb = QComboBox()
        self.cb.addItem('Stop pipeline')
        self.cb.addItem('restart this modul with default entries')
        self.cb.currentIndexChanged.connect(self.selectionChange)
        hbox3.addWidget(self.cb)

        self.vbox.addLayout(hbox)
        self.vbox.addLayout(hbox2)
        self.vbox.addLayout(hbox3)

        button = QPushButton('Ok', self)
        self.vbox.addWidget(button)

        self.setLayout(self.vbox)

        button.clicked.connect(self.OK)

    def OK(self):
        self.listVal = []
        self.close()

    def selectionChange(self, i):
        self.answ = self.cb.currentText()

    def getNewValues(self):
        return self.answ

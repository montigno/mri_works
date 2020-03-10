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


class editParamLoopFor(QDialog):
    def __init__(self, nameBlock, unit, parent=None):
        super(editParamLoopFor, self).__init__(parent)
        self.setWindowTitle('Parameters Loop For')
        self.setWindowFlags(self.windowFlags() &
                            QtCore.Qt.WindowCloseButtonHint)
        self.adjustSize()
        checkedTo = False
        if '*' in unit:
            checkedTo = True

        self.vbox = QVBoxLayout(self)

        hbox = QHBoxLayout()
        label = QLabel("Block Name : ")
        hbox.addWidget(label)
        label = QLineEdit(nameBlock)
        label.setDisabled(True)
        label.setAlignment(QtCore.Qt.AlignTop)
        hbox.addWidget(label)
        hbox2 = QHBoxLayout()
        label = QLabel("Block Unit : ")
        hbox2.addWidget(label)
        label = QLineEdit(unit)
        label.setDisabled(True)
        label.setAlignment(QtCore.Qt.AlignTop)
        hbox2.addWidget(label)
        hbox3 = QHBoxLayout()
        self.multiproc = QCheckBox("Multiprocessing", self)
        self.multiproc.setChecked(checkedTo)
        hbox3.addWidget(self.multiproc)
        self.vbox.addLayout(hbox)
        self.vbox.addLayout(hbox2)
        self.vbox.addLayout(hbox3)

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
        return self.multiproc.isChecked()

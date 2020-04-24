##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit,\
    QPushButton, QComboBox
from PyQt5 import QtCore

class define_inputs_outputs(QDialog):
    def __init__(self, unit, typeport, parent=None):
        super(define_inputs_outputs, self).__init__(parent)
        self.typeport = typeport
        listformat = ["int", "float", "str", "path", "bool", "dict", "tuple"]
        listdim = ["", "list", "array"]
        
        self.vbox = QVBoxLayout(self)

        hbox = QHBoxLayout()
        label = QLabel("Script Unit : ")
        hbox.addWidget(label)
        label = QLineEdit(unit)
        label.setDisabled(True)
        label.setAlignment(QtCore.Qt.AlignTop)
        hbox.addWidget(label)
        
        hbox2 = QHBoxLayout()
        label = QLabel("Name "+typeport+" port : ")
        hbox2.addWidget(label)
        self.portName = QLineEdit()
        label.setAlignment(QtCore.Qt.AlignTop)
        hbox2.addWidget(self.portName)
        
        hbox3 = QHBoxLayout()
        self.comboFormat = QComboBox(self)
        self.comboFormat.addItems(listformat)
        self.comboDim = QComboBox(self)
        self.comboDim.addItems(listdim)
        hbox3.addWidget(self.comboDim)
        hbox3.addWidget(self.comboFormat)
        buttonOk = QPushButton('Ok', self)
        buttonCancel = QPushButton('Cancel', self)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(buttonOk)
        hbox4.addWidget(buttonCancel)

        buttonOk.clicked.connect(self.OK)
        buttonCancel.clicked.connect(self.CANCEL)
        
        self.vbox.addLayout(hbox)
        self.vbox.addLayout(hbox2)
        self.vbox.addLayout(hbox3)
        self.vbox.addLayout(hbox4)
        self.info = QLabel()
        self.vbox.addWidget(self.info)
        
    def OK(self):
        self.format = []
        if not self.portName.text():
            self.info.setText("<span style=\" \
                                            font-size:10pt; \
                                            color:#cc0000;\" > error : Name "
                                            + self.typeport+
                                          " port  is empty </span>")
            return
        self.format.append(self.portName.text())
        if self.comboDim.currentText():
            self.format.append(self.comboDim.currentText()+'_'+
                                                       self.comboFormat.currentText() )
        else:
            self.format.append(self.comboFormat.currentText() )
        self.close()

    def CANCEL(self):
        self.format = []
        self.close()
        
    def getNewValues(self):
        return self.format
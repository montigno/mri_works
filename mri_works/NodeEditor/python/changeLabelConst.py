##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

from PyQt5 import QtCore
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QDialog, QLabel, QLineEdit, \
    QPushButton, QWidget, QGroupBox

class changeLabel(QDialog):
    def __init__(self,nameConn,unit,oldlab,parent=None):
        super(changeLabel, self).__init__(parent)

        self.setWindowTitle('Change Label Constant')
#         self.resize(630, 150)

        self.vbox = QVBoxLayout(self)

        hbox = QHBoxLayout()
        label=QLabel("Constant Name : ")
        hbox.addWidget(label)
        label=QLineEdit(nameConn)
        label.setDisabled(True)
        label.setAlignment(QtCore.Qt.AlignTop)
        hbox.addWidget(label)
        hbox2 = QHBoxLayout()
        label=QLabel("Constant Unit : ")
        hbox2.addWidget(label)
        label=QLineEdit(unit)
        label.setDisabled(True)
        label.setAlignment(QtCore.Qt.AlignTop)
        hbox2.addWidget(label)
        self.vbox.addLayout(hbox)
        self.vbox.addLayout(hbox2)
        hbox3=QHBoxLayout()
        label=QLabel("Label")
        lab = QLineEdit(oldlab)
        self.zoneline = lab
        hbox3.addWidget(label)
        hbox3.addWidget(self.zoneline)
        self.vbox.addLayout(hbox3)

        button = QPushButton('Ok', self)
        self.vbox.addWidget(button)
        
        self.setLayout(self.vbox)

        button.clicked.connect(self.OK)

    def OK(self):
        self.listVal=str(self.zoneline.text())
        self.close()
   
    def getNewLabel(self):    
        return self.listVal
    
    
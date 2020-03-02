##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################


from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout,\
    QComboBox, QPushButton
from PyQt5 import QtCore

class defineTunnels(QDialog):
    def __init__(self,name,typeLoop,parent=None):
        super(defineTunnels, self).__init__(parent)
        self.setWindowTitle('Define input tunnels')
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.adjustSize()
       
        listformat=["int","float","str","path","bool"]
        
        if 'If' in typeLoop:
            self.list1=["array","list","simple"]
            self.list2=["array","list","simple"]
        else:
            if 'in' in name:
                self.list1=["array","list"]
                self.list2=["list","simple"]
            else:
                self.list1=["list","simple"]
                self.list2=["array","list"]                   
        
        self.vbox = QVBoxLayout(self)       

        hbox = QHBoxLayout()
        label=QLabel("Tunnel Name : ")
        hbox.addWidget(label)
        label=QLineEdit(name)
        label.setDisabled(True)
        label.setAlignment(QtCore.Qt.AlignTop)
        hbox.addWidget(label)
        
        hbox2 = QHBoxLayout()
        self.comboFormat = QComboBox(self)
        self.comboFormat.addItems(listformat)

        hbox2.addWidget(self.comboFormat)
        
        hbox3 = QHBoxLayout()
        label=QLabel("Format left Tunnel ")
        hbox3.addWidget(label)
        self. comboLeft = QComboBox(self)
        self.comboLeft.addItems(self.list1)
        self.comboLeft.currentIndexChanged.connect(self.changeComboRight)
        hbox3.addWidget(self.comboLeft)
        
        hbox4 = QHBoxLayout()
        label=QLabel("Format right Tunnel ")
        hbox4.addWidget(label)
        self.comboRight = QLineEdit(self.list2[0])
        self.comboRight.setEnabled(False)
        hbox4.addWidget(self.comboRight)
        
        buttonOk = QPushButton('Ok', self)
        buttonCancel = QPushButton('Cancel', self)
        hbox5=QHBoxLayout()
        hbox5.addWidget(buttonOk)
        hbox5.addWidget(buttonCancel)
        
        buttonOk.clicked.connect(self.OK)
        buttonCancel.clicked.connect(self.CANCEL)
        
        self.vbox.addLayout(hbox)
        self.vbox.addLayout(hbox2)
        self.vbox.addLayout(hbox3)
        self.vbox.addLayout(hbox4)
        self.vbox.addLayout(hbox5)
   
    def changeComboRight(self):
        indice = self.comboLeft.currentIndex()
        self.comboRight.setText(self.list2[indice])
        
    def OK(self):
        self.format=[]
        self.format.append(self.comboFormat.currentText())
        self.format.append(self.comboLeft.currentText())
        self.format.append(self.comboRight.text())
        self.close()
             
    def CANCEL(self):
        self.format=[]
        self.close()
        
    def getNewValues(self):    
        return self.format
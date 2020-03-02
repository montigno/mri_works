##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################


from PyQt5.QtWidgets import QDialog, QTextEdit, QVBoxLayout, QWidget,\
    QScrollArea, QHBoxLayout, QPushButton
from PyQt5 import QtCore

class editCombobox(QDialog):
    def __init__(self,itemsList,parent=None):
        super(editCombobox, self).__init__(parent)
        self.listVal = itemsList
        self.setWindowTitle('Edit Combobox')
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.adjustSize()
        
        vbox = QVBoxLayout(self)
        self.txtEdit = QTextEdit()
        self.txtEdit.setPlainText("\n".join(itemsList))
        vbox.addWidget(self.txtEdit)
        
        buttonOk = QPushButton('Ok', self)
        buttonCancel = QPushButton('Cancel', self)
        hbox4=QHBoxLayout()
        hbox4.addWidget(buttonOk)
        hbox4.addWidget(buttonCancel)
        
        vbox.addLayout(hbox4)

        buttonOk.clicked.connect(self.OK)
        buttonCancel.clicked.connect(self.CANCEL)

    def CANCEL(self):
        self.answer = "cancel"
        self.close()
        
    def OK(self):
        self.listVal=self.txtEdit.toPlainText().split('\n')
        self.answer = "ok"
        self.close()
        
    def getNewList(self):    
        return self.listVal
    
    def getAnswer(self):
        return self.answer
        

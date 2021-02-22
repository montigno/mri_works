##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox,\
    QButtonGroup, QCheckBox, QPushButton, QLineEdit
from PyQt5 import QtCore

class multiple_execution(QDialog):
    def __init__(self, listDiagram, parent=None):
        super(multiple_execution, self).__init__(parent)
        self.setWindowTitle('Multiple execution')
        self.setWindowFlags(self.windowFlags() &
                            QtCore.Qt.WindowCloseButtonHint)
        self.listVal = []
        self.adjustSize()
        vbox = QVBoxLayout(self)
        self.zonecombo = []
        for i, lst in enumerate(listDiagram):
            lab = QLabel('Pipeline '+str(i))
            comb = QComboBox(self)
            comb.addItems(listDiagram)
            comb.setCurrentIndex(i)
            self.zonecombo.append(comb)
            hbox = QHBoxLayout()
            hbox.addWidget(lab)
            hbox.addWidget(comb)
            vbox.addLayout(hbox)
        self.a = QCheckBox('run sequentially')
        self.a.setChecked(True)
        self.b = QCheckBox('run sequentially in Threading mode')
        self.c = QCheckBox('run in multiprocessing mode')
        cs = QButtonGroup(self)
        cs.addButton(self.a)
        cs.addButton(self.b)
        cs.addButton(self.c)
        vbox.addWidget(self.a)
        vbox.addWidget(self.b)
        vbox.addWidget(self.c)
    
        buttonGo = QPushButton('Go!', self)
        buttonCancel = QPushButton('Cancel', self)
        hboxbutton = QHBoxLayout()
        hboxbutton.addWidget(buttonGo)
        hboxbutton.addWidget(buttonCancel)
        vbox.addLayout(hboxbutton)

        buttonGo.clicked.connect(self.GO)
        buttonCancel.clicked.connect(self.CANCEL)
            
    def CANCEL(self):
        self.close()

    def GO(self):
        for lst_comb in self.zonecombo:
            self.listVal.append(lst_comb.currentText())
        self.listVal.append(self.a.isChecked())
        self.listVal.append(self.b.isChecked())
        self.listVal.append(self.c.isChecked())
        self.close()
        
    def closeEvent(self, event):
        return QDialog.closeEvent(self, event)

    def getNewValues(self):
        return self.listVal
##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

import os
import numpy
from PyQt5 import QtCore
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QDialog, QLabel, \
    QPushButton, QWidget, QGroupBox, QComboBox, QScrollArea, QLineEdit
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import Qt


class editParam(QDialog):

    def __init__(self, nameBlock, unit, inout, valInit, parent=None):
        super(editParam, self).__init__(parent)
        self.inout = inout
        self.setWindowTitle('Input parameters')
        self.setWindowFlags(self.windowFlags() &
                            QtCore.Qt.WindowCloseButtonHint)
        self.setMinimumWidth(280)

        nIn = len(inout[0])
        self.listField = {}
        for i in range(0, nIn):
            self.listField[inout[0][i]] = DefinitType(valInit[i]).returntype()

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
        self.vbox.addLayout(hbox)
        self.vbox.addLayout(hbox2)

        scrolllayout = QVBoxLayout()

        scrollwidget = QWidget()
        scrollwidget.setLayout(scrolllayout)

        scroll = QScrollArea()
#         scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(scrollwidget)
        scroll.setMinimumWidth(200)

        self.label = []
        self.zoneline = []
        palette = QPalette()
        font = QFont("Times", 10)
        font.setBold(True)
        for i in range(len(inout[0])):
            hbox3 = QHBoxLayout()
            label = QLabel(inout[0][i])
            if ('enumerate' not in self.listField[inout[0][i]] and
                self.listField[inout[0][i]] != 'bool') or (
                    'Node(' in str(inout[1][i])):
                lab = QLineEdit()
                lab.setText(str(inout[1][i]))
                lab.setFont(font)
                if 'Node(' in lab.text():
                    lab.setReadOnly(True)
                    self.listField[inout[0][i]] = 'str'
                    palette.setColor(QPalette.Text, QtCore.Qt.darkGray)
                else:
                    palette.setColor(QPalette.Text, QtCore.Qt.blue)
                lab.setPalette(palette)
                self.label.append(inout[0][i])
                self.zoneline.append(lab)
                hbox3.addWidget(label)
                hbox3.addWidget(self.zoneline[i])
                scrolllayout.addLayout(hbox3)
            else:
                lab = QComboBox()
                lab.setMinimumWidth(self.size().width() / 4)
                if self.listField[inout[0][i]] == 'bool':
                    lab.addItem('True')
                    lab.addItem('False')
                else:
                    for it in list(eval(valInit[i])):
                        lab.addItem(it[1])
#                         lab.addItem(str(it))
                index = lab.findText(str(inout[1][i]), Qt.MatchFixedString)
                if index >= 0:
                    lab.setCurrentIndex(index)
                lab.setFont(font)
                palette.setColor(QPalette.Text, QtCore.Qt.blue)
                lab.setPalette(palette)
                self.label.append(inout[0][i])
                self.zoneline.append(lab)
                hbox3.addWidget(label)
                hbox3.addWidget(self.zoneline[i])
                scrolllayout.addLayout(hbox3)
        self.vbox.addWidget(scroll)

        self.info = QLabel()
        self.vbox.addWidget(self.info)

        buttonOk = QPushButton('Ok', self)
        buttonCancel = QPushButton('Cancel', self)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(buttonOk)
        hbox4.addWidget(buttonCancel)

        self.vbox.addLayout(hbox4)

#         self.setLayout(self.vbox)

        self.adjustSize()

        buttonOk.clicked.connect(self.OK)
        buttonCancel.clicked.connect(self.CANCEL)

    def CANCEL(self):
        self.listVal = self.inout[1]
        self.close()

    def OK(self):
        self.listVal = []

        for index, i in enumerate(self.zoneline):

            if type(i) == QComboBox:
                try:
                    self.listVal.append(eval(i.currentText()))
                except (SyntaxError,
                        NameError,
                        TypeError,
                        ZeroDivisionError):
                    self.listVal.append(i.currentText())

            else:
                if i.text():
                    try:
                        tmp = eval(i.text())
                    except (SyntaxError,
                            NameError,
                            TypeError,
                            ZeroDivisionError):
                        tmp = i.text()
                else:
                    tmp = ''

                if (self.listField[self.label[index]] == 'path' and
                        tmp not in 'path'):
                    if not os.path.exists(tmp):
                        self.info.setText("<span style=\" \
                                            font-size:10pt; \
                                            color:#cc0000;\" > error :"
                                          + self.label[index] +
                                          " does't seems exist </span>")
                        return
                    else:
                        self.listVal.append(tmp)

                elif (DefinitType(tmp).returntype() !=
                        self.listField[self.label[index]]):
                    self.info.setText("<span style=\" \
                                        font-size:10pt; \
                                        color:#cc0000;\" > error :"
                                      + self.label[index] + " must be "
                                      + self.listField[self.label[index]]
                                      + "</span>")
                    return
                else:
                    self.listVal.append(tmp)
        self.close()

    def closeEvent(self, event):
        return QDialog.closeEvent(self, event)

    def getNewValues(self):
        return self.listVal


class DefinitType:

    def __init__(self, var):
        self.var = var

    def returntype(self):
        if self.var == 'path':
            typVal = 'path'
        else:
            typVal = type(self.var).__name__
        typVar = ''
        if type(self.var).__name__ in 'list':
            if len(numpy.shape(self.var)) == 1:
                typVar = 'list'
                typVal = self.isPath(self.var[0])
            elif len(numpy.shape(self.var)) == 2:
                typVar = 'array'
                typVal = self.isPath(self.var[0][0])
            elif len(numpy.shape(self.var)) == 3:
                typVar = 'array'
                typVal = self.isPath(self.var[0][0][0])

        elif type(self.var).__name__ in 'tuple':
            typVar = 'tuple'
            typVal = self.isPath(self.var[0])

        elif type(self.var).__name__ in 'str':
            if 'enumerate' in self.var:
                typVar = 'enumerate'
                typVal = 'str'
        return typVar + typVal

    def isPath(self, varble):
        if type(varble).__name__ == 'str':
            if 'path' in varble:
                return 'path'
            else:
                return type(varble).__name__
        else:
            return type(varble).__name__

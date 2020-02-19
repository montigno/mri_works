##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################


import os
import yaml
from PyQt5.QtWidgets import QDialog, QCheckBox, QVBoxLayout, QHBoxLayout, QTextEdit, \
    QLabel, QPushButton, QScrollArea, QWidget, QMenuBar, QAction, QPlainTextEdit
from PyQt5.QtCore import QDir
from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QScrollBar
from PyQt5.QtGui import QFontMetrics


class chOptions(QDialog):

    def __init__(self, pathYaml, nameclass, ports, parent=None):
        super(chOptions, self).__init__(parent)
               
        doc = "No description"
        try :
            if '_' in nameclass:
                firstAttr = nameclass[0:nameclass.index("_")]
                secondAttr = nameclass[nameclass.index("_") + 1:]
                TxtToExecute = firstAttr + "." + secondAttr + "().help(True)"

            else:
                firstAttr = nameclass
                secondAttr = ''
                TxtToExecute = firstAttr + ".help(True)"
               
            TxtToImport = "from nipype.interfaces import " + firstAttr
            
            exec(TxtToImport)
            doc = eval(TxtToExecute)
            doc = doc[doc.index('[Optional]') + 11:doc.index('Outputs')]
        except:
            doc = "No description"

        self.nameclass = nameclass
        self.poqs = ports
        
        self.labels_inputs = self.poqs[0]
        self.values_inputs = self.poqs[1]
        
#         print(self)
#         print('self.labels_inputs , self.values_inputs',self.labels_inputs," , ",self.values_inputs)
        
        self.setWindowTitle('choose options input')
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        
        menubar = QMenuBar()
        checkAll = QAction('Check all options', self)
        checkAll.setShortcut('Ctrl+A')
        menubar.addAction(checkAll)
        checkAll.triggered.connect(self.checkAllOptions)
        
        uncheckAll = QAction('Uncheck all options', self)
        uncheckAll.setShortcut('Ctrl+U')
        menubar.addAction(uncheckAll)
        uncheckAll.triggered.connect(self.uncheckAllOptions)
        
        self.listCh = []
        
        vbox = QVBoxLayout(self)
        vbox.addWidget(menubar)

        _ss = ports
        
        self.list1 = []
        self.list2 = []
        self.list3 = []
        
        for tr in _ss[0]:
            self.list1.append(tr)

        for tr in _ss[1]:
            self.list2.append(tr)
            self.list3.append(tr)

        scrolllayout = QVBoxLayout()

        scrollwidget = QWidget()
        scrollwidget.setLayout(scrolllayout)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(scrollwidget)

        desc = QPlainTextEdit()
        desc.setPlainText(doc)
        desc.setReadOnly(True)
        desc.setLineWrapMode(True)
        
        font = desc.document().defaultFont()
        fontMetrics = QFontMetrics(font)
        textSize = fontMetrics.size(0, doc)

        textWidth = textSize.width() + 30
        textHeight = textSize.height() + 30

        desc.setMinimumSize(textWidth, textHeight)
        desc.resize(textWidth, textHeight)
         
        hbox2 = QHBoxLayout()
      
        vbox2 = QVBoxLayout()
        with open(pathYaml, 'r') as stream:
            try:
                self.dicts = yaml.load(stream, yaml.FullLoader)
                for el in self.dicts[nameclass]:
                    checkedTo = False
                    enableTo = True
                    if el in self.list1:
                        ind = self.list1.index(el)
#                         print('list1,list2,list3 = ',el," , ",self.list2[ind]," , ",self.list3[ind])
                        self.list1.remove(el)
                        if 'Node(' in str(self.list2[ind]):
                            enableTo = False
                        vals = self.list2[ind]
                        del self.list2[ind]
                        del self.list3[ind]
                        checkedTo = True
                    b = QCheckBox(el, self)
                    b.setChecked(checkedTo)
                    b.setEnabled(enableTo)
                    self.listCh.append(b)
                    vbox2.addWidget(self.listCh[-1])
            except yaml.YAMLError as exc:
                print('yamlerror', exc)
                return
            
        hbox2.addLayout(vbox2)
        hbox2.addWidget(desc)

        scrolllayout.addLayout(hbox2)
         
        vbox.addWidget(scroll)
        buttonOk = QPushButton('Ok', self)
        buttonCancel = QPushButton('Cancel', self)
        hboxButton = QHBoxLayout()
        hboxButton.addWidget(buttonOk)
        hboxButton.addWidget(buttonCancel)
        vbox.addLayout(hboxButton)
                
        self.setMinimumWidth(800)        
        buttonOk.clicked.connect(self.go)
        buttonCancel.clicked.connect(self.CANCEL)
        
    def CANCEL(self):
        self.answer = "cancel"
        self.close()

    def go(self):

        for aze in self.listCh:
            if aze.isChecked():
                txt = aze.text()
                self.list1.append(str(txt))
                
                valueExists = False
                val = ''
                ind = 0
                
                try:
                    ind = self.labels_inputs.index(txt)
#                     print("type ? ",type(self.values_inputs[ind]).__name__)
                    if 'Node(' in str(self.values_inputs[ind]):
                        val = self.values_inputs[ind]
                        valueExists = True
                except:
                    pass
                
#                 print('valueexist ? :',valueExists,' , ',txt,' , ',ind,' , ',val)
                
                if not valueExists:
             
                    if type(self.dicts[self.nameclass][aze.text()]).__name__ == 'str':
                        if 'enumerate' in self.dicts[self.nameclass][aze.text()]:
                            imb = self.dicts[self.nameclass][aze.text()]
                        else:
                            try:
                                imb = eval(self.dicts[self.nameclass][aze.text()])
                            except:
                                imb = self.dicts[self.nameclass][aze.text()]
                    else:
                        try:
                            imb = eval(self.dicts[self.nameclass][aze.text()])
                        except:
                            imb = self.dicts[self.nameclass][aze.text()]
    #                 self.list3.append(imb)
                    _imb1 = imb
    #                 if type(imb).__name__ == 'tuple':
    #                     self.list2.append(_imb1[0])
                    if type(imb).__name__ == 'str':
                        if 'enumerate' in imb:
                            self.list2.append(list(eval(_imb1))[0][1])
                        else:
                            self.list2.append(_imb1)
    #                     self.list2.append(_imb1[0])
                    else:
                        self.list2.append(_imb1)
    #                     self.list2.append(_imb1)
                    self.list3.append(imb)
    #                 self.list3.append(imb)
   
                else:
                    self.list2.append(val)
   
            else:
                if aze.text() in self.list1:
                    ind = self.list1.index(aze.text())
                    self.list1.remove(aze.text())
                    del self.list2[ind]
                    del self.list3[ind]
        
        self.newports = (self.list1, self.list2, self.poqs[2], self.poqs[3])
#         print('newports ',self.newports)
        self.close()
        self.answer = "ok"

    def getNewValues(self):    
        return self.newports, list(self.list3)
    
    def getAnswer(self):
        return self.answer
    
    def checkAllOptions(self):
        for aze in self.listCh:
            aze.setChecked(True)
            
    def uncheckAllOptions(self):
        for aze in self.listCh:
            if aze.isEnabled():
                aze.setChecked(False)        
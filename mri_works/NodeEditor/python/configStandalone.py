##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################


import os
import yaml
import collections
from PyQt5.QtWidgets import QWidget, QDialog, QTabWidget, \
    QVBoxLayout, QLineEdit, QHBoxLayout, QFormLayout, QLabel, QPushButton, \
    QFileDialog
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import QDir


class ConfigModuls():

    global config
    config = {}

    def loadConfig(self, listStand):

        pathConfig = os.path.dirname(__file__)
        pathConfig, last = os.path.split(pathConfig)
        pathConfig = os.path.join(pathConfig,
                                  'python',
                                  'config_standalone.yml')
        if os.path.exists(pathConfig):
            with open(pathConfig, 'r') as stream:
                try:
                    tmp = yaml.load(stream, yaml.FullLoader)
                    for it in listStand:
                        if it in tmp.keys():
                            config[it] = self.checkPathStandalone(tmp[it])
                        else:
                            config[it] = ''
                except yaml.YAMLError as exc:
                    return
        else:
            print('no standalone yaml found')
            return

        self.saveConfig()

    def checkPathStandalone(self, pathStand):
        if os.path.exists(pathStand):
            return pathStand
        else:
            return ''

    def getPathConfig(self, cat):
        return config[cat]

    def saveConfig(self):
        fileConfig = os.path.join(QDir.currentPath(),
                                  'NodeEditor',
                                  'python',
                                  'config_standalone.yml')
        with open(fileConfig, 'w', encoding='utf8') as configfile:
            yaml.dump(config,
                      configfile,
                      default_flow_style=False,
                      allow_unicode=True)


class windowConfig(QDialog):

    def __init__(self, parent=None):
        super(windowConfig, self).__init__(parent)
        self.resize(500, 200)
        self.move(300, 300)
        self.currentTab = 0
        self.labpath = []
        self.setWindowTitle('Setting standalone paths')
        self.tab = QTabWidget()
        self.tab.setStyleSheet('''
                            QTabBar::tab {font-size: 8pt;
                                          font-family:Times;
                                          font:italic;
                                          width: 100px;
                                          height: 30px;
                                          background-color: lightGray;}
                            QTabBar::tab:selected {background-color: gray;}
                                                        ''')
        self.tab.currentChanged.connect(self.tabSelected)
        inc = 0
        for elem in config:
            self.tab.addTab(self.field(elem, inc), elem)
            inc += 1
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.tab)

        buttonOk = QPushButton('Ok', self)
        buttonCancel = QPushButton('Cancel', self)

        hbox = QHBoxLayout()
        hbox.addWidget(buttonOk)
        hbox.addWidget(buttonCancel)

        vbox.addLayout(hbox)

        buttonOk.clicked.connect(self.OK)
        buttonCancel.clicked.connect(self.CANCEL)

        self.setLayout(vbox)
        self.show()

    def field(self, elem, i):
        wd = QWidget()
        palette = QPalette()
        font = QFont("Times", 9)
#         font.setBold(True)
        layoutV = QVBoxLayout()

        layoutH = QHBoxLayout()
        label = QLabel("Path ")
        lbpath = QLineEdit()
        lbpath.setText(config.get(elem))
        lbpath.setFont(font)
        self.labpath.append(lbpath)
        btn = QPushButton("Dir")
        rep = btn.clicked.connect(self.handle)
        layoutH.addWidget(label)
        layoutH.addWidget(self.labpath[i])
        layoutH.addWidget(btn)

        layoutV.addLayout(layoutH)

        wd.setLayout(layoutV)
        return wd

    def handle(self):
        currentTab = self.tab.currentIndex()
        tit = self.tab.tabText(currentTab)
        file = QFileDialog.getOpenFileName(self,
                                           "Choose " + tit,
                                           config.get(tit),
                                           '',
                                           None,
                                           QFileDialog.DontUseNativeDialog)
        self.labpath[self.currentTab].setText(file[0])

    def tabSelected(self, arg=None):
        self.currentTab = arg

    def CANCEL(self):
        self.close()

    def OK(self):
        for ik in range(0, self.tab.count()):
            self.tab.setCurrentIndex(ik)
            tabTxt = self.tab.tabText(ik)
            config[tabTxt] = self.labpath[ik].text()
        self.close()

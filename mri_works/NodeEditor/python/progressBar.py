##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QPushButton
from PyQt5.QtCore import QThread
from PyQt5 import QtCore
import time


class progressBar(QWidget):

    def __init__(self, parent=None):
        super(progressBar, self).__init__(parent)
        layout = QVBoxLayout(self)

        # Create a progress bar and a button and add them to the main layout
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(200, 80, 250, 25)

        self.progressBar.setRange(0, 1)
        layout.addWidget(self.progressBar)

        self.myLongTask = TaskThread()
        self.myLongTask.taskFinished.connect(self.onFinished)

        self.onStart()

    def onStart(self):
        self.progressBar.setRange(0, 0)
        self.myLongTask.start()

    def onFinished(self):
        # Stop the pulsation
        self.progressBar.setRange(0, 1)


class TaskThread(QThread):
    taskFinished = QtCore.pyqtSignal()

    def run(self):
        time.sleep(3)
        self.taskFinished.emit()

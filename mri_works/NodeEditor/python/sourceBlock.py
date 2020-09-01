##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################


import importlib
import inspect
import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QDialog, QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt


class seeCode(QDialog):
    def __init__(self, category, nameClass, parent=None):
        super(seeCode, self).__init__(parent)

        imp = importlib.import_module('NodeEditor.modules.'+category)
        importlib.reload(imp)

        src = category + ' , ' + nameClass

        for name, obj in inspect.getmembers(imp):
            if inspect.isclass(obj):
                if name == nameClass:
                    try:
                        src = inspect.getcomments(obj) + '\n'
                        src += inspect.getsource(obj)
                    except Exception as e:
                        src = inspect.getsource(obj)
                    break

        self.setWindowTitle('Source code of ' + nameClass)
        layout = QVBoxLayout()
        font = QFont("Times", 11, QFont.Bold)
        label = QLabel(src)
        label.setFont(font)
        label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        scroll = QScrollArea()
        # Set to make the inner widget resize with scroll area
        scroll.setWidgetResizable(True)
        scroll.setWidget(label)

        layout.addWidget(scroll)
        self.setLayout(layout)

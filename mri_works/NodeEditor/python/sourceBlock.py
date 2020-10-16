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
from NodeEditor.python.syntax import PythonHighlighter
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QDialog, QScrollArea, QTextEdit
from PyQt5.QtGui import QFont, QFontMetrics
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
        txt = QTextEdit()
        txt.setReadOnly(True)
        txt.setPlainText(src)
        PythonHighlighter(txt)
        font = txt.document().defaultFont()
        fontMetrics = QFontMetrics(font)
        textSize = fontMetrics.size(0, txt.toPlainText())
        w = textSize.width() + 10
        h = 250
        txt.setMinimumSize(w, h)
        txt.resize(w, h)

        layout.addWidget(txt)
        self.setLayout(layout)
        self.setMinimumWidth(w + 50)

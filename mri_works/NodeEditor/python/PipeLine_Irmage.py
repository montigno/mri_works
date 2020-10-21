##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

'''
Created on 14 december 2017
Modified on 21 oct. 2020
@author: omonti
'''

import os
import re
import webbrowser
import yaml
from enum import Enum
from math import atan, cos, sin
from collections import deque

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QByteArray, Qt, QStringListModel, QLineF, QPointF, \
    QRectF, QDir, QRect
from PyQt5.QtGui import QStandardItemModel, QPixmap, QPainterPath, \
    QCursor, QBrush, QStandardItem, QPen, QPainter, \
    QImage, QTransform, QColor, QFont, QPolygonF, QLinearGradient, \
    QKeySequence, QIcon, QFontMetrics, QTextCursor
from PyQt5.QtWidgets import QMenuBar, QTextEdit, QGraphicsScene, \
    QGraphicsView, QGraphicsPathItem, QGraphicsPolygonItem, \
    QGraphicsRectItem, QDialog, QSpinBox, QDoubleSpinBox, QComboBox, \
    QTreeView, QWidget, QVBoxLayout, QTabBar, QTabWidget, QSplitter, \
    QStylePainter, QStyleOptionTab, QStyle, QFileDialog, QSizePolicy, \
    QGraphicsItem, QMessageBox, QMenu, QAction, QHBoxLayout, QLabel, \
    QPushButton, QGraphicsProxyWidget, QGraphicsTextItem

from . import analyze
from . import execution
from . import editParam
from . import editParamLoopFor
from . import changeTitle
from . import chOptions
from . import defineTunnels
from . import define_inputs_outputs
from . import changeLabel
from . import errorHandler
from . import getlistModules
from . import getlistSubModules
from . import seeCode
from . import ConfigModuls, windowConfig
from . import editCombobox
from . import exportCapsul
from . import PythonHighlighter

from Config import Config

currentpathwork = ''


class Menu(QMenuBar):

    def __init__(self, parent=None):
        QMenuBar.__init__(self, parent)
        self.setFixedHeight(30)
        hist = Config().getPathHistories()
        self.Dictexamples = {}

        self.menu1 = self.addMenu('Diagram')
        newdgr = self.menu1.addAction('New Diagram')
        newdgr.setShortcut('Ctrl+N')
        opendgr = self.menu1.addAction('Open Diagram')
        opendgr.setShortcut('Ctrl+O')
        saveDgr = self.menu1.addAction('Save Diagram')
        saveDgr.setShortcut('Ctrl+S')
        self.menu1.addAction('Save Diagram As...')
        closeDgr = self.menu1.addAction('Close Diagram')
        closeDgr.setShortcut('Ctrl+W')
        self.menu1.addSeparator()
        self.openRecent = self.menu1.addMenu('Open Recent')
        if hist:
            for h in hist:
                self.openRecent.addAction(h.strip())
        self.menu1.triggered[QAction].connect(self.btnPressed)

        self.menu12 = self.addMenu('Edit')
        undo = self.menu12.addAction('Undo')
        undo.setShortcut('Ctrl+Z')
        redo = self.menu12.addAction('Redo')
        redo.setShortcut('Ctrl+Y')
        self.menu12.triggered[QAction].connect(self.btnPressed)
        self.menu2 = self.addMenu('Pipeline')
        anaPipe = self.menu2.addAction('Analyze Pipeline')
        anaPipe.setShortcut('Ctrl+A')
        runpipe = self.menu2.addAction('Run Pipeline')
        runpipe.setShortcut('Ctrl+R')
        runpipethreadless = self.menu2.addAction('Run Pipeline with Thread')
        runpipethreadless.setShortcut('Ctrl+T')
        listItm = self.menu2.addAction('See List Items')
        listItm.setShortcut('Ctrl+I')
        listLib = self.menu2.addAction('See List Libraries')
        listLib.setShortcut('Ctrl+L')
        rawFile = self.menu2.addAction('See Raw file')
        rawFile.setShortcut(('Ctrl+B'))
        self.menu2.addSeparator()
        self.menu2.addAction('Pipeline execution by Capsul')
        self.menu2.addAction('Export pipeline for Capsul')
        self.menu2.triggered[QAction].connect(self.btnPressed)

        self.menu3 = self.addMenu('Submodul')
        self.menu3.addAction('Create Submodul')
        self.menu3.addAction('Save Submodul        Ctrl+S')
        self.menu3.triggered[QAction].connect(self.btnPressed)

        self.menu4 = self.addMenu('Configuration')
        self.menu4.addAction('Setting Standalone Paths')
        self.menu4.triggered[QAction].connect(self.btnPressed)

        self.menu5 = self.addMenu('Help')
        self.menu5.addAction('HTML documentation')
        self.menu5.addSeparator()
        self.examples = self.menu5.addMenu('Examples')
        expl = self.load_dir_examples()
        if expl:
            pathExamples = os.path.dirname(os.path.realpath(__file__))
            pathExamples = dir_path = os.path.dirname(pathExamples)
            pathExamples = os.path.join(pathExamples, 'examples')
            expl = sorted(expl)
            for lstD in expl:
                self.exs = self.examples.addMenu(lstD)
                expl_files = self.load_file_examples(
                    os.path.join(pathExamples,
                                 lstD))
                for lstF in expl_files:
                    self.Dictexamples[lstF] = os.path.join(pathExamples,
                                                           lstD)
                    self.exs.addAction(lstF)

        self.menu5.triggered[QAction].connect(self.btnPressed)

    def load_dir_examples(self):
        pathExamples = os.path.dirname(os.path.realpath(__file__))
        pathExamples = dir_path = os.path.dirname(pathExamples)
        pathExamples = os.path.join(pathExamples,
                                    'examples')
        if os.path.isdir(pathExamples):
            listDir = [dI for dI in os.listdir(pathExamples)
                       if os.path.isdir(os.path.join(pathExamples, dI))]
            return listDir
        else:
            return None

    def load_file_examples(self, pathExemp):
        onlyfiles = [f for f in os.listdir(pathExemp)
                     if os.path.isfile(os.path.join(pathExemp, f))]
        return onlyfiles

    def loadHistories(self):
        path_config = os.path.dirname(os.path.realpath(__file__))
        print('path_config = ', path_config)
        pathYml = os.path.join(QDir.currentPath(), "config.yml")
        if os.path.isdir(pathYml):
            with open(pathYml, 'r') as stream:
                dicts = yaml.load(stream, yaml.FullLoader)
                return dicts['paths']['histories']
        else:
            return None

    def saveHistories(self, path):
        hist = Config().getPathHistories()
        if hist:
            if path not in hist:
                if len(hist) > 9:
                    hist.pop(0)
                    firstAction = self.openRecent.actions()[0]
                    self.openRecent.removeAction(firstAction)
                hist.append(path)
                Config().setPathHistories(hist)
                self.openRecent.addAction(path)
        else:
            hist = [path]
            Config().setPathHistories(hist)
            self.openRecent.addAction(path)

    def btnPressed(self, act):
        global currentpathwork
        tmpActText = act.text()
        ct = editor.currentTab

        if tmpActText == 'New Diagram':
            editor.addTab('')
            textInf.setText('')

        if tmpActText == 'Save Diagram' or tmpActText == 'Save Diagram As...':
            file = editor.pathDiagram[editor.currentTab]
            extension = os.path.splitext(file)[1]
            fileNameonly = os.path.basename(file)

            connectorPresent = False
            for item in editor.diagramView[editor.currentTab].items():
                if type(item) == ConnectorItem:
                    connectorPresent = True
                    break

            if not connectorPresent:
                txt = SaveDiagram()
                if ('.dgr' not in extension or
                        tmpActText == 'Save Diagram As...'):
                    file = QFileDialog\
                                .getSaveFileName(
                                    self,
                                    "save diagram " + str(editor.currentTab),
                                    currentpathwork, "Diagrams (*.dgr)",
                                    None,
                                    QFileDialog.DontUseNativeDialog)
                    file = file[0]
                    currentpathwork = file
                    if file:
                        if '.dgr' not in file:
                            file += '.dgr'
                        fileNameonly = os.path.basename(file)
                try:
                    if file:
                        f = open(file, 'w')
                        f.write(txt.toPlainText())
                        f.write('\n[execution]\n')
                        f.write(analyze(txt.toPlainText(), textEdit, True)
                                .getListForExecution())
                        f.close()
                        editor.pathDiagram[editor.currentTab] = file
                        editor.tabsDiagram.setTabText(editor.currentTab,
                                                      fileNameonly)
                        textInf.setText(file)
                        if 'NodeEditor/examples' not in file:
                            self.saveHistories(file)
                except OSError as err:
                    print("OS error: {0}".format(err))
            else:
                if '.mod' not in extension:
                    tmpActText = 'Create Submodul'
                else:
                    tmpActText = 'Save Submodul        Ctrl+S'

        if tmpActText == 'Open Diagram':
            fileDiagram = QFileDialog.getOpenFileName(
                                self,
                                "Open diagram",
                                currentpathwork,
                                'Diagrams (*.dgr)',
                                None,
                                QFileDialog.DontUseNativeDialog)

            if fileDiagram[0] != '':
                currentpathwork = fileDiagram[0]
                editor.addTab(os.path.basename(fileDiagram[0]))
                editor.pathDiagram[editor.currentTab] = fileDiagram[0]
                textInf.setText(fileDiagram[0])
                f = open(fileDiagram[0], 'r')
                txt = f.readlines()
                f.close()
                LoadDiagram(txt)
                editor.diagramView[editor.currentTab]\
                      .fitInView(editor.diagramScene[editor.currentTab].
                                 sceneRect(),
                                 QtCore.Qt.KeepAspectRatio)
                editor.diagramView[editor.currentTab].scale(0.8, 0.8)
                editor.diagramView[editor.currentTab].scene().clearSelection()
                self.saveHistories(fileDiagram[0])
#                 UpdateUndoRedo()

        if tmpActText == 'Close Diagram':
            editor.closeTab(editor.currentTab)

        if tmpActText == 'Export pipeline for Capsul':
            txt = SaveDiagram()
            rep = QFileDialog.getExistingDirectory(self, 'Select directory')
            exportCapsul(txt.toPlainText(), rep, False, textEdit)

        if tmpActText == 'Pipeline execution by Capsul':
            txt = SaveDiagram()
            path_tmp = os.path.expanduser("~")
            rep = str(os.path.join(path_tmp, 'tmp'))
            if not os.path.exists(rep):
                os.makedirs(rep)
            exportCapsul(txt.toPlainText(), rep, True, textEdit)

        if (tmpActText == 'Run Pipeline' or
                tmpActText == 'Run Pipeline with Thread'):
            textEdit.clear()
            txt_raw = SaveDiagram().toPlainText()
            txt_code = ''
            for keyS, valS in listTools[editor.currentTab].items():
                if 'S' in keyS:
                    tmpS = 'source ' + keyS + ']'
                    txt_code += txt_raw[txt_raw.index('[' +
                                        tmpS):txt_raw.index('[/' +
                                        tmpS) + len(tmpS) + 2] + '\n'
            if 'with Thread' in tmpActText:
                txt = analyze(txt_raw, textEdit, True).\
                                getListForExecution()
            else:
                txt = analyze(txt_raw, textEdit, False).\
                                getListForExecution()
            if txt_code:
                txt += txt_code
            textEdit.append("<span style=\" font-size:10pt;"
                            "font-weight:600; color:#0000CC;"
                            "\" >Pipeline started ! </span>")
            textEdit.append("<span style=\" font-size:10pt;"
                            "font-weight:600; color:#0000CC;"
                            "\" >Pipeline running ......... </span>")
            execution(txt, textEdit)

        if tmpActText == 'Analyze Pipeline':
            txt = SaveDiagram()
            analyze(txt.toPlainText(), textEdit, True)

        if tmpActText == 'Create Submodul':
            connectPresent = False
            for item in editor.diagramView[editor.currentTab].items():
                if type(item) == ConnectorItem:
                    connectPresent = True
                    break

            if connectPresent:
                pat_submod = os.path.dirname(os.path.realpath(__file__))
                pat_submod = os.path.dirname(pat_submod)
                txt = SaveDiagram()
                file = QFileDialog.getSaveFileName(self,
                                                   "save submodul " +
                                                   str(editor.currentTab),
                                                   str(os.path.join(
                                                       pat_submod,
                                                       'submodules')),
                                                   "SubModul (*.mod)",
                                                   None,
                                                   QFileDialog.
                                                   DontUseNativeDialog)

                file = file[0]
                try:
                    if '.mod' not in file and file:
                        file += '.mod'
                    f = open(file, 'w')
                    f.write(txt.toPlainText())
                    f.write('\n[execution]\n')
                    f.write(analyze(txt.toPlainText(),
                                    textEdit,
                                    True).getListForExecution())
                    f.close()
                    editor.pathDiagram[editor.currentTab] = file
                    fileNameonly = os.path.basename(file)
                    editor.tabsDiagram.setTabText(editor.currentTab,
                                                  fileNameonly)
                    editor.refreshSubModLib()
                except Exception as e:
                    pass
            else:
                if not connectPresent:
                    textEdit.append("<span style=\" font-size:10pt;"
                                    "font-weight:600; color:#cc0000;"
                                    "\" > You can't create modul without \
                                    connectors</span>")

        if tmpActText == 'Save Submodul        Ctrl+S':
            file = editor.pathDiagram[editor.currentTab]
            fileNameonly = os.path.basename(file)
            connectPresent = False
            for item in editor.diagramView[editor.currentTab].items():
                if type(item) == ConnectorItem:
                    connectPresent = True

            if connectPresent:
                txt = SaveDiagram()
                try:
                    f = open(file, 'w')
                    f.write(txt.toPlainText())
                    f.write('\n[execution]\n')
                    f.write(analyze(txt.toPlainText(),
                                    textEdit,
                                    True).getListForExecution())
                    f.close()
                    editor.pathDiagram[editor.currentTab] = file
                    editor.tabsDiagram.setTabText(editor.currentTab,
                                                  fileNameonly)
                    editor.refreshSubModLib()
                except Exception as e:
                    pass
            else:
                if not connectPresent:
                    textEdit.append("<span style=\" font-size:10pt;"
                                    "font-weight:600; color:#cc0000;"
                                    "\" > You can't create modul without \
                                    connectors</span>")

        if tmpActText == 'See List Items':
            textEdit.clear()
#             txt = SaveDiagram()
#             textEdit.append(txt.toPlainText())
            textEdit.append('listItems :')
            textEdit.append(str(listItems[editor.currentTab]))
            textEdit.append('listNodes :')
            textEdit.append(str(listNodes[editor.currentTab]))
            textEdit.append('listBlocks :')
            textEdit.append(str(listBlocks[editor.currentTab]))
            textEdit.append('listConnects :')
            textEdit.append(str(listConnects[editor.currentTab]))
            textEdit.append('listSubMod :')
            textEdit.append(str(listSubMod[editor.currentTab]))
            textEdit.append('listConstants :')
            textEdit.append(str(listConstants[editor.currentTab]))
            textEdit.append('listProbes :')
            textEdit.append(str(listProbes[editor.currentTab]))
            textEdit.append('listTools :')
            textEdit.append(str(listTools[editor.currentTab]))
            textEdit.append('libTools :')
            textEdit.append(str(libTools[editor.currentTab]))

        if tmpActText == 'See List Libraries':
            textEdit.clear()
            textEdit.append('libBlocks :')
            textEdit.append(str(editor.getlib()))
            textEdit.append('libSubMod :')
            textEdit.append(str(libSubMod))

        if tmpActText == 'See Raw file':
            if editor.pathDiagram[editor.currentTab]:
                f = open(editor.pathDiagram[editor.currentTab], 'r')
                textEdit.append(f.read())
                f.close()

        if tmpActText == 'HTML documentation':
            path_html = os.path.dirname(os.path.realpath(__file__))
            tmp = str(os.path.join(path_html,
                                   '../../../docs',
                                   'index.html'))
            webbrowser.open(tmp)

        if tmpActText == 'Setting Standalone Paths':
            c = windowConfig()
            c.exec_()
            ConfigModuls().saveConfig()

        if tmpActText == 'Undo':
            ct = editor.currentTab
            if pointTyping[ct] > 0:
                pointTyping[ct] -= 1
                for item in editor.diagramScene[ct].items():
                    editor.diagramScene[ct].removeItem(item)
                newDiagram = undoredoTyping[ct][pointTyping[ct]]
                LoadDiagram(newDiagram.splitlines())
                UpdateList(newDiagram)

        if tmpActText == 'Redo':
            ct = editor.currentTab
            if pointTyping[ct] < len(undoredoTyping[ct]) - 1:
                pointTyping[ct] += 1
                for item in editor.diagramScene[ct].items():
                    editor.diagramScene[ct].removeItem(item)
                newDiagram = undoredoTyping[ct][pointTyping[ct]]
                LoadDiagram(newDiagram.splitlines())
                UpdateList(newDiagram)

        if os.path.splitext(tmpActText)[1] == '.dgr':
            editor.addTab(os.path.basename(tmpActText))
            if not os.path.exists(tmpActText):
                tmpActText = os.path.join(self.Dictexamples[tmpActText],
                                          tmpActText)
            editor.pathDiagram[editor.currentTab] = tmpActText
            f = open(tmpActText, 'r')
            txt = f.readlines()
            f.close()
            try:
                LoadDiagram(txt)
                editor.diagramView[editor.currentTab].fitInView(
                                    editor.diagramScene[editor.currentTab].sceneRect(),
                                    QtCore.Qt.KeepAspectRatio)
                editor.diagramView[editor.currentTab].scale(0.8, 0.8)
#                 UpdateUndoRedo()
                textEdit.clear()
            except Exception as e:
                redText = "<span style=\" font-size:10pt; font-weight:600; color:#ff0000;\" >"
                redText = redText + ('This diagram contains errors !')
                redText = redText + ("</span>")
                textEdit.clear()
                textEdit.append(redText)


class ShowLegend:

    def __init__(self):

        pos1X, pos1Y, pos2X, pos2Y = 0, 0, 60, 0
        labColum = 'simple            list              array'
        textColumn = QGraphicsTextItem(labColum, parent=None)
        textColumn.setDefaultTextColor(QtGui.QColor(250, 250, 250))
        textColumn.setFont(QFont("Times", 12, QFont.Bold))
        textColumn.setPos(pos1X, pos1Y - 40)
#         editor.diagramScene[editor.currentTab].addItem(textColumn)
        legendScene.addItem(textColumn)

        for types in TypeColor:
            if types != TypeColor.unkn:
                color = types.value
                for i in [2, 5, 8]:
                    if not (i > 2 and types.name in ['dict', 'tuple']):
                        line = QGraphicsPathItem()
                        bisLine = QGraphicsPathItem()
                        link = QGraphicsPolygonItem()

                        line.setPen(QtGui.QPen(color, i))
                        link.setPen(QtGui.QPen(color, 2))
                        link.setBrush(color)
                        off = 6
                        posPolygon = QPolygonF(
                            [QPointF(-off + (pos2X + pos1X) / 2, -off + pos1Y),
                             QPointF((pos2X + pos1X) / 2, pos1Y),
                             QPointF(-off + (pos2X + pos1X) / 2, off + pos1Y)])
                        link.setPolygon(posPolygon)

                        if i == 8:
                            bisLine.setPen(QtGui.QPen(ItemColor.bis_link.value,
                                                      3,
                                                      Qt.SolidLine))
                        else:
                            bisLine.setPen(QtGui.QPen(Qt.NoPen))

                        path = QPainterPath()
                        self.start_x, self.start_y = pos1X, pos1Y
                        self.end_x, self.end_y = pos2X, pos2Y
                        self.ctrl1_x = pos1X + (pos2X - pos1X) * 0.7
                        self.ctrl1_y = pos1Y
                        self.ctrl2_x = pos2X + (pos1X - pos2X) * 0.7
                        self.ctrl2_y = pos2Y
                        path.moveTo(self.start_x, self.start_y)
                        path.cubicTo(self.ctrl1_x,
                                     self.ctrl1_y,
                                     self.ctrl2_x,
                                     self.ctrl2_y,
                                     self.end_x,
                                     self.end_y)

                        line.setPath(path)
                        bisLine.setPath(path)

                        legendScene.addItem(link)
                        legendScene.addItem(line)
                        legendScene.addItem(bisLine)

                    pos1X = pos1X + 80
                    pos2X = pos1X + 60

                if types.name != 'float':
                    txtLab = types.name
                else:
                    txtLab = types.name+' (or ndarray)'

                textRow = QGraphicsTextItem(txtLab, parent=None)
                textRow.setDefaultTextColor(QtGui.QColor(color))
                textRow.setFont(QFont("Times", 12, QFont.Bold))
                textRow.setPos(pos1X, pos1Y - 15)

                legendScene.addItem(textRow)

                pos1X, pos1Y = 0, pos1Y + 20
                pos2X, pos2Y = 60, pos1Y

#         editor.diagramView[editor.currentTab].setDragMode(QGraphicsView.ScrollHandDrag)
        legendDiagram.setEnabled(False)
        legendDiagram.setInteractive(False)


class LibMod(QStandardItemModel):

    def __init__(self, nameItem, parent=None):
        QStandardItemModel.__init__(self, parent)
        self.name = nameItem

    def mimeTypes(self):
        return [self.name]

    def mimeData(self, items):
        mimedata = QtCore.QMimeData()
        for item in items:
            if item.isValid():
                try:
                    txt = self.data(item, Qt.DisplayRole)
                    if txt not in listCategorySubMod:
                        mimedata.setData(self.name, QByteArray(txt.encode()))
                except Exception as e:
                    pass
        return mimedata


class LibIcon(QPixmap):

    def __init__(self, color, parent=None):
        QPixmap.__init__(self, 100, 100)
#         self.fill()
        icon = QPainter(self)
#         icon.setPen()
        icon.fillRect(0, 0, 100, 100, color)
        icon.setBrush(ItemColor.backGround.value)
        icon.drawRect(0, 0, 100, 30)
        icon.end()


class LoadCodeScript:

    def __init__(self):
        self.listCodeScript = ''
        for keyS, valS in listItems[editor.currentTab].items():
            if 'S' in keyS:
                if type(valS) == ScriptItem:
                    txt = '[source ' + valS.unit + ']\n'
                    txt += repr(self.getInputsScript(keyS)) + '\n'
                    txt += valS.elemProxy.toPlainText() + '\n'
                    txt += str([keyS + ':' + item.name for item in valS.outputs]) + '\n'
                    txt += '[/source ' + valS.unit + ']\n'
                    self.listCodeScript += txt

    def writeListScript(self):
        return self.listCodeScript

    def getInputsScript(self, unitScript):
        listInputVal = []
        for key, val in listNodes[editor.currentTab].items():
            tmpout = val[val.index("#Node") + 6:]
            if unitScript + ':' in tmpout:
                tmpIn = tmpout[tmpout.index(':') + 1:]
                tmpVal = val[0:val.index('#Node#')]
                if 'A' in tmpVal[0:1]:
                    tmpConstName = tmpVal[0:-1]
                    tmpVal = repr(listConstants[editor.currentTab][tmpConstName][1])
                listInputVal.append(tmpIn + '=' + tmpVal)
        return listInputVal


class LoadDiagram:

    def __init__(self, txt):

        edit = DiagramView(editor.diagramScene[editor.currentTab])
#         listItems[editor.currentTab] = {}
        listNd = {}
        listCn, listBl, listFo, listIf = {}, {}, {}, {}
        listSm, listCt, listSc, listPr = {}, {}, {}, {}
        listCode = {}
        insource = False
        tmpKeyScript = ''
        tmpValScript = ''

        for line in txt:
            if line[0:5] == 'connt':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('name=') + 6:len(line)]
                name = line[0:line.index(']')]
                line = line[line.index('type=') + 6:len(line)]
                typ = line[0:line.index(']')]
                line = line[line.index('format=') + 8:len(line)]
                form = line[0:line.index(']')]
                Vinput = ''
                try:
                    line = line[line.index('valOut=') + 8:len(line)]
                    Vinput = line[0:line.index('] RectF=')]
                except Exception as e:
                    pass
                line = line[line.index('RectF=') + 7:len(line)]
                try:
                    pos = edit.mapToScene(eval(line[0:line.index(']')]))
                except Exception as e:
                    pos = eval(line[0:line.index(']')])
                edit.loadConn(unit, name, pos, str(typ), form, Vinput)
                listCn[unit] = edit.returnBlockSystem()

            elif line[0:5] == 'probe':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('label=') + 7:len(line)]
                label = line[0:line.index(']')]
                line = line[line.index('format=') + 8:len(line)]
                form = line[0:line.index('] RectF')]
                line = line[line.index('RectF=') + 7:len(line)]
                pos = eval(line[0:line.index(']')])
                edit.loadProbe(unit, label, form, pos)
                listPr[unit] = edit.returnBlockSystem()

            elif line[0:5] == 'block':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('category=') + 10:len(line)]
                cat = line[0:line.index(']')]
                line = line[line.index('class=') + 7:len(line)]
                classs = line[0:line.index(']')]
                line = line[line.index('valInputs=') + 11:len(line)]
                Vinput = line[0:line.index('] RectF=')]
                line = line[line.index('RectF=') + 7:len(line)]
                pos = eval(line[0:line.index(']')])
                edit.loadBlock(unit, classs, cat, pos, eval(Vinput))
                listBl[unit] = edit.returnBlockSystem()

            elif line[0:8] == 'comments':
                line = line[line.index('RectF=') + 7:len(line)]
                pos = eval(line[0:line.index(']')])
                line = line[line.index('text=') + 6:len(line)]
                cmt = line[0:line.index(']')]
                cmt = cmt.replace("\\n", '\n')
                cmt = cmt.replace("'", '')
                cmt = cmt.replace('"', '')
                edit.loadComments(pos, cmt)

            elif line[0:7] == 'loopFor':
                unit = re.search(r"\[([A-Za-z0-9*_]+)\]", line).group(1)
                line = line[line.index('inputs=') + 8:len(line)]
                inp = line[0:line.index('] outputs')]
                line = line[line.index('outputs=') + 9:len(line)]
                outp = line[0:line.index('] listItems=')]
                line = line[line.index('listItems=') + 11:len(line)]
                listIt = line[0:line.index('] RectF=')]
                line = line[line.index('RectF=') + 7:len(line)]
                pos = eval(line[0:line.index(']')])
                edit.loadLoopFor(unit, pos, eval(inp), eval(outp))
                listFo[unit] = edit.returnBlockSystem()
                listTools[editor.currentTab][unit] = eval(listIt)

            elif line[0:6] == 'loopIf':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('inputs=') + 8:len(line)]
                inp = line[0:line.index('] outputs')]
                line = line[line.index('outputs=') + 9:len(line)]
                outp = line[0:line.index('] listItems=')]
                line = line[line.index('listItems=') + 11:len(line)]
                listIt = line[0:line.index('] RectF=')]
                line = line[line.index('RectF=') + 7:len(line)]
                pos = eval(line[0:line.index(']')])
                edit.loadLoopFor(unit, pos, eval(inp), eval(outp))
                listIf[unit] = edit.returnBlockSystem()
                listTools[editor.currentTab][unit] = eval(listIt)

            elif line[0:6] == 'submod':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('nameMod=') + 9:len(line)]
                nameMod = line[0:line.index(']')]
                line = line[line.index('valInputs=') + 11:len(line)]
                Vinput = line[0:line.index('] RectF')]
                line = line[line.index('RectF=') + 7:len(line)]
                pos = eval(line[0:line.index(']')])
                edit.loadMod(unit, nameMod, pos, eval(Vinput))
                listSm[unit] = edit.returnBlockSystem()

            elif line[0:8] == 'constant':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('value=') + 7:len(line)]
                vout = line[0:line.index('] format')]
                line = line[line.index('format=') + 8:len(line)]
                fort = line[0:line.index('] label')]
                if not fort:
                    fort = ''
                line = line[line.index('label=') + 7:len(line)]
                lab = line[0:line.index(']')]
                line = line[line.index('RectF=') + 7:len(line)]
                pos = eval(line[0:line.index(']')])
                try:
                    edit.loadConstant(unit, pos, eval(vout), fort, lab)
                except Exception as e:
                    edit.loadConstant(unit, pos, vout, fort, lab)
                listCt[unit] = edit.returnBlockSystem()

            elif line[0:6] == 'script':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('title=') + 7:len(line)]
                tit = line[0:line.index('] inputs')]
                line = line[line.index('inputs=') + 7:len(line)]
                inp = line[0:line.index(' outputs')]
                line = line[line.index('outputs=') + 8:len(line)]
                outp = line[0:line.index(' code=')]
                line = line[line.index('code=') + 6:len(line)]
                code = line[0:line.index('] RectF=')]
                line = line[line.index('RectF=') + 7:len(line)]
                pos = eval(line[0:line.index(']')])
                edit.loadScriptItem(unit, tit, pos, eval(inp), eval(outp))
                listSc[unit] = edit.returnBlockSystem()
                listTools[editor.currentTab][unit] = code

            elif line[0:8] == '[source ':
                insource = True
                tmpKeyScript = line[line.index('[source ') + 8:]
                tmpKeyScript = tmpKeyScript[0:tmpKeyScript.index(']')]
            elif line[0:9] == '[/source ':
                tmpValScript = '\n'.join(tmpValScript.splitlines()[1:-1])
                listCode[tmpKeyScript] = tmpValScript
                insource = False
                tmpValScript = ''
            elif insource:
                if '\n' not in line:
                    line += '\n'
                tmpValScript += line

            elif line[0:4] == 'link':
                nameNode = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('node=') + 6:len(line)]
                line = line[0:line.index(']')]
                listNodes[editor.currentTab][nameNode] = line
                listNd[nameNode] = line.replace('#Node#', ':').split(':')

        for lk, lv in listNd.items():
            unitStart = lv[0]
            namePortStart = lv[1]
            unitEnd = lv[2]
            namePortEnd = lv[3]

            fromPort = None
            toPort = None

            if 'U' in unitStart:
                for lin in listBl[unitStart].outputs:
                    if type(lin) == Port and lin.name == namePortStart:
                        fromPort = lin
                        break
            elif 'M' in unitStart:
                for lin in listSm[unitStart].outputs:
                    if type(lin) == Port and lin.name == namePortStart:
                        fromPort = lin
                        break
            elif 'C' in unitStart:
                fromPort = listCn[unitStart].output
            elif 'F' in unitStart:
                for lin in listFo[unitStart].outputs:
                    if type(lin) == Port and lin.name == namePortStart:
                        fromPort = lin
                        break
            elif 'I' in unitStart:
                for lin in listIf[unitStart].outputs:
                    if type(lin) == Port and lin.name == namePortStart:
                        fromPort = lin
                        break
            elif 'S' in unitStart:
                for lin in listSc[unitStart].outputs:
                    if type(lin) == Port and lin.name == namePortStart:
                        fromPort = lin
                        break
            elif 'A' in unitStart:
                fromPort = listCt[unitStart].outputs[0]

            if 'U' in unitEnd:
                for lout in listBl[unitEnd].inputs:
                    if type(lout) == Port and lout.name == namePortEnd:
                        toPort = lout
                        break
            elif 'M' in unitEnd:
                for lout in listSm[unitEnd].inputs:
                    if type(lout) == Port and lout.name == namePortEnd:
                        toPort = lout
                        break
            elif 'C' in unitEnd:
                toPort = listCn[unitEnd].input
            elif 'P' in unitEnd:
                toPort = listPr[unitEnd].inputs[0]
            elif 'F' in unitEnd:
                for lout in listFo[unitEnd].inputs:
                    if type(lout) == Port and lout.name == namePortEnd:
                        toPort = lout
                        break
            elif 'I' in unitEnd:
                for lout in listIf[unitEnd].inputs:
                    if type(lout) == Port and lout.name == namePortEnd:
                        toPort = lout
                        break
            elif 'S' in unitEnd:
                for lout in listSc[unitEnd].inputs:
                    if type(lout) == Port and lout.name == namePortEnd:
                        toPort = lout
                        break

            startConnection = Connection(lk, fromPort, toPort, fromPort.format)
            startConnection.setEndPos(toPort.scenePos())
            startConnection.setToPort(toPort)

        if listSc:
            for elem in editor.diagramView[editor.currentTab].items():
                if type(elem) == ScriptItem:
                    elem.elemProxy.setPlainText(listCode[elem.unit])

        ValueZ2()

        UpdateUndoRedo()


class ValueZ:

    def __init__(self):
        listZ = {}
        zref = len(listTools)
        lst = listTools[editor.currentTab]
        keyZ = list(lst.keys())
        uniZ = lst.values()
        uniZ = [item for sublist in uniZ for item in sublist]

        listLowNivel = list(set(keyZ) - set(uniZ))

        ind = 0
        while uniZ:
            for le in listLowNivel:
                listZ[le] = ind
                for le2 in lst[le]:
                    listZ[le2] = ind + 1
                    uniZ.remove(le2)
                keyZ.remove(le)
            listLowNivel = list(set(keyZ) - set(uniZ))
            ind += 1

        for its in editor.diagramView[editor.currentTab].items():
            try:
                its.setZValue(listZ[its.unit])
            except Exception as e:
                pass


class ValueZ2:

    def __init__(self):
        listZ = {}
        lst = listTools[editor.currentTab]

        keyZ = []
        uniZ = []
        for keyList, valList in listTools[editor.currentTab].items():
            keyZ.append(keyList)
            if 'I' in keyList:
                uniZ.append(valList[0])
                uniZ.append(valList[1])
            else:
                uniZ.append(valList)

        uniZ = [item for sublist in uniZ for item in sublist]

        listLowNivel = list(set(keyZ) - set(uniZ))

        ind = 0
        while uniZ:
            for le in listLowNivel:
                listZ[le] = ind
                if 'I' in le:
                    for le2 in lst[le][0]:
                        listZ[le2] = ind + 1
                        uniZ.remove(le2)
                    for le2 in lst[le][1]:
                        listZ[le2] = ind + 1
                        uniZ.remove(le2)
                else:
                    for le2 in lst[le]:
                        listZ[le2] = ind + 1
                        uniZ.remove(le2)
                keyZ.remove(le)
            listLowNivel = list(set(keyZ) - set(uniZ))
            ind += 1

        for its in editor.diagramView[editor.currentTab].items():
            try:
                its.setZValue(listZ[its.unit])
            except Exception as e:
                pass

        for its in editor.diagramView[editor.currentTab].items():
            if type(its) == ForLoopItem:
                if 'I' in its.unit:
                    tmp = its.elemProxy.currentText()
                    its.elemProxy.newValue()
                    its.elemProxy.setCurrentText(tmp)


class SaveDiagram(QTextEdit):

    def __init__(self, parent=None):
        super(SaveDiagram, self).__init__(parent)
        listCodeScript = {}

        self.append('[diagram]')
        for item in editor.diagramView[editor.currentTab].items():
            try:
                coord = item.pos()
            except Exception as e:
                coord = item.sceneBoundingRect()

            if type(item) == BlockCreate:
                if item.category:
                    rect = item.rect()
                    self.append('block=[' + item.unit +
                                '] category=[' + item.category +
                                '] class=[' + item.name +
                                '] valInputs=[' + str(listBlocks[editor.currentTab][item.unit][2]) +
                                '] RectF=[' + str((coord.x(), coord.y(), rect.width(), rect.height())) +
                                ']')
                else:
                    rect = item.rect()
                    self.append('submod=[' + item.unit +
                                '] nameMod=[' + item.name +
                                '] valInputs=[' + str(listSubMod[editor.currentTab][item.unit][1]) +
                                '] RectF=[' + str((coord.x(), coord.y(), rect.width(), rect.height())) +
                                ']')

            elif type(item) == LinkItem:
                self.append('link=[' + item.name +
                            '] node=[' + listNodes[editor.currentTab][item.name] + ']')

            elif type(item) == ConnectorItem:
                if 'in' in item.inout:
                    self.append('connt=[' + str(item.connct) +
                                '] name=[' + str(listConnects[editor.currentTab][item.connct][1]) +
                                '] type=[' + str(item.inout) +
                                '] format=[' + str(listConnects[editor.currentTab][item.connct][2]) +
                                '] valOut=[' + str(listConnects[editor.currentTab][item.connct][3]) +
                                '] RectF=[' + str((coord.x(), coord.y(), 70, 24)) +
                                ']')
                else:
                    self.append('connt=[' + str(item.connct) +
                                '] name=[' + str(listConnects[editor.currentTab][item.connct][1]) +
                                '] type=[' + str(item.inout) +
                                '] format=[' + str(listConnects[editor.currentTab][item.connct][2]) +
                                '] RectF=[' + str((coord.x(), coord.y(), 70, 24)) +
                                ']')
            elif type(item) == Probes:
                self.append('probe=[' + str(item.unit) +
                            '] label=[' + str(listProbes[editor.currentTab][item.unit][1]) +
                            '] format=[' + str(listProbes[editor.currentTab][item.unit][0]) +
                            '] RectF=[' + str((coord.x(), coord.y(), 70, 24)) +
                            ']')
            elif type(item) == CommentsItem:
                rect = item.rect()
                comm = item.label.toPlainText()
                self.append('comments=[] RectF=[' + str((coord.x(), coord.y(), rect.width(), rect.height())) +
                            '] text=[' + repr(comm) +
                            ']')
            elif type(item) == ForLoopItem:
                rect = item.rect()
                if 'F' in item.unit:
                    try:
                        self.append('loopFor=[' + str(item.unit) +
                                    '] inputs=[' + str(libTools[editor.currentTab][item.unit][0]) +
                                    '] outputs=[' + str(libTools[editor.currentTab][item.unit][1]) +
                                    '] listItems=[' + str(listTools[editor.currentTab][item.unit]) +
                                    '] RectF=[' + str((coord.x(), coord.y(), rect.width(), rect.height())) +
                                    ']')
                    except Exception as e:
                        pass
                else:
                    try:
                        self.append('loopIf=[' + str(item.unit) +
                                    '] inputs=[' + str(libTools[editor.currentTab][item.unit][0]) +
                                    '] outputs=[' + str(libTools[editor.currentTab][item.unit][1]) +
                                    '] listItems=[' + str(listTools[editor.currentTab][item.unit]) +
                                    '] RectF=[' + str((coord.x(), coord.y(), rect.width(), rect.height())) +
                                    ']')
                    except Exception as e:
                        pass

            elif type(item) == Constants:
                rect = item.rect()
                if type(item.elemProxy) == Constants_Combo:
                    value = repr(item.elemProxy.currentText())
                elif type(item.elemProxy) == Constants_text:
                    value = repr(item.elemProxy.toPlainText())
                elif type(item.elemProxy) == Constants_float or type(item.elemProxy) == Constants_int:
                    value = item.elemProxy.value()
                self.append('constant=[' + str(item.unit) +
                            '] value=[' + str(value) +
                            '] format=[' + str(item.form) +
                            '] label=[' + str(item.label) +
                            '] RectF=[' + str((coord.x(), coord.y(), rect.width(), rect.height())) +
                            ']')

            elif type(item) == ScriptItem:
                listCodeScript[item.unit] = item.elemProxy.toPlainText()
                rect = item.rect()
                self.append('script=[' + str(item.unit) +
                            '] title=[' + item.name +
                            '] inputs=' + str(libTools[editor.currentTab][item.unit][0]) +
                            ' outputs=' + str(libTools[editor.currentTab][item.unit][1]) +
                            ' code=[' + "your code" +
                            '] RectF=[' + str((coord.x(), coord.y(), rect.width(), rect.height())) +
                            ']')

        if listCodeScript:
            for line in LoadCodeScript().writeListScript().split('\n'):
                self.append(line)


class UpdateList:

    def __init__(self, txt):
        listNodes[editor.currentTab].clear()
        listBlocks[editor.currentTab].clear()
        listSubMod[editor.currentTab].clear()
        listConnects[editor.currentTab].clear()
        listConstants[editor.currentTab].clear()
        listTools[editor.currentTab].clear()
        libTools[editor.currentTab].clear()

        for line in txt.splitlines():

            if line[0:4] == 'link':
                nameNode = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('node=') + 6:len(line) - 1]

                listNodes[editor.currentTab][nameNode] = line

            elif line[0:5] == 'block':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('category=') + 10:len(line)]
                cat = line[0:line.index(']')]
                line = line[line.index('class=') + 7:len(line)]
                classs = line[0:line.index(']')]
                line = line[line.index('valInputs=') + 11:len(line)]
                Vinput = line[0:line.index('] RectF=')]

                listBlocks[editor.currentTab][unit] = (classs, cat, eval(Vinput))

            elif line[0:6] == 'submod':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('nameMod=') + 9:len(line)]
                nameMod = line[0:line.index(']')]
                line = line[line.index('valInputs=') + 11:len(line)]
                Vinput = line[0:line.index('] RectF=')]

                listSubMod[editor.currentTab][unit] = (nameMod, eval(Vinput))

            elif line[0:5] == 'connt':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('name=') + 6:len(line)]
                name = line[0:line.index(']')]
                line = line[line.index('type=') + 6:len(line)]
                typ = line[0:line.index(']')]
                line = line[line.index('format=') + 8:len(line)]
                form = line[0:line.index(']')]
                Vinput = ''
                try:
                    line = line[line.index('valOut=') + 8:len(line)]
                    Vinput = line[0:line.index('] RectF=')]
                except Exception as e:
                    pass

                if 'in' in typ:
                    listConnects[editor.currentTab][unit] = (typ, name, form, Vinput)
                else:
                    listConnects[editor.currentTab][unit] = (typ, name, form)

            elif line[0:8] == 'constant':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('value=') + 7:len(line)]
                vout = line[0:line.index('] format')]
                line = line[line.index('format=') + 8:len(line)]
                fort = line[0:line.index('] label')]
                if not fort:
                    fort = ''
                line = line[line.index('label=') + 7:len(line)]
                lab = line[0:line.index(']')]
                line = line[line.index('RectF=') + 7:len(line)]
                try:
                    listConstants[editor.currentTab][unit] = (fort, eval(vout), lab)
                except Exception as e:
                    listConstants[editor.currentTab][unit] = (fort, vout, lab)

            elif line[0:7] == 'loopFor':
                unit = re.search(r"\[([A-Za-z0-9*_]+)\]", line).group(1)
                line = line[line.index('inputs=') + 8:len(line)]
                inp = line[0:line.index('] outputs')]
                line = line[line.index('outputs=') + 9:len(line)]
                outp = line[0:line.index('] listItems=')]
                line = line[line.index('listItems=') + 11:len(line)]
                listIt = line[0:line.index('] RectF=')]
                line = line[line.index('RectF=') + 7:len(line)]

                listTools[editor.currentTab][unit] = eval(listIt)
                libTools[editor.currentTab][unit] = (eval(inp), eval(outp))

            elif line[0:6] == 'loopIf':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('inputs=') + 8:len(line)]
                inp = line[0:line.index('] outputs')]
                line = line[line.index('outputs=') + 9:len(line)]
                outp = line[0:line.index('] listItems=')]
                line = line[line.index('listItems=') + 11:len(line)]
                listIt = line[0:line.index('] RectF=')]
                line = line[line.index('RectF=') + 7:len(line)]

                listTools[editor.currentTab][unit] = eval(listIt)
                libTools[editor.currentTab][unit] = (eval(inp), eval(outp))

            elif line[0:6] == 'script':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('inputs=') + 7:len(line)]
                inp = line[0:line.index(' outputs')]
                line = line[line.index('outputs=') + 8:len(line)]
                outp = line[0:line.index(' code=')]
                line = line[line.index('code=') + 6:len(line)]
                code = line[0:line.index('] RectF=')]
                line = line[line.index('RectF=') + 7:len(line)]

                listTools[editor.currentTab][unit] = code
                libTools[editor.currentTab][unit] = [eval(inp), eval(outp)]


class UpdateUndoRedo:

    def __init__(self):
        for i in range(pointTyping[editor.currentTab] + 1, len(undoredoTyping[editor.currentTab])):
            del undoredoTyping[editor.currentTab][i]
        pointTyping[editor.currentTab] += 1
        undoredoTyping[editor.currentTab][pointTyping[editor.currentTab]] = SaveDiagram().toPlainText()
        index = editor.tabsDiagram.currentIndex()
        currentTitle = editor.tabsDiagram.tabText(index)
        if currentTitle[-1] != '*' and len(undoredoTyping[editor.currentTab]) > 1:
            currentTitle += '*'
            editor.tabsDiagram.setTabText(editor.currentTab, currentTitle)


class DiagramScene(QGraphicsScene):

    def __init__(self, parent=None):
        super(DiagramScene, self).__init__(parent)
        self.prevItem = []
        self._selectedItemVec = deque()

        pen = QtGui.QPen(ItemColor.cross_scene.value, 2)
        crss = QLineF(-10, 0, 10, 0)
        self.addLine(crss, pen)
        crss = QLineF(0, -10, 0, 10)
        self.addLine(crss, pen)

    def draw_grid(self):
        WIDTH = 20
        HEIGHT = 15
        NUM_BLOCKS_X = 100
        NUM_BLOCKS_Y = 140

        width = NUM_BLOCKS_X * WIDTH
        height = NUM_BLOCKS_Y * HEIGHT
        self.setSceneRect(0, 0, width, height)
        self.setItemIndexMethod(self.NoIndex)

        pen = QPen(QColor(150, 150, 150), 1, Qt.SolidLine)

        for x in range(-NUM_BLOCKS_X, NUM_BLOCKS_X + 1):
            xc = x * WIDTH
            self.lines.append(self.addLine(xc, -height, xc, height, pen))

        for y in range(-NUM_BLOCKS_Y, NUM_BLOCKS_Y + 1):
            yc = y * HEIGHT
            self.lines.append(self.addLine(-width, yc, width, yc, pen))

    def set_visible(self, visible=True):
        for line in self.lines:
            line.setVisible(visible)

    def delete_grid(self):
        for line in self.lines:
            self.removeItem(line)
        del self.lines[:]

    def set_opacity(self, opacity):
        for line in self.lines:
            line.setOpacity(opacity)

    def mouseMoveEvent(self, mouseEvent):
        editor.sceneMouseMoveEvent(mouseEvent)
        super(DiagramScene, self).mouseMoveEvent(mouseEvent)

    def mouseReleaseEvent(self, mouseEvent):
        if mouseEvent.button() == 2:  # Right mouse click
            # Set previous selections selected
            for item in self.prevItem:
                item.setSelected(1)

            item = self.itemAt(mouseEvent.scenePos().x(), mouseEvent.scenePos().y(), QTransform(0, 0, 0, 0, 0, 0))
            if item:
                item.setSelected(1)

        if mouseEvent.button() == 1:  # Left mouse click
            # Get selected item
            items = editor.diagramScene[editor.currentTab].selectedItems()
            # Shift click
            if mouseEvent.modifiers() & Qt.ShiftModifier:
                # Set previous items selected
                for item in self.prevItem:
                    item.setSelected(1)

                for item in items:
                    self.prevItem.append(item)

                item = self.itemAt(mouseEvent.scenePos().x(), mouseEvent.scenePos().y(), QTransform(0, 0, 0, 0, 0, 0))
                if item is None:
                    self.clearSelection()
            else:
                self.prevItem = []
                for item in items:
                    self.prevItem.append(item)
        editor.sceneMouseReleaseEvent(mouseEvent)
        super(DiagramScene, self).mouseReleaseEvent(mouseEvent)
#         UpdateUndoRedo()

    def mousePressEvent(self, mouseEvent):

        item = self.itemAt(mouseEvent.scenePos().x(),
                           mouseEvent.scenePos().y(),
                           QTransform(0, 0, 0, 0, 0, 0))

        if not item and len(editor.diagramScene[editor.currentTab].selectedItems()) == 0:
            if mouseEvent.button() == 2:  # Right mouse click
                pos = mouseEvent.scenePos()
                menu = QMenu()
                fitWindow = menu.addAction('Fit to window')
                fitWindow.triggered.connect(self.fitwindow)
                menu.addSeparator()
                addin = menu.addAction('Add input connector')
                addin.triggered.connect(lambda: self.addInputConn(pos.x(), pos.y()))
                addout = menu.addAction('Add output connector')
                addout.triggered.connect(lambda: self.addOutputConn(pos.x(), pos.y()))

                menu.exec_(mouseEvent.screenPos())
#                 mouseEvent.accept()

#             if mouseEvent.button() == 1 and int(mouseEvent.modifiers())\
#                                         == (Qt.ControlModifier + Qt.AltModifier):
#                 editor.sceneMousePressEvent(mouseEvent)

            if mouseEvent.button() == 1 and mouseEvent.modifiers() == Qt.ShiftModifier:
                print("Shift")
                item = self.itemAt(mouseEvent.scenePos().x(),
                                   mouseEvent.scenePos().y(),
                                   QTransform(0, 0, 0, 0, 0, 0))
                if item:
                    item.setSelected(1)
                    self._selectedItemVec.append(item)
                else:
                    return QGraphicsScene.mousePressEvent(self, mouseEvent)

        return QGraphicsScene.mousePressEvent(self, mouseEvent)

    def addInputConn(self, x, y):
        self.conn = ConnectorItem('unkn', '', 70, 26, 'in', 'unkn', '')
        self.conn.setPos(x + 10, y)
        editor.diagramScene[editor.currentTab].addItem(self.conn)
        UpdateUndoRedo()

    def addOutputConn(self, x, y):
        self.conn = ConnectorItem('unkn', '', 70, 26, 'out', 'unkn', '')
        self.conn.setPos(x, y)
        editor.diagramScene[editor.currentTab].addItem(self.conn)
        UpdateUndoRedo()

    def fitwindow(self):
        self.setSceneRect(self.itemsBoundingRect())
        editor.diagramView[editor.currentTab].centerOn(0, 0)
        editor.diagramView[editor.currentTab]\
            .fitInView(self.sceneRect(), QtCore.Qt.KeepAspectRatio)
        editor.diagramView[editor.currentTab].scale(0.8, 0.8)


class DiagramView(QGraphicsView):

    def __init__(self, scene, parent=None):
        QGraphicsView.__init__(self, scene, parent)
        global undoredoTyping
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.scalefactor = 1
        self.setBackgroundBrush(ItemColor.backGround.value)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemShape)
        self.setContentsMargins(0, 0, 0, 0)

        self.caseFinal = False
        self.currentLoop = None
        self.m_originX, self.m_originY = 0, 0

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('mod_SubMod')\
                or event.mimeData().hasFormat('blocks_subModules')\
                or event.mimeData().hasFormat('structures_tools'):
            event.accept()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat('mod_SubMod')\
                or event.mimeData().hasFormat('blocks_subModules')\
                or event.mimeData().hasFormat('structures_tools'):
            pos = self.mapToScene(event.pos())
            itm = self.scene().itemAt(pos, QTransform(0, 0, 0, 0, 0, 0))

            if type(itm) == ForLoopItem:
                itm.activeState()
                self.caseFinal = True
#                 self.currentLoop = itm.unit
                if self.currentLoop:
                    if self.currentLoop.unit != itm.unit:
                        self.currentLoop.normalState()
                self.currentLoop = itm
            else:
                for elem in self.items():
                    if type(elem) == ForLoopItem:
                        elem.normalState()
                        self.caseFinal = False
            event.accept()

    def dropEvent(self, event):
        if event.mimeData().hasFormat('mod_SubMod'):
            name = str(event.mimeData().data('mod_SubMod'))
            name = name[2:len(name) - 1]
            ind = 0
            for i, j in enumerate(editor.getlib()):
                if j[0] == name:
                    ind = i
                    break
            self.b1 = ProcessItem('newBlock',
                                  name,
                                  editor.getlib()[ind][1],
                                  150, 80,
                                  editor.getlib()[ind][2]).getBlocks()
            self.b1.setPos(self.mapToScene(event.pos()))
            self.scene().addItem(self.b1)
            listItems[editor.currentTab][self.b1.unit] = self.b1
            self.addItemLoop(self.b1.unit)

        elif event.mimeData().hasFormat('blocks_subModules'):
            name = str(event.mimeData().data('blocks_subModules'))
            name = name[2:len(name) - 1]
            self.bm = SubProcessItem('newSubMod', name, 150, 80, None).getSubblocks()
            self.bm.setPos(self.mapToScene(event.pos()))
            self.scene().addItem(self.bm)
            listItems[editor.currentTab][self.bm.unit] = self.bm
            self.addItemLoop(self.bm.unit)

        elif event.mimeData().hasFormat('structures_tools'):
            name = str(event.mimeData().data('structures_tools'))
            name = name[2:len(name) - 1]
            if "For" in name:
                self.a1 = ForLoopItem('newForLoop', name, 200.0, 200.0, True)
                self.a1.setPos(self.mapToScene(event.pos()))
                self.scene().addItem(self.a1)
                self.addItemLoop(self.a1.unit)
            elif "If" in name:
                self.a1 = ForLoopItem('newIf', name, 200.0, 200.0, True)
                self.a1.setPos(self.mapToScene(event.pos()))
                self.scene().addItem(self.a1)
                self.addItemLoop(self.a1.unit)  # ???? needed ?
            elif "Comments" in name:
                self.a1 = CommentsItem(200, 150, 'Comments', True)
                self.a1.setPos(self.mapToScene(event.pos()))
                self.scene().addItem(self.a1)
            elif "Constant" in name:
                if 'string' in name:
                    val = 'your text'
                    form = 'str'
                elif 'integer' in name:
                    val = 0
                    form = 'int'
                elif 'float' in name:
                    val = 0.0
                    form = 'float'
                elif 'combobox' in name:
                    form = "enumerate(('item1','item2','item3'))"
                    val = 'item1'
                elif 'boolean' in name:
                    val = True
                    form = 'bool'
                elif 'path' in name:
                    val = 'path'
                    form = 'path'
                self.a1 = Constants('newConstant', 80, 30, val, form, '', True)
                self.a1.setPos(self.mapToScene(event.pos()))
                self.scene().addItem(self.a1)
                self.addItemLoop(self.a1.unit)
            elif "Script" in name:
                self.a1 = ScriptItem('newScript', name, 200.0, 200.0, True)
                self.a1.setPos(self.mapToScene(event.pos()))
                self.scene().addItem(self.a1)
                self.addItemLoop(self.a1.unit)
            elif name in ["Value", "Type", "Length"]:
                self.a1 = Probes('new', 'unkn', name, True)
                self.a1.setPos(self.mapToScene(event.pos()))
                self.scene().addItem(self.a1)
                self.addItemLoop(self.a1.unit)
            try:
                listItems[editor.currentTab][self.a1.unit] = self.a1
            except Exception as e:
                pass
        UpdateUndoRedo()
        return QGraphicsView.dropEvent(self, event)

    def addItemLoop(self, unitItem):
        if self.currentLoop:
            ind = 0
            if self.currentLoop.loopIf:
                if self.currentLoop.elemProxy.currentText() == 'False':
                    ind = 1
            for elem in editor.diagramScene[editor.currentTab].items():
                if type(elem) == ForLoopItem and elem.unit == self.currentLoop.unit:
                    elem.normalState()
                    elem.IteminLoop(unitItem, self.caseFinal, ind)
#                     elem.setDimension()
                    self.currentLoop = None
                    self.caseFinal = False
                    break

    def loadBlock(self, unit, name, cat, pos, *inout):
        self.b2 = ProcessItem(unit, name, cat, pos[2], pos[3], *inout).getBlocks()
        self.b2.setPos(pos[0], pos[1])
        self.scene().addItem(self.b2)
        listItems[editor.currentTab][self.b2.unit] = self.b2
        self.ball = self.b2

    def loadMod(self, unit, name, pos, *inout):
        self.b3 = SubProcessItem(unit, name, pos[2], pos[3], *inout).getSubblocks()
        self.b3.setPos(pos[0], pos[1])
        self.scene().addItem(self.b3)
        listItems[editor.currentTab][self.b3.unit] = self.b3
        self.ball = self.b3

    def loadConn(self, unit, name, pos, inout, format, Vinput):
        self.b4 = ConnectorItem(name, unit, pos[2], pos[3], str(inout), format, Vinput)
        self.b4.setPos(pos[0], pos[1])
        self.scene().addItem(self.b4)
        self.ball = self.b4

    def loadComments(self, pos, text):
        self.b5 = CommentsItem(pos[2], pos[3], text, True)
        self.b5.setPos(pos[0], pos[1])
        self.scene().addItem(self.b5)
        self.ball = self.b5

    def loadLoopFor(self, unit, pos, inp, outp):
        if 'I' in unit:
            name = 'If'
        else:
            name = 'For'
            if 'm' in unit:
                name += '_multiprocessing'
        self.b6 = ForLoopItem(unit, name, pos[2], pos[3], True, inp, outp)
        self.b6.setPos(pos[0], pos[1])
        self.scene().addItem(self.b6)
        listItems[editor.currentTab][self.b6.unit] = self.b6
        self.ball = self.b6

    def loadConstant(self, unit, pos, vout, format, label):
        self.b7 = Constants(unit, pos[2], pos[3], vout, format, label, True)
        self.b7.setPos(pos[0], pos[1])
        self.scene().addItem(self.b7)
        listItems[editor.currentTab][self.b7.unit] = self.b7
        self.ball = self.b7

    def loadScriptItem(self, unit, title, pos, inp, outp):
        self.b8 = ScriptItem(unit, title, pos[2], pos[3], True, inp, outp)
        self.b8.setPos(pos[0], pos[1])
        self.scene().addItem(self.b8)
        listItems[editor.currentTab][self.b8.unit] = self.b8
        self.ball = self.b8

    def loadProbe(self, unit, label, format, pos):
        self.b9 = Probes(unit, format, label, True)
        self.b9.setPos(pos[0], pos[1])
        self.scene().addItem(self.b9)
        listItems[editor.currentTab][self.b9.unit] = self.b9
        self.ball = self.b9

    def mousePressEvent(self, event):
        if event.button() == Qt.MidButton:
            self.__prevMousePos = event.pos()
        elif event.button() == Qt.LeftButton:
            self.m_originX, self.m_originY = self.mapToScene(event.pos()).x(), self.mapToScene(event.pos()).y()
            return QGraphicsView.mousePressEvent(self, event)
        else:
            super(DiagramView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MidButton:
            offset = self.__prevMousePos - event.pos()
            self.__prevMousePos = event.pos()
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() + offset.y())
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() + offset.x())
        else:
            super(DiagramView, self).mouseMoveEvent(event)

    def wheelEvent(self, event):
        adj = 0.1777
        if event.angleDelta().y() < 0:
            adj = -adj

        self.scalefactor += adj
        self.scale(1 + adj, 1 + adj)

        rectBounds = self.scene().itemsBoundingRect()
        self.scene().setSceneRect(rectBounds.x() - 200, rectBounds.y() - 200, rectBounds.width() + 400, rectBounds.height() + 400)

    def returnBlockSystem(self):
        return self.ball

    def keyPressEvent(self, event):
        if QKeySequence(event.key() + int(event.modifiers())) == QKeySequence("Ctrl+V"):
            try:
                posRe = (self.m_originX, self.m_originY, itemStored.boundingRect().width(), itemStored.boundingRect().height())
            except Exception as e:
                posRe = (0, 0, 100, 100)

            if type(itemStored) == ConnectorItem:
                if 'in' in itemStored.inout:
                    self.scene().addInputConn(self.m_originX, self.m_originY)
                else:
                    self.scene().addOutputConn(self.m_originX, self.m_originY)
                UpdateUndoRedo()

            if type(itemStored) == BlockCreate:
                if itemStored.category is not None:
                    self.loadBlock('newBlock', itemStored.name, itemStored.category, posRe, itemStored.inout[0])
                else:
                    self.loadMod('newSubMod', itemStored.name, posRe)

            if type(itemStored) == CommentsItem:
                self.loadComments(posRe, itemStored.label.toPlainText())

            if type(itemStored) == Constants:
                self.loadConstant('newConstant', posRe, itemStored.val, itemStored.form, '')

            if type(itemStored) == Probes:
                self.loadProbe('new', itemStored.label, 'unkn', posRe)

            UpdateUndoRedo()
        return QGraphicsView.keyPressEvent(self, event)


class PreviewBlock(QGraphicsView):

    def __init__(self, parent=None):
        QGraphicsView.__init__(self, parent)

        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.fitInView(self.sceneRect(), QtCore.Qt.KeepAspectRatio)

        self.setEnabled(True)
        self.scalefactor = 1

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            adj = 0.1777
        else:
            adj = -0.1777

        self.scalefactor += adj
        self.scale(1 + adj, 1 + adj)


class TextInfo(QTextEdit):

    def __init__(self, parent=None):
        super(TextInfo, self).__init__(parent)
        self.setReadOnly(True)
        self.text = ''

        def append(self, txt):
            txt.append(txt)
            txt._text += str(txt) if isinstance(txt, QStringListModel) else txt

        def text(self):
            return self.document().toPlainText()


class Connection:

    def __init__(self, name, fromPort, toPort, format):
        self.fromPort = fromPort
        self.pos1 = None
        self.pos2 = None
        if 'array' in format:
            self.a = 12
            self.b = 10
        else:
            self.a = 8
            self.b = 6

        if fromPort:
            self.pos1 = fromPort.scenePos()
            fromPort.posCallbacks.append(self.setBeginPos)
        self.toPort = toPort
        # Create link item:
        self.link = LinkItem(name, format)
        editor.diagramScene[editor.currentTab].addItem(self.link)
        self.link.setPositionTxt(self.pos1)

    def setFromPort(self, fromPort):
        self.fromPort = fromPort
        if self.fromPort:
            self.pos1 = fromPort.scenePos()
            self.fromPort.posCallbacks.append(self.setBeginPos)

    def setToPort(self, toPort):
        self.toPort = toPort
        if self.toPort:
            self.pos2 = toPort.scenePos()
            self.toPort.posCallbacks.append(self.setEndPos)

    def setEndPos(self, endpos):
        self.pos2 = endpos

        path = QPainterPath()
        self.start_x, self.start_y = self.pos1.x(), self.pos1.y() - 1
        self.end_x, self.end_y = self.pos2.x(), self.pos2.y() - 1
        self.ctrl1_x, self.ctrl1_y = self.pos1.x() + (self.pos2.x() - self.pos1.x()) * 0.7, self.pos1.y()
        self.ctrl2_x, self.ctrl2_y = self.pos2.x() + (self.pos1.x() - self.pos2.x()) * 0.7, self.pos2.y()
        path.moveTo(self.start_x, self.start_y)

        path.cubicTo(self.ctrl1_x, self.ctrl1_y, self.ctrl2_x, self.ctrl2_y, self.end_x, self.end_y)

        self.link.setPath(path)
        self.link.bislink.setPath(path)
        self.link.setPositionTxt((self.start_x + self.end_x) / 2, (self.start_y + self.end_y) / 2)
        try:
            theta = atan((self.ctrl2_y - self.ctrl1_y) / (self.ctrl2_x - self.ctrl1_x))
        except Exception as e:
            theta = 1.5708
        polyhead = QPolygonF([
            QPointF((self.start_x + self.end_x) / 2, (1 + self.start_y + self.end_y) / 2),
            QPointF(-self.a * cos(theta) + self.b * sin(theta) + (self.start_x + self.end_x) / 2,
                    self.b * cos(theta) + self.a * sin(theta) + (self.start_y + self.end_y) / 2),
            QPointF(-self.a * cos(theta) - self.b * sin(theta) + (self.start_x + self.end_x) / 2,
                    1 - self.b * cos(theta) + self.a * sin(theta) + (self.start_y + self.end_y) / 2)])
        self.link.setPositionShow(polyhead)

    def setBeginPos(self, pos1):
        self.pos1 = pos1

        path = QPainterPath()
        self.start_x, self.start_y = self.pos1.x(), self.pos1.y() - 1
        self.end_x, self.end_y = self.pos2.x(), self.pos2.y() - 1
        self.ctrl1_x, self.ctrl1_y = self.pos1.x() + (self.pos2.x() - self.pos1.x()) * 0.7, self.pos1.y()
        self.ctrl2_x, self.ctrl2_y = self.pos2.x() + (self.pos1.x() - self.pos2.x()) * 0.7, self.pos2.y()
        path.moveTo(self.start_x, self.start_y)

        path.cubicTo(self.ctrl1_x, self.ctrl1_y, self.ctrl2_x, self.ctrl2_y, self.end_x, self.end_y)

        self.link.setPath(path)
        self.link.bislink.setPath(path)
        self.link.setPositionTxt((self.start_x + self.end_x) / 2, (self.start_y + self.end_y) / 2)

        try:
            theta = atan((self.ctrl2_y - self.ctrl1_y) / (self.ctrl2_x - self.ctrl1_x))
        except Exception as e:
            theta = 1.5708
        polyhead = QPolygonF([
            QPointF((self.start_x + self.end_x) / 2, (self.start_y + self.end_y) / 2),
            QPointF(-self.a * cos(theta) + self.b * sin(theta) + (self.start_x + self.end_x) / 2,
                    self.b * cos(theta) + self.a * sin(theta) + (self.start_y + self.end_y) / 2),
            QPointF(-self.a * cos(theta) - self.b * sin(theta) + (self.start_x + self.end_x) / 2,
                    -self.b * cos(theta) + self.a * sin(theta) + (self.start_y + self.end_y) / 2)])
        self.link.setPositionShow(polyhead)

    # if link connected nowhere
    def delete(self):
        editor.diagramScene[editor.currentTab].removeItem(self.link)
        editor.diagramScene[editor.currentTab].removeItem(self.link.getlinkTxt())
        editor.diagramScene[editor.currentTab].removeItem(self.link.getlinkShow())
        editor.diagramScene[editor.currentTab].removeItem(self.link.getBislink())

##########################################################################


class LinkItem(QGraphicsPathItem):

    def __init__(self, name, typeColor):
        super(LinkItem, self).__init__(None)

        self.bislink = QGraphicsPathItem()
        self.bislink.setZValue(2)

        for types in TypeColor:
            if types.name in typeColor:
                self.color = types.value

        if 'list' in str(typeColor):
            self.weight = DimLink.list.value
            self.bislink.setPen(QtGui.QPen(Qt.NoPen))

        elif 'array' in str(typeColor):
            self.weight = DimLink.array.value
            self.bislink.setPen(QtGui.QPen(ItemColor.bis_link.value, DimLink.bis.value, Qt.SolidLine))

        else:
            self.weight = DimLink.simple.value
            self.bislink.setPen(QtGui.QPen(Qt.NoPen))

        self.setPen(QtGui.QPen(self.color, self.weight))
        self.setZValue(1)

        self.setFlag(QGraphicsItem.ItemIsSelectable, False)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)

        self.name = ''

        if name == '':
            NodeExist = True
            inc = 0
            while NodeExist:
                if 'N' + str(inc) in listNodes[editor.currentTab]:
                    inc += 1
                else:
                    NodeExist = False
            self.name = 'N' + str(inc)
        else:
            self.name = name

        self.linkTxt = LinkText(self.name, self.color)
        self.linkTxt.setVisible(True)
        self.linkShow = LinkArrow(self.color)
        self.linkShow.setVisible(True)

        editor.diagramScene[editor.currentTab].addItem(self.linkTxt)
        editor.diagramScene[editor.currentTab].addItem(self.linkShow)
        editor.diagramScene[editor.currentTab].addItem(self.bislink)

    def foncedBlock(self, fcd):
        if fcd:
            self.setOpacity(0.4)
        else:
            self.setOpacity(1.0)

    def focusInEvent(self, event):
        self.setPen(QtGui.QPen(QColor(150, 150, 250, 255), 2, Qt.DashDotDotLine))
        self.linkTxt.setDefaultTextColor(QColor(150, 150, 250, 255))
        self.linkShow.setPen(QtGui.QPen(QColor(150, 150, 250, 255), 2))
        self.bislink.setPen(QtGui.QPen(Qt.NoPen))
        return QGraphicsPathItem.focusInEvent(self, event)

    def focusOutEvent(self, event):
        self.setPen(QtGui.QPen(self.color, self.weight))
        self.linkTxt.setDefaultTextColor(self.color)
        self.linkShow.setPen(QtGui.QPen(self.color, 2))
        if self.weight == 8:
            self.bislink.setPen(QtGui.QPen(ItemColor.bis_link.value, DimLink.bis.value, Qt.SolidLine))
        return QGraphicsPathItem.focusOutEvent(self, event)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Delete:
            self.deletelink()

    def setPath(self, event):
        return QGraphicsPathItem.setPath(self, event)

    def setPositionTxt(self, *pos):
        self.linkTxt.setPos(*pos)

    def setPositionShow(self, posPolygon):
        self.linkShow.setPolygon(posPolygon)

    def getlinkTxt(self):
        return self.linkTxt

    def getlinkShow(self):
        return self.linkShow

    def getBislink(self):
        return self.bislink

    def contextMenuEvent(self, event):
        menu = QMenu()
        de = menu.addAction('Delete')
        de.triggered.connect(self.deletelink)
        menu.exec_(event.screenPos())

    def deletelink(self):

        nameItem = listNodes[editor.currentTab][self.name]
        nameItemTmp0 = nameItem[0:nameItem.index('#Node#')]
        unitTmp0 = nameItemTmp0[0:nameItemTmp0.index(':')]
        nameItemTmp0 = nameItemTmp0[nameItemTmp0.index(':') + 1:len(nameItemTmp0)]

        if 'C' in unitTmp0:
            for elem in editor.diagramView[editor.currentTab].items():
                if type(elem) == Port:
                    if elem.unit == unitTmp0:
                        other = False
                        for lstNode in listNodes[editor.currentTab]:
                            if not lstNode == self.name:
                                tmpq = listNodes[editor.currentTab][lstNode]
                                tmpq = tmpq[0:tmpq.index(':')]
                                if tmpq == unitTmp0:
                                    other = True
                                    break
                        if not other:
                            elem.setBrush(QBrush(TypeColor.unkn.value))
                            elem.label.setPlainText('unkn')
                            elem.format = 'unkn'
                            elem.name = 'unkn'
                            elem.label.setPos(elem.pos().x() - 160 - elem.label.boundingRect().size().width(),
                                              elem.label.pos().y())
                            tmp = listConnects[editor.currentTab][elem.unit]
                            del listConnects[editor.currentTab][elem.unit]
                            if 'in' in tmp[0]:
                                listConnects[editor.currentTab][elem.unit] = (tmp[0], 'unkn', 'unkn', '')
        # replace values input
        nameItemTmp = nameItem[nameItem.index('#Node#') + 6:len(nameItem)]
        unitTmp = nameItemTmp[0:nameItemTmp.index(':')]
        nameItemTmp = nameItemTmp[nameItemTmp.index(':') + 1:len(nameItemTmp)]

        if 'U' in unitTmp:
            listVal = listBlocks[editor.currentTab][unitTmp]
            mod = listVal[0]

            for i, j in enumerate(editor.getlib()):
                if j[0] == mod:
                    indMod = i
                    break
            ################################################################
            category = listVal[1]
            cat = category.split('.')
            listEnter = editor.getlib()[indMod][2][0]
            listValDefault = editor.getlib()[indMod][2][1]
            if len(listEnter) != len(listVal[2][1]):
                if '_dyn' in mod:
                    listEnter = listVal[2][0]
                    tmplistVal = listVal[2][1]
                    tmpList = []
                    for indDef in listValDefault:
                        tmpList.append(indDef)
                    for i in range(len(listValDefault), len(tmplistVal)):
                        tmpList.append(tmpList[-1])
                    listValDefault = tmpList
                else:
                    pathYml = os.path.dirname(os.path.realpath(__file__))
                    pathYml = os.path.join(pathYml, '../modules', cat[0], cat[1] + ".yml")
                    if os.path.exists(pathYml):
                        with open(pathYml, 'r') as stream:
                            self.dicts = yaml.load(stream, yaml.FullLoader)
                            for el in self.dicts[mod]:
                                if el in listVal[2][0]:
                                    listEnter = (*listEnter, el)
                                    if type(self.dicts[mod][el]).__name__ == 'str':
                                        if 'enumerate' in self.dicts[mod][el]:
                                            listValDefault = (*listValDefault, self.dicts[mod][el])
                                        else:
                                            try:
                                                listValDefault = (*listValDefault, eval(self.dicts[mod][el]))
                                            except Exception as e:
                                                listValDefault = (*listValDefault, self.dicts[mod][el])
                                    else:
                                        try:
                                            listValDefault = (*listValDefault, eval(self.dicts[mod][el]))
                                        except Exception as e:
                                            listValDefault = (*listValDefault, self.dicts[mod][el])
            ################################################################
            newList = []
            for i in range(len(listEnter)):
                if listEnter[i] == nameItemTmp:
                    newValfromModules = listValDefault[i]
                    if type(newValfromModules).__name__ == 'str':
                        if 'enumerate' in newValfromModules:
                            newValfromModules = list(eval(newValfromModules))[0][1]
                    newList.append(newValfromModules)
                else:
                    newList.append(listVal[2][1][i])
            ################################################################
            del listBlocks[editor.currentTab][unitTmp]
            listBlocks[editor.currentTab][unitTmp] = (listVal[0], listVal[1], (listVal[2][0], newList, listVal[2][2], listVal[2][3]))

        elif 'C' in unitTmp:
            for elem in editor.diagramView[editor.currentTab].items():
                if type(elem) == Port:
                    if elem.unit == unitTmp:
                        elem.setBrush(QBrush(TypeColor.unkn.value))
                        elem.label.setPlainText('unkn')
                        elem.format = 'unkn'
                        elem.name = 'unkn'
                        tmp = listConnects[editor.currentTab][elem.unit]
                        del listConnects[editor.currentTab][elem.unit]
                        listConnects[editor.currentTab][elem.unit] = (tmp[0], 'unkn', 'unkn')

        elif 'P' in unitTmp:
            for elem in editor.diagramView[editor.currentTab].items():
                if type(elem) == Port:
                    if elem.unit == unitTmp:
                        elem.setBrush(QBrush(TypeColor.unkn.value))
                        elem.format = 'unkn'
                        tmp = listProbes[editor.currentTab][elem.unit]
                        del listProbes[editor.currentTab][elem.unit]
                        listProbes[editor.currentTab][elem.unit] = ('unkn', tmp[1])

        elif 'M' in unitTmp:
            listVal = listSubMod[editor.currentTab][unitTmp]
            mod = listVal[0]

            for i, j in enumerate(libSubMod):
                if j[0] == mod:
                    indMod = i
                    break
            ind = listVal[1][0].index(nameItemTmp)
            newValfromModules = libSubMod[indMod][1][0][1][ind]
            if type(newValfromModules).__name__ == 'str':
                if 'enumerate' in newValfromModules:
                    newValfromModules = list(eval(newValfromModules))[0][1]

            newList = []
            for i in range(len(listVal[1][1])):
                if i == ind:
                    newList.append(newValfromModules)
                else:
                    newList.append(listVal[1][1][i])

            del listSubMod[editor.currentTab][unitTmp]
            listSubMod[editor.currentTab][unitTmp] = (listVal[0], (listVal[1][0], newList, listVal[1][2], listVal[1][3]))

        if 'I' in unitTmp0 and 'I' in unitTmp:
            tmplistTools = listTools[editor.currentTab][unitTmp]
            tmp0 = tmplistTools[0]
            for elem in tmp0:
                if elem == self.name:
                    tmp0.remove(self.name)
            tmp1 = tmplistTools[1]
            for elem in tmp1:
                if elem == self.name:
                    tmp1.remove(self.name)
            listTools[editor.currentTab][unitTmp] = [tmp0, tmp1]

        del listNodes[editor.currentTab][self.name]
        listNodes[editor.currentTab] = ReorderList(listNodes[editor.currentTab]).getNewList()

        editor.diagramScene[editor.currentTab].removeItem(self)
        editor.diagramScene[editor.currentTab].removeItem(self.linkTxt)
        editor.diagramScene[editor.currentTab].removeItem(self.linkShow)
        editor.diagramScene[editor.currentTab].removeItem(self.bislink)

        UpdateUndoRedo()


class LinkArrow(QGraphicsPolygonItem):

    def __init__(self, color, parent=None):
        super(LinkArrow, self).__init__(parent)
        self.setPen(QtGui.QPen(color, 2))
        self.setBrush(color)


class LinkText(QGraphicsTextItem):

    def __init__(self, textNode, color, parent=None):
        super(LinkText, self).__init__(parent)
        self.setPlainText(textNode)
        self.setFont(QFont("Times", 10, QFont.AnyStyle))
        self.setDefaultTextColor(color)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)

    def mousePressEvent(self, event):
        editor.diagramScene[editor.currentTab].clearSelection()
        return QGraphicsTextItem.mousePressEvent(self, event)

#########################################################################


class ProcessItem():

    def __init__(self, unit='newBlock', name='Untitled', category='untitled', w=150, h=80, *inout, parent=None):
        self.category = category
        self.name = name
        self.unit = unit

        if unit in 'newBlock':
            BlockExist = True
            inc = 0
            while BlockExist:
                if 'U' + str(inc) in listBlocks[editor.currentTab]:
                    inc += 1
                else:
                    BlockExist = False
            self.unit = 'U' + str(inc)
        else:
            self.unit = unit

        ind = 0
        for i, j in enumerate(editor.getlib()):
            if j[0] == self.name:
                ind = i
                break

        listVal = inout[0]

        cat = category.split('.')
        listEnter = editor.getlib()[ind][2][0]
        listValDefault = editor.getlib()[ind][2][1]
        if len(listEnter) != len(listVal[0]):
            if '_dyn' in self.name:
                listVal = inout[0][1]
                tmpList = []
                for indDef in listValDefault:
                    tmpList.append(indDef)
                for i in range(len(listValDefault), len(listVal)):
                    tmpList.append(tmpList[-1])
                listValDefault = tmpList
            else:
                pathYml = os.path.dirname(os.path.realpath(__file__))
                pathYml = os.path.join(pathYml, '../modules', cat[0], cat[1] + ".yml")
                if os.path.exists(pathYml):
                    with open(pathYml, 'r') as stream:
                        self.dicts = yaml.load(stream, yaml.FullLoader)
                        for el in self.dicts[name]:
                            if el in listVal[0]:
                                listEnter = (*listEnter, el)
                                if type(self.dicts[name][el]).__name__ == 'str':
                                    if 'enumerate' in self.dicts[name][el]:
                                        listValDefault = (*listValDefault, self.dicts[name][el])
                                    else:
                                        try:
                                            listValDefault = (*listValDefault, str(eval(self.dicts[name][el])))
                                        except Exception as e:
                                            listValDefault = (*listValDefault, str(self.dicts[name][el]))
                                else:
                                    try:
                                        listValDefault = (*listValDefault, eval(self.dicts[name][el]))
                                    except Exception as e:
                                        listValDefault = (*listValDefault, self.dicts[name][el])

        ###############################################################################
        newVal = []
        if inout[0][1]:
            for it in inout[0][1]:
                if type(it).__name__ == 'str':
                    if 'enumerate' in it:
                        newVal.append(list(eval(it))[0][1])
                    else:
                        newVal.append(it)
                else:
                    newVal.append(it)
        ###############################################################################
        self.block = BlockCreate(self.name, self.unit, self.category, w, h, listValDefault, True, *inout)
        listBlocks[editor.currentTab][self.unit] = (name, category, (inout[0][0], newVal, inout[0][2], inout[0][3]))
        ###############################################################################

    def getBlocks(self):
        return self.block


class SubProcessItem():

    def __init__(self, unit='newSubMod', nameSubModule='', w=150, h=80, *inout, parent=None):
        self.name = nameSubModule
        self.unit = 'M0'
        self.w = w
        self.h = h
        self.inout = inout

        self.inputs = []
        self.outputs = []

        listlabelIn = []
        listVal = []
        listlabelOut = []
        listForm = []

        wminIn = 0.0
        wminOut = 0.0

        if unit in 'newSubMod':
            SubModExist = True
            inc = 0
            while SubModExist:
                if 'M' + str(inc) in listSubMod[editor.currentTab]:
                    inc += 1
                else:
                    SubModExist = False
            self.unit = 'M' + str(inc)

            ind = 0
            for i, j in enumerate(libSubMod):
                if j[0] == self.name:
                    indMod = i
                    break
            inout = (libSubMod[indMod][1][0],)

        else:
            self.unit = unit
            for i, j in enumerate(libSubMod):
                if j[0] == self.name:
                    indMod = i
                    break

        listVal = libSubMod[indMod][1][0][1]

        newVal = []
        for it in inout[0][1]:
            if type(it).__name__ == 'enumerate':
                newVal.append(list(it)[0][1])
            else:
                newVal.append(it)

        self.subBlock = BlockCreate(self.name, self.unit, None, w, h, listVal, True, *inout)
        listSubMod[editor.currentTab][self.unit] = (self.name, (inout[0][0], newVal, inout[0][2], inout[0][3]))

    def getSubblocks(self):
        return self.subBlock


class BlockCreate(QGraphicsRectItem):

    def __init__(self, name='', unit='', category=None, w=150, h=80, listValIn=(), isMod=True, *inout, parent=None):
        super(BlockCreate, self).__init__(parent)
        global undoredoTyping
        self.name = name
        self.unit = unit
        self.category = category
        self.listValIn = listValIn
        self.inout = inout
        self.isMod = isMod
        self.w = w
        self.h = h
        self.wmin = 0.0
        self.hmin = 0.0
        self.setZValue(0)
        self.preview = False
        self.link = ''

        self.moved = False
        self.setAcceptHoverEvents(True)

        if self.category:
            self.editBlock(ItemColor.process.value, ItemColor.frame_process.value)
        else:
            self.editBlock(ItemColor.subprocess.value, ItemColor.frame_subprocess.value)

        self.caseFinal = False
        self.currentLoop = None

    def editBlock(self, colorGradient, colorPen):
        gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 50))
        gradient.setColorAt(0.3, colorGradient)

        self.setPen(QtGui.QPen(colorPen, 2))
        self.setBrush(QBrush(gradient))
        if self.isMod:
            self.setFlags(self.ItemIsSelectable | self.ItemIsMovable)
        self.setFlag(self.ItemIsFocusable, True)

        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # Label:
        self.label = QGraphicsTextItem(self.name, self)
        self.label.setDefaultTextColor(ItemColor.text_block_label.value)
        self.label.setFont(QFont("Times", 12, QFont.Bold))

        self.nameUnit = QGraphicsTextItem(self.unit, self)
        self.nameUnit.setDefaultTextColor(ItemColor.text_block_label.value)
        self.nameUnit.setFont(QFont("Times", 12, QFont.Bold))

        self.box_title = QGraphicsRectItem(self)
        self.box_title.setBrush(QBrush(ItemColor.backGround.value))
        self.box_title.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        self.box_title.setZValue(-2)
        self.box_title.setParentItem(self)

        wminIn = 0.0
        self.inputs = []
        i = 0
        if self.listValIn:
            for i, j in enumerate(self.listValIn):
                typ = 'str'
                if type(j).__name__ not in 'str' or j == 'path' or 'enumerate' in j:
                    try:
                        typ = DefinitType(eval(j)).returntype()
                    except Exception as e:
                        typ = DefinitType(j).returntype()

                portIn = Port(self.inout[0][0][i], 'in', typ, self.unit, True, self.isMod, 4, -16, self)
                self.inputs.append(portIn)
                if wminIn < portIn.label.boundingRect().width():
                    wminIn = portIn.label.boundingRect().width()
                i += 1

        wminOut = 0.0
        self.outputs = []
        for i in range(len(self.inout[0][2])):
            portOut = Port(self.inout[0][2][i], 'out', self.inout[0][3][i], self.unit, True, self.isMod, 4, -16, self)
            self.outputs.append(portOut)
            if wminOut < portOut.label.boundingRect().width():
                wminOut = portOut.label.boundingRect().width()

        self.wmin = wminIn + 20 + wminOut

        factorh = 20
        self.hmin = factorh * len(self.inputs)
        if self.hmin < factorh * len(self.outputs):
            self.hmin = factorh * len(self.outputs)

        x, y = self.newSize(self.w, self.h)

        if '_dyn' in self.name:
            self.polUp = ArrowDynamicUp(self)
            self.polUp.setPos(0, y)

            self.polDown = ArrowDynamicDown(self)
            self.polDown.setPos(0, y)

        if self.isMod:
            self.resize = Wrist(self)
            self.resize.setPos(x, y)
            self.resize.posChangeCallbacks.append(self.newSize)  # Connect the callback
            self.resize.setFlag(self.resize.ItemIsSelectable, True)
            self.resize.wmin = self.wmin
            self.resize.hmin = self.hmin

    def newSize(self, w, h):
        # Limit the block size:
        if h < self.hmin:
            h = self.hmin
        if w < self.wmin:
            w = self.wmin

        self.setRect(0.0, 0.0, w, h)
        self.box_title.setRect(0.0, -22, w, 20)
        # center label:
        rect = self.label.boundingRect()
        lw, lh = rect.width(), rect.height()
        lx = (w - lw) / 2
        ly = (-30)
        self.label.setPos(lx, ly + 2)
        # bottom name unit:
        rect = self.nameUnit.boundingRect()
        lw, lh = rect.width(), rect.height()
        lx = (w - lw) / 2
        ly = (h)
        self.nameUnit.setPos(lx, ly)
        # Update port positions:
        if len(self.inputs) == 1:
            self.inputs[0].setPos(0, h / 2)
        elif len(self.inputs) > 1:
            y = (h) / (len(self.inputs) + 1)
            dy = (h) / (len(self.inputs) + 1)
            for inp in self.inputs:
                inp.setPos(0, y)
                y += dy

        if len(self.outputs) == 1:
            self.outputs[0].setPos(w, h / 2)

        elif len(self.outputs) > 1:
            y = (h) / (len(self.outputs) + 1)
            dy = (h) / (len(self.outputs) + 1)
            for outp in self.outputs:
                outp.setPos(w, y)
                y += dy

        try:
            self.polUp.setPos(0, h)
            self.polDown.setPos(0, h)
        except Exception as e:
            pass

        return w, h

    def hoverEnterEvent(self, event):
        # self.setFocus(True)
        pos = event.screenPos()
        self.showToolTip(self.name, pos)
        event.accept()
#         return QGraphicsRectItem.hoverEnterEvent(self, event)

    def hoverLeaveEvent(self, event):
        self.setSelected(False)
        return QGraphicsRectItem.hoverLeaveEvent(self, event)

    def contextMenuEvent(self, event):
        menu = QMenu()
        activ = False
        if self.name[len(self.name) - 2:] == '_d':
            activ = True

        if self.isMod:
            ac = menu.addAction('')
#             ci = menu.addAction('Add constants to all inputs')
#             ci.triggered.connect(self.addConstantsInputs)
#             menu.addSeparator()
            ac = menu.addAction('Add all inputs to connectors')
            ac.triggered.connect(self.addConnectorInputs)
            ad = menu.addAction('Add all outputs to connectors')
            ad.triggered.connect(self.addConnectorOutputs)
            menu.addSeparator()
            de = menu.addAction('Delete')
            de.triggered.connect(self.deleteBlocks)
            pa = menu.addAction('Parameters')
            if self.category:
                pa.triggered.connect(self.editParametersProcess)
                er = menu.addAction('Error handler')
                er.triggered.connect(self.errorHandl)
                sc = menu.addAction('See code')
                sc.triggered.connect(self.seeCode)
                ao = menu.addAction('Input options')
                ao.triggered.connect(self.inputOptions)
                if '_dyn' in self.name:
                    menu.addSeparator()
                    dya = menu.addAction('Add input dyn (+)')
                    dya.triggered.connect(self.addinput)
                    dys = menu.addAction('Remove input dyn (-)')
                    dys.triggered.connect(self.subinput)
            else:
                pa.triggered.connect(self.editParametersSubProcess)
                su = menu.addAction('See submodul')
                su.triggered.connect(self.seeSubMod)
        else:
            if self.category:
                sc = menu.addAction('See code')
                sc.triggered.connect(self.seeCode)
#                 menu.addSeparator()
#                 cs = menu.addAction('Capture Screen')
#                 cs.triggered.connect(self.captureScreen)
            else:
                su = menu.addAction('See submodul')
                su.triggered.connect(self.seeSubMod)

        menu.exec_(event.screenPos())

#     def addConstantsInputs(self):#         pass

    def addConnectorInputs(self):
        height = self.boundingRect().height() / 2
        i = 0
        for inp in self.inputs:
            inputTaken = False
            for key, val in listNodes[editor.currentTab].items():
                val = val[val.index("#Node") + 6:]
                inputTaken = (self.unit + ":" + inp.name) == val
                if inputTaken:
                    break

            if not inputTaken:
                posY = (((len(self.inputs) - 1) / 2) - i) * height / len(self.inputs)
                self.conn = ConnectorItem(inp.name, '', 80, 20, 'in', inp.format, self.listValIn[i])
                self.conn.setPos(self.mapToScene(inp.pos()).x() - 200, self.mapToScene(inp.pos()).y() - 4 * posY)
                editor.diagramScene[editor.currentTab].addItem(self.conn)
                startConnection = Connection('', self.conn.output, inp, inp.format)
                startConnection.setEndPos(inp.scenePos())
                startConnection.setToPort(inp)
                nt = startConnection.link.name
                nc = self.conn.connct
                listNodes[editor.currentTab][nt] = nc + ':' + self.conn.name + '#Node#' + self.unit + ':' + inp.name
                i += 1

                if 'U' in self.unit:
                    listVal = listBlocks[editor.currentTab][self.unit]
                    ind = listVal[2][0].index(inp.name)
                    newList = []
                    for j in range(len(listVal[2][1])):
                        if j == ind:
                            oldVal = listVal[2][1][j]
                            newList.append('Node(' + nt + ')')
                        else:
                            newList.append(listVal[2][1][j])
                    del listBlocks[editor.currentTab][self.unit]
                    listBlocks[editor.currentTab][self.unit] = (listVal[0], listVal[1], (listVal[2][0], newList, listVal[2][2], listVal[2][3]))

                if 'M' in self.unit:
                    listVal = listSubMod[editor.currentTab][self.unit]
                    ind = listVal[1][0].index(inp.name)
                    newList = []
                    for j in range(len(listVal[1][1])):
                        if j == ind:
                            oldVal = listVal[1][1][j]
                            newList.append('Node(' + nt + ')')
                        else:
                            newList.append(listVal[1][1][j])
                    del listSubMod[editor.currentTab][self.unit]
                    listSubMod[editor.currentTab][self.unit] = (listVal[0], (listVal[1][0], newList, listVal[1][2], listVal[1][3]))
        UpdateUndoRedo()

    def addConnectorOutputs(self):
        height = self.boundingRect().height() / 2
        i = 0
        for outp in self.outputs:
            posY = (((len(self.outputs) - 1) / 2) - i) * height / len(self.outputs)
            self.conn = ConnectorItem(outp.name, '', 70, 26, 'out', outp.format, '')
            self.conn.setPos(self.mapToScene(outp.pos()).x() + 100, self.mapToScene(outp.pos()).y() - 4 * posY)
            editor.diagramScene[editor.currentTab].addItem(self.conn)
            startConnection = Connection('', self.conn.input, outp, outp.format)
            startConnection.setEndPos(outp.scenePos())
            startConnection.setToPort(outp)
            nt = startConnection.link.name
            nc = self.conn.connct
            listNodes[editor.currentTab][nt] = self.unit + ':' + outp.name + '#Node#' + nc + ':' + self.conn.name
            i += 1
        UpdateUndoRedo()

    def editParametersProcess(self):
        for i, j in enumerate(editor.getlib()):
            if j[0] == self.name:
                indMod = i
                break
        cat = self.category.split('.')
        listValDefault = editor.getlib()[indMod][2][1]
        if '_dyn' in self.name:
            tmplistVal = self.inout[0][1]
            tmpList = []
            for indDef in listValDefault:
                tmpList.append(indDef)
            for i in range(len(listValDefault), len(tmplistVal)):
                tmpList.append(tmpList[-1])
            listValDefault = tmpList
        else:
            pathYml = os.path.dirname(os.path.realpath(__file__))
            pathYml = os.path.join(pathYml, '../modules', cat[0], cat[1] + ".yml")
            if os.path.exists(pathYml):
                with open(pathYml, 'r') as stream:
                    self.dicts = yaml.load(stream, yaml.FullLoader)
                    for el in self.dicts[self.name]:
                        if el in listBlocks[editor.currentTab][self.unit][2][0]:
                            if type(self.dicts[self.name][el]).__name__ == 'str':
                                if 'enumerate' in self.dicts[self.name][el]:
                                    listValDefault = (*listValDefault, self.dicts[self.name][el])
                                else:
                                    try:
                                        listValDefault = (*listValDefault, eval(self.dicts[self.name][el]))
                                    except Exception as e:
                                        listValDefault = (*listValDefault, self.dicts[self.name][el])
                            else:
                                try:
                                    listValDefault = (*listValDefault, eval(self.dicts[self.name][el]))
                                except Exception as e:
                                    listValDefault = (*listValDefault, self.dicts[self.name][el])

        c = editParam(self.name, self.unit, listBlocks[editor.currentTab][self.unit][2], listValDefault)
        c.exec_()
        listVal = listBlocks[editor.currentTab][self.unit]
        try:
            del listBlocks[editor.currentTab][self.unit]
            listBlocks[editor.currentTab][self.unit] = (listVal[0], listVal[1], (listVal[2][0], c.getNewValues(), listVal[2][2], listVal[2][3]))
        except Exception as e:
            listBlocks[editor.currentTab][self.unit] = listVal

    def editParametersSubProcess(self):
        for i, j in enumerate(libSubMod):
            if j[0] == self.name:
                indMod = i
                break
        c = editParam(self.name, self.unit, listSubMod[editor.currentTab][self.unit][1], libSubMod[indMod][1][0][1])
        c.exec_()
        listVal = listSubMod[editor.currentTab][self.unit]
        try:
            del listSubMod[editor.currentTab][self.unit]
            listSubMod[editor.currentTab][self.unit] = (listVal[0], (listVal[1][0], c.getNewValues(), listVal[1][2], listVal[1][3]))
        except Exception as e:
            listSubMod[editor.currentTab][self.unit] = listVal

    def errorHandl(self):
        c = errorHandler(self.name, self.unit)
        c.exec_()

    def seeCode(self):
        c = seeCode(self.category, self.name)
        c.exec_()

    def captureScreen(self):
        area = QRect(self.sceneBoundingRect().x() - 100, self.sceneBoundingRect().y() - 50, self.sceneBoundingRect().width() + 200, self.sceneBoundingRect().height() + 100)
#         area = previewScene.sceneRect()
        image = QImage(area.width(), area.height(), QImage.Format_ARGB32)
        image.fill(ItemColor.backGround.value)
        painter = QPainter()
        painter.begin(image)
        painter.setRenderHint(QPainter.Antialiasing, True)
        previewScene.render(painter, QRectF(image.rect()), QRectF(area), Qt.KeepAspectRatio)
        painter.end()
        tmpCategory = self.category.split('.')
        tmp = str(os.path.join(QDir.currentPath(), '../DocHtml', 'Nodes_documentation', tmpCategory[0], 'images', self.name + ".png"))
        image.save(tmp)

    def foncedBlock(self, fcd):
        if fcd:
            self.setOpacity(0.4)
        else:
            self.setOpacity(1.0)

#     def hoverEnterEvent(self, event):
#         self.setSelected(True)
#         return QGraphicsRectItem.hoverEnterEvent(self, event)

#     def hoverLeaveEvent(self, event):
#         self.setSelected(False)
#         return QGraphicsRectItem.hoverLeaveEvent(self, event)

    def mouseMoveEvent(self, mouseEvent):
        mouseEvent.accept()
        editor.loopMouseMoveEvent(self, mouseEvent.scenePos())
        return QGraphicsRectItem.mouseMoveEvent(self, mouseEvent)

    def mouseReleaseEvent(self, event):
        editor.loopMouseReleaseEvent(self)
        return QGraphicsRectItem.mouseReleaseEvent(self, event)

    def mousePressEvent(self, event):

        if event.button() == 2:
            editor.diagramScene[editor.currentTab].clearSelection()
            self.setSelected(True)

        if event.button() == 1 and self.isMod:
            if not self.isSelected():
                editor.diagramScene[editor.currentTab].clearSelection()
                self.setSelected(True)

            try:
                if self.polUp.answer:
                    self.addinput()
                if self.polDown.answer:
                    self.subinput()
                    self.polUp.answer = False
                    self.polDown.answer = False
            except Exception as e:
                pass

            if 'U' in self.unit:
                ind = 0
                for i, j in enumerate(editor.getlib()):
                    if j[0] == self.name:
                        ind = i
                        break
                b1 = BlockCreate(self.name, '', editor.getlib()[ind][1], 150, 80, editor.getlib()[ind][2][1], False, editor.getlib()[ind][2])
                b1.preview = True
                textSource = 'Source : ' + editor.getlib()[ind][1]
                TreeLibrary().showModel(b1, textSource)
            else:
                ind = 0
                for i, j in enumerate(libSubMod):
                    if j[0] == self.name:
                        indMod = i
                        break
                bm = BlockCreate(self.name, '', None, 150, 80, libSubMod[indMod][1][0][1], False, libSubMod[indMod][1][0])
                TreeLibrary().showModel(bm, '')

        event.accept()
#         if event.button() == 1 and event.modifiers() == Qt.ControlModifier:
#             editor.blockSelection(self)
#         return QGraphicsRectItem.mousePressEvent(self, event)

    def mouseDoubleClickEvent(self, event):
        if self.isMod:
            if self.category:
                self.editParametersProcess()
            else:
                self.editParametersSubProcess()

    def keyPressEvent(self, event):
        global itemStored
        if event.key() == QtCore.Qt.Key_Delete:
            self.deleteBlocks()
        elif event.key() == QtCore.Qt.Key_Up:
            self.setPos(self.x(), self.y() - 1)
        elif event.key() == QtCore.Qt.Key_Down:
            self.setPos(self.x(), self.y() + 1)
        elif event.key() == QtCore.Qt.Key_Left:
            self.setPos(self.x() - 1, self.y())
        elif event.key() == QtCore.Qt.Key_Right:
            self.setPos(self.x() + 1, self.y())
        elif QKeySequence(event.key() + int(event.modifiers())) == QKeySequence("Ctrl+C"):
            itemStored = self
        elif event.key() == QtCore.Qt.Key_Plus and '_dyn' in self.name:
            self.addinput()
        elif event.key() == QtCore.Qt.Key_Minus and '_dyn' in self.name:
            self.subinput()
        elif QKeySequence(event.key() + int(event.modifiers())) == QKeySequence("Ctrl+U"):
            if self.link:
                webbrowser.open(self.link)

    def showToolTip(self, classUnit, position):
        self.link = ''
        path_blockdoc = os.path.dirname(os.path.realpath(__file__))
        docYml = os.path.join(path_blockdoc, '../blocsdoc', "BlocsDoc.yml")
        if os.path.exists(docYml):
            with open(docYml, 'r') as stream:
                dicts = yaml.load(stream, yaml.FullLoader)
                if classUnit in dicts.keys():
                    txtFunctionalité = dicts[classUnit]['functionality']
                    if 'http://' in txtFunctionalité or 'https://' in txtFunctionalité:
                        self.link = txtFunctionalité
                    txt = "<p style=\"background-color: #ffffff;\">"
                    txt += "<span style=\" \
                            font-size:12pt; \
                            font-weight:1000; \
                            color:#000000; \" >" + classUnit + " : <br><br></span>"
                    txt += " <img src='" + os.path.join(path_blockdoc,
                                                       '../blocsdoc',
                                                       classUnit+'.png') + \
                           "'><br>"
                    txt += "<span style=\" \
                            font-size:10pt; \
                            font-weight:600; \
                            color:#3060FF;\" >" + txtFunctionalité + "<br>"
                    if self.link:
                        txt += "<span style=\" \
                                font-size:10pt; \
                                font-weight:1000; \
                                color:#000000; \" > (type Ctrl+U to go to this link)<br>"
                    txt += "<br></span>"
                    for ks, vl in dicts[classUnit].items():
                        if ks not in ['functionality', 'dependencies']:
                            txt += "<span style=\" \
                                    font-size:10pt; \
                                    font-weight:800; \
                                    color:#000000;\" >" + ks + ": </span> \
                                    <span style=\" \
                                    font-size:9pt; \
                                    font-weight:600; \
                                    color:#00AA50;\" >" + vl + "<br></span>"
                    try:
                        txt += "<br><span style=\" \
                                font-size:10pt; \
                                font-weight:800; \
                                color:#000000;\" >Dependencies: \
                                <span style=\" \
                                font-size:9pt; \
                                font-weight:600; \
                                color:#AA1100;\" >" + dicts[classUnit]['dependencies'] + "<br></span>"
                    except Exception as e:
                        pass
                    txt += "</p>"
                    self.setToolTip(txt)

    def inputOptions(self):
        cat = self.category.split('.')
        pathYml = os.path.dirname(os.path.realpath(__file__))
        pathYml = os.path.join(pathYml, '../modules', cat[0], cat[1] + ".yml")

        if os.path.exists(pathYml):
            lvl = listBlocks.copy()[editor.currentTab][self.unit]
            
            try:
                c = chOptions(pathYml, self.name, lvl[2])
                c.exec_()
                if c.getAnswer() == "cancel":
                    return
                asq = (c.getNewValues()[0],)
                self.updateBlock(asq)

            except OSError as err:
                greenText = "<span style=\" font-size:10pt; font-weight:600; color:#ff0000;\" >"
                greenText = greenText + (' No options available ')
                greenText = greenText + ("</span>")
                textEdit.append(greenText)
        else:
            greenText = "<span style=\" font-size:10pt; font-weight:600; color:#ff0000;\" >"
            greenText = greenText + (' No options available ')
            greenText = greenText + ("</span>")
            textEdit.append(greenText)

    def addinput(self):
        ind = 0
        for i, j in enumerate(editor.getlib()):
            if j[0] == self.name:
                ind = i
                break
        tmpnameEnters = []
        tmpvalEnters = []
        tmpnameEnters = listBlocks[editor.currentTab][self.unit][2][0].copy()
        tmpvalEnters = listBlocks[editor.currentTab][self.unit][2][1].copy()
        tmplastEnter = tmpnameEnters[-1]
        tmplastVal = editor.getlib()[ind][2][1][-1]

        try:
            sg = [int(s) for s in tmplastEnter.split('_') if s.isdigit()]
            newb = str(int(sg[-1]) + 1)
            tmplastEnter = tmplastEnter.replace(str(sg[-1]), newb)
        except Exception as e:
            tmplastEnter += '_0'
        tmpnameEnters.append(tmplastEnter)
        tmpvalEnters.append(tmplastVal)
        ase = ((tmpnameEnters, tmpvalEnters, listBlocks[editor.currentTab][self.unit][2][2],
                listBlocks[editor.currentTab][self.unit][2][3]),)

        self.updateBlock(ase)

    def subinput(self):
        ind = 0
        for i, j in enumerate(editor.getlib()):
            if j[0] == self.name:
                ind = i
                break
        tmpnameEnters = []
        tmpvalEnters = []
        tmpnameEnters = listBlocks[editor.currentTab][self.unit][2][0].copy()
        tmpvalEnters = listBlocks[editor.currentTab][self.unit][2][1].copy()
        tmplastEnter = tmpnameEnters[-1]
        tmplastVal = tmpvalEnters[-1]

        tmpListLink = []
        for key, val in listNodes[editor.currentTab].items():
            tmpListLink.append(val[val.index('#Node#') + 6:len(val)])

        if len(tmpnameEnters) > len(editor.getlib()[ind][2][0]):
            if tmpListLink:
                if self.unit + ':' + tmplastEnter in tmpListLink:
                    return
            del tmpnameEnters[-1]
            del tmpvalEnters[-1]
            ase = ((tmpnameEnters, tmpvalEnters, listBlocks[editor.currentTab][self.unit][2][2],
                    listBlocks[editor.currentTab][self.unit][2][3]),)
            self.updateBlock(ase)

    def updateBlock(self, newListVal):
        try:
            diagram = undoredoTyping[editor.currentTab][len(undoredoTyping[editor.currentTab]) - 1]
        except Exception as e:
            diagram = undoredoTyping[editor.currentTab][0]

        unddiagram = diagram[diagram.index("block=[" + self.unit + "]"):]

        try:
            unddiagram = unddiagram[0:unddiagram.index("\n") + 1]
        except Exception as e:
            pass

        diagram = diagram.replace(unddiagram, "")

        for item in editor.diagramScene[editor.currentTab].items():
            editor.diagramScene[editor.currentTab].removeItem(item)
        block = ProcessItem(self.unit, self.name, self.category, 150, 80, *newListVal).getBlocks()
        block.setPos(self.pos())

        coord = block.sceneBoundingRect()
        rect = block.rect()
        diagram += '\nblock=[' + self.unit + \
                   '] category=[' + self.category + \
                   '] class=[' + self.name + \
                   '] valInputs=[' + str(listBlocks[editor.currentTab][self.unit][2]) + \
                   '] RectF=[' + str((coord.x(), coord.y(), rect.width(), rect.height())) + \
                   ']'
        LoadDiagram(diagram.splitlines())
        UpdateList(diagram)
        undoredoTyping[editor.currentTab][len(undoredoTyping[editor.currentTab])] = diagram

    def deleteBlocks(self):
        for elem in editor.diagramView[editor.currentTab].items():
            if type(elem) == LinkItem:
                if listNodes[editor.currentTab][elem.name].find(self.unit + ':') != -1:
                    self.deletelink(elem, self.unit)
        editor.diagramScene[editor.currentTab].removeItem(self)
        del listItems[editor.currentTab][self.unit]
        if self.category:
            del listBlocks[editor.currentTab][self.unit]
            listBlocks[editor.currentTab] = ReorderList(listBlocks[editor.currentTab]).getNewList()
        else:
            del listSubMod[editor.currentTab][self.unit]
            listSubMod[editor.currentTab] = ReorderList(listSubMod[editor.currentTab]).getNewList()
        editor.deleteItemsLoop(self)
        listNodes[editor.currentTab] = ReorderList(listNodes[editor.currentTab]).getNewList()
        UpdateUndoRedo()

    def deletelink(self, linkEle, unt):
        nameItem = listNodes[editor.currentTab][linkEle.name]
        nameItemTmp0 = nameItem[0:nameItem.index('#Node#')]
        unitTmp0 = nameItemTmp0[0:nameItemTmp0.index(':')]
        nameItemTmp0 = nameItemTmp0[nameItemTmp0.index(':') + 1:len(nameItemTmp0)]
        if 'C' in unitTmp0:
            for elem in editor.diagramView[editor.currentTab].items():
                if type(elem) == Port:
                    if elem.unit == unitTmp0:
                        other = False
                        for lstNode in listNodes[editor.currentTab]:
                            if not lstNode == linkEle.name:
                                tmpq = listNodes[editor.currentTab][lstNode]
                                tmpq = tmpq[0:tmpq.index(':')]
                                if tmpq == unitTmp0:
                                    other = True
                                    break
                        if not other:
                            elem.setBrush(QBrush(TypeColor.unkn.value))
                            elem.label.setPlainText('unkn')
                            elem.format = 'unkn'
                            elem.name = 'unkn'
                            elem.label.setPos(elem.pos().x() - 160 - elem.label.boundingRect().size().width(), elem.label.pos().y())
                            tmp = listConnects[editor.currentTab][elem.unit]
                            del listConnects[editor.currentTab][elem.unit]
                            if 'in' in tmp[0]:
                                listConnects[editor.currentTab][elem.unit] = (tmp[0], 'unkn', 'unkn', '')

        nameItem = listNodes[editor.currentTab][linkEle.name]
        nameItemTmp = nameItem[0:nameItem.index('#Node#')]
        unitTmp = nameItemTmp[0:nameItemTmp.index(':')]
        if unitTmp == unt:
            nameItemTmp = nameItem[nameItem.index('#Node#') + 6:len(nameItem)]
            unitTmp = nameItemTmp[0:nameItemTmp.index(':')]
            nameItemTmp = nameItemTmp[nameItemTmp.index(':') + 1:len(nameItemTmp)]
            if 'C' in unitTmp:
                for elem in editor.diagramView[editor.currentTab].items():
                    if type(elem) == Port:
                        if elem.unit == unitTmp:
                            elem.setBrush(QBrush(TypeColor.unkn.value))
                            elem.label.setPlainText('unkn')
                            elem.format = 'unkn'
                            elem.name = 'unkn'
                            tmp = listConnects[editor.currentTab][elem.unit]
                            del listConnects[editor.currentTab][elem.unit]
                            listConnects[editor.currentTab][elem.unit] = (tmp[0], 'unkn', 'unkn')
            if 'P' in unitTmp:
                for elem in editor.diagramView[editor.currentTab].items():
                    if type(elem) == Port:
                        if elem.unit == unitTmp:
                            elem.setBrush(QBrush(TypeColor.unkn.value))
                            elem.format = 'unkn'
                            tmp = listProbes[editor.currentTab][elem.unit]
                            del listProbes[editor.currentTab][elem.unit]
                            listProbes[editor.currentTab][elem.unit] = ('unkn', tmp[1])
            if 'U' in unitTmp:
                listVal = listBlocks[editor.currentTab][unitTmp]
                mod = listVal[0]
                ###############################################################################
                for i, j in enumerate(editor.getlib()):
                    if j[0] == mod:
                        indMod = i
                        break
                ###############################################################################
                category = listVal[1]
                cat = category.split('.')
                listEnter = editor.getlib()[indMod][2][0]
                listValDefault = editor.getlib()[indMod][2][1]
                if len(listEnter) != len(listVal[2][1]):
                    if '_dyn' in mod:
                        listEnter = listVal[2][0]
                        tmplistVal = listVal[2][1]
                        tmpList = []
                        for indDef in listValDefault:
                            tmpList.append(indDef)
                        for i in range(len(listValDefault), len(tmplistVal)):
                            tmpList.append(tmpList[-1])
                        listValDefault = tmpList
                    else:
                        pathYml = os.path.dirname(os.path.realpath(__file__))
                        pathYml = os.path.join(pathYml, '../modules', cat[0], cat[1] + ".yml")
                        if os.path.exists(pathYml):
                            with open(pathYml, 'r') as stream:
                                self.dicts = yaml.load(stream, yaml.FullLoader)
                                for el in self.dicts[mod]:
                                    if el in listVal[2][0]:
                                        listEnter = (*listEnter, el)
                                        if type(self.dicts[mod][el]).__name__ == 'str':
                                            if 'enumerate' in self.dicts[mod][el]:
                                                listValDefault = (*listValDefault, self.dicts[mod][el])
                                            else:
                                                try:
                                                    listValDefault = (*listValDefault, eval(self.dicts[mod][el]))
                                                except Exception as e:
                                                    listValDefault = (*listValDefault, self.dicts[mod][el])
                                        else:
                                            try:
                                                listValDefault = (*listValDefault, eval(self.dicts[mod][el]))
                                            except Exception as e:
                                                listValDefault = (*listValDefault, self.dicts[mod][el])
                ###############################################################################
                newList = []
                for i in range(len(listEnter)):
                    if listEnter[i] == nameItemTmp:
                        newValfromModules = listValDefault[i]

                        if type(newValfromModules).__name__ == 'str':
                            if 'enumerate' in newValfromModules:
                                newValfromModules = list(eval(newValfromModules))[0][1]
                        newList.append(newValfromModules)
                    else:
                        newList.append(listVal[2][1][i])
                ###############################################################################

                del listBlocks[editor.currentTab][unitTmp]
                listBlocks[editor.currentTab][unitTmp] = (listVal[0], listVal[1], (listVal[2][0], newList, listVal[2][2], listVal[2][3]))

            elif 'M' in unitTmp:
                listVal = listSubMod[editor.currentTab][unitTmp]
                mod = listVal[0]

                for i, j in enumerate(libSubMod):
                    if j[0] == mod:
                        indMod = i
                        break
                ind = listVal[1][0].index(nameItemTmp)
                newValfromModules = libSubMod[indMod][1][0][1][ind]

                if type(newValfromModules).__name__ == 'str':
                    if 'enumerate' in newValfromModules:
                        newValfromModules = list(eval(newValfromModules))[0][1]

                newList = []
                for i in range(len(listVal[1][1])):
                    if i == ind:
                        newList.append(newValfromModules)
                    else:
                        newList.append(listVal[1][1][i])

                del listSubMod[editor.currentTab][unitTmp]
                listSubMod[editor.currentTab][unitTmp] = (listVal[0], (listVal[1][0], newList, listVal[1][2], listVal[1][3]))

        editor.diagramScene[editor.currentTab].removeItem(linkEle)
        editor.diagramScene[editor.currentTab].removeItem(linkEle.getlinkTxt())
        editor.diagramScene[editor.currentTab].removeItem(linkEle.getlinkShow())
        editor.diagramScene[editor.currentTab].removeItem(linkEle.getBislink())
        del listNodes[editor.currentTab][linkEle.name]

    def seeSubMod(self):
        editor.addTab(self.name + '.mod')
        path_submod = os.path.dirname(os.path.realpath(__file__))
        file = os.path.join(path_submod, '../submodules', self.name + '.mod')
        editor.pathDiagram[editor.currentTab] = file
        textInf.setText(file)
        f = open(file, 'r')
        txt = f.readlines()
        f.close()
        LoadDiagram(txt)
        editor.diagramView[editor.currentTab].fitInView(editor.diagramScene[editor.currentTab].sceneRect(), QtCore.Qt.KeepAspectRatio)


class Probes(QGraphicsPolygonItem):
    def __init__(self, unit='', format='unkn', label='', isMod=True, parent=None):
        super(Probes, self).__init__(parent)

        self.label = label
        self.isMod = isMod
        self.preview = False
        self.caseFinal = False
        self.currentLoop = None
        self.moved = False

        if isMod:
            self.setAcceptHoverEvents(True)
            self.setFlags(self.ItemIsSelectable | self.ItemIsMovable | self.ItemIsFocusable)

        if unit == 'new':
            ProbeExist = True
            inc = 0
            while ProbeExist:
                if 'P' + str(inc) in listProbes[editor.currentTab]:
                    inc += 1
                else:
                    ProbeExist = False
            self.unit = 'P' + str(inc)
        else:
            self.unit = unit

        polyhead = QPolygonF([QPointF(0, 8), QPointF(20, 0), QPointF(70, 0),
                              QPointF(70, 26), QPointF(20, 26), QPointF(0, 18)])
        self.setPolygon(polyhead)

        self.setPen(QtGui.QPen(ItemColor.frame_probe.value, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.darkGray))

        lab = QGraphicsTextItem(self.unit, self)
        lab.setDefaultTextColor(QtGui.QColor(255, 255, 255, 255))
        lab.setPos(75, 0)

        self.inputs = []
        input = Port(label, 'in', format, self.unit, True, isMod, 10, -15, self)
        input.setPos(0, 13)
        self.inputs.append(input)

        if isMod:
            listProbes[editor.currentTab][self.unit] = (format, label)

    def contextMenuEvent(self, event):
        if not self.isSelected():
            return
        if self.isMod:
            menu = QMenu()
            de = menu.addAction('Delete')
            de.triggered.connect(self.deleteProbe)
            menu.exec_(event.screenPos())

    def mouseMoveEvent(self, mouseEvent):
        mouseEvent.accept()
        editor.loopMouseMoveEvent(self, mouseEvent.scenePos())
        return QGraphicsRectItem.mouseMoveEvent(self, mouseEvent)

    def mouseReleaseEvent(self, event):
        editor.loopMouseReleaseEvent(self)
        return QGraphicsRectItem.mouseReleaseEvent(self, event)

    def keyPressEvent(self, event):
        global itemStored
        if event.key() == QtCore.Qt.Key_Delete:
            self.deleteProbe()
        if event.key() == QtCore.Qt.Key_Up:
            self.setPos(self.x(), self.y() - 1)
        if event.key() == QtCore.Qt.Key_Down:
            self.setPos(self.x(), self.y() + 1)
        if event.key() == QtCore.Qt.Key_Left:
            self.setPos(self.x() - 1, self.y())
        if event.key() == QtCore.Qt.Key_Right:
            self.setPos(self.x() + 1, self.y())
        if QKeySequence(event.key() + int(event.modifiers())) == QKeySequence("Ctrl+C"):
            itemStored = self

    def deleteProbe(self):
        for elem in editor.diagramView[editor.currentTab].items():
            if type(elem) == LinkItem:
                if listNodes[editor.currentTab][elem.name].find(self.unit + ':') != -1:
                    BlockCreate.deletelink(self, elem, self.unit)
        editor.diagramScene[editor.currentTab].removeItem(self)
        del listProbes[editor.currentTab][self.unit]
        editor.deleteItemsLoop(self)
        UpdateUndoRedo()

    def hoverLeaveEvent(self, event):
        self.setSelected(0)


class ConnectorItem(QGraphicsPolygonItem):

    def __init__(self, name, connct='', w=70, h=26, inout='in', format='unkn', Vinput='', parent=None):
        super(ConnectorItem, self).__init__(parent)

        self.name = name
        self.inout = inout
        self.w = 70
        self.h = 26
        self.format = format
        self.moved = False
        self.setAcceptHoverEvents(True)

        if connct == '':
            ConnExist = True
            inc = 0
            while ConnExist:
                if 'C' + str(inc) in listConnects[editor.currentTab]:
                    inc += 1
                else:
                    ConnExist = False
            self.connct = 'C' + str(inc)

        else:
            self.connct = connct

        if 'in' in inout:
            listConnects[editor.currentTab][self.connct] = (self.inout, self.name, self.format, Vinput)
            polyhead = QPolygonF([QPointF(0, 0), QPointF(50, 0), QPointF(70, 8),
                                  QPointF(70, 18), QPointF(50, 26), QPointF(0, 26)])
        else:
            listConnects[editor.currentTab][self.connct] = (self.inout, self.name, self.format)
            polyhead = QPolygonF([QPointF(0, 8), QPointF(20, 0), QPointF(70, 0),
                                  QPointF(70, 26), QPointF(20, 26), QPointF(0, 18)])

        self.editConnect()
        self.setPolygon(polyhead)

    def editConnect(self):
        self.setPen(QtGui.QPen(ItemColor.frame_connect.value, 2))
        self.setBrush(QtGui.QBrush(QtCore.Qt.darkGray))
        self.setFlags(self.ItemIsSelectable | self.ItemIsMovable)
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # Label:
        self.label = QGraphicsTextItem('Conn.', self)
        self.label.setDefaultTextColor(QtGui.QColor(255, 255, 255, 255))
        rect = self.label.boundingRect()
        lw, lh = rect.width(), rect.height()
        lx1 = lw
        ly1 = (-25)

        self.nameConnect = QGraphicsTextItem(self.connct, self)
        self.nameConnect.setDefaultTextColor(QtGui.QColor(255, 255, 255, 255))
        rect = self.nameConnect.boundingRect()
        lw, lh = rect.width(), rect.height()
        lx2 = lw
        ly2 = 0

        self.setFlag(self.ItemIsFocusable, True)

        # Inputs and outputs of the block:
        if 'in' in self.inout:
            self.input = None
            self.output = Port(self.name, 'out', self.format, self.connct, True, True, 80, -12, self)
            self.output.setPos(self.w + 2, 1 + self.h / 2)
            lx1 = 2
            lx2 = 4

        else:
            self.output = None
            self.input = Port(self.name, 'in', self.format, self.connct, True, True, 80, -12, self)
            self.input.setPos(0, 1 + self.h / 2)
            lx1 = self.w - lx1
            lx2 = (self.w - lx2 - 4)

        self.label.setPos(lx1, ly1)
        self.nameConnect.setPos(lx2, ly2)

    def mouseDoubleClickEvent(self, event):
        if self.inout in 'in':
            if self.output.label.toPlainText() not in 'unkn':
                self.changelabel()
        if self.inout in 'out':
            if self.input.label.toPlainText() not in 'unkn':
                self.changelabel()
        return QGraphicsRectItem.mouseDoubleClickEvent(self, event)

    def mouseMoveEvent(self, event):
        self.moved = True
        event.accept()
        return QGraphicsRectItem.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        if self.moved:
            UpdateUndoRedo()
            self.moved = False
        return QGraphicsRectItem.mouseReleaseEvent(self, event)

    def keyPressEvent(self, event):
        global itemStored
        if event.key() == QtCore.Qt.Key_Delete:
            self.deleteConnct()
        if event.key() == QtCore.Qt.Key_Up:
            self.setPos(self.x(), self.y() - 1)
        if event.key() == QtCore.Qt.Key_Down:
            self.setPos(self.x(), self.y() + 1)
        if event.key() == QtCore.Qt.Key_Left:
            self.setPos(self.x() - 1, self.y())
        if event.key() == QtCore.Qt.Key_Right:
            self.setPos(self.x() + 1, self.y())
        if QKeySequence(event.key() + int(event.modifiers())) == QKeySequence("Ctrl+C"):
            itemStored = self

    def contextMenuEvent(self, event):
        if not self.isSelected():
            return
        menu = QMenu()
        de = menu.addAction('Delete')
        de.triggered.connect(self.deleteConnct)
        pa = menu.addAction('Change label')
        if self.inout in 'in':
            if self.output.label.toPlainText() == 'unkn':
                pa.setEnabled(False)
        if self.inout in 'out':
            if self.input.label.toPlainText() == 'unkn':
                pa.setEnabled(False)
        pa.triggered.connect(self.changelabel)
        menu.exec_(event.screenPos())

    def changelabel(self):
        oldVal = listConnects[editor.currentTab][self.connct][1]
        c = changeLabel('Conn', self.connct, oldVal)
        c.exec_()
        listVal = listConnects[editor.currentTab][self.connct]
        try:
            del listConnects[editor.currentTab][self.connct]
            if self.inout in 'in':
                listConnects[editor.currentTab][self.connct] = (listVal[0], c.getNewLabel(), listVal[2], listVal[3])
                self.output.label.setPlainText(c.getNewLabel())
                for ln in listNodes[editor.currentTab]:
                    tmp = listNodes[editor.currentTab][ln]
                    tmp2 = tmp[0:tmp.index(':')]
                    if self.connct == tmp2:
                        tmp = (self.connct + ':' + c.getNewLabel()) + tmp[tmp.index("#Node#"):]
                        del listNodes[editor.currentTab][ln]
                        listNodes[editor.currentTab][ln] = tmp
#                         break
            else:
                listConnects[editor.currentTab][self.connct] = (listVal[0], c.getNewLabel(), listVal[2])
                self.input.label.setPlainText(c.getNewLabel())
                for ln in listNodes[editor.currentTab]:
                    tmp = listNodes[editor.currentTab][ln]
                    tmp2 = tmp[tmp.index('#Node#') + 6:]
                    tmp2 = tmp2[0:tmp2.index(':')]
                    if self.connct == tmp2:
                        tmp = tmp[0:tmp.index('#Node#') + 6] + (self.connct + ':' + c.getNewLabel())
                        del listNodes[editor.currentTab][ln]
                        listNodes[editor.currentTab][ln] = tmp
        except OSError as err:
            print('error change label : ', str(err))
            listConnects[editor.currentTab][self.connct] = listVal

    def deleteConnct(self):
        for elem in editor.diagramView[editor.currentTab].items():
            if type(elem) == LinkItem:
                if listNodes[editor.currentTab][elem.name].find(self.connct + ':') != -1:
                    BlockCreate.deletelink(self, elem, self.connct)
        editor.diagramScene[editor.currentTab].removeItem(self)
        del listConnects[editor.currentTab][self.connct]
        listConnects[editor.currentTab] = ReorderList(listConnects[editor.currentTab]).getNewList()
        UpdateUndoRedo()

    def hoverEnterEvent(self, event):
        self.setSelected(1)

    def hoverLeaveEvent(self, event):
        self.setSelected(0)


class CommentsItem(QGraphicsRectItem):

    def __init__(self, w, h, text, isMod, parent=None):
        super(CommentsItem, self).__init__(None)

        self.wmin = 10.0
        self.hmin = 10.0
        self.isMod = isMod
        self.inputs = []
        self.outputs = []
        self.setPen(QtGui.QPen(ItemColor.background_comment.value, 5))
        self.setBrush(QtGui.QBrush(ItemColor.frame_comment.value))
        self.setZValue(-2)
        self.setOpacity(0.6)
        self.label = LabelGroup(self)
        self.label.setPlainText(text)
        x, y = self.newSize(w, h)

        if self.isMod:
            self.setFlags(self.ItemIsSelectable | self.ItemIsMovable | self.ItemIsFocusable)
            self.label.setFlags(self.ItemIsFocusable | self.ItemIsMovable)
            self.resize = Wrist(self)
            self.resize.setPos(x, y)
            self.resize.posChangeCallbacks.append(self.newSize)  # Connect the callback
            self.resize.setFlag(self.resize.ItemIsSelectable, True)
            self.resize.wmin = self.wmin
            self.resize.hmin = self.hmin

    def newSize(self, w, h):
        # Limit the block size:
        if h < self.hmin:
            h = self.hmin
            w = self.wmin

        self.setRect(0.0, 0.0, w, h)
        # center label:
        rect = self.label.boundingRect()
        self.label.setPos(0, self.boundingRect().y() - rect.height())

        return w, h

    def keyPressEvent(self, event):
        global itemStored
        if event.key() == QtCore.Qt.Key_Delete:
            editor.diagramScene[editor.currentTab].removeItem(self)
            UpdateUndoRedo()
        if event.key() == QtCore.Qt.Key_Up:
            self.setPos(self.x(), self.y() - 1)
        if event.key() == QtCore.Qt.Key_Down:
            self.setPos(self.x(), self.y() + 1)
        if event.key() == QtCore.Qt.Key_Left:
            self.setPos(self.x() - 1, self.y())
        if event.key() == QtCore.Qt.Key_Right:
            self.setPos(self.x() + 1, self.y())
        if QKeySequence(event.key() + int(event.modifiers())) == QKeySequence("Ctrl+C"):
            itemStored = self


class LabelGroup(QGraphicsTextItem):

    def __init__(self, parent=None):
        super(LabelGroup, self).__init__(parent)

        self.setDefaultTextColor(ItemColor.text_comment.value)
        self.setFont(QFont("Times", 20, QFont.Bold))
        self.setZValue(0)

    def mouseDoubleClickEvent(self, event):
        self.changeComment()
        UpdateUndoRedo()

    def mousePressEvent(self, event):
        if event.button() == 1:
            editor.diagramScene[editor.currentTab].clearSelection()
            self.setSelected(True)
            event.accept()
            return QGraphicsTextItem.mousePressEvent(self, event)

    class _CommentEdit(QDialog):

        def __init__(self, parent=None):
            super(LabelGroup._CommentEdit, self).__init__(parent)
            layout = QVBoxLayout(self)
            hlay1 = QHBoxLayout()
            layout.addLayout(hlay1)
            hlay1.addWidget(QLabel('Comment:'))
            self.name_line = QTextEdit()
            hlay1.addWidget(self.name_line)
            hlay2 = QHBoxLayout()
            layout.addLayout(hlay2)
            ok = QPushButton('OK')
            hlay2.addWidget(ok)
            cancel = QPushButton('Cancel')
            hlay2.addWidget(cancel)
            ok.clicked.connect(self.accept)
            cancel.clicked.connect(self.reject)

    def changeComment(self):
        dial = self._CommentEdit()
        dial.name_line.setText(self.toPlainText())

        res = dial.exec_()
        if res:
            self.setPlainText(str(dial.name_line.toPlainText()))
            self.setPos(self.boundingRect().x(), self.boundingRect().y() - self.boundingRect().height())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.setPos(self.x(), self.y() - 2)
        if event.key() == Qt.Key_Down:
            self.setPos(self.x(), self.y() + 2)
        if event.key() == Qt.Key_Left:
            self.setPos(self.x() - 2, self.y())
        if event.key() == Qt.Key_Right:
            self.setPos(self.x() + 2, self.y())

###############################################################################


class Constants(QGraphicsRectItem):

    def __init__(self, unit='', w=80, h=30, val='', form='', label='', isMod=True, parent=None):
        super(Constants, self).__init__(parent)
        self.isMod = isMod

        self.caseFinal = False
        self.currentLoop = None

        self.moved = False
        self.form = form
        self.val = val
        self.setZValue(2)
        self.preview = False

        if self.isMod:
            self.setFlags(self.ItemIsSelectable | self.ItemIsMovable)
            self.setFlag(self.ItemIsFocusable, True)
            self.setAcceptHoverEvents(True)

        if unit in 'newConstant':
            ConstantExist = True
            inc = 0
            while ConstantExist:
                if 'A' + str(inc) in listConstants[editor.currentTab]:
                    inc += 1
                else:
                    ConstantExist = False
            self.unit = 'A' + str(inc)
        else:
            self.unit = unit

        if label:
            self.label = label
        else:
            self.label = self.unit

        self.format = form

        if 'path' == form:
            self.elemProxy = Constants_text(self.unit, val, self.label)
            self.elemProxy.setStyleSheet("background-color: rgb(255, 100, 100);")
            self.elemProxy.textChanged.connect(self.changeText)
            color = TypeColor.path.value
        elif 'enumerate' in form:
            self.elemProxy = Constants_Combo(self.unit, form, val, self.label)
            self.elemProxy.setStyleSheet("background-color: rgb(100, 0, 150);selection-background-color: blue")
            self.format = 'str'
            color = TypeColor.str.value
        elif 'str' == form:
            self.elemProxy = Constants_text(self.unit, val, self.label)
            self.elemProxy.setStyleSheet("background-color: rgb(200, 0, 250);")
            self.elemProxy.textChanged.connect(self.changeText)
            color = TypeColor.str.value
        elif 'float' == form:
            self.elemProxy = Constants_float(self.unit, val, self.label)
            self.elemProxy.setStyleSheet("background-color: rgb(200, 100, 0);")
            color = TypeColor.float.value
        elif 'int' == form:
            self.elemProxy = Constants_int(self.unit, val, self.label)
            self.elemProxy.setStyleSheet("background-color: rgb(0, 100, 255);")
            color = TypeColor.int.value
        elif 'bool' == form:
            self.elemProxy = Constants_Combo(self.unit, "bool", str(val), self.label)
            self.elemProxy.setStyleSheet("background-color: rgb(50, 250, 50);selection-background-color: blue")
            color = TypeColor.bool.value

        self.proxyWidget = QGraphicsProxyWidget(self, Qt.Widget)
        self.proxyWidget.setWidget(self.elemProxy)
        self.proxyWidget.setPos(3, 3)
        self.proxyWidget.setZValue(3)

        self.w = self.proxyWidget.boundingRect().size().width() + 15
        self.h = self.proxyWidget.boundingRect().size().height() + 6

        self.nameUnit = QGraphicsTextItem(self.unit, self)
        self.nameUnit.setDefaultTextColor(QtGui.QColor(255, 255, 255, 255))
        self.nameUnit.setFont(QFont("Times", 12, QFont.Bold))
        self.nameUnit.setPos(0, 60)
        self.nameUnit.setVisible(False)

        self.lab = QGraphicsTextItem(self.label, self)
        self.lab.setDefaultTextColor(QtGui.QColor(255, 255, 255, 255))
        self.lab.setFont(QFont("Times", 12, QFont.Bold))
        self.lab.setPos(0, -30)
        self.lab.setVisible(True)

        self.wmin = self.w
        self.hmin = self.h
        self.setPen(QtGui.QPen(ItemColor.frame_constants.value, 3))
        self.setBrush(QtGui.QBrush(color))
        self.setRect(0.0, 0.0, self.w, self. h)
        self.inputs = []
        self.outputs = []
        self.outputs.append(Port('', 'out', self.format, self.unit, True, self.isMod, 80, -12, self))
        self.outputs[0].setPos(self.w + 2, self.h / 2)
        if self.isMod:
            listConstants[editor.currentTab][self.unit] = (self.form, val, self.label)
        else:
            self.elemProxy.setEnabled(False)
        if form == 'str' or form == 'path':
            self.changeText()

    def changeText(self):
        self.elemProxy.setCursorWidth(1)
        textEdit = self.elemProxy
        font = textEdit.document().defaultFont()
        fontMetrics = QFontMetrics(font)
        textSize = fontMetrics.size(0, textEdit.toPlainText())
        w = textSize.width() + 10
        h = textSize.height() + 10
        self.elemProxy.setMinimumSize(w, h)
        self.elemProxy.setMaximumSize(w, h)
        self.elemProxy.resize(w, h)
        self.setRect(0.0, 0.0, w + 15, h + 6)
        self.outputs[0].setPos(w + 15 + 2, (h + 6) / 2)

    def changeCombo(self):
        w = self.elemProxy.size().width()
        h = self.elemProxy.size().height()
#         self.elemProxy.resize(w, h)
        self.setRect(0.0, 0.0, w + 20, h + 6)
        self.outputs[0].setPos(w + 20 + 2, (h + 6) / 2)

    def foncedBlock(self, fcd):
        if fcd:
            self.setOpacity(0.4)
        else:
            self.setOpacity(1.0)

    def changeLabel(self):
        listLabCts = []
        for x, y in listConstants[editor.currentTab].items():
            listLabCts.append(y[2])
        listVal = listConstants[editor.currentTab][self.unit]
        oldVal = listVal[2]
        c = changeLabel('Const', self.unit, oldVal)
        c.exec_()
        try:
            self.label = c.getNewLabel()
            if self.label in listLabCts:
                self.label += '-b'
            self.lab.setPlainText(self.label)
            del listConstants[editor.currentTab][self.unit]
            listConstants[editor.currentTab][self.unit] = (listVal[0], listVal[1], self.label)
            UpdateUndoRedo()
        except OSError as err:
            print("OS error: {0}".format(err))

    def contextMenuEvent(self, event):
        if self.isMod:
            menu = QMenu()
            de = menu.addAction('Delete')
            de.triggered.connect(self.deleteConstant)
            pa = menu.addAction('Change label')
            pa.triggered.connect(self.changeLabel)
            menu.exec_(event.screenPos())
#             return QGraphicsRectItem.contextMenuEvent(self, event)

    def hoverEnterEvent(self, event):
        global itemStored
        itemStored = None
        self.setSelected(True)
#         return QGraphicsRectItem.hoverEnterEvent(self, event)

    def hoverLeaveEvent(self, event):
        self.setSelected(False)
#         return QGraphicsRectItem.hoverLeaveEvent(self, event)

    def mouseMoveEvent(self, event):
        event.accept()
        editor.loopMouseMoveEvent(self, event.scenePos())
        return QGraphicsRectItem.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        editor.loopMouseReleaseEvent(self)
        return QGraphicsRectItem.mouseReleaseEvent(self, event)

    def mousePressEvent(self, event):
        if event.button() == 2:
            self.setSelected(True)

        if event.button() == 1:
            editor.diagramScene[editor.currentTab].clearSelection()
            self.setSelected(True)

#         if event.button() == 1 and event.modifiers() == Qt.ControlModifier:
#             editor.blockSelection(self)

    def mouseDoubleClickEvent(self, event):
        global itemStored
        itemStored = None
        if self.isMod:
            if type(self.elemProxy) == Constants_Combo and self.form != 'bool':
                AllItems = [self.elemProxy.itemText(i) for i in range(self.elemProxy.count())]
                p = editCombobox(AllItems)
                p.exec_()
                if p.getAnswer() == 'ok':
                    newList = p.getNewList()
                    self.elemProxy.clear()
                    self.elemProxy.addItems(newList)
                    self.elemProxy.txt = "enumerate(" + str(tuple(newList)) + ")"
                    self.elemProxy.value = str(newList[0])
                    self.elemProxy.setSizeAdjustPolicy(QComboBox.AdjustToContents)
                    self.elemProxy.adjustSize()
                    self.form = "enumerate(" + str(tuple(newList)) + ")"
                    self.changeCombo()
                    del listConstants[editor.currentTab][self.unit]
                    listConstants[editor.currentTab][self.unit] = (self.elemProxy.txt, self.elemProxy.value, self.label)
            elif type(self.elemProxy) == Constants_text and self.form == 'path':
                currentpathTmp = self.elemProxy.toPlainText()
    #             currentpathTmp=currentpathwork
                fileCh = QFileDialog.getOpenFileName(None,
                                                     "Choose file",
                                                     currentpathTmp,
                                                     'All Files (*)',
                                                     None,
                                                     QFileDialog.DontUseNativeDialog)
                if fileCh[0]:
                    self.elemProxy.setPlainText(fileCh[0])
            UpdateUndoRedo()
#         return QGraphicsRectItem.mouseDoubleClickEvent(self,event)

    def keyPressEvent(self, event):
        global itemStored
        if event.key() == QtCore.Qt.Key_Delete:
            self.deleteConstant()
        if event.key() == QtCore.Qt.Key_Up:
            self.setPos(self.x(), self.y() - 1)
        if event.key() == QtCore.Qt.Key_Down:
            self.setPos(self.x(), self.y() + 1)
        if event.key() == QtCore.Qt.Key_Left:
            self.setPos(self.x() - 1, self.y())
        if event.key() == QtCore.Qt.Key_Right:
            self.setPos(self.x() + 1, self.y())
        if QKeySequence(event.key() + int(event.modifiers())) == QKeySequence("Ctrl+C"):
            itemStored = self
#         return QGraphicsRectItem.keyPressEvent(self, *args, **kwargs)

    def deleteConstant(self):
        for elem in editor.diagramView[editor.currentTab].items():
            if type(elem) == LinkItem:
                if listNodes[editor.currentTab][elem.name].find(self.unit + ':') != -1:
                    BlockCreate.deletelink(self, elem, self.unit)
        editor.diagramScene[editor.currentTab].removeItem(self)
        del listConstants[editor.currentTab][self.unit]
        del listItems[editor.currentTab][self.unit]
        editor.deleteItemsLoop(self)
        UpdateUndoRedo()

###############################################################################


class Constants_int(QSpinBox):

    def __init__(self, unit, val, lab, parent=None):
        super(Constants_int, self).__init__(parent)
#         self.setButtonSymbols(QSpinBox.NoButtons)
        self.setMaximum(100000)
        self.setMinimum(-100000)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setValue(val)
        self.unit = unit
        self.lab = lab

    def focusOutEvent(self, event):
        self.lineEdit().deselect()
        del listConstants[editor.currentTab][self.unit]
        listConstants[editor.currentTab][self.unit] = ('int', self.value(), self.lab)
        self.setReadOnly(True)

    def focusInEvent(self, event):
        self.setReadOnly(False)

###############################################################################


class Constants_float(QDoubleSpinBox):

    def __init__(self, unit, val, lab, parent=None):
        super(Constants_float, self).__init__(parent)
#         self.setButtonSymbols(QSpinBox.NoButtons)
        self.setRange(-100000, 100000)
        self.setDecimals(4)
        self.setValue(val)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.unit = unit
        self.lab = lab

    def focusOutEvent(self, event):
        self.lineEdit().deselect()
        del listConstants[editor.currentTab][self.unit]
        listConstants[editor.currentTab][self.unit] = ('float', self.value(), self.lab)
        self.setReadOnly(True)

    def focusInEvent(self, event):
        self.setReadOnly(False)

###############################################################################


class Constants_text(QTextEdit):

    def __init__(self, unit, txt, lab, parent=None):
        super(Constants_text, self).__init__(parent)
        self.setPlainText(txt)
        self.setMinimumSize(110, 25)
        self.setMaximumWidth(110)
        self.setMaximumHeight(25)
        self.setAutoFillBackground(False)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setCursorWidth(1)
        self.unit = unit
        self.lab = lab

    def focusInEvent(self, event):
        self.setCursorWidth(1)
#         event.accept()

    def focusOutEvent(self, event):
        self.setPlainText(self.toPlainText())
        self.setCursorWidth(0)
        tmpTxt = repr(self.toPlainText())
        tmpTxt = tmpTxt.replace('\\n', '')
        del listConstants[editor.currentTab][self.unit]
        listConstants[editor.currentTab][self.unit] = ('str', tmpTxt, self.lab)

###############################################################################


class Constants_Combo(QComboBox):

    def __init__(self, unit, txt, val, lab, parent=None):
        super(Constants_Combo, self).__init__(parent)
        self.txt = txt
        if txt == 'bool':
            txt = "enumerate(('True','False'))"
        self.addItems([x[1] for x in list(eval(txt))])
        self.setCurrentText(val)
        self.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.currentTextChanged.connect(self.newValue)
        self.unit = unit
        self.lab = lab

    def newValue(self):
        del listConstants[editor.currentTab][self.unit]
        listConstants[editor.currentTab][self.unit] = (self.txt, self.currentText(), self.lab)

###############################################################################


class ForLoopItem(QGraphicsRectItem):

    def __init__(self, unit, name, w, h, isMod, *inout, parent=None):
        super(ForLoopItem, self).__init__(None)
        self.normalState()
        self.setBrush((QtGui.QBrush(QColor(80, 80, 80, 200))))
        self.setZValue(-1)
        self.unit = unit
        self.w = w
        self.h = h
        self.wmin = 100.0
        self.hmin = 100.0
        self.nbin, self.nbout = 0, 0
        self.moved = False
        self.isMod = isMod
        self.preview = False
        self.loopIf = False
        self.name = name

        self.setAcceptHoverEvents(True)

        self.caseFinal = False
        self.currentLoop = None

        if unit in 'newForLoop':
            ForLoopExist = True
            inc = 0
            while ForLoopExist:
                if  'F' + str(inc) in listTools[editor.currentTab] or \
                    'F' + str(inc) + "m" in listTools[editor.currentTab] or \
                    'F' + str(inc) + "m*" in listTools[editor.currentTab]:
                    inc += 1
                else:
                    ForLoopExist = False
            self.unit = 'F' + str(inc)
            if name == 'For_multiprocessing':
                self.unit += 'm'

        elif unit in 'newIf':
            self.loopIf = True
            IfConditionExist = True
            inc = 0
            while IfConditionExist:
                if 'I' + str(inc) in listTools[editor.currentTab]:
                    inc += 1
                else:
                    IfConditionExist = False
            self.unit = 'I' + str(inc)

        else:
            if 'I' in unit:
                self.loopIf = True
            self.unit = unit

        self.inputs = []
        self.outputs = []
        if self.isMod:
            if self.loopIf:
                listTools[editor.currentTab][self.unit] = [[], []]
            else:
                listTools[editor.currentTab][self.unit] = []
            libTools[editor.currentTab][self.unit] = [[], []]

        if inout:
            libTools[editor.currentTab][self.unit] = inout
            for i in range(0, len(inout[0])):
                self.updateTunnelInput(inout[0][i])
            for i in range(0, len(inout[1])):
                self.updateTunnelOutput(inout[1][i])

        self.label = QGraphicsTextItem(name, self)
        self.label.setFont(QFont("Times", 16, QFont.Bold))
        self.label.setDefaultTextColor(QtGui.QColor(160, 160, 160, 255))

        self.nameUnit = QGraphicsTextItem(self.unit, self)
        self.nameUnit.setDefaultTextColor(QtGui.QColor(255, 255, 255, 255))

        x, y = self.newSize(self.w, self.h)

        if self.isMod:
            self.setFlags(self.ItemIsSelectable | self.ItemIsMovable | self.ItemIsFocusable)
            self.resize = Wrist(self)
            self.resize.setPos(x, y)
            self.resize.posChangeCallbacks.append(self.newSize)  # Connect the callback
            self.resize.setFlag(self.resize.ItemIsSelectable, True)
            self.resize.wmin = self.wmin
            self.resize.hmin = self.hmin

        if name == 'If':
            self.elemProxy = Control_IF(self.unit, "bool", 'True')
            self.elemProxy.setStyleSheet("background-color: rgb(50, 250, 50);selection-background-color: blue")
            self.proxyWidget = QGraphicsProxyWidget(self, Qt.Widget)
            self.proxyWidget.setWidget(self.elemProxy)
            self.proxyWidget.setPos(3, 3)
            self.proxyWidget.setZValue(3)
            portCondition = Port('val', 'in', 'bool', self.unit, False, True, -18, -25, self)
            self.inputs.append(portCondition)
            portCondition.setPos(0, 15)

#     def setDimension(self):
#         print(self.x(), self.y(), self.boundingRect().width(), self.boundingRect().height())
#         xmin, ymin = self.x(), self.y()
#         xmax, ymax = xmin + self.boundingRect().width(), ymin + self.boundingRect().height()
#         for its in listTools[editor.currentTab][self.unit]:
#             coord = listItems[editor.currentTab][its].sceneBoundingRect()
#             x, y, w, h = coord.x(), coord.y(), coord.width(), coord.height()
#             print('its : ', x, y, w, h)
#             if x < xmin : xmin = x
#             if y < ymin : ymin = y
#             if (x + w) > xmax : xmax = x + w
#             if (y + h) > ymax : ymax = y + h
#         self.wmin = xmax - xmin
#         self.hmin = ymax - ymin
#         self.setPos(xmin, ymin)
#         self.updateSize()
#         print('dimension loop : ', xmin, ymin, xmax, ymax)

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == QtCore.Qt.Key_Delete:
            self.deleteLoopFor()
            UpdateUndoRedo()
        if keyEvent.key() == QtCore.Qt.Key_Up:
            self.setPos(self.x(), self.y() - 1)
        if keyEvent.key() == QtCore.Qt.Key_Down:
            self.setPos(self.x(), self.y() + 1)
        if keyEvent.key() == QtCore.Qt.Key_Left:
            self.setPos(self.x() - 1, self.y())
        if keyEvent.key() == QtCore.Qt.Key_Right:
            self.setPos(self.x() + 1, self.y())
        return QGraphicsRectItem.keyPressEvent(self, keyEvent)

    def mousePressEvent(self, event):

        if self.isMod:
            if event.button() == 1:
                editor.diagramScene[editor.currentTab].clearSelection()
                self.setSelected(True)

            if event.button() == 2:
                self.setSelected(True)

            self.selectItemsInside(self.unit, True)
            UpdateUndoRedo()
#         return QGraphicsRectItem.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        pos = event.scenePos()
        if not self.preview:
            listTypeItems = []
            itms = editor.diagramScene[editor.currentTab].items(pos)

            for elem in itms:
                if type(elem) == ForLoopItem:
                    if elem.unit != self.unit:
                        listTypeItems.append(elem)

            if listTypeItems:
                if len(listTypeItems) > 1:
                    postmp = None
                    elemtmp = None
                    try:
                        self.currentLoop.normalState()
                    except Exception as e:
                        pass
                    for lsElem in listTypeItems:
                        if not postmp:
                            postmp = lsElem.pos()
                            elemtmp = lsElem
                        elif postmp.x() < lsElem.pos().x():
                            postmp = lsElem.pos()
                            elemtmp = lsElem

#                     self.currentLoop = elemtmp
#                     self.currentLoop.activeState()
#                     self.caseFinal = True
                else:
                    elemtmp = listTypeItems[0]
                    try:
                        ind = 0
                        if self.currentLoop.loopIf:
                            if self.currentLoop.elemProxy.currentText() == 'False':
                                ind = 1
                        self.currentLoop.normalState()
                        self.currentLoop.IteminLoop(self.unit, False, ind)
                        self.currentLoop = None
                        self.caseFinal = False
                    except Exception as e:
                        pass

                self.currentLoop = elemtmp
                self.currentLoop.activeState()
                self.caseFinal = True
            else:
                if self.currentLoop:
                    ind = 0
                    if self.currentLoop.loopIf:
                        if self.currentLoop.elemProxy.currentText() == 'False':
                            ind = 1
                    self.currentLoop.normalState()
                    self.currentLoop.IteminLoop(self.unit, False, ind)
                    self.currentLoop = None
                    self.caseFinal = False

            event.accept()
            self.moved = True

        return QGraphicsRectItem.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        if self.isMod:
            pos = event.scenePos()
            if self.currentLoop:
                ind = 0
                if self.currentLoop.loopIf:
                    if self.currentLoop.elemProxy.currentText() == 'False':
                        ind = 1
                self.currentLoop.IteminLoop(self.unit, True, ind)
                self.currentLoop.normalState()
                self.currentLoop = None
                self.caseFinal = False
            if self.moved:
                UpdateUndoRedo()
                self.moved = False

            self.selectItemsInside(self.unit, False)
            UpdateUndoRedo()

            return QGraphicsRectItem.mouseReleaseEvent(self, event)

    def selectItemsInside(self, unit, state):
        listToMove = []

        if 'I' in unit:
            listToMove.extend(listTools[editor.currentTab][unit][0])
            listToMove.extend(listTools[editor.currentTab][unit][1])

        else:
            listToMove.extend(listTools[editor.currentTab][unit])

        for elemts in self.scene().items():
            if (type(elemts) == BlockCreate
                or type(elemts) == ForLoopItem
                or type(elemts) == Constants
                or type(elemts) == ScriptItem
                or type(elemts) == Probes) \
                            and elemts.unit in listToMove:
                elemts.setSelected(state)
                if type(elemts) == ForLoopItem and elemts.unit != self.unit:
                    self.selectItemsInside(elemts.unit, state)

    def hoverEnterEvent(self, event):
        self.setSelected(True)
        return QGraphicsRectItem.hoverEnterEvent(self, event)

    def hoverLeaveEvent(self, event):
        self.setSelected(False)
        return QGraphicsRectItem.hoverLeaveEvent(self, event)

    def newSize(self, w, h):
        self.setRect(0.0, 0.0, w, h)
        self.label.setPos(0, -40)
        if self.nbin > 0:
            y = (h) / (self.nbin + 1)
            dy = (h) / (self.nbin + 1)
            for inp in range(len(self.inputs)):
                if 'in' in self.inputs[inp].name:
                    self.inputs[inp].setPos(-9, y)
                    self.outputs[inp].setPos(11, y)
                    y += dy
        if self.nbout > 0:
            y = (h) / (self.nbout + 1)
            dy = (h) / (self.nbout + 1)
            for inp in range(len(self.inputs)):
                if 'out' in self.inputs[inp].name:
                    self.inputs[inp].setPos(w - 9, y)
                    self.outputs[inp].setPos(w + 11, y)
                    y += dy
        rect = self.nameUnit.boundingRect()
        lw, lh = rect.width(), rect.height()
        lx = (w - lw) / 2
        ly = (h)
        self.nameUnit.setPos(lx, ly)
        self.w = w
        self.h = h
        return w, h

    def updateSize(self):

        factorh = 20
        hmin = factorh * len(self.inputs)

        if self.hmin < hmin:
            self.hmin = hmin
        w = self.w
        h = self.h

        if h < hmin:
            h = hmin
        hmin = factorh * len(self.outputs)
        if h < hmin:
            h = hmin
        if w < self.wmin:
            w = self.wmin
        x, y = self.newSize(w, h)
        return x, y

    def contextMenuEvent(self, event):
        if event.isAccepted:
            pass
        if self.isMod:
            menu = QMenu()
            intu = menu.addAction('Add tunnel input')
            intu.triggered.connect(self.addTunnelInput)
            outtu = menu.addAction('Add tunnel output')
            outtu.triggered.connect(self.addTunnelOutput)
            de = menu.addAction('Delete')
            de.triggered.connect(self.deleteLoopFor)
            if 'm' in self.unit:
                pa = menu.addAction('Parameters')
                pa.triggered.connect(self.editParameters)
                outtu.setEnabled(False)
            menu.exec_(event.screenPos())
#             return QGraphicsRectItem.contextMenuEvent(self, event)

    def deleteLoopFor(self):
        editor.diagramScene[editor.currentTab].removeItem(self)
        for elem in editor.diagramView[editor.currentTab].items():
            if type(elem) == LinkItem:
                if listNodes[editor.currentTab][elem.name].find(self.unit + ':') != -1:
                    BlockCreate.deletelink(self, elem, self.unit)
        del listTools[editor.currentTab][self.unit]
        del libTools[editor.currentTab][self.unit]
        del listItems[editor.currentTab][self.unit]

    def addTunnelInput(self):
        self.nbin += 1

        listNameTunnel = []
        for el in libTools[editor.currentTab][self.unit][0]:
            listNameTunnel.append(el[0][0])

        for inc in range(0, len(listNameTunnel) + 1):
            if 'in' + str(inc) not in listNameTunnel:
                name = 'in' + str(inc)
                break

        portIn = Port(name, 'in', 'unkn', self.unit, False, True, -18, -25, self)
        portOut = Port(name, 'out', 'unkn', self.unit, False, True, 4, -12, self)
        self.inputs.append(portIn)
        self.outputs.append(portOut)
        self.inputs.sort(key=lambda x: x.name)
        self.outputs.sort(key=lambda x: x.name)

        x, y = self.updateSize()
        self.resize.setPos(x, y)

        c = defineTunnels(name, self.name)
        c.exec_()

        if c.getNewValues():
            format = c.getNewValues()[0]
            typein = c.getNewValues()[1] + '_'
            typein = typein.replace('simple_', '')
            typeout = c.getNewValues()[2] + '_'
            typeout = typeout.replace('simple_', '')

            portIn.format = typein + format
            portOut.format = typeout + format

            for types in TypeColor:
                if types.name in format:
                    color = types.value

            portIn.setBrush(color)
            portOut.setBrush(color)

            listEnter = libTools[editor.currentTab][self.unit][0]
            listOut = libTools[editor.currentTab][self.unit][1]
            if listEnter:
                listEnter.append([[portIn.name, portIn.typeio, portIn.format], [portOut.name, portOut.typeio, portOut.format]])
            else:
                listEnter = [[[portIn.name, portIn.typeio, portIn.format], [portOut.name, portOut.typeio, portOut.format]]]

            libTools[editor.currentTab][self.unit] = [listEnter, listOut]
            UpdateUndoRedo()
        else:
            ct = editor.currentTab
            if pointTyping[ct] > 0:
                pointTyping[ct] -= 1
                for item in editor.diagramScene[ct].items():
                    editor.diagramScene[ct].removeItem(item)
                newDiagram = undoredoTyping[ct][pointTyping[ct]]
                LoadDiagram(newDiagram.splitlines())
                UpdateList(newDiagram)

    def addTunnelOutput(self):
        self.nbout += 1
        listNameTunnel = []
        for el in libTools[editor.currentTab][self.unit][1]:
            listNameTunnel.append(el[0][0])

        for inc in range(0, len(listNameTunnel) + 1):
            if 'out' + str(inc) not in listNameTunnel:
                name = 'out' + str(inc)
                break

        portOut = Port(name, 'out', 'unkn', self.unit, False, True, -24, -25, self)
        portIn = Port(name, 'in', 'unkn', self.unit, False, True, 4, -12, self)
        self.outputs.append(portOut)
        self.inputs.append(portIn)
#         self.scene().addItem(portOut)
#         self.scene().addItem(portIn)

        self.inputs.sort(key=lambda x: x.name)
        self.outputs.sort(key=lambda x: x.name)

        x, y = self.updateSize()
        self.resize.setPos(x, y)

        c = defineTunnels(name, self.name)
        c.exec_()

        if c.getNewValues():
            format = c.getNewValues()[0]
            typein = c.getNewValues()[1] + '_'
            typein = typein.replace('simple_', '')
            typeout = c.getNewValues()[2] + '_'
            typeout = typeout.replace('simple_', '')

            portIn.format = typein + format
            portOut.format = typeout + format

            for types in TypeColor:
                if types.name in format:
                    color = types.value

            portIn.setBrush(color)
            portOut.setBrush(color)

            listEnter = libTools[editor.currentTab][self.unit][0]
            listOut = libTools[editor.currentTab][self.unit][1]

            if listOut:
                listOut.append([[portIn.name, portIn.typeio, portIn.format], [portOut.name, portOut.typeio, portOut.format]])
            else:
                listOut = [[[portIn.name, portIn.typeio, portIn.format], [portOut.name, portOut.typeio, portOut.format]]]

            libTools[editor.currentTab][self.unit] = [listEnter, listOut]
            UpdateUndoRedo()
        else:
            ct = editor.currentTab
            if pointTyping[ct] > 0:
                pointTyping[ct] -= 1
                for item in editor.diagramScene[ct].items():
                    editor.diagramScene[ct].removeItem(item)
                newDiagram = undoredoTyping[ct][pointTyping[ct]]
                LoadDiagram(newDiagram.splitlines())
                UpdateList(newDiagram)

    def updateTunnelInput(self, inp):
        self.nbin += 1
        name = inp[0][0]
        portIn = Port(name, 'in', inp[0][2], self.unit, False, True, -18, -25, self)
        portOut = Port(name, 'out', inp[1][2], self.unit, False, True, 4, -12, self)
#         portIn.label.setPlainText(name)
        self.inputs.append(portIn)
        self.outputs.append(portOut)

        listEnter = []
        listOut = []
        try:
            listEnter = libTools[editor.currentTab][self.unit][0]
        except Exception as e:
            pass

        try:
            listOut = libTools[editor.currentTab][self.unit][1]
        except Exception as e:
            pass

        format = inp[0][2]

        for types in TypeColor:
            if types.name in format:
                color = types.value

        portIn.setBrush(color)
        portOut.setBrush(color)

    def updateTunnelOutput(self, outp):
        self.nbout += 1
        name = outp[0][0]
        portOut = Port(name, 'out', outp[1][2], self.unit, False, True, -24, -25, self)
        portIn = Port(name, 'in', outp[0][2], self.unit, False, True, 4, -12, self)
        self.outputs.append(portOut)
        self.inputs.append(portIn)

        listEnter = []
        listOut = []
        try:
            listEnter = libTools[editor.currentTab][self.unit][0]
        except Exception as e:
            pass

        try:
            listOut = libTools[editor.currentTab][self.unit][1]
        except Exception as e:
            pass

        format = outp[0][2]

        for types in TypeColor:
            if types.name in format:
                color = types.value

        portIn.setBrush(color)
        portOut.setBrush(color)

    def deleteTunnel(self, name):

        if 'in' in name:
            self.nbin -= 1
        elif 'out' in name:
            self.nbout -= 1

        for elem in editor.diagramView[editor.currentTab].items():
            if type(elem) == Port:
                if elem.name == name and elem.unit == self.unit:
                    editor.diagramScene[editor.currentTab].removeItem(elem)
                    if elem.typeio == 'in':
                        self.inputs.remove(elem)
                    else:
                        self.outputs.remove(elem)
            if type(elem) == LinkItem:
                if listNodes[editor.currentTab][elem.name].find(self.unit + ':' + name) != -1:
                    BlockCreate.deletelink(self, elem, self.unit)
        x, y = self.updateSize()
        self.resize.setPos(x, y)

        listEnter = []
        listOut = []
        try:
            listEnter = libTools[editor.currentTab][self.unit][0]
            c = 0
            for le in listEnter:
                if le[0][0] == name:
                    del listEnter[c]
                    break
                c += 1
        except Exception as e:
            pass

        try:
            listOut = libTools[editor.currentTab][self.unit][1]
            c = 0
            for lo in listOut:
                if lo[0][0] == name:
                    del listOut[c]
                    break
                c += 1
        except Exception as e:
            pass

        del libTools[editor.currentTab][self.unit]
        libTools[editor.currentTab][self.unit] = [listEnter, listOut]
        UpdateUndoRedo()

    def normalState(self):
        self.setPen(QtGui.QPen(QColor(160, 160, 160, 255), 8))

    def activeState(self):
        self.setPen(QtGui.QPen(QColor(50, 250, 0, 255), 8))

    def IteminLoop(self, unitItem, case, ind):
        listItem = listTools[editor.currentTab][self.unit]

        if self.loopIf:
            if case:
                listItem[ind].append(unitItem)
            else:
                try:
                    listItem[ind].remove(unitItem)
                except Exception as e:
                    pass
            listItem[ind] = list(set(listItem[ind]))

        else:
            if case:
                listItem.append(unitItem)
            else:
                try:
                    listItem.remove(unitItem)
                except Exception as e:
                    pass
            listItem = list(set(listItem))
        listTools[editor.currentTab][self.unit] = listItem
        ValueZ2()

    def editParameters(self):
        c = editParamLoopFor('For Loop', self.nameUnit.toPlainText())
        c.exec_()
        tmp = self.unit
        check, answ = c.getNewValues()
        if answ == 'ok':
            if check:
                if '*' not in self.unit:
                    tmp += '*'
                    self.updateListNodeTools(self.unit, tmp)
                    self.nameUnit.setPlainText(tmp)
                    self.unit = tmp
                    UpdateUndoRedo()
            else:
                tmp = self.unit.replace('*', '')
                self.updateListNodeTools(self.unit, tmp)
                self.nameUnit.setPlainText(tmp)
                self.unit = tmp
                UpdateUndoRedo()

    def updateListNodeTools(self, oldUnit, newUnit):
        libTools[editor.currentTab][newUnit] = libTools[editor.currentTab][oldUnit]
        del libTools[editor.currentTab][oldUnit]
        listTools[editor.currentTab][newUnit] = listTools[editor.currentTab][oldUnit]
        del listTools[editor.currentTab][oldUnit]
        for keyN, valN in listNodes[editor.currentTab].items():
            if oldUnit in valN:
                listNodes[editor.currentTab][keyN] = valN.replace(oldUnit, newUnit)
        listItems[editor.currentTab][newUnit] = listItems[editor.currentTab][oldUnit]
        del listItems[editor.currentTab][oldUnit]    

##############################################################################


class ScriptItem(QGraphicsRectItem):

    def __init__(self, unit, name, w, h, isMod, *inout, parent=None):
        super(ScriptItem, self).__init__(None)
        self.setBrush((QtGui.QBrush(QColor(80, 80, 80, 200))))
        self.setPen(QtGui.QPen(QColor(160, 160, 160, 255), 8))
        self.setFlags(self.ItemIsSelectable | self.ItemIsMovable)
        self.setZValue(-1)
        self.unit = unit
        self.w = w
        self.h = h
        self.wmin = 80.0
        self.hmin = 0.0
        self.nbin, self.nbout = 0, 0
        self.moved = False
        self.isMod = isMod
        self.preview = False
        self.loopIf = False
        self.name = name

        self.setAcceptHoverEvents(True)

        self.caseFinal = False
        self.currentLoop = None

        if unit in 'newScript':
            ScriptExist = True
            inc = 0
            while ScriptExist:
                if 'S' + str(inc) in listTools[editor.currentTab]:
                    inc += 1
                else:
                    ScriptExist = False
            self.unit = 'S' + str(inc)
        else:
            self.unit = unit

        self.inputs = []
        self.outputs = []
        if self.isMod:
            listTools[editor.currentTab][self.unit] = []
            libTools[editor.currentTab][self.unit] = [[], []]

        if inout:
            libTools[editor.currentTab][self.unit] = inout
            for i in range(0, len(inout[0])):
                self.updateInput(inout[0][i])
            for i in range(0, len(inout[1])):
                self.updateOutput(inout[1][i])

        factorh = 20
        self.hmin = factorh * len(self.inputs)
        if self.hmin < factorh * len(self.outputs):
            self.hmin = factorh * len(self.outputs)

        self.label = QGraphicsTextItem(name, self)
        self.label.setFont(QFont("Times", 16, QFont.Bold))
        self.label.setDefaultTextColor(QtGui.QColor(160, 160, 160, 255))

        self.nameUnit = QGraphicsTextItem(self.unit, self)
        self.nameUnit.setDefaultTextColor(QtGui.QColor(255, 255, 255, 255))

        if self.isMod:
            self.setFlags(self.ItemIsSelectable | self.ItemIsMovable | self.ItemIsFocusable)
        self.elemProxy = QTextEdit()
        PythonHighlighter(self.elemProxy)
        self.elemProxy.setLineWrapMode(QTextEdit.NoWrap)
        self.proxyWidget = QGraphicsProxyWidget(self, Qt.Widget)
        self.proxyWidget.setWidget(self.elemProxy)
        self.proxyWidget.setPos(5, 5)

        x, y = self.newSize(self.w, self.h)

        if self.isMod:
            self.resize = Wrist(self)
            self.resize.setPos(x, y)
            self.resize.posChangeCallbacks.append(self.newSize)  # Connect the callback
            self.resize.setFlag(self.resize.ItemIsSelectable, True)
            self.resize.wmin = self.wmin
            self.resize.hmin = self.hmin

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == QtCore.Qt.Key_Delete:
            self.deleteScript()
            UpdateUndoRedo()
        if keyEvent.key() == QtCore.Qt.Key_Up:
            self.setPos(self.x(), self.y() - 1)
        if keyEvent.key() == QtCore.Qt.Key_Down:
            self.setPos(self.x(), self.y() + 1)
        if keyEvent.key() == QtCore.Qt.Key_Left:
            self.setPos(self.x() - 1, self.y())
        if keyEvent.key() == QtCore.Qt.Key_Right:
            self.setPos(self.x() + 1, self.y())
        return QGraphicsRectItem.keyPressEvent(self, keyEvent)

    def mousePressEvent(self, event):
        if self.isMod:
            if event.button() == 1:
                editor.diagramScene[editor.currentTab].clearSelection()
                self.setSelected(True)

            if event.button() == 2:
                self.setSelected(True)

            UpdateUndoRedo()
#         return QGraphicsRectItem.mousePressEvent(self, event)

    def mouseMoveEvent(self, mouseEvent):
        mouseEvent.accept()
        editor.loopMouseMoveEvent(self, mouseEvent.scenePos())
        return QGraphicsRectItem.mouseMoveEvent(self, mouseEvent)

    def mouseReleaseEvent(self, event):
        editor.loopMouseReleaseEvent(self)
        return QGraphicsRectItem.mouseReleaseEvent(self, event)

    def hoverEnterEvent(self, event):
        global itemStored
        itemStored = None
        self.setSelected(True)
        return QGraphicsRectItem.hoverEnterEvent(self, event)

    def hoverLeaveEvent(self, event):
        self.setSelected(False)
        return QGraphicsRectItem.hoverLeaveEvent(self, event)

    def newSize(self, w, h):
        # Limit the block size:
        if h < self.hmin:
            h = self.hmin
        if w < self.wmin:
            w = self.wmin

        self.setRect(0.0, 0.0, w, h)
        self.elemProxy.setMinimumSize(w - 10, h - 10)
        self.elemProxy.setMaximumSize(w - 10, h - 10)
        self.elemProxy.resize(w - 10, h - 10)
        self.label.setPos(0, -40)
        if self.nbin > 0:
            y = (h) / (self.nbin + 1)
            dy = (h) / (self.nbin + 1)
            for inp in range(len(self.inputs)):
                self.inputs[inp].setPos(-9, y)
                y += dy
        if self.nbout > 0:
            y = (h) / (self.nbout + 1)
            dy = (h) / (self.nbout + 1)
            for outp in range(len(self.outputs)):
                self.outputs[outp].setPos(w + 11, y)
                y += dy
        rect = self.nameUnit.boundingRect()
        lw, lh = rect.width(), rect.height()
        lx = (w - lw) / 2
        ly = (h)
        self.nameUnit.setPos(lx, ly)
        self.w = w
        self.h = h
        return w, h

    def updateSize(self):
        factorh = 20
        hmin = factorh * len(self.inputs)
#         w = self.boundingRect().width()
#         h = self.boundingRect().height()
        w = self.w
        h = self.h

        self.hmin = hmin

        if h < hmin:
            h = hmin
        hmin = factorh * len(self.outputs)

        if self.hmin < hmin:
            self.hmin = hmin
        if h < hmin:
            h = hmin
        if w < 100:
            w = 100

        x, y = self.newSize(w, h)
        return x, y

    def contextMenuEvent(self, event):
        if event.isAccepted:
            pass
        if self.isMod:
            menu = QMenu()
            intu = menu.addAction('Add input')
            intu.triggered.connect(self.add_Input)
            outtu = menu.addAction('Add output')
            outtu.triggered.connect(self.add_Output)
            de = menu.addAction('Delete')
            de.triggered.connect(self.deleteScript)
            ct = menu.addAction('Change title')
            ct.triggered.connect(self.changeTitle)
            menu.exec_(event.screenPos())
#             event.accept()
#             return QGraphicsRectItem.contextMenuEvent(self, event)

    def deleteScript(self):
        editor.diagramScene[editor.currentTab].removeItem(self)
        for elem in editor.diagramView[editor.currentTab].items():
            if type(elem) == LinkItem:
                if listNodes[editor.currentTab][elem.name].find(self.unit + ':') != -1:
                    BlockCreate.deletelink(self, elem, self.unit)
        del listTools[editor.currentTab][self.unit]
        del libTools[editor.currentTab][self.unit]
        del listItems[editor.currentTab][self.unit]
        editor.deleteItemsLoop(self)
#         UpdateUndoRedo()

    def changeTitle(self):
        c = changeTitle(self.name, self.nameUnit.toPlainText())
        c.exec_()
        if c.getNewValues():
            self.name = c.getNewValues()
            self.label.setPlainText(c.getNewValues())

    def add_Input(self):
        c = define_inputs_outputs(self.unit, 'input', self.inputs)
        c.exec_()

        if c.getNewValues():
            self.nbin += 1
            portIn = Port(c.getNewValues()[0], 'in', c.getNewValues()[1], self.unit, True, True, -18, -25, self)
            portIn.label.setPos(5 - portIn.label.boundingRect().width(), -28)
            self.inputs.append(portIn)
            x, y = self.updateSize()

            listEnter = libTools[editor.currentTab][self.unit][0]
            listOut = libTools[editor.currentTab][self.unit][1]
            if listEnter:
                listEnter.append([portIn.name, portIn.typeio, portIn.format])
            else:
                listEnter = [[portIn.name, portIn.typeio, portIn.format]]

            libTools[editor.currentTab][self.unit] = [listEnter, listOut]
            UpdateUndoRedo()

    def add_Output(self):
        c = define_inputs_outputs(self.unit, 'output', self.outputs)
        c.exec_()

        if c.getNewValues():
            self.nbout += 1
            portOut = Port(c.getNewValues()[0], 'out', c.getNewValues()[1], self.unit, True, True, -24, -25, self)
            portOut.label.setPos(-8, -28)
            self.outputs.append(portOut)
            x, y = self.updateSize()

            listEnter = libTools[editor.currentTab][self.unit][0]
            listOut = libTools[editor.currentTab][self.unit][1]

            if listOut:
                listOut.append([portOut.name, portOut.typeio, portOut.format])
            else:
                listOut = [[portOut.name, portOut.typeio, portOut.format]]

            libTools[editor.currentTab][self.unit] = [listEnter, listOut]
            UpdateUndoRedo()

    def updateInput(self, inp):
        self.nbin += 1
        portIn = Port(inp[0], 'in', inp[2], self.unit, True, True, -18, -25, self)
        portIn.label.setPos(5 - portIn.label.boundingRect().width(), -28)
        self.inputs.append(portIn)

    def updateOutput(self, outp):
        self.nbout += 1
        portOut = Port(outp[0], 'out', outp[2], self.unit, True, True, -24, -25, self)
        portOut.label.setPos(-8, -28)
        self.outputs.append(portOut)

    def deletePort(self, name, typeio):

        if 'in' in typeio:
            self.nbin -= 1
        elif 'out' in typeio:
            self.nbout -= 1

        for elem in editor.diagramView[editor.currentTab].items():
            if type(elem) == Port:
                if elem.name == name and elem.unit == self.unit:
                    editor.diagramScene[editor.currentTab].removeItem(elem)
                    if elem.typeio == 'in':
                        self.inputs.remove(elem)
                    else:
                        self.outputs.remove(elem)
            if type(elem) == LinkItem:
                if listNodes[editor.currentTab][elem.name].find(self.unit + ':' + name) != -1:
                    BlockCreate.deletelink(self, elem, self.unit)

        x, y = self.updateSize()

        listEnter = []
        listOut = []
        try:
            listEnter = libTools[editor.currentTab][self.unit][0]
            c = 0
            for le in listEnter:
                if le[0] == name:
                    del listEnter[c]
                    break
                c += 1
        except Exception as e:
            pass

        try:
            listOut = libTools[editor.currentTab][self.unit][1]
            c = 0
            for lo in listOut:
                if lo[0] == name:
                    del listOut[c]
                    break
                c += 1
        except Exception as e:
            pass

        del libTools[editor.currentTab][self.unit]
        libTools[editor.currentTab][self.unit] = [listEnter, listOut]
        UpdateUndoRedo()

##############################################################################


class Control_IF(QComboBox):

    def __init__(self, unit, txt, val, parent=None):
        super(Control_IF, self).__init__(parent)
        self.txt = txt
        if txt == 'bool':
            txt = "enumerate(('True','False'))"
        self.addItems([x[1] for x in list(eval(txt))])
        self.setCurrentText(val)
        self.currentTextChanged.connect(self.newValue)
        self.unit = unit

    def newValue(self):
        if self.currentText() == 'True':
            self.trueCase()
        else:
            self.falseCase()
#         UpdateUndoRedo()
#         del listConstants[editor.currentTab][self.unit]
#         listConstants[editor.currentTab][self.unit] = (self.txt, self.currentText())

    def trueCase(self):
        for item in editor.diagramView[editor.currentTab].items():
            if type(item) == BlockCreate or type(item) == ForLoopItem \
                                         or type(item) == ScriptItem \
                                         or type(item) == Constants \
                                         or type(item) == Probes:
                if item.unit in listTools[editor.currentTab][self.unit][0]:
                    item.setOpacity(1)
                    self.opacityLink(item.unit, 1)
                    if type(item) == ForLoopItem:
                        self.opacity_1_InLoop(item.unit, 1)
                        try:
                            item.elemProxy.newValue()
                        except Exception as e:
                            pass
                if item.unit in listTools[editor.currentTab][self.unit][1]:
                    item.setOpacity(0)
                    self.opacityLink(item.unit, 0)
                    if type(item) == ForLoopItem:
                        self.opacity_0_InLoop(item.unit, 0)

        for lsi in listTools[editor.currentTab][self.unit][0]:
            if 'N' in lsi:
                self.opacityLink2(lsi, 1)
        for lsi in listTools[editor.currentTab][self.unit][1]:
            if 'N' in lsi:
                self.opacityLink2(lsi, 0)

    def falseCase(self):
        for item in editor.diagramView[editor.currentTab].items():
            if type(item) == BlockCreate or type(item) == ForLoopItem \
                                         or type(item) == ScriptItem \
                                         or type(item) == Constants \
                                         or type(item) == Probes:
                if item.unit in listTools[editor.currentTab][self.unit][0]:
                    item.setOpacity(0)
                    self.opacityLink(item.unit, 0)
                    if type(item) == ForLoopItem:
                        self.opacity_0_InLoop(item.unit, 0)
                if item.unit in listTools[editor.currentTab][self.unit][1]:
                    item.setOpacity(1)
                    self.opacityLink(item.unit, 1)
                    if type(item) == ForLoopItem:
                        self.opacity_1_InLoop(item.unit, 1)
                        try:
                            item.elemProxy.newValue()
                        except Exception as e:
                            pass
        for lsi in listTools[editor.currentTab][self.unit][0]:
            if 'N' in lsi:
                self.opacityLink2(lsi, 0)
        for lsi in listTools[editor.currentTab][self.unit][1]:
            if 'N' in lsi:
                self.opacityLink2(lsi, 1)

    def opacity_0_InLoop(self, unit, state):
        listToOpacit = []
        if 'I' in unit:
            listToOpacit.extend(listTools[editor.currentTab][unit][0])
            listToOpacit.extend(listTools[editor.currentTab][unit][1])
        else:
            listToOpacit.extend(listTools[editor.currentTab][unit])

        for elemts in editor.diagramView[editor.currentTab].items():
            if (type(elemts) == BlockCreate or type(elemts) == ForLoopItem or type(elemts) == Constants)\
                                        and elemts.unit in listToOpacit:
                elemts.setOpacity(state)

                if type(elemts) == ForLoopItem and elemts.unit != unit:
                    self.opacity_0_InLoop(elemts.unit, state)

    def opacity_1_InLoop(self, unit, state):
        listToOpacit = []
        if 'I' in unit:
            listToOpacit.extend(listTools[editor.currentTab][unit][0])
            listToOpacit.extend(listTools[editor.currentTab][unit][1])
        else:
            listToOpacit.extend(listTools[editor.currentTab][unit])

        for elemts in editor.diagramView[editor.currentTab].items():
            if (type(elemts) == BlockCreate or type(elemts) == ForLoopItem or type(elemts) == Constants)\
                                        and elemts.unit in listToOpacit:
                elemts.setOpacity(state)
#                 if state == 1 and ('I' in unit or 'I' in elemts.unit):
#                     elemts.elemProxy.newValue()
                if state == 1:
                    try:
                        item.elemProxy.newValue()
                    except Exception as e:
                        pass

                if type(elemts) == ForLoopItem and elemts.unit != unit:
                    self.opacity_1_InLoop(elemts.unit, state)

    def opacityLink(self, unit, state):
        listNode_to_opacity = []
        for key_link, val_link in listNodes[editor.currentTab].items():
            tmp_in = val_link[val_link.index("#Node#") + 6:]
            tmp_in = tmp_in[0:tmp_in.index(':')]
            tmp_out = val_link[0:val_link.index(":")]
            if tmp_in == unit or tmp_out == unit:
                listNode_to_opacity.append(key_link)
        for itLink in editor.diagramView[editor.currentTab].items():
            if type(itLink) == LinkItem:
                if itLink.name in listNode_to_opacity:
                    itLink.setOpacity(state)
                    itLink.bislink.setOpacity(state)
                    itLink.linkTxt.setOpacity(state)
                    itLink.linkShow.setOpacity(state)

    def opacityLink2(self, name, state):
        for itLink in editor.diagramView[editor.currentTab].items():
            if type(itLink) == LinkItem:
                if itLink.name == name:
                    itLink.setOpacity(state)
                    itLink.bislink.setOpacity(state)
                    itLink.linkTxt.setOpacity(state)
                    itLink.linkShow.setOpacity(state)

###############################################################################


class TypeColor(Enum):
    str = QColor(200, 0, 250, 255)
    float = QColor(200, 150, 0, 255)
    int = QColor(0, 100, 255, 255)
    path = QColor(255, 100, 100, 255)
    bool = QColor(50, 250, 50, 255)
    dict = QColor(200, 250, 0, 255)
    tuple = QColor(180, 180, 180, 255)
    unkn = QColor(255, 255, 255, 255)


class DimLink(Enum):
    simple = 2
    list = 5
    array = 8
    bis = 3


class ItemColor(Enum):
    backGround = QColor(40, 40, 40, 255)
    process = QColor(100, 100, 100, 255)
    frame_process = QColor(200, 200, 200, 255)
    subprocess = QColor(200, 50, 0, 255)
    frame_subprocess = QColor(250, 100, 0, 255)
    text_block_label = QColor(255, 255, 255, 255)
    text_port_label_input = QColor(200, 200, 200, 255)
    text_port_label_output = QColor(200, 200, 200, 255)
    bis_link = QColor(50, 50, 50, 255)
    frame_comment = QColor(90, 150, 250, 255)
    background_comment = QColor(100, 100, 200, 255)
    text_comment = QColor(120, 150, 250, 255)
    cross_scene = QColor(250, 100, 0, 255)
    frame_connect = QColor(0, 250, 100, 255)
    frame_constants = QColor(200, 200, 200, 255)
    frame_probe = QColor(50, 50, 150, 255)
    text_tab = QColor(20, 20, 20, 255)

###############################################################################


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
            if isinstance(self.var, list):
                len = 1
                if isinstance(self.var[0], list):
                    len = 2
                    if isinstance(self.var[0][0], list):
                        len = 3
            if len == 1:
                typVar = 'list'
                typVal = self.isPath(self.var[0])
            elif len == 2:
                typVar = 'array'
                typVal = self.isPath(self.var[0][0])
            elif len == 3:
                typVar = 'array'
                typVal = self.isPath(self.var[0][0][0])

        elif type(self.var).__name__ in 'tuple':
            typVar = 'tuple'
            typVal = self.isPath(self.var[0])

        elif type(self.var).__name__ in 'enumerate':
            typVar = 'enumerate'
            typVal = 'str'

        if typVar == '':
            return typVal
        else:
            return typVar + '_' + typVal

    def isPath(self, varble):
        if type(varble).__name__ == 'str':
            if 'path' in varble:
                return 'path'
            else:
                return type(varble).__name__
        else:
            return type(varble).__name__

########################################################################################


class ArrowDynamicUp(QGraphicsPolygonItem):

    def __init__(self, parent=None):
        super(ArrowDynamicUp, self).__init__(QPolygonF([QPointF(2, -7), QPointF(6, -2), QPointF(10, -7),
                                                        QPointF(8, -7), QPointF(8, -12), QPointF(4, -12),
                                                        QPointF(4, -7)]), parent)
        self.setBrush(QtGui.QBrush(Qt.green))
        self.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.answer = False

    def mousePressEvent(self, event):
        super(ArrowDynamicUp, self).mousePressEvent(event)
        if event.button() == 1:
            self.answer = True

    def mouseReleaseEvent(self, event):
        self.answer = False

########################################################################################


class ArrowDynamicDown(QGraphicsPolygonItem):

    def __init__(self, parent=None):
        super(ArrowDynamicDown, self).__init__(QPolygonF([QPointF(11, -6), QPointF(13, -6), QPointF(13, -2),
                                                          QPointF(17, -2), QPointF(17, -6), QPointF(19, -6),
                                                          QPointF(15, -12)]), parent)
        self.setBrush(QtGui.QBrush(Qt.red))
        self.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.answer = False

    def mousePressEvent(self, event):
        super(ArrowDynamicDown, self).mousePressEvent(event)
        if event.button() == 1:
            self.answer = True

    def mouseReleaseEvent(self, event):
        self.answer = False

########################################################################################


class Wrist(QGraphicsPolygonItem):

    def __init__(self, parent=None):
        super(Wrist, self).__init__(QPolygonF([QPointF(-12, -2), QPointF(-2, -2), QPointF(-2, -12)]), parent)
        self.posChangeCallbacks = []
        self.setBrush(QtGui.QBrush(Qt.green))
        self.setFlag(self.ItemIsMovable, True)
        self.setFlag(self.ItemSendsScenePositionChanges, True)
        self.setCursor(QtGui.QCursor(Qt.SizeFDiagCursor))

        self.effectiveOpacity()
        self.setOpacity(0.6)

        self.wmin = 0.0
        self.hmin = 0.0

    def itemChange(self, change, value):
        if change == self.ItemPositionChange:
            self.x, self.y = value.x(), value.y()
            if abs(self.x) < self.wmin:
                self.x = self.wmin
            if abs(self.y) < self.hmin:
                self.y = self.hmin

            for cb in self.posChangeCallbacks:
                res = cb(self.x, self.y)
                if res:
                    self.x, self.y = res
                    if self.x < self.wmin:
                        self.x = self.wmin
                    if self.y < self.hmin:
                        self.y = self.hmin

                    value = QtCore.QPointF(self.x, self.y)
            return value
        return super(Wrist, self).itemChange(change, value)

    def mouseReleaseEvent(self, mouseEvent):
        self.setSelected(False)
        self.setPos(self.x, self.y)
        UpdateUndoRedo()
        return QGraphicsPolygonItem.mouseReleaseEvent(self, mouseEvent)


class Port(QGraphicsRectItem):

    def __init__(self, name, nameItem, format, unit, showlabel, isMod, dx, dy, parent=None):

        if 'tunnel' not in nameItem:
            self.rectgl = QRectF(-6, -6, 10.0, 10.0)
        else:
            self.rectgl = QRectF(-15, -12, 30.0, 20.0)

        QGraphicsRectItem.__init__(self, self.rectgl, parent)

        self.setCursor(QCursor(QtCore.Qt.CrossCursor))

        self.name = name
        self.unit = unit
        self.typeio = nameItem
        self.format = format
        self.isMod = isMod
        self.posCallbacks = []
        self.setAcceptHoverEvents(True)
        if isMod:
            self.setFlag(self.ItemSendsScenePositionChanges, True)
        color = QtGui.QColor(255, 255, 255, 255)

        for types in TypeColor:
            if types.name in format:
                color = types.value

        self.setBrush(QBrush(color))

        if showlabel:
            self.label = QGraphicsTextItem(name, self)
            self.label.setFont(QFont("Times", 11, QFont.Bold))
            if self.typeio == 'in':
                self.label.setDefaultTextColor(ItemColor.text_port_label_input.value)
                self.label.setPos(dx, dy)
            elif self.typeio == 'out':
                self.label.setDefaultTextColor(ItemColor.text_port_label_output.value)
                self.label.setPos(-self.label.boundingRect().size().width() - dx, dy)

    def itemChange(self, change, value):
        if change == self.ItemScenePositionHasChanged:
            for cb in self.posCallbacks:
                cb(value)
            return value
        return super(Port, self).itemChange(change, value)

    def hoverEnterEvent(self, event):
        pos = event.screenPos()
        self.setToolTip("<span style=\"background-color: #ffffff;\">format: <b>{}</b></span>".format(self.format))

#     def hoverLeaveEvent(self, event):
#         event.accept()
#         return QGraphicsRectItem.hoverLeaveEvent(self, event)

    def mousePressEvent(self, event):
        if self.isMod and event.button() == 1:
            editor.startLink(self, self.format, event.pos())

    def contextMenuEvent(self, event):
        ac, cp = None, None
        if self.isMod:
            menu = QMenu()
            if ('F' in self.unit or 'I' in self.unit):
                if 'val' not in self.name:
                    ac = menu.addAction('Delete this tunnel')
                    ac.triggered.connect(self.deleteConnector)
            elif ('S' in self.unit):
                ac = menu.addAction('Delete this port')
                ac.triggered.connect(self.deletePort)
            if self.typeio == 'out' and 'A' not in self.unit:
                cp = menu.addAction('add Value Probe')
                cp.triggered.connect(self.addValueP)
                cp = menu.addAction('add Type Probe')
                cp.triggered.connect(self.addTypeP)
                cp = menu.addAction('add Length Probe')
                cp.triggered.connect(self.addLengthP)
                menu.addSeparator()
                cp = menu.addAction('add Print block')
                cp.triggered.connect(self.addPrint)
            elif 'list' not in self.format and \
                 'array' not in self.format and \
                 'dict' not in self.format and \
                 'A' not in self.unit:
                yet = False
                for key, val in listNodes[editor.currentTab].items():
                    tmpVal = val[val.index("#Node#") + 6:]
                    if self.unit + ':' + self.name == tmpVal:
                        yet = True
                if not yet:
                    cp = menu.addAction('add constant for this port')
                    cp.triggered.connect(self.addConstant)

        if ac or cp:
            menu.exec_(event.screenPos())

#             event.accept()
#         return QGraphicsRectItem.contextMenuEvent(self, event)

    def deleteConnector(self):
        listItems[editor.currentTab][self.unit].deleteTunnel(self.name)

    def deletePort(self):
        listItems[editor.currentTab][self.unit].deletePort(self.name, self.typeio)

    def addConstant(self):
        if 'U' in self.unit:
            it = self.addConstantBlock()
        elif 'M' in self.unit:
            it = self.addConstantSubMod()
        elif 'I' in self.unit or 'S' in self.unit:
            it = self.addConstantStr()

        editor.loopMouseMoveEvent(it, it.scenePos())
        editor.loopMouseReleaseEvent(it)

    def addConstantBlock(self):
        nameClass = listItems[editor.currentTab][self.unit].name
        ind = 0
        for i, j in enumerate(editor.getlib()):
            if j[0] == nameClass:
                ind = i
                break
        listEnter = listBlocks[editor.currentTab][self.unit][2][0]
        indx = listEnter.index(self.name)
        val = listBlocks[editor.currentTab][self.unit][2][1][indx]
        if 'enumerate' in self.format:
            for lst in range(len(listEnter)):
                if listEnter[lst] == self.name:
                    try:
                        self.format = editor.getlib()[ind][2][1][lst]
                    except Exception as e:
                        self.format = self.getEnumerateFromYml()
            val = self.format[11:self.format.index(',')]
        a1 = Constants('newConstant', 80, 30, val, self.format, self.name, True)
        a1.setPos(self.mapToScene(self.boundingRect().x() - 100, self.boundingRect().y()))
        editor.diagramScene[editor.currentTab].addItem(a1)
        listItems[editor.currentTab][a1.unit] = a1
        if 'enumerate' in self.format:
            self.format = 'enumerate_str'
        startConnection = Connection('',
                                     a1.outputs[0],
                                     self,
                                     self.format)
        startConnection.setEndPos(self.scenePos())
        startConnection.setToPort(self)
        listNodes[editor.currentTab][startConnection.link.name] = a1.unit + ':' + '#Node#' + self.unit + ':' + self.name

        listVal = listBlocks[editor.currentTab][self.unit]
        newList = []
        for i in range(len(listEnter)):
            if listEnter[i] == self.name:
                newList.append('Node(' + startConnection.link.name + ')')
            else:
                newList.append(listVal[2][1][i])

        del listBlocks[editor.currentTab][self.unit]
        listBlocks[editor.currentTab][self.unit] = (listVal[0], listVal[1], (listVal[2][0], newList, listVal[2][2], listVal[2][3]))
        UpdateUndoRedo()
        return a1

    def addConstantSubMod(self):
        nameClass = listItems[editor.currentTab][self.unit].name
        ind = 0
        for i, j in enumerate(libSubMod):
            if j[0] == nameClass:
                ind = i
                break
        listEnter = listSubMod[editor.currentTab][self.unit][1][0]
        indx = listEnter.index(self.name)
        val = listSubMod[editor.currentTab][self.unit][1][1][indx]
        if 'enumerate' in self.format:
            for lst in range(len(listEnter)):
                if listEnter[lst] == self.name:
                    self.format = libSubMod[ind][1][0][1][lst]
            val = self.format[11:self.format.index(',')]
        a1 = Constants('newConstant', 80, 30, val, self.format, self.name, True)
        a1.setPos(self.mapToScene(self.boundingRect().x() - 100, self.boundingRect().y()))
        editor.diagramScene[editor.currentTab].addItem(a1)
        listItems[editor.currentTab][a1.unit] = a1
        if 'enumerate' in self.format:
            self.format = 'enumerate_str'
        startConnection = Connection('',
                                     a1.outputs[0],
                                     self,
                                     self.format)
        startConnection.setEndPos(self.scenePos())
        startConnection.setToPort(self)
        listNodes[editor.currentTab][startConnection.link.name] = a1.unit + ':' + '#Node#' + self.unit + ':' + self.name

        listVal = listSubMod[editor.currentTab][self.unit]
        newList = []
        for i in range(len(listEnter)):
            if listEnter[i] == self.name:
                newList.append('Node(' + startConnection.link.name + ')')
            else:
                newList.append(listVal[1][1][i])

        del listSubMod[editor.currentTab][self.unit]
        listSubMod[editor.currentTab][self.unit] = (listVal[0], (listVal[1][0], newList, listVal[1][2], listVal[1][3]))
        UpdateUndoRedo()
        return a1

    def addConstantStr(self):
        if 'int' in self.format:
            val = 0
        elif 'float' in self.format:
            val = 0.0
        elif 'str' in self.format:
            val = 'your text'
        elif 'path' in self.format:
            val = 'path'
        elif 'bool' in self.format:
            val = True
        a1 = Constants('newConstant', 80, 30, val, self.format, self.name, True)
        a1.setPos(self.mapToScene(self.boundingRect().x() - 100, self.boundingRect().y()))
        editor.diagramScene[editor.currentTab].addItem(a1)
        listItems[editor.currentTab][a1.unit] = a1

        startConnection = Connection('',
                                     a1.outputs[0],
                                     self,
                                     self.format)
        startConnection.setEndPos(self.scenePos())
        startConnection.setToPort(self)
        listNodes[editor.currentTab][startConnection.link.name] = a1.unit + ':' + '#Node#' + self.unit + ':' + self.name

        UpdateUndoRedo()
        return a1

    def addValueP(self):
        self.addProbe('Value')

    def addTypeP(self):
        self.addProbe('Type')

    def addLengthP(self):
        self.addProbe('Length')

    def addProbe(self, name):
        b1 = Probes('new', self.format, name, True)
        b1.setPos(self.mapToScene(self.boundingRect().x() + 100, self.boundingRect().y()))
        editor.diagramScene[editor.currentTab].addItem(b1)
        listItems[editor.currentTab][b1.unit] = b1
        toPort = b1.inputs[0]
        startConnection = Connection('',
                                     self,
                                     toPort,
                                     self.format)
        startConnection.setEndPos(toPort.scenePos())
        startConnection.setToPort(toPort)
        listNodes[editor.currentTab][startConnection.link.name] = self.unit + ':' + self.name + '#Node#' + b1.unit + ':' + toPort.name

        if 'F' in self.unit and 'in' in self.name:
            curF = listItems[editor.currentTab][self.unit]
            curF.IteminLoop(b1.unit, True, 0)
        elif 'I' in self.unit and 'in' in self.name:
            ind = 0
            curI = listItems[editor.currentTab][self.unit]
            if curI.elemProxy.currentText() == 'False':
                ind = 1
            curI.IteminLoop(b1.unit, True, ind)
        editor.loopMouseMoveEvent(b1, self.scenePos())
        editor.loopMouseReleaseEvent(b1)

    def addPrint(self):
        if 'tuple' in self.format:
            name = 'Print_tuple'
        else:
            name = 'Print_' + self.format
        ind = 0
        for i, j in enumerate(editor.getlib()):
            if j[0] == name:
                ind = i
                break
        b1 = ProcessItem('newBlock',
                         name,
                         editor.getlib()[ind][1],
                         150, 80,
                         editor.getlib()[ind][2]).getBlocks()
        b1.setPos(self.mapToScene(self.boundingRect().x() + 100, self.boundingRect().y()))
        inp = b1.inputs
        for fd in inp:
            if fd.name != 'comment':
                toPort = fd
        editor.diagramScene[editor.currentTab].addItem(b1)
        listItems[editor.currentTab][b1.unit] = b1

        startConnection = Connection('',
                                     self,
                                     toPort,
                                     self.format)
        startConnection.setEndPos(toPort.scenePos())
        startConnection.setToPort(toPort)
        listNodes[editor.currentTab][startConnection.link.name] = self.unit + ':' + self.name + '#Node#' + b1.unit + ':' + toPort.name

        listVal = listBlocks[editor.currentTab][b1.unit]
        listEnter = editor.getlib()[ind][2][0]
        newList = []
        for i in range(len(listEnter)):
            if listEnter[i] != 'comment':
                newList.append('Node(' + startConnection.link.name + ')')
            else:
                newList.append(listVal[2][1][i])

        del listBlocks[editor.currentTab][b1.unit]
        listBlocks[editor.currentTab][b1.unit] = (listVal[0], listVal[1], (listVal[2][0], newList, listVal[2][2], listVal[2][3]))
        UpdateUndoRedo()

    def getEnumerateFromYml(self):
        pathBlock = listBlocks[editor.currentTab][self.unit][1].split('.')
        classBlock = listBlocks[editor.currentTab][self.unit][0]
        pathYml = os.path.dirname(os.path.realpath(__file__))
        pathYml = os.path.join(pathYml, '../modules', pathBlock[0], pathBlock[1] + ".yml")
        if os.path.exists(pathYml):
            with open(pathYml, 'r') as stream:
                self.dicts = yaml.load(stream, yaml.FullLoader)
        en = self.dicts[classBlock][self.name]
        return en


class TreeLibrary(QTreeView):

    def __init__(self, parent=None):
        super(TreeLibrary, self).__init__(parent)
        self.loading = False

    def __new__(self, *args, **kwargs):
        self.loading = False
        return QTreeView.__new__(self, *args, **kwargs)

    def contextMenuEvent(self, event):
        menu = QMenu()
        ac = menu.addAction('Collapse all fields')
        ac.triggered.connect(self.colps)
        ad = menu.addAction('Uncollapse all fields')
        ad.triggered.connect(self.uncolps)
        menu.exec_(QCursor.pos())

    def colps(self):
        self.collapseAll()

    def uncolps(self):
        self.expandAll()

    def selectionChanged(self, *args, **kwargs):
        try:
            index = self.selectedIndexes()
            if index and not self.loading:
                self.getSelectedItem()
            else:
                for elem in previewScene.items():
                    previewScene.removeItem(elem)
        except Exception as e:
            pass
        return QTreeView.selectionChanged(self, *args, **kwargs)

    def getSelectedItem(self):
        index = self.selectedIndexes()[0]
        crawler = index.model().itemFromIndex(index)
        name = crawler.text()
        sel = crawler.text()
        mimidat = index.model().name
        if mimidat in 'mod_SubMod':
            if sel not in listCategory:
                ind = 0
                for i, j in enumerate(editor.getlib()):
                    if j[0] == name:
                        ind = i
                        break
                b1 = BlockCreate(name, '', editor.getlib()[ind][1], 150, 80, editor.getlib()[ind][2][1], False, editor.getlib()[ind][2])
                b1.preview = True
                textSource = 'Source : ' + editor.getlib()[ind][1]
                self.showModel(b1, textSource)
            else:
                for elem in previewScene.items():
                    previewScene.removeItem(elem)

        elif mimidat in 'blocks_subModules':
            if sel not in listCategorySubMod:
                ind = 0
                for i, j in enumerate(libSubMod):
                    if j[0] == name:
                        indMod = i
                        break
                bm = BlockCreate(name, '', None, 150, 80, libSubMod[indMod][1][0][1], False, libSubMod[indMod][1][0])
                self.showModel(bm, '')
            else:
                for elem in previewScene.items():
                    previewScene.removeItem(elem)

        elif mimidat in 'structures_tools':
            # name = model.itemFromIndex(idx).text()
            if sel not in listCategoryTools:
                if "Constant" in name:
                    if 'string' in name:
                        val = 'your text'
                        form = 'str'
                    elif 'integer' in name:
                        val = 0
                        form = 'int'
                    elif 'float' in name:
                        val = 0.0
                        form = 'float'
                    elif 'combobox' in name:
                        form = "enumerate(('item1','item2','item3'))"
                        val = 'item1'
                    elif 'boolean' in name:
                        val = True
                        form = 'bool'
                    elif 'path' in name:
                        val = 'path'
                        form = 'path'
                    bc = Constants('', 80, 30, val, form, '', False)
                elif 'Comments' in name:
                    bc = CommentsItem(200, 100, 'your comments', False)
                elif 'For' in name:
                    bc = ForLoopItem('', name, 200, 200, False)
                elif 'If' in name:
                    bc = ForLoopItem('', name, 200, 200, False)
                elif 'Script' in name:
                    bc = ScriptItem('', name, 200, 200, False)
                elif name in ['Value', 'Type', 'Length']:
                    bc = Probes('', 'int', name, False)

                self.showModel(bc, name)
            else:
                for elem in previewScene.items():
                    previewScene.removeItem(elem)

    def showModel(self, item, text):
        previewScene.clear()
        previewDiagram.scene().addItem(item)
        previewDiagram.scene().update()

        rec = item.boundingRect()
        height = rec.height() / 2

        if len(item.inputs) > 10:
            posX = 100
        else:
            posX = 50
        i = 0
        for inp in item.inputs:
            posY = (((len(item.inputs) - 1) / 2) - i) * height / len(item.inputs)
            self.drawLink(inp, -posX, posY)
            i += 1

        if len(item.outputs) > 10:
            posX = 100
        else:
            posX = 50
        i = 0
        for inp in item.outputs:
            posY = (((len(item.outputs) - 1) / 2) - i) * height / len(item.outputs)
            self.drawLink(inp, posX, posY)
            i += 1

        textSource = QGraphicsTextItem(text, item)
        textSource.setDefaultTextColor(QtGui.QColor(255, 255, 255, 255))
        textSource.setFont(QFont("Times", 14, QFont.Bold))
        textSource.setPos(rec.x() + (rec.width() / 2) - (textSource.boundingRect().width() / 2), rec.y() + rec.height() + 20)

        previewScene.setSceneRect(previewScene.itemsBoundingRect())
        previewDiagram.centerOn(0, 0)
#         previewDiagram.fitInView(rec.x(), rec.y(), rec.width() , rec.height(), QtCore.Qt.KeepAspectRatio)
        previewDiagram.fitInView(previewScene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        previewDiagram.scale(0.8, 0.8)

    def drawLink(self, inp, posX, posY):
        format = inp.format
        link = QGraphicsPathItem()
        bislink = QGraphicsPathItem()

        for types in TypeColor:
            if types.name in format:
                color = types.value

        if 'list' in str(format):
            link.setPen(QtGui.QPen(color, 5))
            bislink.setPen(QtGui.QPen(Qt.NoPen))

        elif 'array' in str(format):
            link.setPen(QtGui.QPen(color, 8))
            bislink.setPen(QtGui.QPen(ItemColor.bis_link.value, 3, Qt.SolidLine))

        else:
            link.setPen(QtGui.QPen(color, 2))
            bislink.setPen(QtGui.QPen(Qt.NoPen))

        path = QPainterPath()
        pos2X, pos2Y = inp.scenePos().x(), inp.scenePos().y() - 1
        pos1X, pos1Y = pos2X + posX, pos2Y - posY
        self.start_x, self.start_y = pos1X, pos1Y
        self.end_x, self.end_y = pos2X, pos2Y
        self.ctrl1_x, self.ctrl1_y = pos1X + (pos2X - pos1X) * 0.7, pos1Y
        self.ctrl2_x, self.ctrl2_y = pos2X + (pos1X - pos2X) * 0.7, pos2Y
        path.moveTo(self.start_x, self.start_y)
        path.cubicTo(self.ctrl1_x, self.ctrl1_y, self.ctrl2_x, self.ctrl2_y, self.end_x, self.end_y)

        link.setPath(path)
        bislink.setPath(path)

        previewDiagram.scene().addItem(link)
        previewDiagram.scene().addItem(bislink)


class ReorderList:

    def __init__(self, list):
        listOrder = self.sorted_nicely(list)
        self.list = list

    def sorted_nicely(self, lst):
        convert = lambda text: int(text) if text.isdigit() else text
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        return sorted(lst, key=alphanum_key)

    def getNewList(self):
        return self.list

###################################################################################################


class NodeEdit(QWidget):

    def __init__(self, textInfo):

        global textEdit
        global previewDiagram, previewScene, legendDiagram, legendScene, editor, textInf, currentTab
        global listItems, listBlocks, listNodes, listConnects, listSubMod, listTools, listConstants, listProbes
        global listCategory, libSubMod, listCategorySubMod, libTools, listCategoryTools
        global undoredoTyping, pointTyping, itemStored
        global listConfigModul, currentpathwork

        editor = self
        textInf = textInfo
        itemStored = None
        listStand = []
        listImport = []

        currentpathwork = os.path.dirname(os.path.realpath(__file__))
        currentpathwork = str(os.path.join(currentpathwork, '../examples'))

        QWidget.__init__(self)
        self.setWindowTitle("Diagram editor")

        self.menub = Menu(self)

        self.verticalLayout = QVBoxLayout(self)

# create libraries processes

        class HorizontalTabBar(QTabBar):

            def __init__(self, parent=None):
                super(HorizontalTabBar, self).__init__(parent)

            def mousePressEvent(self, *args, **kwargs):
                self.setFocus(True)
                return QTabBar.mousePressEvent(self, *args, **kwargs)

            def paintEvent(self, event):
                painter = QStylePainter(self)
                option = QStyleOptionTab()
                for index in range(self.count()):
                    self.initStyleOption(option, index)
                    painter.drawControl(QStyle.CE_TabBarTabShape, option)
                    painter.drawText(self.tabRect(index),
                                     QtCore.Qt.AlignCenter | QtCore.Qt.TextDontClip,
                                     self.tabText(index))

        self.tabLib = QTabWidget()
        self.tabLib.setTabBar(HorizontalTabBar())
        self.tabLib.setTabPosition(QTabWidget.West)
        self.tabLib.setStyleSheet('''
                            QTabBar {color:blue; font-size:14pt;}
                            QTabBar::tab {width: 100%;height: 25px;background-color: lightGray;}
                            QTabBar::tab:selected {background-color: gray;}
                            ''')

        self.icon1 = LibIcon(Qt.darkYellow)
        self.icon2 = LibIcon(ItemColor.process.value)
        self.icon3 = LibIcon(ItemColor.subprocess.value)

#         self.libMod2 = []

        self.libMod3 = LibMod('blocks_subModules')
        self.libMod3.setColumnCount(1)

        self.model1 = LibMod('structures_tools')
        self.model1.setColumnCount(1)
        self.model1.setHeaderData(0, QtCore.Qt.Horizontal, '')
        self.rootNode1 = self.model1.invisibleRootItem()

        self.model3 = LibMod('blocks_subModules')
        self.model3.setColumnCount(1)
        self.model3.setHeaderData(0, QtCore.Qt.Horizontal, '')
        self.rootNode3 = self.model3.invisibleRootItem()

# libraries of processes

        libBlocks, listCategory, listConfigModul = [], [], []

        reps = os.path.dirname(__file__)
        reps, last = os.path.split(reps)
#         reps=reps.replace('python','')
        reps = os.path.join(reps, 'modules')
        lstmod = os.listdir(reps)
        lstmod.sort()

        self.libBrowser, self.model2, self.rootNode2, self.stdItem2 = [], [], [], []
        ind = 0

        for name in lstmod:
            tmp = (os.path.join(reps, name))
            if os.path.isdir(tmp) and '__pycache__' not in tmp and 'sources' not in tmp:
                self.libBrowser.append(TreeLibrary())
                self.model2.append(LibMod('mod_SubMod'))
                self.model2[ind].setColumnCount(1)
                self.model2[ind].setHeaderData(0, QtCore.Qt.Horizontal, '')
                self.rootNode2.append(self.model2[ind].invisibleRootItem())

                # library of processes
                listMod = getlistModules(name)
                infoModules = listMod.listInspect()
                listStand.extend(listMod.listStandalone())
                listImport.extend(listMod.listDepends())

                for category in infoModules:
                    self.stdItem2.clear()
                    branch1 = QStandardItem(category[0])
                    branch1.setEditable(False)
                    branch1.setSelectable(False)
                    listCategory.append(category[0])
                    for clas in category[1]:
                        self.stdItem2.append(QStandardItem(QIcon(self.icon2), clas[0]))
                        libBlocks.append((clas[0], name + '.' + category[0], clas[1:5]))
                    for i in self.stdItem2:
                        i.setEditable(False)
#                         self.libMod2[ind].appendRow(i)
                        branch1.appendRow([QStandardItem(i), None])
                    self.rootNode2[ind].appendRow([branch1, None])

                self.libBrowser[ind].setModel(self.model2[ind])
                self.libBrowser[ind].setColumnWidth(0, 200)
                self.libBrowser[ind].hideColumn(1)
                self.libBrowser[ind].setAlternatingRowColors(True)
                self.libBrowser[ind].expandAll()
                self.libBrowser[ind].setDragDropMode(self.libBrowser[ind].DragOnly)

                self.tabLib.addTab(self.libBrowser[ind], name)

                ind += 1

        self.setlib(libBlocks)

        listStand = set(listStand)
        ConfigModuls().loadConfig(listStand)

# add separator
        self.tabLib.addTab(TreeLibrary(), ' ')

        libTools = []
        listCategoryTools = ['Loop', 'Condition', 'Tools', 'Constants', 'Script', 'Probes']
        self.libMod1 = LibMod('structures_tools')
        self.libMod1.setColumnCount(1)

        branch1 = QStandardItem(listCategoryTools[0])
        branch1.setEditable(False)
        self.stdItem1 = QStandardItem(QIcon(self.icon1), 'For')
        self.stdItem1.setEditable(False)
        self.libMod1.appendRow(self.stdItem1)
        branch1.appendRow([QStandardItem(self.stdItem1), None])
        self.stdItem1 = QStandardItem(QIcon(self.icon1), 'For_multiprocessing')
        self.stdItem1.setEditable(False)
        self.libMod1.appendRow(self.stdItem1)
        branch1.appendRow([QStandardItem(self.stdItem1), None])
        self.rootNode1.appendRow([branch1, None])

        branch1 = QStandardItem(listCategoryTools[1])
        branch1.setEditable(False)
        self.stdItem1 = QStandardItem(QIcon(self.icon1), 'If')
        self.stdItem1.setEditable(False)
        self.libMod1.appendRow(self.stdItem1)
        branch1.appendRow([QStandardItem(self.stdItem1), None])
        self.rootNode1.appendRow([branch1, None])

        branch1 = QStandardItem(listCategoryTools[2])
        branch1.setEditable(False)
        self.stdItem1 = QStandardItem(QIcon(self.icon1), 'Comments')
        self.stdItem1.setEditable(False)
        self.libMod1.appendRow(self.stdItem1)
        branch1.appendRow([QStandardItem(self.stdItem1), None])
        self.rootNode1.appendRow([branch1, None])

        branch1 = QStandardItem(listCategoryTools[3])
        branch1.setEditable(False)
        listCst = ['Constant_float',
                   'Constant_string',
                   'Constant_integer',
                   'Constant_combobox',
                   'Constant_boolean',
                   'Constant_path']

        for cst in listCst:
            self.stdItem1 = QStandardItem(QIcon(self.icon1), cst)
            self.stdItem1.setEditable(False)
            self.libMod1.appendRow(self.stdItem1)
            branch1.appendRow([QStandardItem(self.stdItem1), None])
        self.rootNode1.appendRow([branch1, None])

        branch1 = QStandardItem(listCategoryTools[4])
        branch1.setEditable(False)
        self.stdItem1 = QStandardItem(QIcon(self.icon1), 'Script_editor')
        self.stdItem1.setEditable(False)
        self.libMod1.appendRow(self.stdItem1)
        branch1.appendRow([QStandardItem(self.stdItem1), None])
        self.rootNode1.appendRow([branch1, None])

        branch1 = QStandardItem(listCategoryTools[5])
        branch1.setEditable(False)
        self.stdItem1 = QStandardItem(QIcon(self.icon1), 'Value')
        self.stdItem1.setEditable(False)
        self.libMod1.appendRow(self.stdItem1)
        branch1.appendRow([QStandardItem(self.stdItem1), None])
        self.stdItem1 = QStandardItem(QIcon(self.icon1), 'Type')
        self.stdItem1.setEditable(False)
        self.libMod1.appendRow(self.stdItem1)
        branch1.appendRow([QStandardItem(self.stdItem1), None])
        self.stdItem1 = QStandardItem(QIcon(self.icon1), 'Length')
        self.stdItem1.setEditable(False)
        self.libMod1.appendRow(self.stdItem1)
        branch1.appendRow([QStandardItem(self.stdItem1), None])
        self.rootNode1.appendRow([branch1, None])

        self.libBrowser.append(TreeLibrary())
        self.libBrowser[len(self.libBrowser) - 1].setModel(self.model1)
        self.libBrowser[len(self.libBrowser) - 1].setColumnWidth(0, 200)
        self.libBrowser[len(self.libBrowser) - 1].hideColumn(1)
        self.libBrowser[len(self.libBrowser) - 1].setAlternatingRowColors(True)
        self.libBrowser[len(self.libBrowser) - 1].expandAll()
        self.libBrowser[len(self.libBrowser) - 1].setDragDropMode(self.libBrowser[len(self.libBrowser) - 1].DragOnly)

        self.tabLib.addTab(self.libBrowser[len(self.libBrowser) - 1], 'Structures')

# library of submodules ##########################################################

        infoSubModules = getlistSubModules().listSubModules()
        libSubMod = []
        listCategorySubMod = []
        branch1 = QStandardItem('SubModules')
        branch1.setEditable(False)
        branch1.setSelectable(False)
        listCategorySubMod.append('SubModules')
        for submod in infoSubModules:
            self.stdItem3 = QStandardItem(QIcon(self.icon3), submod[0])
            self.stdItem3.setEditable(False)
            libSubMod.append(submod)
            self.libMod3.appendRow(self.stdItem3)
            branch1.appendRow([QStandardItem(self.stdItem3), None])
        self.rootNode3.appendRow([branch1, None])

        self.libBrowser.append(TreeLibrary())
        self.libBrowser[len(self.libBrowser) - 1].setModel(self.model3)
        self.libBrowser[len(self.libBrowser) - 1].setColumnWidth(0, 200)
        self.libBrowser[len(self.libBrowser) - 1].hideColumn(1)
        self.libBrowser[len(self.libBrowser) - 1].setAlternatingRowColors(True)
        self.libBrowser[len(self.libBrowser) - 1].expandAll()
        self.libBrowser[len(self.libBrowser) - 1].setDragDropMode(self.libBrowser[len(self.libBrowser) - 1].DragOnly)

        self.tabLib.addTab(self.libBrowser[len(self.libBrowser) - 1], 'SubModuls')

        #######################################################################

        textEdit = TextInfo(self)
        textEdit.setStyleSheet("background-color : lightgray")
        redText = "<span style=\" font-size:10pt; font-weight:600; color:#ff0000;\" >"
        redText = redText + ("Welcome to Irmage")
        redText = redText + ("</span>")
        textEdit.append(redText)

        #######################################################################

        previewBlock = QWidget(self)
        previewScene = QGraphicsScene()
        previewScene.setSceneRect(QtCore.QRectF())
        previewDiagram = PreviewBlock()
        previewDiagram.setScene(previewScene)
        layoutDiagram = QVBoxLayout()
        layoutDiagram.addWidget(previewDiagram)
        layoutDiagram.setContentsMargins(0, 0, 0, 0)
        previewBlock.setStyleSheet("background-color:rgb(50,50,50)")
        previewBlock.setLayout(layoutDiagram)

        legend = QWidget(self)
        legendScene = QGraphicsScene()
        legendScene.setSceneRect(QtCore.QRectF())
        legendDiagram = PreviewBlock()
        legendDiagram.setScene(legendScene)
        layoutDiagram = QVBoxLayout()
        layoutDiagram.addWidget(legendDiagram)
        layoutDiagram.setContentsMargins(0, 0, 0, 0)
        legend.setStyleSheet("background-color:rgb(50,50,50)")
        legend.setLayout(layoutDiagram)
        ShowLegend()

        self.tabsDiagram = QTabWidget()
        self.tabsDiagram.setAutoFillBackground(False)
        self.tabsDiagram.setContentsMargins(0, 0, 0, 0)
        self.tabsDiagram.setStyleSheet('''
                            QTabBar::tab {font-size: 11pt; font-family:Times;font:bold;background-color: lightGray;font:italic}
                            QTabBar::tab:selected {background-color: gray;font:bold}
                            ''')
        self.tabsDiagram.setTabsClosable(True)
        self.tabsDiagram.tabCloseRequested.connect(self.closeTab)
        self.tabsDiagram.currentChanged.connect(self.tabSelected)

        listItems, listBlocks, listNodes, listConnects, listProbes = [], [], [], [], []
        listSubMod, listTools, listConstants, libTools = [], [], [], []
        undoredoTyping, pointTyping = [], []
        self.diagramScene, self.diagramView, self.pathDiagram = [], [], []

        self.splitter1 = QSplitter(Qt.Vertical)
        self.splitter1.addWidget(self.tabLib)
        self.splitter1.addWidget(previewBlock)
        self.splitter1.setSizes([400, 150])

        self.splitter2 = QSplitter(Qt.Horizontal)
        self.splitter2.addWidget(textEdit)
        self.splitter2.addWidget(legend)
        self.splitter2.setSizes([400, 200])

        self.splitter3 = QSplitter(Qt.Vertical)
        self.splitter3.addWidget(self.tabsDiagram)
        self.splitter3.addWidget(self.splitter2)
        self.splitter3.setSizes([400, 200])

        self.splitter4 = QSplitter(Qt.Horizontal)
        self.splitter4.addWidget(self.splitter1)
        self.splitter4.addWidget(self.splitter3)
        self.splitter4.setSizes([50, 800])

        self.verticalLayout.addWidget(self.menub)
        self.verticalLayout.addWidget(self.splitter4)

        self.addTab('')
        textInf.setText('')

        self.startConnection = None
        self.startSelection = None

    def getlib(self):
        return self.libBlocks

    def setlib(self, lib):
        self.libBlocks = lib.copy()

    def addTab(self, title):
        i = self.tabsDiagram.count()
        listItems.append({})
        listBlocks.append({})
        listNodes.append({})
        listConnects.append({})
        listSubMod.append({})
        listTools.append({})
        listConstants.append({})
        libTools.append({})
        listProbes.append({})
        pointTyping.append(-1)
        undoredoTyping.append({})
        self.pathDiagram.append('')
        self.diagramScene.append(DiagramScene(self))
        self.diagramView.append(DiagramView(self.diagramScene[i], self))
        layoutDiagram = QVBoxLayout()
        layoutDiagram.addWidget(self.diagramView[i])
        layoutDiagram.setContentsMargins(0, 0, 0, 0)
        wid = QWidget()
        wid.setStyleSheet("background-color:rgb(30,30,30)")
        wid.setLayout(layoutDiagram)
        if title == '':
            title = str(i)
        self.tabsDiagram.addTab(wid, title)
        self.tabsDiagram.tabBar().setTabTextColor(i, ItemColor.text_tab.value)
        self.tabsDiagram.setCurrentIndex(i)
        self.tabsDiagram.setTabToolTip(i, title)

    def closeTab(self, currentIndex):
        currentQWidget = self.tabsDiagram.widget(currentIndex)
        currentTitle = self.tabsDiagram.tabText(currentIndex)
        a = 'yes'
        if currentTitle[-1] == '*':
            a = self.saveDiagramDialog(currentTitle[0:-1])
        if a in ['yes', 'no']:
            currentQWidget.deleteLater()
            self.tabsDiagram.removeTab(currentIndex)
            del listItems[currentIndex]
            del listBlocks[currentIndex]
            del listNodes[currentIndex]
            del listSubMod[currentIndex]
            del listConnects[currentIndex]
            del listConstants[currentIndex]
            del listTools[currentIndex]
            del libTools[currentIndex]
            del listProbes[currentIndex]
            del undoredoTyping[currentIndex]
            del pointTyping[currentIndex]
            del editor.diagramView[currentIndex]
            del editor.diagramScene[currentIndex]
            del editor.pathDiagram[currentIndex]

            try:
                textInf.setText(editor.pathDiagram[editor.currentTab])
            except Exception as e:
                pass

            if self.tabsDiagram.count() == 0:
                self.addTab('')

    def saveDiagramDialog(self, title):
        choice = QMessageBox.question(self, 'Save resource',
                                            "Save changes in " + title + " ?",
                                            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        if choice == QMessageBox.Yes:
            self.menub.btnPressed(QAction('Save Diagram'))
            return 'yes'
        elif choice == QMessageBox.Cancel:
            return 'cancel'
        else:
            return 'no'

    def tabSelected(self, arg=None):
        global textInf
        editor.currentTab = arg
        textInf.setText(editor.pathDiagram[editor.currentTab])

    def blockSelection(self, blockSelected):
        for dd in editor.diagramScene[editor.currentTab].items():
            if type(dd) == LinkItem:
                tmp = listNodes[editor.currentTab][dd.name]
                if blockSelected.unit + ':' in tmp:
                    dd.foncedBlock(False)
                else:
                    dd.foncedBlock(True)
            if type(dd) == BlockCreate or type(dd) == Constants:
                if dd == blockSelected:
                    dd.foncedBlock(False)
                else:
                    dd.foncedBlock(True)

    def refreshSubModLib(self):
        global libSubMod

        self.tabLib.removeTab(len(self.tabLib) - 1)

        self.model3 = LibMod('blocks_subModules')
        self.model3.setColumnCount(1)
        self.rootNode3 = self.model3.invisibleRootItem()

        infoSubModules = getlistSubModules().listSubModules()
        libSubMod = []
        branch1 = QStandardItem('SubModules')
        branch1.setEditable(False)
        branch1.setSelectable(False)
        for submod in infoSubModules:
            self.stdItem3 = QStandardItem(QIcon(self.icon3), submod[0])
            self.stdItem3.setEditable(False)
            libSubMod.append(submod)
            self.libMod3.appendRow(self.stdItem3)
            branch1.appendRow([QStandardItem(self.stdItem3), None])
        self.rootNode3.appendRow([branch1, None])

        self.model3.setHeaderData(0, QtCore.Qt.Horizontal, 'SubProcess blocks')
        del self.libBrowser[len(self.libBrowser) - 1]
        self.libBrowser.append(TreeLibrary())
        self.libBrowser[len(self.libBrowser) - 1].setModel(self.model3)
        self.libBrowser[len(self.libBrowser) - 1].setColumnWidth(0, 200)
        self.libBrowser[len(self.libBrowser) - 1].hideColumn(1)
        self.libBrowser[len(self.libBrowser) - 1].setAlternatingRowColors(True)
        self.libBrowser[len(self.libBrowser) - 1].expandAll()
        self.libBrowser[len(self.libBrowser) - 1].setDragDropMode(self.libBrowser[len(self.libBrowser) - 1].DragOnly)

        self.tabLib.addTab(self.libBrowser[len(self.libBrowser) - 1], 'subModules')
        self.tabLib.setCurrentIndex(len(self.tabLib) - 1)

    def startLink(self, port, format, pos):
        self.startConnection = Connection('', port, None, format)
        self.fromPort = port
        textEdit.setStyleSheet("background-color : lightgray")
        greenText = "<span style=\" font-size:10pt; font-weight:600; color:#003300;\" >"
        greenText = greenText + ('start connection : ' + port.unit + ' ' + port.name + ' ' + port.typeio + ' ' + port.format)
        greenText = greenText + ("</span>")
        textEdit.append(greenText)

    def deleteItemsLoop(self, item):
        for keyF, valueF in listTools[editor.currentTab].items():
            if 'F' in keyF:
                if item.unit in valueF:
                    tmplistTools = valueF
                    tmplistTools.remove(item.unit)
                    listTools[editor.currentTab][keyF] = tmplistTools
            elif 'I' in keyF:
                if item.unit in valueF[0]:
                    tmplistTools = valueF[0]
                    tmplistTools.remove(item.unit)
                    listTools[editor.currentTab][keyF] = [tmplistTools, valueF[1]]
                if item.unit in valueF[1]:
                    tmplistTools = valueF[1]
                    tmplistTools.remove(item.unit)
                    listTools[editor.currentTab][keyF] = [valueF[0], tmplistTools]

    def loopMouseMoveEvent(self, item, pos):
        item.moved = True
#         event.accept()
#         pos = event.scenePos()
        if not item.preview:
            listTypeItems = []
            itms = editor.diagramScene[editor.currentTab].items(pos)

            for elem in itms:
                if type(elem) == ForLoopItem:
                    listTypeItems.append(elem)

            if listTypeItems:
                if len(listTypeItems) > 1:
                    postmp = None
                    elemtmp = None
                    try:
                        ind = 0
                        if item.currentLoop.loopIf:
                            if item.currentLoop.elemProxy.currentText() == 'False':
                                ind = 1
                        item.currentLoop.normalState()
                        item.currentLoop.IteminLoop(item.unit, False, ind)
                        item.currentLoop = None
                        item.caseFinal = False
                    except Exception as e:
                        pass
                    for lsElem in listTypeItems:
                        if not postmp:
                            postmp = lsElem.pos()
                            elemtmp = lsElem

                        elif postmp.x() < lsElem.pos().x():
                            postmp = lsElem.pos()
                            elemtmp = lsElem
                else:
                    elemtmp = listTypeItems[0]
                    try:
                        ind = 0
                        if item.currentLoop.loopIf:
                            if item.currentLoop.elemProxy.currentText() == 'False':
                                ind = 1
                        item.currentLoop.normalState()
                        item.currentLoop.IteminLoop(item.unit, False, ind)
                        item.currentLoop = None
                        item.caseFinal = False
                    except Exception as e:
                        pass

                item.currentLoop = elemtmp
                item.currentLoop.activeState()
                item.caseFinal = True
            else:
                if item.currentLoop:
                    ind = 0
                    if item.currentLoop.loopIf:
                        if item.currentLoop.elemProxy.currentText() == 'False':
                            ind = 1
                    item.currentLoop.normalState()
                    item.currentLoop.IteminLoop(item.unit, False, ind)
                    item.currentLoop = None
                    item.caseFinal = False
#             event.accept()
            item.moved = True

    def loopMouseReleaseEvent(self, item):
        if item.currentLoop:
            ind = 0
            if item.currentLoop.loopIf:
                if item.currentLoop.elemProxy.currentText() == 'False':
                    ind = 1
            item.currentLoop.IteminLoop(item.unit, True, ind)
            item.currentLoop.normalState()
#             item.currentLoop.setDimension()
            item.currentLoop = None
            item.caseFinal = False
        if item.moved:
            UpdateUndoRedo()
            item.moved = False

    def sceneMouseMoveEvent(self, event):
        if self.startConnection:
            pos = event.scenePos()
            self.startConnection.setEndPos(pos)

    def sceneMouseReleaseEvent(self, event):
        self.touchF = (int(event.modifiers()) == (Qt.ControlModifier))

        if self.startConnection:
            pos = event.scenePos()
            items = self.diagramScene[editor.currentTab].items(pos)
            nt = self.startConnection.link.name
            tmpformat = ''

            for item in items:
                if type(item) is LinkItem:
                    if item.name == nt:
                        linkcurrent = item
                if type(item) is Port:
                    portcurrent = item
                    tmpname = item.name
                    tmpunit = item.unit
                    tmptypeio = item.typeio
                    tmpformat = item.format
                    # print(tmpname,tmpunit,tmptypeio,tmpformat)
                    # print(self.fromPort.name,self.fromPort.unit,self.fromPort.typeio,self.fromPort.format)
                    if 'enumerate' in tmpformat:
                        tmpformat = tmpformat[10:]
                    textEdit.setStyleSheet("background-color : lightgray")
                    greenText = "<span style=\" font-size:10pt; font-weight:600; color:#003300;\" >"
                    greenText = greenText + ('try to connect to : ' + tmpunit + ' ' + tmpname + ' ' + tmptypeio + ' ' + tmpformat)
                    greenText = greenText + ("</span>")
                    textEdit.append(greenText)
                    self.startConnection.setToPort(item)

            if 'enumerate' in self.fromPort.format:
                self.fromPort.format = self.fromPort.format[10:]
            if self.startConnection.toPort is None:
                self.startConnection.delete()
            elif self.startConnection.pos1 == self.startConnection.pos2:
                self.startConnection.delete()
            elif tmptypeio == self.fromPort.typeio:
                self.startConnection.delete()
                greenText = "<span style=\" font-size:10pt; font-weight:600; color:#ff0000;\" >"
                greenText = greenText + ('Connection impossible : same type of connector (input=input or output=output) ')
                greenText = greenText + ("</span><br>")
                textEdit.append(greenText)
            elif tmpformat == 'unkn' and self.fromPort.format == 'unkn':
                self.startConnection.delete()
                greenText = "<span style=\" font-size:10pt; font-weight:600; color:#ff0000;\" >"
                greenText = greenText + ('Connection impossible : unknow plug to unknow plug')
                greenText = greenText + ("</span><br>")
                textEdit.append(greenText)
            elif (tmpformat == 'unkn' and 'A' in self.fromPort.unit) or (
                    self.fromPort.format == 'unkn' and 'A' in tmpunit):
                self.startConnection.delete()
                greenText = "<span style=\" font-size:10pt; font-weight:600; color:#ff0000;\" >"
                greenText = greenText + ('Connection impossible : constant to connector ')
                greenText = greenText + ("</span><br>")
                textEdit.append(greenText)
            elif not self.touchF and tmpformat != 'unkn' and self.fromPort.format != 'unkn' and tmpformat != self.fromPort.format:
                self.startConnection.delete()
                greenText = "<span style=\" font-size:10pt; font-weight:600; color:#ff0000;\" >"
                greenText = greenText + ('Connection not recommended due to different formats')
                greenText = greenText + ("</span>")
                greenText = greenText + "<span style=\" font-size:10pt; font-weight:600; color:#003300;\" >"
                greenText = greenText + (' (but you can force the connection by keeping the "Ctrl" key pressed)')
                greenText = greenText + ("</span><br>")
                textEdit.append(greenText)
            else:
                if self.fromPort.typeio == 'out':
                    a = self.fromPort.unit
                    b = self.fromPort.name
                    c = tmpunit
                    d = tmpname
                else:
                    a = tmpunit
                    b = tmpname
                    c = self.fromPort.unit
                    d = self.fromPort.name
                inAlready = False
                indiceLoopIf = 0  # can connect 2 links for LoopIf out
                for ele in listNodes[editor.currentTab]:
                    tmp = listNodes[editor.currentTab][ele]
                    tmp = tmp[tmp.index('#Node#') + 6:len(tmp)]
                    if tmp == c + ":" + d:
                        if 'I' in c:
                            indiceLoopIf += 1
                        if indiceLoopIf == 0 or indiceLoopIf == 2:
                            self.startConnection.delete()
                            greenText = "<span style=\" font-size:10pt; font-weight:600; color:#ff0000;\" >"
                            greenText = greenText + ('Connection impossible : input already taken')
                            greenText = greenText + ("</span><br>")
                            textEdit.append(greenText)
                            inAlready = True
                            break

                if not inAlready:
                    # print(a+':'+b+'#Node#'+c+':'+d)
                    # print(self.fromPort.format,' , ',tmpformat)
                    if 'U' in c:
                        listVal = listBlocks[editor.currentTab][c]
                        ###################################################
                        name = listVal[0]
                        for i, j in enumerate(self.getlib()):
                            if j[0] == name:
                                inds = i
                                break
                        ###################################################
                        category = listVal[1]
                        cat = category.split('.')
                        listEnter = editor.getlib()[inds][2][0]
                        listValDefault = editor.getlib()[inds][2][1]
                        if len(listEnter) != len(listVal[2][1]):
                            if '_dyn' in name:
                                listEnter = listVal[2][0]
                                listValDefault = listVal[2][1]
                            else:
                                pathYml = os.path.dirname(os.path.realpath(__file__))
                                pathYml = os.path.join(pathYml, '../modules', cat[0], cat[1] + ".yml")
                                if os.path.exists(pathYml):
                                    with open(pathYml, 'r') as stream:
                                        self.dicts = yaml.load(stream, yaml.FullLoader)
                                        for el in self.dicts[name]:
                                            if el in listVal[2][0]:
                                                listEnter = (*listEnter, el)
                                                if type(self.dicts[name][el]).__name__ == 'str':
                                                    if 'enumerate' in self.dicts[name][el]:
                                                        listValDefault = (*listValDefault, self.dicts[name][el])
                                                    else:
                                                        try:
                                                            listValDefault = (*listValDefault, eval(self.dicts[name][el]))
                                                        except Exception as e:
                                                            listValDefault = (*listValDefault, self.dicts[name][el])
                                                else:
                                                    try:
                                                        listValDefault = (*listValDefault, eval(self.dicts[name][el]))
                                                    except Exception as e:
                                                        listValDefault = (*listValDefault, self.dicts[name][el])

                        ###################################################
                        newList = []
                        for i in range(len(listEnter)):
                            if listEnter[i] == d:
                                oldVal = listValDefault[i]
                                newList.append('Node(' + nt + ')')
                            else:
                                newList.append(listVal[2][1][i])
                        ###################################################
                        del listBlocks[editor.currentTab][c]
                        listBlocks[editor.currentTab][c] = (listVal[0], listVal[1], (listVal[2][0], newList, listVal[2][2], listVal[2][3]))

                    if 'M' in c:
                        listVal = listSubMod[editor.currentTab][c]

                        ###################################################
                        mod = listVal[0]
                        for i, j in enumerate(libSubMod):
                            if j[0] == mod:
                                indMod = i
                                break
                        ###################################################

                        ind = listVal[1][0].index(d)
                        newList = []
                        for i in range(len(listVal[1][1])):
                            if i == ind:
                                # oldVal = listVal[1][1][i]
                                oldVal = libSubMod[indMod][1][0][1][i]
                                newList.append('Node(' + nt + ')')
                            else:
                                newList.append(listVal[1][1][i])
                        del listSubMod[editor.currentTab][c]
                        listSubMod[editor.currentTab][c] = (listVal[0], (listVal[1][0], newList, listVal[1][2], listVal[1][3]))
                    changeColorLink = False

                    if 'F' in c or 'I' in c or 'S' in c:
                        if tmpformat == "unkn":
                            tmpformat = self.fromPort.format
                        if 'int' in tmpformat:
                            oldVal = 0
                        elif 'float' in tmpformat:
                            oldVal = 0.0
                        elif 'str' in tmpformat:
                            oldVal = ''
                        elif 'path' in tmpformat:
                            oldVal = 'path'
                        elif 'bool' in tmpformat:
                            oldVal = True

                        if 'list' in tmpformat:
                            oldVal = [oldVal]
                        elif 'array' in tmpformat:
                            oldVal = [[oldVal]]

                    if 'I' in a and 'I' in c:
                        for item in items:
                            if type(item) == ForLoopItem and item.unit == a:
                                tmplistTools = listTools[editor.currentTab][a]
                                if item.elemProxy.currentText() == 'True':
                                    tmp = tmplistTools[0]
                                    tmp.append(nt)
                                    listTools[editor.currentTab][a] = [tmp, tmplistTools[1]]
                                else:
                                    tmp = tmplistTools[1]
                                    tmp.append(nt)
                                    listTools[editor.currentTab][a] = [tmplistTools[0], tmp]

                    if tmpformat == 'unkn' or self.fromPort.format == 'unkn':
                        if tmpformat in 'unkn':
                            tmpformat = self.fromPort.format
                        else:
                            self.fromPort.format = tmpformat
                            changeColorLink = True

                    for types in TypeColor:
                        if types.name in tmpformat:
                            color = types.value

                    for types in TypeColor:
                        if types.name in self.fromPort.format:
                            color2 = types.value

                    if 'C' in a and b == 'unkn':
                        b = d
                        mm = True
                        suffix = 0
                        ref = b
                        while mm:
                            found = False
                            for ele in listConnects[editor.currentTab].keys():
                                if b in listConnects[editor.currentTab][ele]:
                                    suffix += 1
                                    b = ref + '_' + str(suffix)
                                    found = True
                            if not found:
                                mm = False

                        if self.fromPort.typeio == 'out':
                            portcurrent = self.fromPort
                        portcurrent.setBrush(color)
                        portcurrent.format = tmpformat
                        portcurrent.name = b
                        portcurrent.label.setPlainText(b)
                        portcurrent.label.setPos(portcurrent.pos().x() - 160 - portcurrent.label.boundingRect().size().width(),
                                                 portcurrent.label.pos().y())
                        tmp = listConnects[editor.currentTab][a]
                        del listConnects[editor.currentTab][a]
                        listConnects[editor.currentTab][a] = (tmp[0], b, tmpformat, oldVal)

                    if 'C' in c and d == 'unkn':
                        d = b
                        mm = True
                        suffix = 0
                        ref = d
                        while mm:
                            found = False
                            for ele in listConnects[editor.currentTab].keys():
                                if d in listConnects[editor.currentTab][ele]:
                                    suffix += 1
                                    d = ref + '_' + str(suffix)
                                    found = True
                            if not found:
                                mm = False
                        if self.fromPort.typeio == 'in':
                            portcurrent = self.fromPort
                        portcurrent.format = tmpformat
                        portcurrent.setBrush(color)
                        portcurrent.name = d
                        portcurrent.label.setPlainText(d)
                        tmp = listConnects[editor.currentTab][c]
                        del listConnects[editor.currentTab][c]
                        listConnects[editor.currentTab][c] = (tmp[0], d, tmpformat)

                    if 'P' in c:
                        if self.fromPort.typeio == 'in':
                            portcurrent = self.fromPort
                        portcurrent.format = tmpformat
                        portcurrent.setBrush(color)
                        tmp = listProbes[editor.currentTab][c]
                        del listProbes[editor.currentTab][c]
                        listProbes[editor.currentTab][c] = (tmpformat, tmp[1])

                    listNodes[editor.currentTab][nt] = a + ':' + b + '#Node#' + c + ':' + d
                    UpdateUndoRedo()

# attribute constants combobox value automatically ######################
                    if 'A' in a and 'enumerate' in str(oldVal):
                        tmpitems = self.diagramScene[editor.currentTab].items()
                        for gh in tmpitems:
                            if type(gh) == Constants:
                                if gh.unit == a and type(gh.elemProxy) == Constants_Combo:
                                    lst = []
                                    for ij in list(eval(oldVal)):
                                        lst.append(ij[1])
                                        gh.elemProxy.clear()
                                        gh.elemProxy.addItems(lst)
                                        gh.elemProxy.txt = "enumerate(" + str(tuple(newList)) + ")"
                                        gh.elemProxy.value = str(newList[0])
                                        gh.elemProxy.setSizeAdjustPolicy(QComboBox.AdjustToContents)
                                        gh.elemProxy.adjustSize()
                                        gh.form = "enumerate(" + str(tuple(lst)) + ")"
                                        gh.changeCombo()
                                        del listConstants[editor.currentTab][gh.unit]
                                        listConstants[editor.currentTab][gh.unit] = (gh.elemProxy.txt, gh.elemProxy.value, gh.label)

                    #################################################################################

                    if changeColorLink:
                        linkcurrent.setPen(QtGui.QPen(color, DimLink.simple.value))
                        if 'list' in str(tmpformat):
                            linkcurrent.setPen(QtGui.QPen(color, DimLink.list.value))
                            linkcurrent.bislink.setPen(QtGui.QPen(Qt.NoPen))
                            linkcurrent.weight = DimLink.list.value
                        elif 'array' in str(tmpformat):
                            linkcurrent.setPen(QtGui.QPen(color, DimLink.array.value))
                            linkcurrent.bislink.setPen(QtGui.QPen(ItemColor.bis_link.value, DimLink.bis.value, Qt.SolidLine))
                            linkcurrent.weight = DimLink.array.value
                        else:
                            linkcurrent.setPen(QtGui.QPen(color, DimLink.simple.value))
                            linkcurrent.bislink.setPen(QtGui.QPen(Qt.NoPen))
                            linkcurrent.weight = DimLink.simple.value
                        linkcurrent.linkTxt.setDefaultTextColor(color)
                        linkcurrent.linkShow.setPen(QtGui.QPen(color, 2))
                        linkcurrent.linkShow.setBrush(color)
                        linkcurrent.color = color

                    textEdit.setStyleSheet("background-color : lightgray")
                    greenText = "<span style=\" font-size:10pt; font-weight:600; color:#003300;\" >"
                    greenText = greenText + ('Connection ok')
                    greenText = greenText + ("</span><br>")
                    textEdit.append(greenText)

            self.startConnection = None

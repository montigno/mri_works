'''
Created on 19 déc. 2017
Update on 08 jan. 2018

@author:  Olivier MONTIGON - IRMaGe
@mail:    olivier.montigon@univ-grenoble-alpes.fr
'''
import json
import os, fnmatch

from PIL import Image, ImageEnhance  # image processing
from PyQt5.Qt import QMenuBar
from PyQt5.QtCore import Qt, QEvent, QModelIndex
from PyQt5.QtGui import QPalette, QPixmap, QImage, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSplitter, \
    QTreeView, QFileSystemModel, QLabel, QSizePolicy, QScrollArea, \
    QLineEdit, QGroupBox, QGridLayout, QPushButton, QSlider, QHBoxLayout, QMenu, \
    QAction, QTextEdit, QTableWidget, QTableWidgetItem, QToolBar, QToolButton, \
    QFrame, QAbstractScrollArea
from scipy.ndimage import rotate  # to work with NumPy arrays

from About import AboutSoft
from Config import Config
import nibabel as nib  # to read nifti file
import numpy as np  # a N-dimensional array object


class DataBrowser(QWidget):
    def __init__(self,textInfo):
     
        global txtInf
        
        super(DataBrowser,self).__init__()
        
        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.lightGray)
        
        self.textInfo = textInfo
        txtInf = self.textInfo
       
        self.factor = 3.0

        self.config=Config()
        self.currentRep = self.config.getPathData()

        self.createActions()
        self.createToolbarMenus()
        #self.createMenus()

        self.browserFile()
        self.imgqLabel()
        self.boxSliders()

        self.verticalLayout = QVBoxLayout(self)
        self.horizontalLayout = QHBoxLayout(self)

        self.textInfoTop = QTextEdit()
        self.textInfoTop.setEnabled(True)
        self.textInfoTop.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        self.textInfoTop.setFontPointSize(11)
        self.textInfoTop.setStyleSheet("background-color: lightgray")
        #self.textInfoTop.adjustSize()
        self.textInfoTop.setText('Welcome to IRMaGe')

        self.tableJson = QTableWidget()
        self.tableJson.setColumnCount(2)
        self.tableJson.setColumnWidth(0,150)
        self.tableJson.setColumnWidth(1,400)
        self.tableJson.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tableJson.setHorizontalHeaderLabels(['Keys','Values'])
        #self.tableJson.setBackgroundRole(QPalette.Light)

        self.scrollText = QScrollArea()
        self.scrollText.setBackgroundRole(QPalette.Dark)
        self.scrollText.setWidget(self.textInfoTop)
        self.scrollText.setWidgetResizable(True)
        #=======================================================================
        # self.adjustScrollBar(self.scrollText.horizontalScrollBar(), 1.0)
        # self.adjustScrollBar(self.scrollText.verticalScrollBar(), 2.0)
        #=======================================================================
        self.scrollTable = QScrollArea()
        self.scrollTable.setBackgroundRole(QPalette.Dark)
        self.scrollTable.setWidget(self.tableJson)
        self.scrollTable.setWidgetResizable(True)
        #=======================================================================
        # self.adjustScrollBar(self.scrollTable.horizontalScrollBar(), 2.0)
        # self.adjustScrollBar(self.scrollTable.verticalScrollBar(), 2.0)
        #=======================================================================
        
        self.headerTabData = ['Data','PatientName','StudyName','DateCreation','PatientSex','PatientWeight','ProtocolName','SequenceName']
        
        self.tableData = TableDataBrower(self)
        self.tableData.setColumnCount(8)
        self.tableData.setRowCount(10)
        self.tableData.setColumnWidth(0,200)
        self.tableData.setHorizontalHeaderLabels(self.headerTabData)
        self.tableData.setBackgroundRole(QPalette.Light)
        self.tableData.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableData.verticalHeader().hide()
                
        self.scrollBrowser = QScrollArea()
        self.scrollBrowser.setBackgroundRole(QPalette.Dark)
        self.scrollBrowser.setWidget(self.tableData)
        self.scrollBrowser.setWidgetResizable(True)
        
        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(Qt.AlignCenter)
    
        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), 0.8)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), 1.0)
        
        self.splitter0 = QSplitter(Qt.Horizontal)
        self.splitter0.addWidget(self.browser)
        self.splitter0.addWidget(self.scrollArea)
        self.splitter0.setSizes([300, 300])
               
        self.splitter2 = QSplitter(Qt.Vertical)
        self.splitter2.addWidget(self.splitter0)
#         self.splitter2.addWidget(self.scrollBrowser)
        self.splitter2.addWidget(self.scrollTable)
        self.splitter2.setSizes([300, 300])
        
        self.splitter3 = QSplitter(Qt.Horizontal)
        self.splitter3.addWidget(self.splitter2)
        self.splitter3.addWidget(self.layoutSlide)
        self.splitter3.setSizes([300, 300])

        self.verticalLayout.addWidget(self.menuToolBar)
        self.verticalLayout.addWidget(self.splitter3)
       
        self.setWindowTitle("MRImage Viewer (IRMaGe)")
        self.resize(800,600)
        
        self.setAutoFillBackground(True)
        self.setPalette(pal)

    def changeSel(self):
        print('Tab changed')

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                                + ((factor - 1) * scrollBar.pageStep()/2)))

    def imgqLabel(self):
        QLabel.__init__(self)
        image = QImage('sources_images/LogoIRMaGe.png')
        self.scaleFactor = 1.0
        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setPixmap(QPixmap.fromImage(image))
        self.scaleFactor *= self.factor
        self.imageLabel.adjustSize()
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

    def open(self, filePath):
        self.img = nib.load(filePath)
        self.textInfoTop.setText('File : '+filePath+'\n')
        self.textInfoTop.append('Dim : ' + str(self.img.shape)+'\n')
        self.enableSliders()
        self.a1.setValue(0)
        self.a2.setValue(0)
        self.a3.setValue(0)
        self.c2.setMaximum(self.img.shape[0])
        self.c2.setMinimum(-self.img.shape[0])
        self.c3.setMaximum(self.img.shape[1])
        self.c3.setMinimum(-self.img.shape[1])
        self.navigImage()
        self.fitToWindowAct.setEnabled(True)
        self.fitToWindow()
    
    def openJson(self,pathJson,fileName):
        with open(pathJson, 'r') as stream:
            try:
                json_object = json.load(stream)
                data = json.dumps(json_object, indent=0,sort_keys=True)
                data = json.loads(data)
                rowPosition=0
                self.tableJson.setRowCount(0)
                
                i=0
                for keyd in self.headerTabData:
                    try:
                        val = str(data[keyd])
                        val = val.replace('[', '')
                        val = val.replace(']', '')
                    except:
                        val = ''
                    #===========================================================
                    # self.tableData.insertRow(i)
                    # self.tableData.setItem(0,i,QTableWidgetItem(val))
                    # i+=1
                    #===========================================================
                #===============================================================
                # self.tableData.setItem(0,0,QTableWidgetItem(fileName))
                # self.tableData.selectRow(0)
                #===============================================================
                for keys in data:
                    try:
                        stringValue = str(data[keys]['value'])
                    except:
                        stringValue = str(data[keys])
#                     stringValue=stringValue.replace('[', '')
#                     stringValue=stringValue.replace(']', '')
                    self.tableJson.insertRow(rowPosition)
                    self.tableJson.setItem(rowPosition,0,QTableWidgetItem(keys))
                    self.tableJson.setItem(rowPosition,1,QTableWidgetItem(stringValue))
                    rowPosition+=1
                self.tableJson.resizeColumnsToContents()
            except json.JSONDecodeError as exc:
                itemError = 'Error Json format'
                self.tableJson.setRowCount(0)
                self.tableJson.insertRow(0)
                self.tableJson.setItem(0,0,QTableWidgetItem(itemError))
                print(exc)
    
    def jsonParser(self,pathJson):
        with open(pathJson,'r') as stream:
            try:
                json_object = json.load(stream)
                listTag = json.dumps(json_object, indent=0,sort_keys=True)
                listTag = json.loads(listTag)
            except json.JSONDecodeError as exc:
                itemError = 'Error Json format'
        return listTag
    
    def tableDataFill(self,pathRepertory):
        files = [f for f in fnmatch.filter(os.listdir(pathRepertory),'*.nii') ]
        self.tableData.setRowCount(0)
        j=0
        for f in files:
            base = os.path.splitext(f)[0]
            g = os.path.join(pathRepertory,base+".json")
            self.tableData.insertRow(j)
            if os.path.isfile(g) :
                data = self.jsonParser(g)
                i=0
                for keyw in self.headerTabData:
                    try:
                        val = str(data[keyw])
                        val = val.replace('[', '')
                        val = val.replace(']', '')
                    except:
                        val = ''
                    self.tableData.setItem(j,i,QTableWidgetItem(val))
                    i+=1
            else :
                self.tableData.setItem(j,1,QTableWidgetItem('No json file found'))
            self.tableData.setItem(j,0,QTableWidgetItem(f))
            self.tableData.resizeColumnsToContents()
            j+=1
 
    def indexImage(self):
        sl1=self.a1.value()
        sl2=self.a2.value()
        sl3=self.a3.value()
        if (len(self.img.shape)==3):
            x = self.img.get_data()[:,:,sl1].copy()
            self.a1.setMaximum(self.img.shape[2]-1)
            self.a2.setMaximum(0)
            self.a3.setMaximum(0)
        if (len(self.img.shape)==4):
            x = self.img.get_data()[:,:,sl1,sl2].copy()
            self.a1.setMaximum(self.img.shape[2]-1)
            self.a2.setMaximum(self.img.shape[3]-1)
            self.a3.setMaximum(0)
        if (len(self.img.shape)==5):
            x = self.img.get_data()[:,:,sl1,sl2,sl3].copy()
            self.a1.setMaximum(self.img.shape[2]-1)
            self.a2.setMaximum(self.img.shape[3]-1)
            self.a3.setMaximum(self.img.shape[4]-1)
        x = rotate(x,-90,reshape=False)
        x = np.uint8((x - x.min())/x.ptp()*255.0)
        self.x = x

############################ Slice controls  #########################################
    def boxSliders(self):
        self.k1 = QLabel('Slider 1    ')
        self.k2 = QLabel('Slider 2')
        self.k3 = QLabel('Slider 3')

        self.a1=self.createSlider(0,0,0)
        self.a2=self.createSlider(0,0,0)
        self.a3=self.createSlider(0,0,0)

        self.a1.valueChanged.connect(self.changePosValue)
        self.a2.valueChanged.connect(self.changePosValue)
        self.a3.valueChanged.connect(self.changePosValue)

        self.txta1 = self.createFieldValue()
        self.txta2 = self.createFieldValue()
        self.txta3 = self.createFieldValue()

        self.controlsGroup = QGroupBox('Slice Controls')
        gridCtrl = QGridLayout()
        gridCtrl.addWidget(self.k1, 0, 0)
        gridCtrl.addWidget(self.a1, 0, 1)
        gridCtrl.addWidget(self.txta1, 0, 2)
        gridCtrl.addWidget(self.k2, 1, 0)
        gridCtrl.addWidget(self.a2, 1, 1)
        gridCtrl.addWidget(self.txta2, 1, 2)
        gridCtrl.addWidget(self.k3, 2, 0)
        gridCtrl.addWidget(self.a3, 2, 1)
        gridCtrl.addWidget(self.txta3, 2, 2)
        self.controlsGroup.setLayout(gridCtrl)

############################ brightness and contrast  ################################
        self.txtb1 = self.createFieldValue()
        self.txtb2 = self.createFieldValue()
        self.txtb3 = self.createFieldValue()
        self.txtb4 = self.createFieldValue()

        self.l1 = QLabel('Brightness    ')
        self.b1 = self.createSlider(101,0,50)
        self.l2 = QLabel('Contrast')
        self.b2 = self.createSlider(101,0,50)
        self.l3 = QLabel('Sharpness')
        self.b3 = self.createSlider(101,0,50)
        self.l4 = QLabel('Color')
        self.b4 = self.createSlider(101,0,50)

        self.b1.valueChanged.connect(self.changeContValue)
        self.b2.valueChanged.connect(self.changeContValue)
        self.b3.valueChanged.connect(self.changeContValue)
        self.b4.valueChanged.connect(self.changeContValue)

        self.txtb1.setText(str(0))
        self.txtb2.setText(str(0))
        self.txtb3.setText(str(0))
        self.txtb4.setText(str(0))

        self.buttonResetContrast = QPushButton('reset',self)
        self.buttonResetContrast.setToolTip('Reset all values')
        self.buttonResetContrast.setEnabled(False)
        self.buttonResetContrast.clicked.connect(self.resetValuesContrast)

        self.contrastGroup = QGroupBox('Brightness and Contrast')
        gridCont = QGridLayout()
        gridCont.addWidget(self.l1,0,0)
        gridCont.addWidget(self.b1,0,1)
        gridCont.addWidget(self.txtb1,0,2)
        gridCont.addWidget(self.l2,1,0)
        gridCont.addWidget(self.b2,1,1)
        gridCont.addWidget(self.txtb2,1,2)
        gridCont.addWidget(self.l3,2,0)
        gridCont.addWidget(self.b3,2,1)
        gridCont.addWidget(self.txtb3,2,2)
        gridCont.addWidget(self.l4,3,0)
        gridCont.addWidget(self.b4,3,1)
        gridCont.addWidget(self.txtb4,3,2)
        gridCont.addWidget(self.buttonResetContrast,4,2)
        self.contrastGroup.setLayout(gridCont)

############################ Transformation  #########################################
        self.txtc1 = self.createFieldValue()
        self.txtc2 = self.createFieldValue()
        self.txtc3 = self.createFieldValue()
        self.txtc4 = self.createFieldValue()

        self.m1 = QLabel('Rotation')
        self.c1 = self.createSlider(180,-180,0)
        self.m2 = QLabel('Translate X    ')
        self.c2 = self.createSlider(1,-1,0)
        self.m3 = QLabel('Translate Y    ')
        self.c3 = self.createSlider(1,-1,0)
        self.m4 = QLabel('Resize')
        self.c4 = self.createSlider(10,0,0)

        self.c1.valueChanged.connect(self.changeTransValue)
        self.c2.valueChanged.connect(self.changeTransValue)
        self.c3.valueChanged.connect(self.changeTransValue)
        self.c4.valueChanged.connect(self.changeTransValue)

        self.txtc1.setText(str(0))
        self.txtc2.setText(str(0))
        self.txtc3.setText(str(0))
        self.txtc4.setText(str(0))

        self.buttonResetTransform = QPushButton('reset',self)
        self.buttonResetTransform.setToolTip('Reset all values')
        self.buttonResetTransform.setEnabled(False)
        self.buttonResetTransform.clicked.connect(self.resetValuesTransform)

        self.transformationGroup = QGroupBox('Transformations')
        gridTransf = QGridLayout()
        gridTransf.addWidget(self.m1,0,0)
        gridTransf.addWidget(self.c1,0,1)
        gridTransf.addWidget(self.txtc1,0,2)
        gridTransf.addWidget(self.m2,1,0)
        gridTransf.addWidget(self.c2,1,1)
        gridTransf.addWidget(self.txtc2,1,2)
        gridTransf.addWidget(self.m3,2,0)
        gridTransf.addWidget(self.c3,2,1)
        gridTransf.addWidget(self.txtc3,2,2)
        gridTransf.addWidget(self.m4,3,0)
        gridTransf.addWidget(self.c4,3,1)
        gridTransf.addWidget(self.txtc4,3,2)
        gridTransf.addWidget(self.buttonResetTransform,4,2)
        self.transformationGroup.setLayout(gridTransf)

##############################################################################
        self.layoutSliders = QVBoxLayout()
        self.layoutSliders.addWidget(self.controlsGroup)
        self.layoutSliders.addWidget(self.contrastGroup)
        self.layoutSliders.addWidget(self.transformationGroup)

        self.layoutSlide = QWidget()
        self.layoutSlide.setLayout(self.layoutSliders)

    def createSlider(self,maxm=0,minm=0,pos=0):
        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        #slider.setTickPosition(QSlider.TicksBothSides)
        slider.setTickInterval(1)
        #slider.setSingleStep(1)
        slider.setMaximum(maxm)
        slider.setMinimum(minm)
        slider.setValue(pos)
        slider.setEnabled(False)
        return slider

    def createFieldValue(self):
        fieldValue = QLineEdit()
        fieldValue.setEnabled(False)
        fieldValue.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        return fieldValue

    def displayPosValue(self):
        self.txta1.setText(str(self.a1.value()+1)+' / '+str(self.a1.maximum()+1))
        self.txta2.setText(str(self.a2.value()+1)+' / '+str(self.a2.maximum()+1))
        self.txta3.setText(str(self.a3.value()+1)+' / '+str(self.a3.maximum()+1))

    def changePosValue(self):
        self.navigImage()

    def navigImage(self):
        self.indexImage()
        self.displayPosValue()
        w,h = self.x.shape
        image = QImage(self.x.data,w,h,QImage.Format_Indexed8)
        self.pixm = QPixmap.fromImage(image)
        self.imageLabel.setPixmap(self.pixm)
        self.imageLabel.adjustSize()
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())
        self.filter()

    def changeContValue(self):
        self.txtb1.setText(str(self.b1.value()-50))
        self.txtb2.setText(str(self.b2.value()-50))
        self.txtb3.setText(str(self.b3.value()-50))
        self.txtb4.setText(str(self.b4.value()-50))
        self.filter()

    def changeTransValue(self):
        self.txtc1.setText(str(self.c1.value()))
        self.txtc2.setText(str(self.c2.value()))
        self.txtc3.setText(str(self.c3.value()))
        self.txtc4.setText(str(self.c4.value()))
        self.filter()

    def filter(self):
        img = Image.fromarray(self.x, 'L')

        brightness = ImageEnhance.Brightness(img)
        newImg = brightness.enhance(1.2*(self.b1.value()+1)/50.0)

        contrast = ImageEnhance.Contrast(newImg)
        newImg = contrast.enhance((self.b2.value()+1)/50.0)

        sharpness = ImageEnhance.Sharpness(newImg)
        newImg = sharpness.enhance(2.0*(self.b3.value()+1)/50.0)

        color = ImageEnhance.Color(newImg)
        newImg = color.enhance((self.b4.value()+1)/50.0)

        newImg = newImg.rotate(self.c1.value())

        newImg = newImg.transform(img.size, Image.AFFINE,(1,0,self.c2.value(),0,1,self.c3.value()))

        size1 = int(img.size[0] * (self.c4.value()+1))
        size2 = int(img.size[1] * (self.c4.value()+1))

        newImg = newImg.resize((size1,size2), Image.ANTIALIAS)

        self.pixm = QPixmap.fromImage(newImg.toqimage())
        self.imageLabel.setPixmap(self.pixm)
        self.imageLabel.adjustSize()
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

    def resetValuesContrast(self):
        self.b1.setSliderPosition(50)
        self.b2.setSliderPosition(50)
        self.b3.setSliderPosition(50)
        self.b4.setSliderPosition(50)
        self.changeContValue()

    def resetValuesTransform(self):
        self.c1.setSliderPosition(0)
        self.c2.setSliderPosition(0)
        self.c3.setSliderPosition(0)
        self.c4.setSliderPosition(0)
        self.changeTransValue()

    def enableSliders(self):
        self.a1.setEnabled(True)
        self.a2.setEnabled(True)
        self.a3.setEnabled(True)
        self.b1.setEnabled(True)
        self.b2.setEnabled(True)
        self.b3.setEnabled(True)
        self.b4.setEnabled(True)
        self.c1.setEnabled(True)
        self.c2.setEnabled(True)
        self.c3.setEnabled(True)
        self.c4.setEnabled(True)
        self.buttonResetContrast.setEnabled(True)
        self.buttonResetTransform.setEnabled(True)

####################################################################################
    def browserFile(self):
        
        global Browser,Model
        
        self.browser = QTreeView()
                
        model = QFileSystemModel()
        model.setRootPath(self.currentRep)
        model.setNameFilters(['*.nii'])
        model.setNameFilterDisables(False)
        model.setReadOnly(True)
        
        self.browser.setModel(model)
        self.browser.expandAll()
        self.browser.setColumnWidth(0,400)
        self.browser.selectionModel().selectionChanged.connect(self.select)
        self.browser.AdjustIgnored
        
        Browser=self.browser
        Model=model

        #=======================================================================
        # self.browser.doubleClicked.connect(self.selection)
        #self.browser.clicked.connect(self.selection)
        #=======================================================================

    def select(self, signal):
        file_path=self.browser.model().filePath(signal.indexes()[0])
        shortName,fileExt=os.path.splitext(file_path)
        filePath,fileName=os.path.split(file_path)
        self.textInfo.setText(filePath)
        blackColor = QColor(0, 0, 0)

        if os.path.isfile(file_path) :
            if fileExt == ".nii":
                if self.currentRep != filePath :
                    self.tableDataFill(filePath)
                    self.currentRep=filePath
                self.open(file_path)
                self.tableData.selectRow(self.tableData.findItems(fileName, Qt.MatchExactly)[0].row())
                if os.path.isfile(shortName+'.json'):
                    greenColor = QColor(50,150,100)
                    self.textInfoTop.setTextColor(greenColor)
                    self.textInfoTop.append('Json file exists '+'\n')
                    self.openJson(shortName+'.json',fileName)
                else :
                    redColor = QColor(255, 0, 0)
                    self.textInfoTop.setTextColor(redColor)
                    self.textInfoTop.append('Json file doesn\'t exist'+'\n')
                    self.tableJson.setRowCount(0)
        else:
            self.tableData.setRowCount(0)
            self.currentRep=filePath
            

        self.textInfoTop.setTextColor(blackColor)
        self.scrollText.setWidgetResizable(True)


####################################################################################
    def createMenus(self):
        self.fileMenu = QMenu("&File", self)
        self.fileMenu.addAction(self.exitAct)

        self.viewMenu = QMenu("&View", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addAction(self.normalSizeAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fitToWindowAct)
        self.viewMenu.addSeparator()

        self.helpMenu = QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)
        
        self.menuBar = QMenuBar()

        self.menuBar.addMenu(self.fileMenu)
        self.menuBar.addMenu(self.viewMenu)
        self.menuBar.addMenu(self.helpMenu)
    
    def createToolbarMenus(self):
        self.menuToolBar = QToolBar()
        
        viewMenu = QToolButton()
        viewMenu.setText('View')
        viewMenu.setPopupMode(QToolButton.MenuButtonPopup)
        aMenu = QMenu()
        aMenu.addAction(self.zoomInAct)
        aMenu.addAction(self.zoomOutAct)
        aMenu.addAction(self.normalSizeAct)
        aMenu.addSeparator()
        aMenu.addAction(self.fitToWindowAct)
        viewMenu.setMenu(aMenu)
        
        helpMenu = QToolButton()
        helpMenu.setText('Help')
        helpMenu.setPopupMode(QToolButton.MenuButtonPopup)
        bMenu = QMenu()
        bMenu.addAction(self.aboutAct)
        helpMenu.setMenu(bMenu)
        
        self.menuToolBar.addWidget(viewMenu)
        self.menuToolBar.addWidget(helpMenu)
        

    def createActions(self):
        self.exitAct = QAction("Exit", self, shortcut="Ctrl+Q",
                triggered=self.close)

        self.zoomInAct = QAction("Zoom In (25%)", self, shortcut="Ctrl++",
                enabled=False, triggered=self.zoomIn)

        self.zoomOutAct = QAction("Zoom Out (25%)", self, shortcut="Ctrl+-",
                enabled=False, triggered=self.zoomOut)

        self.normalSizeAct = QAction("Normal Size", self, shortcut="Ctrl+S",
                enabled=False, triggered=self.normalSize)

        self.fitToWindowAct = QAction("Fit to Window", self, enabled=False,
                checkable=True, shortcut="Ctrl+F", triggered=self.fitToWindow)

        self.aboutAct = QAction("About", self, triggered=self.about)

    def zoomIn(self):
        self.factor=1.25
        self.scaleImage(self.factor)

    def zoomOut(self):
        self.factor=0.8
        self.scaleImage(self.factor)

    def normalSize(self):
        self.imageLabel.adjustSize()
        self.scaleFactor = 1.0

    def fitToWindow(self):
        fitToWindow = self.fitToWindowAct.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        self.scrollText.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.normalSize()

        self.updateActions()

    def updateActions(self):
        self.zoomInAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.zoomOutAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.zoomInAct.setEnabled(self.scaleFactor < 5.0)
        self.zoomOutAct.setEnabled(self.scaleFactor > 0.333)

    def about(self):
        AboutSoft()

    def close(self):
        self.close()
        
class TableDataBrower(QTableWidget):
        
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton : 
            temp = self.itemAt(e.pos())
            if temp != None :
                self.t = temp.row()
                self.selectRow(self.t)
                Browser.setModel(Model)
                Browser.setCurrentIndex(Model.index(txtInf.text()+'/'+self.item(self.t, 0).text()))
                Browser.update()
        QTableWidget.mousePressEvent(self,e)

    #===========================================================================
    # def contextMenuEvent(self, event):
    #     menu = QMenu(self)
    #     detailAction = menu.addAction("Add detail")
    #     action = menu.exec(self.mapToGlobal(event.pos()))
    #     if action == detailAction:
    #         self.detAct()
    #===========================================================================
    
    def contextMenuEvent(self, pos):
        if self.selectionModel().selection().indexes():
            for i in self.selectionModel().selection().indexes():
                row, column = i.row(), i.column()
            menu = QMenu()
            openAction = menu.addAction("Open")
            deleAction = menu.addAction("Delete")
            renaAction = menu.addAction("Rename")
            action = menu.exec(self.mapToGlobal(pos.pos()))
            if action ==openAction:
                self.openAction(row, column)

    def openAction(self, row, column):
        print(row,column)
        
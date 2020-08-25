from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette
from PyQt5.QtWidgets import QSlider, QLabel, QApplication, QSizePolicy, \
    QLineEdit, QGroupBox, QGridLayout, QVBoxLayout, QWidget, QDialog
from scipy.ndimage import rotate

import numpy as np
import sys


class DispNifti():

    def __init__(self, img, pixdim=(1.0, 1.0), title='', parent=None):
        
        self.dia = QDialog()
        self.scaleFactor = 3
              
        self.img = img
        self.dim = len(img.shape)

        if (self.dim == 2):
            tmpimg = self.img.copy()
        elif (self.dim == 3):
            tmpimg = self.img[:, :, 0].copy()
        elif (self.dim == 4):
            tmpimg = self.img[:, :, 0, 0].copy()       
        elif (self.dim == 5):
            tmpimg = self.img[:, :, 0, 0, 0].copy()
            
        self.w, self.h = tmpimg.shape
        self.interl = self.w
        self.rx, self.ry = self.w, self.h
       
        if self.w >= self.h:
            if (self.h * pixdim[1] < self.w * pixdim[0]):
                self.rx = int(self.w * pixdim[0] / pixdim[1])
                self.ry = self.h
                self.interl = self.h
            elif (self.h * pixdim[1] > self.w * pixdim[0]):
                self.rx = self.w
                self.ry = int(self.h * pixdim[1] / pixdim[0])
                self.interl = self.w
        else:
            if (self.h * pixdim[1] > self.w * pixdim[0]):
                self.rx = int(self.w * pixdim[0] / pixdim[1])
                self.ry = self.h
                self.interl = self.h
            elif (self.h * pixdim[1] < self.w * pixdim[0]):
                self.rx = self.w
                self.ry = int(self.h * pixdim[1] / pixdim[0])
                self.interl = self.w
               
        self.boxSliders() 
        self.enableSliders()
        self.imgqLabel()
        self.navigImage()
          
        self.verticalLayout = QVBoxLayout(self.dia)
        self.verticalLayout.addWidget(self.imageLabel)
        self.verticalLayout.addWidget(self.layoutSlide)
         
        self.dia.setWindowTitle(title)
        self.dia.resize(self.w * self.scaleFactor, self.h * self.scaleFactor)
#         self.dia.resize(self.w, self.h)
        self.dia.setLayout(self.verticalLayout)

    def getDialog(self):
        return self.dia
             
    def imgqLabel(self):
        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        
    def navigImage(self):
        self.indexImage()
        self.displayPosValue()
        totalBytes = self.x.data.nbytes
        bytesPerLine = int(totalBytes / self.interl)
        image = QImage(self.x.data, self.w , self.h, bytesPerLine, QImage.Format_Grayscale8)
        self.pixm = QPixmap.fromImage(image)
        
        self.pixm = self.pixm.scaled(self.rx , self.ry, Qt.IgnoreAspectRatio)
        self.imageLabel.setPixmap(self.pixm)
        self.imageLabel.adjustSize()

    def indexImage(self):
        sl1 = self.a1.value()
        sl2 = self.a2.value()
        sl3 = self.a3.value()
        if (self.dim == 2):
            x = self.img.copy()
            self.a1.setMaximum(0)
            self.a2.setMaximum(0)
            self.a3.setMaximum(0)
        elif (self.dim == 3):
            x = self.img[:, :, sl1].copy()
            self.a1.setMaximum(self.img.shape[2] - 1)
            self.a2.setMaximum(0)
            self.a3.setMaximum(0)
        elif (self.dim == 4):
            x = self.img[:, :, sl1, sl2].copy()
            self.a1.setMaximum(self.img.shape[2] - 1)
            self.a2.setMaximum(self.img.shape[3] - 1)
            self.a3.setMaximum(0)
        elif (self.dim == 5):
            x = self.img[:, :, sl1, sl2, sl3].copy()
            self.a1.setMaximum(self.img.shape[2] - 1)
            self.a2.setMaximum(self.img.shape[3] - 1)
            self.a3.setMaximum(self.img.shape[4] - 1)
        x = rotate(x, -90, reshape = True)
        x = np.uint8((x - x.min()) / x.ptp() * 255.0)
        self.x = x
        
    def displayPosValue(self):
        self.txta1.setText(str(self.a1.value() + 1) + ' / ' + str(self.a1.maximum() + 1))
        self.txta2.setText(str(self.a2.value() + 1) + ' / ' + str(self.a2.maximum() + 1))
        self.txta3.setText(str(self.a3.value() + 1) + ' / ' + str(self.a3.maximum() + 1))

    def boxSliders(self):
        self.k1 = QLabel('Slider 1    ')
        self.k2 = QLabel('Slider 2')
        self.k3 = QLabel('Slider 3')
 
        self.a1 = self.createSlider(0, 0, 0)
        self.a2 = self.createSlider(0, 0, 0)
        self.a3 = self.createSlider(0, 0, 0)
 
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
         
        self.layoutSliders = QVBoxLayout()
        self.layoutSliders.addWidget(self.controlsGroup)
 
        self.layoutSlide = QWidget()
        self.layoutSlide.setLayout(self.layoutSliders)
        
    def enableSliders(self):
        self.a1.setEnabled(True)
        self.a2.setEnabled(True)
        self.a3.setEnabled(True)
         
    def createSlider(self, maxm=0, minm=0, pos=0):
        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        # slider.setTickPosition(QSlider.TicksBothSides)
        slider.setTickInterval(1)
        # slider.setSingleStep(1)
        slider.setMaximum(maxm)
        slider.setMinimum(minm)
        slider.setValue(pos)
        slider.setEnabled(False)
        return slider
     
    def createFieldValue(self):
        fieldValue = QLineEdit()
        fieldValue.setEnabled(False)
        fieldValue.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        return fieldValue
     
    def changePosValue(self):
        self.navigImage()

        
app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)

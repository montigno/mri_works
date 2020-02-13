from PyQt5.QtWidgets import QMessageBox, QMainWindow


###############################################################################

class DisplayValues(QMainWindow):
    def __init__(self,Array=[[0.0]],Val_filePath='path',Val_string='',Val_float=0.0,Val_int=1,title=''):
        QMainWindow.__init__(self)
        QMessageBox.about(self,title, "Array =%s , (type =%s) \nVal_filePath =%s (type =%s)"+
                          "\nVal_string =%s (type =%s) \nVal_float =%s  (type =%s) \nVal_int =%s (type =%s)" 
                                                                                    %(Array,type(Array).__name__,
                                                                                    Val_filePath,type(Val_filePath).__name__,
                                                                                    Val_string,type(Val_string).__name__,
                                                                                    Val_float,type(Val_float).__name__,
                                                                                    Val_int,type(Val_int).__name__))
        
###############################################################################

class DisplayString(QMainWindow):
    def __init__(self,in_String='',list_String=[''],array_String=[['']],title=''):
        QMainWindow.__init__(self)
        QMessageBox.about(self,title, "in_String = %s \nlist_String = %s \narray_String = \n%s" 
                          % (in_String,list_String,array_String))
        
###############################################################################

class DisplayInt(QMainWindow):
    def __init__(self,inInt=0,listInt=[0],arrayInt=[[0]],title=''):
        QMainWindow.__init__(self)
        QMessageBox.about(self,title, "Input_int = %s \nlistInt = %s \narrayInt = \n%s" 
                          % (inInt,listInt,arrayInt))
        
###############################################################################

class DisplayFloat(QMainWindow):
    def __init__(self,inFloat=0.0,listFloat=[0.0],arrayFloat=[[0.0]],title=''):
        QMainWindow.__init__(self)
        QMessageBox.about(self,title, "inFloat = %s \nlistFloat =%s \narrayFloat = \n%s" 
                          % (inFloat,listFloat,arrayFloat))
        
###############################################################################

class DisplayPath(QMainWindow):
    def __init__(self,inPath='path',listPath=['path'],arrayPath=[['path']],title=''):
        QMainWindow.__init__(self)
        QMessageBox.about(self,title, "inPath = %s \nlistPath = %s \narrayPath = \n%s" 
                          % (inPath,listPath,arrayPath))

###############################################################################

class DisplayBoolean(QMainWindow):  
    def __init__(self,inBool=True,listBool=[False],arrayBool=[[True]],title=''):
        QMainWindow.__init__(self)
        QMessageBox.about(self,title, "inBool = %s \nlistBool = %s \narrayBool = \n%s" 
                          % (inBool,listBool,arrayBool))

###############################################################################

class DisplayDict(QMainWindow):  
    def __init__(self,inDict={},title=''):
        QMainWindow.__init__(self)
        QMessageBox.about(self,title, "inDict = \n%s" 
                          % (inDict))
     
###############################################################################

class DisplayMatPlot:
    def __init__(self,image=[[0.0]],title=''):
        from NodeEditor.modules.Tools.sources.Display_matplot import disp_mat
        disp_mat(image,title)
        
###############################################################################

class MatPlotLib:
    def __init__(self,sourceFile='path', title='original',display_mode="enumerate(('ortho', 'x', 'y', 'z', 'yx', 'xz', 'yz'))", 
                                                dim=1,draw_cross=False,annotate=False):
        from nilearn import plotting
        plotting.plot_anat(sourceFile,title=title,display_mode=display_mode,dim=dim,draw_cross=draw_cross,annotate=annotate)
        plotting.show()
        
###############################################################################

class MatPlotCurve:
    def __init__(self,data=[[0.0]],x=[0.0]):
        
        try:
            import matplotlib.pyplot as plt
            for lst in data:
                plt.plot(x, lst)
            plt.show()
        except ImportError:
            pass
        
###############################################################################

class MatPlotCurve2:
    def __init__(self,data=[0.0],x=[0.0]):
        
        try:
            import matplotlib.pyplot as plt
            plt.plot(x, data)
            plt.show()
        except ImportError:
            pass
        
###############################################################################

class Display_Nifti_Niwidget:
    def __init__(self,path_image='path'):
        from niwidgets import NiftiWidget
        import nilearn.plotting as nip
        
        my_widget = NiftiWidget(path_image)
        my_widget.nifti_plotter(plotting_func=nip.plot_glass_brain)

###############################################################################
        
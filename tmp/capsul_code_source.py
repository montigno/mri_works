class Choose_file:
    def __init__(self,fileDefault='path',extension='*',title='Select a file'):
        import os.path
        from PyQt5.QtWidgets import QFileDialog
        self.fileChosen=fileDefault
        if fileDefault is 'path' or not os.path.exists(fileDefault):
            fileCh = QFileDialog.getOpenFileName(None, title, '', extension, None, QFileDialog.DontUseNativeDialog)
            if fileCh[0]:
                self.fileChosen = fileCh[0]
       
    def filePath(self:'path'):
        return self.fileChosen


class Print_Path:
    def __init__(self,comment='',inPath='path'):
        print('\033[92m' + comment, inPath)



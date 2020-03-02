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
       
##############################################################################

class Choose_multi_files:
    def __init__(self,filesDefault=['path'],extension='*',title='Open files'):
        import os.path
        from PyQt5.QtWidgets import QFileDialog
        self.filesSource=filesDefault
        for lf in filesDefault:
            if os.path.exists(lf):
                filesExists=True
            else:
                filesExists=False
                break
        if filesDefault==['path'] or not filesExists:
            filesCh = QFileDialog.getOpenFileNames(None, title, '', extension, None, QFileDialog.DontUseNativeDialog)
            if filesCh[0]:
                self.filesSource=filesCh[0]
        self.nb = len(self.filesSource)
             
    def filesPath(self:'list_path'):
        return self.filesSource
    
    def numberOfFiles(self:'int'):
        return self.nb

##############################################################################

class Choose_directory:
    def __init__(self,RepDefault='path',title='Select a directory'):
        import os.path
        from PyQt5.QtWidgets import QFileDialog
        self.repChosen=RepDefault
        if RepDefault is 'path' or not os.path.exists(RepDefault):
            self.repChosen = QFileDialog.getExistingDirectory(None, title, '')
       
    def filePath(self:'path'):
        return self.repChosen
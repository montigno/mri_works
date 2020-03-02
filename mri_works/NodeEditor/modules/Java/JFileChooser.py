#########################################################################################################################################################

class ChooseRepertories:
    def __init__(self):
        from PyQt5.QtCore import QDir        
        from subprocess import Popen, PIPE
        import os, sys
        programm = os.path.join(QDir.currentPath(), 'NodeEditor', 'modules', 'Java', 'sources')
        command = 'java -cp ' + programm + " FileChooser"
        p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        txt, error = p.communicate()
        rc = p.returncode
        txt = txt.decode("utf-8")
        self.outRep = []
        self.outFiles = []
        for val in txt.split("\n"):
            if 'rep=' in val:
                self.outRep.append(val[4:])
            elif 'file=' in val:
                self.outFiles.append(val[5:])
    
    def list_repertories(self:'list_path'):    
        return self.outRep
    
    def list_files(self:'list_path'):
        return self.outFiles

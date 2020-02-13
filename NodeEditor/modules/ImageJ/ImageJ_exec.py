##########################################################################################

class ImageJ_execution():
    def __init__(self,command=''):
        from NodeEditor.python.configStandalone import ConfigModuls
        import os
        import subprocess
        from subprocess import Popen
        pathImageJ=os.path.normpath(ConfigModuls().getPathConfig('ImageJ'))
        pathPlugIns=os.path.join(os.path.dirname(pathImageJ),'plugins')
        subprocess.Popen(['java','-jar',pathImageJ,'-ijpath',pathPlugIns,'-eval',command],shell=False)
        
##########################################################################################


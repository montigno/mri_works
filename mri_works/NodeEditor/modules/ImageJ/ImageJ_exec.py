##########################################################################################

class ImageJ_execution():
    def __init__(self,command=''):
        import os
        import subprocess
        from subprocess import Popen
        subprocess.Popen(['ImageJ','-eval',command],shell=False)
        
##########################################################################################


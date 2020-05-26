class ImageJ_execution():
    def __init__(self,command=''):
        import os
        import subprocess
        from subprocess import Popen
        subprocess.Popen(['ImageJ','-eval',command],shell=False)


class askopenfilename():
    def __init__(self, extension='*.*', title='choose your file'):
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        self.filename = filedialog.askopenfilename(title=title,
                                                   filetypes=[('', extension)])

    def filePath(self: 'path'):
        return self.filename


class ImageJ_load_Image():
    def __init__(self, file='path'):
        import os
        img_current = os.path.basename(file)
        script = "fileCurrent = " + "\"" + file + "\"" + ";imageCurrent = " + "\"" + img_current + "\";open(fileCurrent);run('Enhance Contrast', 'saturated=0.35');"
        self.cmd = script

    def cmd_post(self: 'str'):
        return self.cmd


class ortho_view:
    def __init__(self,cmd_ant=''):
        self.cmd = cmd_ant+"\n"+"run('Orthogonal Views');"
        
    def cmd_post(self:'str'):
        return self.cmd



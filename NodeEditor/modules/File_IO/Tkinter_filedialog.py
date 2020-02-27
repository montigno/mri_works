class askopenfilename():
    def __init__(self,extension='*.*',title='choose your file'):
        import tkinter as tk
        from tkinter import filedialog
        root=tk.Tk()
        root.withdraw()
        self.filename = filedialog.askopenfilename(title=title,filetypes=[('', extension)])
        
    def filePath(self:'path'):
        return self.filename
    
##############################################################################

class askopenfilenames():
    def __init__(self,extension='*.*',title='choose your files'):
        import tkinter as tk
        from tkinter import filedialog
        root=tk.Tk()
        root.withdraw()
        self.filename = filedialog.askopenfilenames(title=title,filetypes=[('', extension)])
        
    def filePath(self:'list_path'):
        return self.filename

##############################################################################

class askdirectory():
    def __init__(self,title='choose your directory'):
        import tkinter as tk
        from tkinter import filedialog
        root=tk.Tk()
        root.withdraw()
        self.dirname = filedialog.askdirectory(title=title)
        
    def dirPath(self:'path'):
        return self.dirname

##############################################################################

class numberOfFiles():
    def __init__(self,list_files=['path']):
        self.nb=len(list_files)
        
    def number_files(self:'int'):
        return self.nb
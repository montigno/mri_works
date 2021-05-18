class projet_path:
    def __init__(self):
        from NodeEditor.python.PipeLine_Irmage import getPathWork
        self.proj_path = getPathWork().pathWork()
        print("current projet path = ", self.proj_path)
        
    def projet_path(self:'path'):
        return self.proj_path

###############################################################################

class separator_path:
    def __init__(self):
        import os
        self.separator = os.sep
        
    def out_sep(self:'str'):
        return self.separator
class projet_path:
    def __init__(self):
        from NodeEditor.python.PipeLine_Irmage import getPathWork
        self.proj_path = getPathWork().pathWork()
        
    def projet_path(self:'path'):
        return self.proj_path
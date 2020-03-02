class transtype_path_listToSimple:
        def __init__(self, inListPath=['path']):
            
            self.outPath = inListPath
            
        def outSimplePath(self:'path'):
            return self.outPath
        
############################################################################################

class transtype_path_SimpleTolist:
    def __init__(self,inPath='path'):
        
        self.outPath = [inPath]
        
    def outListPath(self:'list_path'):
        return self.outPath
    
############################################################################################

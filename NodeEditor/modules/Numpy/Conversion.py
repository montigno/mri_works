class nd_to_list():
    def __init__(self, ndarray_list=[0.0]):
        self.out = list(ndarray_list)
        
    def outList(self:'list_float'):
        return self.out
    
###############################################################################

class strTofloat_Array():
    def __init__(self,list_str=['']):
        import numpy as np
        x = np.array(list_str)
        self.output = x.astype(np.float)
        
    def outArray(self:'array_float'):
        return self.output
    
###############################################################################

class listFloat_to_ndArray():
    def __init__(self,list_float=[0.0]):
        import numpy as np
        x = np.array(list_float)
        
    def outArray(self:'list_float'):
        return self.output       

###############################################################################
class numpy_RMS():
    def __init__(self, y=[0.0]):
        import numpy as np
        self.rms = np.sqrt(np.mean(y**2))
        
    def rms(self:'float'):
        return self.rms
    
###############################################################################

class numpy_abs():
    def __init__(self, y=[0.0]):
        import numpy as np
        self.abs = np.absolute(y)
        
    def abs(self:'list_float'):
        return self.abs
    
###############################################################################

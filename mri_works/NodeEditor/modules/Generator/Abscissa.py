#########################################################################################################################################################

class AbsX:
    def __init__(self,xmin=0.0,xmax=10.0,delta_x=1.0):
        import numpy as np
        self.x = np.linspace(xmin,xmax,int(1+(xmax-xmin)/delta_x))
        
    def outAbscissa(self:'list_float'):
        return self.x
class exponential:
    def __init__(self,amplitude=50.0, decay=1.0, shift=1.0,
                 function="enumerate(('a*exp(-bx)','a*exp(-bx)+c','a*(1-exp(-bx))','a*(1-exp(-bx))+c','a*(1-2*exp(-bx))','a*(1-2*c*exp(-bx))'))",
                 x=[0.0]):
        import numpy as np
        self.y=[]
        x=np.asarray(x)
  
        if function == 'a*exp(-bx)':
            self.y=amplitude * np.exp(-x/decay)
        elif function == 'a*exp(-bx)+c':
            self.y= amplitude * np.exp(-x/decay)+shift
        elif function == 'a*(1-exp(-bx))':
            self.y= amplitude * (1-np.exp(-x/decay))
        elif function == 'a*(1-exp(-bx))+c':
            self.y= amplitude * (1-np.exp(-x/decay))+shift
        elif function == 'a*(1-2*exp(-bx))':
            self.y= amplitude * (1-2*np.exp(-x/decay))
        elif function == 'a*(1-2*c*exp(-bx))':
            self.y= amplitude * (1-2*shift*np.exp(-x/decay))
            
    def outFonction(self:'list_float'):
        return self.y
    
###############################################################################

class trigonometric:
    def __init__(self,angle=0.0,
                 function="enumerate(('sin(x)','cos(x)','tan(x)','arcsin(x)','arccos(x)','arctan(x)'))",
                 x_degree=[0.0]):
        import numpy as np
        self.y=[]
        x = np.asarray(x_degree*np.pi/180.0)
        angle *=  np.pi/180.0
              
        if function == 'sin(x)':
            self.y=np.sin(x+angle)
        elif function == 'cos(x)':
            self.y= np.cos(x+angle)
        elif function == 'tan(x)':
            self.y= np.tan(x+angle)
        elif function == 'arcsin(x)':
            self.y= np.arcsin(x+angle)
        elif function == 'arccos(x)':
            self.y= np.arccos(x+angle)
        elif function == 'arctan(x)':
            self.y= np.arctan(x+angle)
    
    def outFonction(self:'list_float'):
        return self.y

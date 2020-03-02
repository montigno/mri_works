import ast, numpy

class DefineTypeVariable:
    def __init__(self, var):
        self.var = var
        try:
            self.var = ast.literal_eval(var)
        except:
            pass
        
    def returntype(self):
        if self.var == 'path':
            typVal='path'
        else:
            typVal=type(self.var).__name__
        typVar=''
        if type(self.var).__name__ in 'list':
#             typVar=type(self.var).__name__
            if len(numpy.shape(self.var))==1:
                typVar='list'
                typVal=self.isPath(self.var[0])
            elif len(numpy.shape(self.var))==2:
                typVar='array'
                typVal=self.isPath(self.var[0][0])
            elif len(numpy.shape(self.var))==3:
                typVar='array'
                typVal=self.isPath(self.var[0][0][0])
        
        elif type(self.var).__name__ in 'tuple':
            typVar='tuple'
            typVal=self.isPath(self.var[0])
        return typVar+typVal, self.var
    
    def isPath(self, varble):
        if type(varble).__name__ == 'str':
            if 'path' in varble:
                return 'path'
            else:
                return type(varble).__name__
        else:
            return type(varble).__name__
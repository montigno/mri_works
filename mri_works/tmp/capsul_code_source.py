class Print_Float:
    def __init__(self,comment='',inFloat=0.0):
        print('\033[92m' + comment, inFloat)


class add_float_dyn:
    def __init__(self,in1=0.0,in2=0.0,**dynamicsInputs):
        self.res = in1+in2
        for di in dynamicsInputs:
            self.res+=dynamicsInputs[di]
        
    def addition(self:'float'):
        return self.res    


class mult_float_dyn:
    def __init__(self,in1=0.0,in2=0.0,**dynamicsInputs):
        self.res = float(in1)*float(in2)
        for di in dynamicsInputs:
            self.res*=dynamicsInputs[di]
        
    def multiplication(self:'float'):
        return self.res      


class sub_float_dyn:
    def __init__(self,in1=0.0,in2=0.0,**dynamicsInputs):
        self.res = in1-in2
        for di in dynamicsInputs:
            self.res-=dynamicsInputs[di]
  
    def subtract(self:'float'):
        return self.res



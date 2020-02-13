##############################################################################

class add_int:
    def __init__(self,int1=0,int2=0):
        self.res = int1+int2
        
    def addition(self:'int'):
        return self.res    
    
##############################################################################

class sub_int:
    def __init__(self,int1=0,int2=0):
        self.res = int1-int2
        
    def subtract(self:'int'):
        return self.res    
 
##############################################################################

class mult_int:
    def __init__(self,int1=0,int2=0):
        self.res = int1*int2
        
    def multiplication(self:'int'):
        return self.res      

##############################################################################

class div_int:
    def __init__(self,int1=0,int2=1):
        self.res = int(int1/int2)
        
    def division(self:'int'):
        return self.res
    
##############################################################################

class add_int_dyn:
    def __init__(self,int1=0,int2=0,**dynamicsInputs):
        self.res = int1+int2
        for di in dynamicsInputs:
            self.res+=dynamicsInputs[di]
        
    def addition(self:'int'):
        return self.res    
    
##############################################################################

class sub_int_dyn:
    def __init__(self,int1=0,int2=0,**dynamicsInputs):
        self.res = int1-int2
        for di in dynamicsInputs:
            self.res-=dynamicsInputs[di]
        
    def subtract(self:'int'):
        return self.res    
 
##############################################################################

class mult_int_dyn:
    def __init__(self,int1=0,int2=0,**dynamicsInputs):
        self.res = int1*int2
        for di in dynamicsInputs:
            self.res*=dynamicsInputs[di]
        
    def multiplication(self:'int'):
        return self.res      

##############################################################################

class div_int_dyn:
    def __init__(self,int1=0,int2=1,**dynamicsInputs):
        self.res = int(int1/int2)
        for di in dynamicsInputs:
            self.res= int(self.res/dynamicsInputs[di])
        
    def division(self:'int'):
        return self.res   
    
##############################################################################

class add_float:
    def __init__(self,int1=0.0,int2=0.0):
        self.res = int1+int2
        
    def addition(self:'float'):
        return self.res    
    
##############################################################################

class sub_float:
    def __init__(self,int1=0.0,int2=0.0):
        self.res = int1-int2
        
    def subtract(self:'float'):
        return self.res    
 
##############################################################################

class mult_float:
    def __init__(self,int1=0.0,int2=0.0):
         self.res = float(int1)*float(int2)
        
    def multiplication(self:'float'):
        return self.res      

##############################################################################

class div_float:
    def __init__(self,int1=0.0,int2=1.0):
        self.res = int1/int2
        
    def division(self:'float'):
        return self.res

##############################################################################

class add_float_dyn:
    def __init__(self,in1=0.0,in2=0.0,**dynamicsInputs):
        self.res = in1+in2
        for di in dynamicsInputs:
            self.res+=dynamicsInputs[di]
        
    def addition(self:'float'):
        return self.res    
    
##############################################################################

class sub_float_dyn:
    def __init__(self,in1=0.0,in2=0.0,**dynamicsInputs):
        self.res = in1-in2
        for di in dynamicsInputs:
            self.res-=dynamicsInputs[di]
  
    def subtract(self:'float'):
        return self.res
    
##############################################################################

class mult_float_dyn:
    def __init__(self,in1=0.0,in2=0.0,**dynamicsInputs):
        self.res = float(in1)*float(in2)
        for di in dynamicsInputs:
            self.res*=dynamicsInputs[di]
        
    def multiplication(self:'float'):
        return self.res      

##############################################################################

class div_float_dyn:
    def __init__(self,in1=0.0,in2=1.0,**dynamicsInputs):
        self.res = in1/in2
        for di in dynamicsInputs:
            self.res/=dynamicsInputs[di]
        
    def division(self:'float'):
        return self.res
###############################################################

class addSimpleValues:
    def __init__(self,in1=0.0,in2=0.0):
        self.result = in1+in2
             
    def valAdd(self:'float'):
        return self.result

###############################################################

class subtractSimpleValues:
    def __init__(self,in1=0.0,in2=0.0):
        self.result = in1-in2
        
    def valSub(self:'float'):
        return self.result

###############################################################

class MultiplySimpleValues:
    def __init__(self,in1=0.0,in2=0.0):
        self.result = in1*in2
        
    def valMult(self:'float'):
        return self.result
    
###############################################################

class DivideSimpleValues:
    def __init__(self,in1=0.0,in2=0.0):
        try:
            self.result = in1/in2
        except:
            self.result = in1
        
    def valDiv(self:'float'):
        return self.result

###############################################################

class addListValues:
    def __init__(self,list1=[0.0],list2=[0.0]):
        import numpy as np
        self.result = np.add(list1,list2)
             
    def listAdd(self:'list_float'):
        return self.result

###############################################################

class subtractListValues:
    def __init__(self,list1=[0.0],list2=[0.0]):
        import numpy as np
        self.result = np.subtract(list1,list2)
        
    def listSub(self:'list_float'):
        return self.result

###############################################################

class MultiplyListValues:
    def __init__(self,list1=[0.0],list2=[0.0]):
        import numpy as np
        self.result = np.multiply(list1,list2)
        
    def listMult(self:'list_float'):
        return self.result
    
###############################################################

class DivideListValues:
    def __init__(self,list1=[0.0],list2=[0.0]):
        import numpy as np
        try:
            self.result = np.divide(list1,list2)
        except:
            self.result = list1
        
    def listDiv(self:'list_float'):
        return self.result
    
###############################################################

class NegativeListValues:
    def __init__(self,listFloat=[0.0]):
        import numpy as np
        self.result=np.negative(listFloat)
        
    def listDiv(self:'list_float'):
        return self.result
    
###############################################################

class MeanListValues:
    def __init__(self,listFloat=[0.0]):
        import numpy as np
        self.result=np.mean(listFloat)
        
    def listDiv(self:'float'):
        return self.result
    
###############################################################

class Add_Int:
    def __init__(self,in1_Int=0,in2_Int=0):
        self.int_inc=in1_Int+in2_Int
        
    def out_Incr(self:'int'):
        return self.int_inc
    
###############################################################

class NameClassBlock():
    def __init__(self, input1=0,input2=0.0,input3=[''],input4=['path'],input5=[[0.0]],input6=[True]):
        pass
    
    def out1(self:'float'):
        return 
    
    def out2(self:'list_int'):
        return 
    
    def out3(self:'array_bool'):
        return
    
    def _method1(self):
        return 
    
    def _method2(self):
        pass
    

###############################################################################

class AllTypes():
    def __init__(self,
                 inInt=0,inFloat=0.0,inString='',inBool=True,inPath='path',
                 listInt=[0],listFloat=[0.0],listString=[''],listBool=[False],listPath=['path'],
                 arrayInt=[[0]],arrayFloat=[[0.0]],arrayString=[['']],arrayBool=[[False]],arrayPath=[['path']],
                 inDict={},inTuple=('',)):

        self.inInt=inInt
        self.inFloat=inFloat
        self.inString=inString
        self.inBool=inBool
        self.inPath=inPath
        
        self.listInt=listInt
        self.listFloat=listFloat
        self.listString=listString
        self.listBool=listBool
        self.listPath=listPath
        
        self.arrayInt=arrayInt
        self.arrayFloat=arrayFloat
        self.arrayString=arrayString
        self.arrayBool=arrayBool
        self.arrayPath=arrayPath
        
        self.dict=inDict
        self.tup=inTuple
       
    def outInt(self:'int'):
        return self.inInt
    
    def outFloat(self:'float'):
        return self.inFloat
    
    def outString(self:'str'):
        return self.inString
    
    def outBool(self:'bool'):
        return self.inBool
    
    def outPath(self:'path'):
        return self.inPath
   
    def listInt(self:'list_int'):
        return self.listInt
    
    def listFloat(self:'list_float'):
        return self.listFloat
    
    def listString(self:'list_str'):
        return self.listString
    
    def listBool(self:'list_bool'):
        return self.listBool
    
    def listPath(self:'list_path'):
        return self.listPath
    
    def arrayInt(self:'array_int'):
        return self.arrayInt
    
    def arrayFloat(self:'array_float'):
        return self.arrayFloat
    
    def arrayString(self:'array_str'):
        return self.arrayString
    
    def arrayBool(self:'array_bool'):
        return self.arrayBool
    
    def arrayPath(self:'array_path'):
        return self.arrayPath
    
    def dictionary(self:'dict'):
        return self.dict
    
    def tuple(self:'tuple_str'):
        return self.tup
    
###############################################################################

class Fibonacci:
    def __init__(self, n=0):
        a = 0
        b = 1
        if n < 0: 
            print("Incorrect input")
            self.res = 0
        elif n == 0: 
            self.res = a
            self.res1 = a
        elif n == 1: 
            self.res = b
            self.res1 = b
        else: 
            for i in range(2,n): 
                c = a + b 
                a = b 
                b = c 
            self.res = b
            self.res1 = a 
        
    def n_out(self:'float'):
        return self.res
    
    def n_1_out(self:'float'):
        return self.res1
    
    
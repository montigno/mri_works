#############################################################################
    
class Constant_dict():
    def __init__(self,inDict={}):
        self.inDict = inDict

    def outDict(self:'dict'):
        return self.inDict

##########################################################################

class Constant_int_simple():
    def __init__(self,inInt=0):
        self.inInt = inInt
        
    def outIn(self:'int'):
        return self.inInt
    
##########################################################################

class Constant_float_simple():
    def __init__(self,inFloat=0.0):
        self.inFloat = inFloat
    
    def outFloat(self:'float'):
        return self.inFloat
    
##########################################################################

class Constant_string_simple():
    def __init__(self,inString=''):
        self.inString = inString
    
    def outString(self:'str'):
        return self.inString
    
##########################################################################

class Constant_int_list():
    def __init__(self,listInt=[0]):
        self.listInt = listInt
        
    def outListInt(self:'list_int'):
        return self.listInt
    
##########################################################################

class Constant_float_list():
    def __init__(self,listFloat=[0.0]):
        self.listFloat = listFloat

    def outListFloat(self:'list_float'):
        return self.listFloat

##########################################################################

class Constant_string_list():
    def __init__(self,listString=['']):
        self.listString = listString
     
    def outListString(self:'list_str'):
        return self.listString
    
##########################################################################

class Constant_int_array():
    def __init__(self,arrayInt=[[0]]):
        self.arrayInt = arrayInt
        
    def outArrayInt(self:'array_int'):
        return self.arrayInt
    
##########################################################################

class Constant_float_array():
    def __init__(self,arrayFloat=[[0.0]]):
        self.arrayFloat = arrayFloat
    
    def outArrayFloat(self:'array_float'):
        return self.arrayFloat

##########################################################################

class Constant_string_array():
    def __init__(self,arrayString=[['']]):
        self.arrayString = arrayString
    
    def outArrayString(self:'array_str'):
        return self.arrayString
    
##########################################################################

class Constant_boolean_simple():
    def __init__(self, in_bool=True):
        self.outputBool = in_bool

    def out_path(self:'bool'):
        return self.outputBool
    
##########################################################################

class Constant_path_simple():
    def __init__(self, in_path='path'):
        self.outputPath = in_path

    def out_path(self:'path'):
        return self.outputPath
##########################################################################

class Increment_int_list():
    def __init__(self,start=0,end=10):
        self.serie = range(start,end+1)
    
    def serie_int(self:'list_int'):
        return self.serie
        
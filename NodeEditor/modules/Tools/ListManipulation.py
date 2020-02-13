#####################################################################

class index_list_float:
    def __init__(self,list_in_float=[0.0],index=0):
        self.outVal = list_in_float[index]
        
    def out_list_indexed(self:'float'):
        return self.outVal
    
#####################################################################

class index_list_int:
    def __init__(self,list_in_int=[0],index=0):
        self.outVal = list_in_int[index]
        
    def out_list_indexed(self:'int'):
        return self.outVal
    
#####################################################################

class build_list_int:
    def __init__(self,int1=0,int2=0):
        self.outList = [int1,int2]
        
    def out_list(self:'list_int'):
        return self.outList
    
#####################################################################

class build_list_int_dyn:
    def __init__(self,int_in=0,**dynamicsInputs):
        self.outList = [int_in]
        for di in dynamicsInputs:
            self.outList.append(dynamicsInputs[di])
        
    def out_list(self:'list_int'):
        return self.outList
    
#####################################################################

class add_in_list_int:
    def __init__(self,list_int=[0],int_to_add=0):
        self.outList=list_int
        self.outList.append(int_to_add)
    
    def out_list(self:'list_int'):
        return self.outList
    
#####################################################################

class build_list_float_dyn:
    def __init__(self,float_in=0.0,**dynamicsInputs):
        self.outList = [float_in]
        for di in dynamicsInputs:
            self.outList.append(dynamicsInputs[di])
        
    def out_list(self:'list_float'):
        return self.outList
    
#####################################################################

class concatenate_list_float_dyn():
    def __init__(self,list_0=[0.0],list_1=[0.0],**dynamicsInputs):
        self.listConcat=list_0.copy()
        self.listConcat.extend(list_1.copy())
        for di in dynamicsInputs:
            self.listConcat.extend(dynamicsInputs[di])
        
    def list_concat(self:'list_float'):
        return self.listConcat
    
#####################################################################

class concatenate_list_int_dyn():
    def __init__(self,list_0=[0],list_1=[0],**dynamicsInputs):
        self.listConcat=list_0.copy()
        self.listConcat.extend(list_1.copy())
        for di in dynamicsInputs:
            self.listConcat.extend(dynamicsInputs[di])
        
    def list_concat(self:'list_int'):
        return self.listConcat

#####################################################################

class length_list_int():
    def __init__(self,in_list=[0]):
        self.len=len(in_list)
        
    def length(self:'int'):
        return self.len

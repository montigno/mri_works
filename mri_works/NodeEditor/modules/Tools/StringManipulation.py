class string_replace:
    def __init__(self,string_in='',charactToreplace='', newCharact=''):
        self.newString = string_in.replace(charactToreplace,newCharact)
        
    def newString(self:'str'):
        return self.newString

###############################################################################

class string_concatenat_dyn:
    def __init__(self,stringIn='',stringIn_0='',**dynamicsInputs):
        
        self.stringConc = ''
        for di in dynamicsInputs:
            self.stringConc += str(dynamicsInputs[di])
        self.stringConc = str(stringIn)+str(stringIn_0)+self.stringConc
    
    def str_conc(self:'str'):
        return self.stringConc

###############################################################################

class string_list_dyn:
    def __init__(self,stringIn='',**dynamicsInputs):
        
        self.stringList = [stringIn]
        for di in dynamicsInputs:
            self.stringList.append(dynamicsInputs[di])
    
    def str_list(self:'list_str'):
        return self.stringList

###############################################################################

class string_add_element_list_dyn:
    def __init__(self,list_stringIn=[''],elem='',**dynamicsInputs):
        
        self.stringList1 = list_stringIn.copy()
        self.stringList1.append(elem)
        for di in dynamicsInputs:
            self.stringList1.append(dynamicsInputs[di])
            
    def str_list(self:'list_str'):
        return self.stringList1
    
###############################################################################

class string_concatenat_list_dyn:
    def __init__(self,list_string_In=[''],list_0=[''],**dynamicsInputs):
        
        self.stringList2 = list_string_In.copy()
        self.stringList2.extend(list_0)
        for di in dynamicsInputs:
            self.stringList2.extend(dynamicsInputs[di])
            
    def out_list(self:'list_str'):
        return self.stringList2
    
###############################################################################

class string_split:
    def __init__(self, in_string='',expr=''):
        self.listString = in_string.split(expr)
        
    def list_string(self:'list_str'):
        return self.listString
    
###############################################################################

class string_substring:
    def __init__(self,in_string='', start=0, end=0):
        self.substr = in_string[start:end]
        
    def substring(self:'str'):
        return self.substr
    
###############################################################################

class string_substring_2:
    def __init__(self,in_string='', begin='', end=''):
        tmp = str(in_string)
        tmp = tmp[tmp.index(begin):]
        self.substr = tmp[0:tmp.index(end)]
        
    def substring(self:'str'):
        return self.substr
    
###############################################################################

class string_compare:
    def __init__(self,in_string='',compareTo='',type_compare="enumerate(('equal','contains'))"):
        if type_compare == 'equal':
            self.res = in_string == compareTo
        else:
            self.res = in_string in compareTo
            
    def compare_res(self:'bool'):
        return self.res
            
            
            
            
            
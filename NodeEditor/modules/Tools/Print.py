
###############################################################################

class Print_String:
    def __init__(self,comment='',in_String=''):
        print('\033[92m' + comment, in_String)
        
###############################################################################
        
class Print_Int:
    def __init__(self,comment='',inInt=0):
        print('\033[92m' + comment, inInt)

###############################################################################
        
class Print_Float:
    def __init__(self,comment='',inFloat=0.0):
        print('\033[92m' + comment, inFloat)

###############################################################################

class Print_Path:
    def __init__(self,comment='',inPath='path'):
        print('\033[92m' + comment, inPath)

###############################################################################

class Print_Boolean:  
    def __init__(self,comment='',inBool=True):
        print('\033[92m' + comment, inBool)

###############################################################################

class Print_list_String:
    def __init__(self,comment='',in_list_String=['']):
        print('\033[92m' + comment, in_list_String)
        
###############################################################################
        
class Print_list_Int:
    def __init__(self,comment='',in_list_Int=[0]):
        print('\033[92m' + comment, in_list_Int)

###############################################################################
        
class Print_list_Float:
    def __init__(self,comment='',in_list_Float=[0.0]):
        print('\033[92m' + comment, in_list_Float)

###############################################################################

class Print_list_Path:
    def __init__(self,comment='',in_list_Path=['path']):
        print('\033[92m' + comment, in_list_Path)

###############################################################################

class Print_list_Boolean:  
    def __init__(self,comment='',in_list_Bool=[True]):
        print('\033[92m' + comment, in_list_Bool)

###############################################################################

class Print_array_String:
    def __init__(self,comment='',in_array_String=[['']]):
        print('\033[92m' + comment, '\n', in_array_String)
        
###############################################################################
        
class Print_array_Int:
    def __init__(self,comment='',in_array_Int=[[0]]):
        print('\033[92m' + comment, '\n', in_array_Int)

###############################################################################
        
class Print_array_Float:
    def __init__(self,comment='',in_array_Float=[[0.0]]):
        print('\033[92m' + comment, '\n', in_array_Float)

###############################################################################

class Print_array_Path:
    def __init__(self,comment='',in_array_Path=[['path']]):
        print('\033[92m' + comment, '\n', in_array_Path)

###############################################################################

class Print_array_Boolean:  
    def __init__(self,comment='',in_array_Bool=[[True]]):
        print('\033[92m' + comment, '\n', in_array_Bool)
        
###############################################################################

class Print_dict:  
    def __init__(self,comment='',in_dict={}):
        print('\033[92m' + comment, '\n', in_dict)

###############################################################################

class Print_tuple:  
    def __init__(self,comment='',in_tuple=('',)):
        print('\033[92m' + comment, '\n', in_tuple)

###############################################################################

class Print_type_var:
    def __init__(self,comment='',in_var=''):
        print('\033[92m' + comment,type(in_var))
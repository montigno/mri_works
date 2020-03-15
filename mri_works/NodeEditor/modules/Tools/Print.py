class Print_type_var:
    def __init__(self,comment='',in_var=''):
        print('\033[0;92m' + comment,type(in_var))
        print('\33[0m')
        
##############################################################################

class Print_str:
    def __init__(self,comment='',in_String=''):
        print('\033[0;35m' + comment, in_String)
        print('\33[0m')

##############################################################################
        
class Print_int:
    def __init__(self,comment='',inInt=0):
        print('\033[0;94m' + comment, inInt)
        print('\33[0m')

##############################################################################
        
class Print_float:
    def __init__(self,comment='',inFloat=0.0):
        print('\033[0;33m' + comment, inFloat)
        print('\33[0m')

##############################################################################

class Print_path:
    def __init__(self,comment='',inPath='path'):
        print('\033[0;33m' + comment, inPath)
        print('\33[0m')

##############################################################################

class Print_bool:  
    def __init__(self,comment='',inBool=True):
        print('\033[0;92m' + comment, inBool)
        print('\33[0m')

##############################################################################

class Print_list_str:
    def __init__(self,comment='',in_list_String=['']):
        print('\033[0;35m' + comment, in_list_String)
        print('\33[0m')
        
##############################################################################
        
class Print_list_int:
    def __init__(self,comment='',in_list_Int=[0]):
        print('\033[0;94m' + comment, in_list_Int)
        print('\33[0m')

##############################################################################
        
class Print_list_float:
    def __init__(self,comment='',in_list_Float=[0.0]):
        print('\033[0;93m' + comment, in_list_Float)
        print('\33[0m')

############################################################################

class Print_list_path:
    def __init__(self,comment='',in_list_Path=['path']):
        print('\033[0;33m' + comment, in_list_Path)
        print('\33[0m')

##############################################################################

class Print_list_bool:  
    def __init__(self,comment='',in_list_Bool=[True]):
        print('\033[0;92m' + comment, in_list_Bool)
        print('\33[0m')

##############################################################################

class Print_array_str:
    def __init__(self,comment='',in_array_String=[['']]):
        print('\033[0;35m' + comment, '\n', in_array_String)
        print('\33[0m')
        
##############################################################################
        
class Print_array_int:
    def __init__(self,comment='',in_array_Int=[[0]]):
        print('\033[0;94m' + comment, '\n', in_array_Int)
        print('\33[0m')

##############################################################################
        
class Print_array_float:
    def __init__(self,comment='',in_array_Float=[[0.0]]):
        print('\033[0;93m' + comment, '\n', in_array_Float)
        print('\33[0m')

##############################################################################

class Print_array_path:
    def __init__(self,comment='',in_array_Path=[['path']]):
        print('\033[0;33m' + comment, '\n', in_array_Path)
        print('\33[0m')

##############################################################################

class Print_array_bool:  
    def __init__(self,comment='',in_array_Bool=[[True]]):
        print('\033[0;92m' + comment, '\n', in_array_Bool)
        print('\33[0m')
        
##############################################################################

class Print_dict:  
    def __init__(self,comment='',in_dict={}):
        print('\033[1;33m' + comment, '\n', in_dict)
        print('\33[0m')

##############################################################################

class Print_tuple:  
    def __init__(self,comment='',in_tuple=('',)):
        print('\033[0;92m' + comment, '\n', in_tuple)
        print('\33[0m')

#############################################################################
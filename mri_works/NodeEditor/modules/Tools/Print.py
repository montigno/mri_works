class Print_type_var:
    def __init__(self, comment='', in_var=''):
        print('\033[0;92m' + comment, type(in_var))
        print('\33[0m')

##############################################################################


class Print_str:
    def __init__(self, comment='', in_String=''):
        print('\33[38;5;201m' + comment, in_String)
        print('\33[0m')

##############################################################################


class Print_int:
    def __init__(self, comment='', inInt=0):
        print('\33[38;5;33m' + comment, inInt)
        print('\33[0m')

##############################################################################


class Print_float:
    def __init__(self, comment='', inFloat=0.0):
        print('\33[38;5;208m' + comment, inFloat)
        print('\33[0m')

##############################################################################


class Print_path:
    def __init__(self, comment='', inPath='path'):
        print('\33[38;5;210m' + comment, inPath)
        print('\33[0m')

##############################################################################


class Print_bool:
    def __init__(self, comment='', inBool=True):
        print('\33[38;5;46m' + comment, inBool)
        print('\33[0m')

##############################################################################


class Print_list_str:
    def __init__(self, comment='', in_list_String=['']):
        print('\33[38;5;201m' + comment, in_list_String)
        print('\33[0m')

##############################################################################


class Print_list_int:
    def __init__(self, comment='', in_list_Int=[0]):
        print('\33[38;5;33m' + comment, in_list_Int)
        print('\33[0m')

##############################################################################


class Print_list_float:
    def __init__(self, comment='', in_list_Float=[0.0]):
        print('\33[38;5;208m' + comment, in_list_Float)
        print('\33[0m')

############################################################################


class Print_list_path:
    def __init__(self, comment='', in_list_Path=['path']):
        import time
        time.sleep(0.1)
        print('\33[38;5;210m' + comment, in_list_Path)
        print('\33[0m')

##############################################################################


class Print_list_bool:
    def __init__(self, comment='', in_list_Bool=[True]):
        print('\33[38;5;46m' + comment, in_list_Bool)
        print('\33[0m')

##############################################################################


class Print_array_str:
    def __init__(self, comment='', in_array_String=[['']]):
        import time
        time.sleep(0.1)
        print('\33[38;5;201m' + comment, '\n', in_array_String)
        print('\33[0m')

##############################################################################


class Print_array_int:
    def __init__(self, comment='', in_array_Int=[[0]]):
        print('\33[38;5;33m' + comment, '\n', in_array_Int)
        print('\33[0m')

##############################################################################


class Print_array_float:
    def __init__(self, comment='', in_array_Float=[[0.0]]):
        print('\33[38;5;208m' + comment, '\n', in_array_Float)
        print('\33[0m')

##############################################################################


class Print_array_path:
    def __init__(self, comment='', in_array_Path=[['path']]):
        print('\33[38;5;210m' + comment, '\n', in_array_Path)
        print('\33[0m')

##############################################################################


class Print_array_bool:
    def __init__(self, comment='', in_array_Bool=[[True]]):
        print('\33[38;5;46m' + comment, '\n', in_array_Bool)
        print('\33[0m')

##############################################################################


class Print_dict:
    def __init__(self, comment='', in_dict={}):
        print('\33[38;5;226m' + comment, '\n', in_dict)
        print('\33[0m')

##############################################################################


class Print_tuple:
    def __init__(self, comment='', in_tuple=('',)):
        print('\33[38;5;245m' + comment, '\n', in_tuple)
        print('\33[0m')

#############################################################################

class Print_type_var:
    def __init__(self, comment='', in_var=''):
        print(comment, type(in_var))

##############################################################################


class Print_str:
    def __init__(self, comment='', in_String=''):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[35m'+comment+in_String))

##############################################################################


class Print_int:
    def __init__(self, comment='', inInt=0):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[34m'+comment+str(inInt)))

##############################################################################


class Print_float:
    def __init__(self, comment='', inFloat=0.0):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[33m'+comment+str(inFloat)))

##############################################################################


class Print_path:
    def __init__(self, comment='', inPath='path'):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[91m'+comment+str(inPath)))

##############################################################################


class Print_bool:
    def __init__(self, comment='', inBool=True):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[92m'+comment+str(inBool)))

##############################################################################


class Print_list_str:
    def __init__(self, comment='', in_list_String=['']):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[35m'+comment+str(in_list_String)))

##############################################################################


class Print_list_int:
    def __init__(self, comment='', in_list_Int=[0]):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[34m'+comment+str(in_list_Int)))

##############################################################################


class Print_list_float:
    def __init__(self, comment='', in_list_Float=[0.0]):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[33m'+comment+str(in_list_Float)))

############################################################################


class Print_list_path:
    def __init__(self, comment='', in_list_Path=['path']):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[91m'+comment+str(in_list_Path)))

##############################################################################


class Print_list_bool:
    def __init__(self, comment='', in_list_Bool=[True]):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[92m'+comment+str(in_list_Bool)))

##############################################################################


class Print_array_str:
    def __init__(self, comment='', in_array_String=[['']]):
        import time
        time.sleep(0.1)
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[35m'+comment+str(in_array_String)))

##############################################################################


class Print_array_int:
    def __init__(self, comment='', in_array_Int=[[0]]):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[34m'+comment+str(in_array_Int)))

##############################################################################


class Print_array_float:
    def __init__(self, comment='', in_array_Float=[[0.0]]):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[33m'+comment+str(in_array_Float)))

##############################################################################


class Print_array_path:
    def __init__(self, comment='', in_array_Path=[['path']]):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[91m'+comment+str(in_array_Path)))

##############################################################################


class Print_array_bool:
    def __init__(self, comment='', in_array_Bool=[[True]]):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[92m'+comment+str(in_array_Bool)))
        
##############################################################################


class Print_dict:
    def __init__(self, comment='', in_dict={}):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[93m'+comment+str(in_dict)))
        
##############################################################################


class Print_list_dict:
    def __init__(self, comment='', in_list_dict=[{}]):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[93m'+comment+str(in_list_dict)))

##############################################################################


class Print_tuple:
    def __init__(self, comment='', in_tuple=('',)):
        from prompt_toolkit import print_formatted_text, ANSI
        print_formatted_text(ANSI('\x1b[98m'+comment+str(in_tuple)))

#############################################################################

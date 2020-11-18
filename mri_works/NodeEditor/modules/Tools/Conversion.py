class FloatToInt_simple():
    def __init__(self, inFloat=0.0):
        self.outint = int(inFloat)

    def outInt(self: 'int'):
        return self.outint

###############################################################################


class FloatToInt_list():
    def __init__(self, listFloat=[0.0]):
        self.outlistint = [int(i) for i in listFloat]

    def outListInt(self: 'list_int'):
        return self.outlistint

###############################################################################


class FloatToInt_array():
    def __init__(self, arrayFloat=[[0.0]]):
        import numpy as np
        self.outarrayint = np.array(arrayFloat)
        self.outarrayint = self.outarrayint.astype(int)

    def outArrayInt(self: 'array_int'):
        return self.outarrayint

###############################################################################


class IntToFloat_simple():
    def __init__(self, inInt=0):
        self.outfloat = float(inInt)

    def outFloat(self: 'float'):
        return self.outfloat

###############################################################################


class IntToFloat_list():
    def __init__(self, listInt=[0]):
        self.outlistfloat = [float(i) for i in listInt]

    def outListFloat(self: 'list_float'):
        return self.outlistfloat

###############################################################################


class IntToFloat_array():
    def __init__(self, arrayInt=[[0]]):
        import numpy as np
        self.outarrayfloat = np.array(arrayInt)
        self.outarrayfloat = self.outarrayfloat.astype(float)

    def outArrayFloat(self: 'array_float'):
        return self.outarrayfloat

###############################################################################


class StringToFloat_array():
    def __init__(self, arrayStr=[['']]):
        import numpy as np
        arrayStr = np.array(arrayStr)
        self.outarrayfloat = arrayStr.astype(np.float)

    def outArrayFloat(self: 'array_float'):
        return self.outarrayfloat

###############################################################################


class PathToString():
    def __init__(self, inPath='path'):
        self.outStr = str(inPath)

    def outString(self: 'str'):
        return self.outStr

###############################################################################


class IntToString():
    def __init__(self, inInt=0):
        self.outStr = str(inInt)

    def outString(self: 'str'):
        return self.outStr

###############################################################################


class FloatToString():
    def __init__(self, inFloat=0.0):
        self.outStr = str(inFloat)

    def outString(self: 'str'):
        return self.outStr

###############################################################################


class StringToEval():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        listType = ['float',
                    'int',
                    'str',
                    'bool',
                    'path',
                    'listfloat',
                    'listint',
                    'liststr',
                    'listbool',
                    'listpath',
                    'arrayfloat',
                    'arrayint',
                    'arraystr',
                    'arraybool',
                    'arraypath']
        self.listVar = []
        for i in range(0, len(listType)):
            self.listVar.append(None)
        typ, val = DefineTypeVariable(inString).returntype()
        ind = listType.index(typ)
        self.listVar[ind] = val

    def Float(self: 'float'):
        return self.listVar[0]

    def Int(self: 'int'):
        return self.listVar[1]

    def String(self: 'str'):
        return self.listVar[2]

    def Boolean(self: 'bool'):
        return self.listVar[3]

    def Path(self: 'path'):
        return self.listVar[4]

    def List_Float(self: 'list_float'):
        return self.listVar[5]

    def List_Int(self: 'list_int'):
        return self.listVar[6]

    def List_String(self: 'list_str'):
        return self.listVar[7]

    def List_Boolean(self: 'list_bool'):
        return self.listVar[8]

    def List_Path(self: 'list_path'):
        return self.listVar[9]

    def Array_Float(self: 'array_float'):
        return self.listVar[10]

    def Array_Int(self: 'array_int'):
        return self.listVar[11]

    def Array_String(self: 'array_str'):
        return self.listVar[12]

    def Array_Boolean(self: 'array_bool'):
        return self.listVar[13]

    def Array_Path(self: 'array_path'):
        return self.listVar[14]

###############################################################################


class StringToFloat():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if typ == 'float':
            self.outval = val
        else:
            self.outval = None

    def outFloat(self: 'float'):
        return self.outval

###############################################################################


class StringToListFloat():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if typ == 'listfloat':
            self.outval = val
        else:
            self.outval = None

    def outListFloat(self: 'list_float'):
        return self.outval

###############################################################################


class StringToArrayFloat():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if typ == 'arrayfloat':
            self.outval = val
        else:
            self.outval = None

    def outArrayFloat(self: 'array_float'):
        return self.outval

###############################################################################


class StringToInt():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if typ == 'int':
            self.outval = val
        else:
            self.outval = None

    def outInt(self: 'int'):
        return self.outval

###############################################################################


class StringToListInt():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if typ == 'listint':
            self.outval = val
        else:
            self.outval = None

    def outInt(self: 'list_int'):
        return self.outval

###############################################################################


class StringToArrayInt():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if typ == 'arrayint':
            self.outval = val
        else:
            self.outval = None

    def outInt(self: 'array_int'):
        return self.outval

###############################################################################


class StringToBoolean():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if typ == 'bool':
            self.outval = val
        else:
            self.outval = None

    def outBool(self: 'bool'):
        return self.outval

###############################################################################


class StringToListBoolean():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if typ == 'listbool':
            self.outval = val
        else:
            self.outval = None

    def outListBool(self: 'list_bool'):
        return self.outval

###############################################################################


class StringToArrayBoolean():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if typ == 'arraybool':
            self.outval = val
        else:
            self.outval = None

    def outArrayBool(self: 'array_bool'):
        return self.outval

###############################################################################


class StringToPath():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if typ == 'path':
            self.outval = val
        else:
            self.outval = None

    def outPath(self: 'path'):
        return self.outval

###############################################################################


class StringToListPath():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if typ == 'listpath':
            self.outval = val
        else:
            self.outval = None

    def outPath(self: 'list_path'):
        return self.outval

###############################################################################


class StringToArrayPath():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if typ == 'arraypath':
            self.outval = val
        else:
            self.outval = None

    def outPath(self: 'array_path'):
        return self.outval
    
###############################################################################


class ListStringToListInt():
    def __init__(self, ListString=['']):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(ListString).returntype()
        print(typ,val)
        if typ == 'liststr':
            self.outval=[]
            for el in ListString:
                self.outval.append(int(el))
        else:
            self.outval = None

    def outPath(self: 'list_int'):
        return self.outval

###############################################################################


class StringToDict():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if typ == 'dict':
            self.outval = val
        else:
            self.outval = None

    def outInt(self: 'dict'):
        return self.outval
    
###############################################################################


class StringToTuple():
    def __init__(self, inString=''):
        from NodeEditor.modules.sources.DefineTypeVariable import DefineTypeVariable
        typ, val = DefineTypeVariable(inString).returntype()
        if 'tuple' in typ:
            self.outval = val
        else:
            self.outval = None

    def outInt(self: 'tuple'):
        return self.outval

###############################################################################


class CSVToList():
    def __init__(self, input_CSV=''):
        import csv
        reader = csv.reader(input_csv, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:  # each row is a list
            self.output.append(row)

    def out_array(self: 'array_float'):
        return self.output

###############################################################################

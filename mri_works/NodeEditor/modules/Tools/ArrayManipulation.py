class getColumm():
    def __init__(self, input_array2D=[[0.0]], index=0):
        self.output = input_array2D[:, index]

    def outColumn(self: 'list_float'):
        return self.output

#############################################################################


class arrayIndex():
    def __init__(self, inArray=[[0.0]], index3=0, index4=0, index5=0):
        if len(inArray.shape) == 3:
            self.outArray = inArray[:, :, index3]

        if len(inArray.shape) == 4:
            self.outArray = inArray[:, :, index3, index4]

        if len(inArray.shape) == 5:
            self.outArray = inArray[:, :, index3, index4, index5]

    def outArray(self: 'array_float'):
        return self.outArray

#############################################################################


class arrayIndex2():
    def __init__(self, inArray=[[0.0]], index=0):
        self.outList = inArray[index]

    def outList(self: 'list_float'):
        return self.outList

#############################################################################


class createListString():
    def __init__(self, elem1='', elem2=''):
        elem = []
        elem.append(elem1)
        elem.append(elem2)
        self.elem1 = elem.copy()

    def out1(self: 'list_str'):
        return self.elem1

#############################################################################


class addElementListString():
    def __init__(self, listIn=[''], element=''):
        self.elem2 = listIn.copy()
        self.elem2.append(element)

    def out2(self: 'list_str'):
        return self.elem2

#############################################################################


class concatenateList_dyn():
    def __init__(self, list=[0.0], list_0=[0.0], **dynamicsInputs):
        self.listConcat = [list, list_0]
        for di in dynamicsInputs:
            self.listConcat.append(dynamicsInputs[di])

    def list_concat(self: 'array_float'):
        return self.listConcat

#############################################################################


class NlargestInArray():
    def __init__(self, in_array=[[0.0]], n=2):
        import numpy as np
        self.result_list = -np.sort(-in_array, axis=None)[0:n]

    def listMax(self: 'list_float'):
        return self.result_list

#############################################################################


class NsmallestInArray():
    def __init__(self, in_array=[[0.0]], n=2):
        import numpy as np
        self.result_list = np.sort(in_array, axis=None)[0:n]

    def listMin(self: 'list_float'):
        return self.result_list

#############################################################################


class indexListofString():
    def __init__(self, in_array_str=[''], n=0):
        self.out = in_array_str[n]

    def outString(self: 'str'):
        return self.out

#############################################################################


class build_array_float_dyn():
    def __init__(self, in_list=[0.0], in_list_0=[0.0], **dynamicsInputs):
        self.out = [in_list, in_list_0]
        for di in dynamicsInputs:
            self.out.append(dynamicsInputs[di])

    def array(self: 'array_float'):
        return self.out

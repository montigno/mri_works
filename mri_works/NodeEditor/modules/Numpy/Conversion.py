class nd_to_list():
    def __init__(self, ndarray_list=[0.0]):
        self.out = list(ndarray_list)

    def outList(self: 'list_float'):
        return self.out

##############################################################################


class strTofloat_Array():
    def __init__(self, list_str=['']):
        import numpy as np
        x = np.array(list_str)
        self.output = x.astype(np.float)

    def outArray(self: 'array_float'):
        return self.output

##############################################################################


class listFloat_to_ndArray():
    def __init__(self, list_float=[0.0]):
        import numpy as np
        self.output = np.array(list_float)

    def outArray(self: 'list_float'):
        return self.output

##############################################################################


class listFloat_to_Array():
    def __init__(self, list_float=[0.0], x=0, y=0):
        import numpy as np
        self.output = np.reshape(list_float, (x, y))

    def outArray(self: 'array_float'):
        return self.output

##############################################################################


class flatten():
    def __init__(self,
                 array_in=[[0.0]],
                 order="enumerate(('C', 'F', 'A', 'K'))"):
        import numpy as np
        a = np.array(array_in)
        self.output = a.flatten(order)

    def outArray(self: 'list_float'):
        return self.output

##############################################################################


class ravel():
    def __init__(self,
                 array_in=[[0.0]],
                 order="enumerate(('C','F', 'A', 'K'))"):
        import numpy as np
        a = np.array(array_in)
        self.output = a.ravel(order)

    def outArray(self: 'list_float'):
        return self.output

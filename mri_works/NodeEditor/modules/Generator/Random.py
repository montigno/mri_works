class Array_random():
    def __init__(self, row=10, col=10):
        import numpy as np
        self.randout = np.random.rand(row, col).tolist()

    def rand_out(self: 'array_float'):
        return self.randout

##########################################################


class List_random():
    def __init__(self, n=10):
        import numpy as np
        self.randout = np.random.rand(1, n)[0].tolist()

    def rand_out(self: 'list_float'):
        return self.randout

##########################################################


class Simple_random():
    def __init__(self):
        import numpy as np
        self.randout = np.random.rand(1, 1)[0][0]

    def rand_out(self: 'float'):
        return self.randout

##########################################################


class Array_3D_random():
    def __init__(self, row=10, col=10, slice=10):
        import numpy as np
        self.randout = np.random.rand(row, col, slice).tolist()

    def rand_out(self: 'array_float'):
        return self.randout

##########################################################


class Array_4D_random():
    def __init__(self, row=10, col=10, slice=10, temporal=10):
        import numpy as np
        self.randout = np.random.rand(row, col, slice, temporal).tolist()

    def rand_out(self: 'array_float'):
        return self.randout

##########################################################


class Array_5D_random():
    def __init__(self, row=10, col=10, slice=10, temporal=10, canal=10):
        import numpy as np
        self.randout = np.random.rand(row, col, slice, temporal, canal).tolist()

    def rand_out(self: 'array_float'):
        return self.randout

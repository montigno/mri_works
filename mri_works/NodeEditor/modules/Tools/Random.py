class Array_random():
    def __init__(self, row=10, col=10):
        import numpy as np
        self.randout = np.random.rand(row, col)

    def rand_out(self: 'array_float'):
        return self.randout

##########################################################


class List_random():
    def __init__(self, n=10):
        import numpy as np
        self.randout = np.random.rand(1, n)[0]

    def rand_out(self: 'list_float'):
        return self.randout

##########################################################


class Simple_random():
    def __init__(self):
        import numpy as np
        self.randout = np.random.rand(1, 1)[0][0]

    def rand_out(self: 'float'):
        return self.randout

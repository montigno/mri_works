class numpy_abs():
    def __init__(self, y=[0.0]):
        import numpy as np
        self.abs = np.absolute(y)

    def abs(self: 'list_float'):
        return self.abs

##############################################################################


class numpy_exponential():
    def __init__(self, y=[0.0]):
        import numpy as np
        self.exp = np.exp(y)

    def exp(self: 'list_float'):
        return self.exp

##############################################################################


class numpy_RMS():
    def __init__(self, y=[0.0]):
        import numpy as np
        y = np.array(y)
        self.rms = np.sqrt(np.mean(y ** 2))

    def rms(self: 'float'):
        return self.rms

##############################################################################


class numpy_std():
    def __init__(self, y=[0.0]):
        import numpy as np
        self.std = np.std(y)

    def rms(self: 'float'):
        return self.std

##############################################################################


class numpy_mean_array():
    def __init__(self, y=[[0.0]]):
        import numpy as np
        self.mean = np.mean(y)

    def rms(self: 'float'):
        return self.mean

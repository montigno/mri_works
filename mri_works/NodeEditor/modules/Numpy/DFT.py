class numpy_fft_1d():
    def __init__(self, data=[0.0]):
        import numpy as np
        self.out = np.fft.fft(data)

    def fft_1d(self: 'list_float'):
        return self.out

###############################################################################


class numpy_fft_freq():
    def __init__(self, n=0, d=1.0):
        import numpy as np
        self.out = np.fft.fftfreq(n, d)

    def fft_freq(self: 'list_float'):
        return self.out

###############################################################################


class numpy_fft_shift():
    def __init__(self, array_like=[[0.0]]):
        import numpy as np
        self.out = np.fft.fftshift(array_like)

    def fft_shift(self: 'array_float'):
        return self.out

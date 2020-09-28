class fft_scipy():
    def __init__(self, x=[0.0]):
        from scipy import fft
        self.y = fft(x)

    def fft(self: 'list_float'):
        return self.y

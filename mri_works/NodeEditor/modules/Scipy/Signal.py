class Convolve2d():
    def __init__(self, image=[[0.0]], kern=[[0.0]], **options):
        from scipy import signal
        import numpy as np
        img = np.array(image)
        dim = len(image.shape)
        if dim == 3:
            tmp = signal.convolve2d(img[:, :, 0], kern, **options)
            self.img = np.zeros((tmp.shape[0], tmp.shape[1], image.shape[2]))
            for sl1 in range(image.shape[2]):
                self.img[:, :, sl1] = signal.convolve2d(img[:, :, sl1], kern, **options)
        if dim == 4:
            tmp = signal.convolve2d(img[:, :, 0, 0], kern, **options)
            self.img = np.zeros((tmp.shape[0], tmp.shape[1], image.shape[2], image.shape[3]))
            for sl1 in range(image.shape[2]):
                for sl2 in range(image.shape[3]):
                    self.img[:, :, sl1, sl2] = signal.convolve2d(img[:, :, sl1, sl2], kern, **options)
        if dim == 5:
            tmp = signal.convolve2d(img[:, :, 0, 0, 0], kern, **options)
            self.img = np.zeros((tmp.shape[0], tmp.shape[1], image.shape[2], image.shape[3], image.shape[4]))
            for sl1 in range(image.shape[2]):
                for sl2 in range(image.shape[3]):
                    for sl3 in range(image.shape[4]):
                        self.img[:, :, sl1, sl2, sl3] = signal.convolve2d(img[:, :, sl1, sl2, sl3], kern, **options)

    def Convol2d(self: 'array_float'):
        return self.img

##############################################################################

class Convolve3d():
    def __init__(self, image=[[0.0]], kern=[0.0]):
        import numpy as np
        from scipy import ndimage
        img = np.array(image)
        k1 = kern #the kernel along the 1nd dimension
        k2 = k1 #the kernel along the 2nd dimension
        k3 = k1 #the kernel along the 3nd dimension

        # Convolve over all three axes in a for loop
        out = img.copy()
        for i, k in enumerate((k1, k2, k3)):
            out = ndimage.convolve1d(out, k, axis=i)
    
        self.img = out
    
    def Convol3d(self: 'array_float'):
        return self.img
    
    

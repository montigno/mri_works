class CannyEdge_Filter():
    def __init__(self, image=[[0.0]], sigma=3):
        from skimage import feature
        import numpy as np
        self.img = np.array(image)
        dim = len(image.shape)
        if dim == 3:
            for sl1 in range(image.shape[2]):
                self.img[:, :, sl1] = feature.canny(self.img[:, :, sl1], sigma)
        if dim == 4:
            for sl1 in range(image.shape[2]):
                for sl2 in range(image.shape[3]):
                    self.img[:, :, sl1, sl2] = feature.canny(self.img[:, :, sl1, sl2], sigma)
        if dim == 5:
            for sl1 in range(image.shape[2]):
                for sl2 in range(image.shape[3]):
                    for sl3 in range(image.shape[4]):
                        self.img[:, :, sl1, sl2, sl3] = feature.canny(self.img[:, :, sl1, sl2, sl3], sigma)

    def CannyEdge(self: 'array_float'):
        return self.img

#####################################################################


class Gaussian_Filter():

    def __init__(self, image=[[0.0]], tau=1):
        from scipy import ndimage as ndi
        import numpy as np
        self.img = np.array(image)
        dim = len(image.shape)
        if dim == 3:
            for sl1 in range(image.shape[2]):
                self.img[:, :, sl1] = ndi.gaussian_filter(self.img[:, :, sl1].copy(), tau)
        if dim == 4:
            for sl1 in range(image.shape[2]):
                for sl2 in range(image.shape[3]):
                    self.img[:, :, sl1, sl2] = ndi.gaussian_filter(self.img[:, :, sl1, sl2].copy(), tau)
        if dim == 5:
            for sl1 in range(image.shape[2]):
                for sl2 in range(image.shape[3]):
                    for sl3 in range(image.shape[4]):
                        self.img[:, :, sl1, sl2, sl3] = ndi.gaussian_filter(self.img[:, :, sl1, sl2, sl3].copy(), tau)

    def Gaussian(self: 'array_float'):
        return self.img

#####################################################################


class Laplacian_Filter():

    def __init__(self, image=[[0.0]]):
        from scipy import signal, misc
        import numpy as np
        self.img = np.array(image)
        dim = len(image.shape)
        derfilt = np.array([1.0, -2, 1.0], dtype=np.float32)
        if dim == 3:
            for sl1 in range(image.shape[2]):
                ck = signal.cspline2d(self.img[:, :, sl1].copy(), 8.0)
                self.img[:, :, sl1] = (signal.sepfir2d(ck, derfilt, [1]) + signal.sepfir2d(ck, [1], derfilt))
        if dim == 4:
            for sl1 in range(image.shape[2]):
                for sl2 in range(image.shape[3]):
                    ck = signal.cspline2d(self.img[:, :, sl1, sl2].copy(), 8.0)
                    self.img[:, :, sl1, sl2] = (signal.sepfir2d(ck, derfilt, [1]) + signal.sepfir2d(ck, [1], derfilt))
        if dim == 5:
            for sl1 in range(image.shape[2]):
                for sl2 in range(image.shape[3]):
                    for sl3 in range(image.shape[4]):
                        ck = signal.cspline2d(self.img[:, :, sl1, sl2, sl3].copy(), 8.0)
                        self.img[:, :, sl1, sl2, sl3] = (signal.sepfir2d(ck, derfilt, [1]) + signal.sepfir2d(ck, [1], derfilt))

    def Laplacian(self: 'array_float'):
        return self.img

class binary_opening:
    def __init__(self, image=[[0]], **options):
        from scipy import ndimage
        import numpy as np
        self.img_op = ndimage.binary_opening(np.array(image), **options)
        
    def image_opening(self:'array_float'):
        return self.img_op

###############################################################################

class binary_closing:
    def __init__(self, image=[[0]], **options):
        from scipy import ndimage
        import numpy as np
        self.img_cl = ndimage.binary_closing(np.array(image), **options)
        
    def image_closing(self:'array_float'):
        return self.img_cl
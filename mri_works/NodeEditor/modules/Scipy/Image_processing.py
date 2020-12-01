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
    
###############################################################################

class binary_propagation:
    def __init__(self, image=[[0]], **options):
        from scipy import ndimage
        import numpy as np
        self.img_pr = ndimage.binary_propagation(np.array(image), **options)
        
    def image_propagation(self:'array_float'):
        return self.img_pr
    
###############################################################################

class binary_fill_holes:
    def __init__(self, image=[[0]], **options):
        from scipy import ndimage
        import numpy as np
        self.img_fh = ndimage.binary_fill_holes(np.array(image), **options)
        
    def image_holes_filled(self:'array_float'):
        return self.img_fh

from h5py.h5t import np
class remove_small_holes:
    def __init__(self, image=[[0.0]], area_threshold=64, **options):
        from skimage import morphology
        import numpy as np
        self.a = np.array(image, dtype=bool)
        for sl1 in range(self.a.shape[2]):
                self.a[:, :, sl1] = morphology.remove_small_holes(self.a[:, :, sl1], area_threshold, connectivity=connectivity, in_place=in_place)
       
    def image_cln(self:'array_float'):
        return np.array(self.a, dtype=float)
    
###########################################################

class remove_small_objects:
    def __init__(self, image=[[0.0]], min_size=64, **options):
        from skimage import morphology
        import numpy as np
        self.a = np.array(image, dtype=bool)
        for sl1 in range(self.a.shape[2]):
                self.a[:, :, sl1] = morphology.remove_small_objects(self.a[:, :, sl1], min_size, **options)
       
    def image_cln(self:'array_float'):
        return np.array(self.a, dtype=float)
    
###########################################################

class skimage_ball:
    def __init__(self, radius=1):
        from skimage.morphology import ball
        self.ball = ball(radius)
        
    def sk_ball(self:'array_float'):
        return self.ball

###########################################################

class skimage_erosion:
    def __init__(self, image=[[0.0]], **options):
        from skimage.morphology import erosion
        import numpy as np
        self.eroded = erosion(np.array(image), **options)
        
    def sk_erosion(self:'array_float'):
        return self.eroded
    
###########################################################

class skimage_dilation:
    def __init__(self, image=[[0.0]], **options):
        from skimage.morphology import dilation
        import numpy as np
        self.dilated = dilation(np.array(image), **options)
        
    def sk_dilation(self:'array_float'):
        return self.dilated
        
###########################################################

class skimage_white_tophat:
    def __init__(self, image=[[0.0]], **options):
        from skimage.morphology import white_tophat
        import numpy as np
        self.wt = white_tophat(np.array(image), **options)
        
    def sk_white_tophat(self:'array_float'):
        return self.wt
    
###########################################################

class skimage_black_tophat:
    def __init__(self, image=[[0.0]], **options):
        from skimage.morphology import black_tophat
        import numpy as np
        self.bt = black_tophat(np.array(image), **options)
        
    def sk_black_tophat(self:'array_float'):
        return self.bt

###########################################################

class skimage_opening:
    def __init__(self, image=[[0.0]], **options):
        from skimage.morphology import opening
        import numpy as np
        self.op = opening(np.array(image), **options)
        
    def sk_opening(self:'array_float'):
        return self.op

###########################################################

class skimage_closing:
    def __init__(self, image=[[0.0]], **options):
        from skimage.morphology import closing
        import numpy as np
        self.cl = closing(np.array(image), **options)
        
    def sk_closing(self:'array_float'):
        return self.cl

###########################################################

class skimage_convex_hull_image:
    def __init__(self, image=[[0.0]], **options):
        from skimage.morphology import convex_hull_image
        import numpy as np
        self.ch = convex_hull_image(image, **options)
        
    def sk_convex(self:'array_bool'):
        return self.ch
        
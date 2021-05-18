class active_contour():
    def __init__(self, image=[[0.0]], snake=[[0.0]], **options):
        from skimage.segmentation import active_contour
        self.a = active_contour(image, snake, **options)
        
    def act_contour(self: 'array_float'):
        return self.a
    
##############################################################################


class ants_get_mask():
    def __init__(self, ants_image=[[0.0]], **options):
        import ants
        self.mask = ants.get_mask(ants_image, **options)
        
    def ants_mask(self:'array_float'):
        return self.mask
    
##############################################################################

class ants_mask_image():
    def __init__(self, ants_image=[[0.0]], mask=[[0.0]], level=1, **options):
        import ants
        self.masking = ants.mask_image(ants_image, mask, level, **options)
        
    def ants_masked(self:'array_float'):
        return self.masking
    
##############################################################################

class ants_n4_bias_field_correction():
    def __init__(self, ants_image=[[0.0]], **options):
        import ants
        self.n4bias = ants.n4_bias_field_correction(ants_image, **options)

    def ants_n4_correction(self:'array_float'):
        return self.n4bias
    
    
    
    
class ants_image_read():
    def __init__(self, filename='path', **options):
        import ants
        self.antsimg = ants.image_read(filename, **options)
        
    def ants_image(self:'array_float'):
        return self.antsimg
    
##############################################################################

class ants_image_write():
    def __init__(self, ants_image=[[0.0]], filename='path'):
        import ants
        self.img = filename
        ants.image_write(ants_image, filename)
        
    def outfile_image(self:'path'):
        return self.img
    
##############################################################################

class ants_set_spacing():
    def __init__(self, ants_image=[[0.0]], new_spacing=(2,2,2)):
        import ants
        ants.set_spacing(ants_image, new_spacing)
        self.antsimg = ants_image

    def ants_image_spacing(self:'array_float'):
        return self.antsimg

class ants_image_read():
    def __init__(self, filename='path', **options):
        import ants
        self.antsimg = ants.image_read(filename, **options)
        
    def ants_image(self:'array_float'):
        return self.antsimg
    
##############################################################################

class ants_image_write():
    def __init__(self, ants_image=[[0.0]], filename='path', **options):
        import ants
        self.img = filename
        ants.image_write(ants_image, filename, **options)
        
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

##############################################################################
    
class ants_read_transform:
    def __init__(self, filename='path', **options):
        import ants
        self.tx = ants.read_transform(filename, **options)
        
    def ants_transform(self:'array_float'):
        return self.tx

##############################################################################

class ants_write_transform:
    def __init__(self, ants_transform=[[0.0]], filename='path'):
        import ants
        ants.write_transform(ants_transform, filename)
        self.tx = filename
        
    def ants_file_transf(self:'path'):
        return self.tx

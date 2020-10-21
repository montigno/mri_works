class concat_Nifti:
    def __init__(self, filenames=['path']):
        import nibabel.funcs as nb
        img_conc = nb.concat_images(filenames, check_affines=False, axis=None)
        self.img = img_conc.get_fdata()
        self.header = img_conc.header

    def concat_img(self: 'array_float'):
        return self.img

    def header_img(self: 'str'):
        return self.header

##############################################################################


class resize_Nifti:
    def __init__(self, file_in='path', file_out_name= 'path', new_size=[128,128,9]):
        import numpy as np
        import nibabel as nib
        import itertools
        img = nib.load(file_in).get_fdata()
        delta_x = img.shape[0]/new_size[0]
        delta_y = img.shape[1]/new_size[1]
        delta_z = img.shape[2]/new_size[2]
        new_data = np.zeros((new_size[0],new_size[1],new_size[2]))
        for x, y, z in itertools.product(range(new_size[0]),
                                         range(new_size[1]),
                                         range(new_size[2])):
            new_data[x][y][z] = img[int(x*delta_x)][int(y*delta_y)][int(z*delta_z)]
        self.img = nib.Nifti1Image(new_data, np.eye(4))
        self.img.to_filename(file_out_name)
        
        
    def out_file(self:'path'):
        return self.img
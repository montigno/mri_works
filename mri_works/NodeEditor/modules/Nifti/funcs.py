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
        img = nib.Nifti1Image(new_data, np.eye(4))
        img.to_filename(file_out_name)
        self.img = file_out_name
        
    def out_file(self:'path'):
        return self.img
    
##############################################################################

class resample_nifti:
    def __init__(self, file_in='path', file_out_name= 'path', voxel_size=[2,2,2]):
        import nibabel
        import nibabel.processing

        input_path = r'/input/path/input_img.nii.gz'
        output_path = r'/output/path/output_img.nii.gz'

        input_img = nibabel.load(file_in)
        resampled_img = nibabel.processing.resample_to_output(input_img, voxel_size)
        nibabel.save(resampled_img, file_out_name)
        self.img = file_out_name
        
    def out_file(self:'path'):
        return self.img

##############################################################################


class four_to_three:
    def __init__(self, image_nii_4D='path', out_directory='path'):
        import nibabel as nib
        import os
        imgs = nib.four_to_three(nib.load(image_nii_4D))
        tmp = os.path.basename(image_nii_4D)
        froot = ('.').join(tmp.split('.')[:-1])
        self.listimg=[]
        for i, img3d in enumerate(imgs):
            fname3d = '%s_%04d.nii' % (froot, i)
            nib.save(img3d, os.path.join(out_directory,fname3d))
            self.listimg.append(os.path.join(out_directory,fname3d))
            
        
    def list_3D_images(self:'list_path'):
        return self.listimg

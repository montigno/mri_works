class Seg_conv3D:
    def __init__(self, file_in='path', file_out_name='path', threshold=5.0, radius=9):
        from NodeEditor.modules.Nifti.Nifti import Open_Nifti
        from NodeEditor.modules.Nifti.Info_Nifti import Nifti_header
        from NodeEditor.modules.Scipy.Signal import Convolve3d
        from NodeEditor.modules.Numpy.Image_filters import Image_threshold
        from NodeEditor.modules.File_IO.Save_image_nii_gz import Save_Nifti_header
        from skimage.morphology import erosion
        from skimage.morphology import dilation
        from skimage.morphology import ball
        from scipy import ndimage
        import numpy as np
        
        image = Open_Nifti(file_in).image()
        kern=[1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]
        img = Convolve3d(image, kern).Convol3d()
        img = -img
        img = Image_threshold(img, threshold, 'high').img_threshold()
        selem = ball(radius)
        img = erosion(img, selem)
        img = dilation(img, selem)
        img = ndimage.binary_fill_holes(img, structure=np.ones((3,3,1)))
        img = np.multiply(image, img)
        hdr = Nifti_header(file_in).nii_hdr()
        self.out_file = Save_Nifti_header(img, file_out_name, hdr, 'nii').pathFile()
        
    def output_file(self:'path'):
        return self.out_file

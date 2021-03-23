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
        
        
        img = Open_Nifti(file_in).image()
        if len(img.shape) < 4:
            image = img
        else:
            image = img[:, :, :, 0]
        kern=[1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 1.0]
        imgtmp = Convolve3d(image, kern).Convol3d()
        imgtmp = -imgtmp
        imgtmp = Image_threshold(imgtmp, threshold, 'high').img_threshold()
        selem = ball(radius)
        imgtmp = erosion(imgtmp, selem)
        imgtmp = dilation(imgtmp, selem)
        imgtmp = ndimage.binary_fill_holes(imgtmp, structure=np.ones((3,3,1)))
        if len(img.shape) < 4:
            imgtmp = np.multiply(image, imgtmp)
        else:
            for i in range(img.shape[3]):
                img[:, :, :, i] = np.multiply(img[:, :, :, i], imgtmp)
            imgtmp = img
        hdr = Nifti_header(file_in).nii_hdr()
        self.out_file = Save_Nifti_header(imgtmp, file_out_name, hdr, 'nii').pathFile()
        
    def output_file(self:'path'):
        return self.out_file

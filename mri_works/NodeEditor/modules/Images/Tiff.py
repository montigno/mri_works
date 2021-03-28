from scipy.integrate._test_odeint_banded import getbands
class Open_TIFF:
    def __init__(self, file_tiff='path'):
        from PIL import Image
        import numpy as np
        img = Image.open(file_tiff)
        nb = img.n_frames
        self.imarray = []
        for i in range(nb):
            img.seek(i)
            self.imarray.append(np.array(img))
        self.imarray = np.array(self.imarray)
        self.imarray = self.imarray.transpose(2,1,0)
        
    def out_tiff(self:'array_float'):
        return self.imarray
    
###############################################################################


class tif_to_nii:
    def __init__(self, Tif_file='path', output_nii='path', pixdim=[0.025, 0.025, 0.05] ):
        from PIL import Image
        import nibabel as nib
        import numpy as np
        imgtif = Image.open(Tif_file)
        nb = imgtif.n_frames
        imgs = []
        for i in range(nb):
            imgtif.seek(i)
            img = np.asarray(imgtif).astype(np.float32).squeeze()
            imgs.append(img)
        img = np.stack(imgs)
        img = img.transpose(2,1,0)

        nib.Nifti1Image(img, None).to_filename(output_nii)
        hdr = nib.load(output_nii).header
        newpixdim = [1.0]
        newpixdim.extend(pixdim)
        newpixdim.extend([0.0, 0.0, 0.0, 0.0])
        hdr['pixdim'] = np.array(newpixdim)
        nib.Nifti1Image(img, None, header=hdr).to_filename(output_nii)
        self.out_nii = output_nii
        
    def output_nii(self:'path'):
        return self.out_nii
        
        
        
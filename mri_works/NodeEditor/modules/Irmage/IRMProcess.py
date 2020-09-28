##############################################################################

class find_t2():

    def __init__(self, nifti_image=['path'], tes=[0.0]):

        import nibabel as nb
        import scipy as sp
        import numpy as np
        import os

        data = np.log(np.array([nb.load(fn).get_data() for fn in nifti_image]))

        data[data < 0] = 0
        print("data shape : ", data.shape)

        tes = np.array(tes)
        x = np.concatenate((np.ones_like(tes[..., np.newaxis]),
                            -tes[..., np.newaxis]),
                           1)

        print("x shape : ", x.shape)

        beta, _, _, _, _ = sp.linalg.lstsq(x, data)

        s0_ = np.exp(beta[0])
        t2_ = 1. / beta[1]

        self.fn_s0 = os.path.abspath('s0.nii.gz')
        self.fn_t2 = os.path.abspath('t2.nii.gz')

        nb.save(nb.Nifti1Image(s0_,
                               nb.load(nifti_images[0]).get_affine()),
                fn_s0)
        nb.save(nb.Nifti1Image(t2_,
                               nb.load(nifti_images[0]).get_affine()),
                fn_t2)

    def outFile_magn(self: 'path'):
        return self.fn_s0

    def outFile_T2(self: 'path'):
        return self.fn_t2

##############################################################################

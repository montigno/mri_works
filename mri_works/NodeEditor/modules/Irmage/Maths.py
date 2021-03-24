class operation_Nifti_3Dby4D:
    def __init__(self, image4D='path', image3D='path',
                       operation="enumerate(('add','sub','mul','div'))",
                       file_output='path'):
        import nibabel as nib
        import numpy as np
        hdr = nib.load(image4D).header
        img = nib.load(image4D).get_fdata()
        img_op = nib.load(image3D).get_fdata()
        print(img.shape,img_op.shape)
        if operation in 'add':
            for i in range(img.shape[3]):
                img[:, :, :, i] = np.add(img[:, :, :, i], img_op)
        if operation in 'sub':
            for i in range(img.shape[3]):
                img[:, :, :, i] = np.sub(img[:, :, :, i], img_op)
        if operation in 'mul':
            for i in range(img.shape[3]):
                img[:, :, :, i] = np.multiply(img[:, :, :, i], img_op)
        if operation in 'div':
            for i in range(img.shape[3]):
                img[:, :, :, i] = np.divide(img[:, :, :, i], img_op)
        imgSave = nib.Nifti1Image(img, None, header=hdr)
        self.silesaved = file_output
        nib.save(imgSave, self.silesaved)
            
    def out_file(self:'path'):
        return self.silesaved
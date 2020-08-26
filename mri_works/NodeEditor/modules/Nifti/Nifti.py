##############################################################################

class Open_Nifti:
    def __init__(self,fileSource='path'):
        import os.path
        import nibabel as nib        
        self.fileSource=fileSource
        self.dim=0
        self.img=[[0.0]]
        if (os.path.splitext(fileSource)[1] =='.nii') or ('.nii.gz' in fileSource):
            img =  nib.load(fileSource)
            self.img = img.get_fdata()
            self.dim = len(img.shape)
            self.pxd = img.header._structarr['pixdim']
        else:
            print('no Nifti file')
    
    def image(self:'array_float'):
        return self.img
    
    def dim(self:'int'): 
        return self.dim
    
    def pixdim(self:'list_float'):
        return self.pxd
             
    def filePath(self:'path'):
        return self.fileSource
    
##############################################################################

class DisplayNifti:
    def __init__(self,image='path', title=''):
        from NodeEditor.modules.Nifti.sources.DispNifti import DispNifti
        Niftifile = Open_Nifti(image)
        pixdim = Niftifile.pixdim()[1:4]
        self.wid = DispNifti(Niftifile.image(), pixdim, title)
        self.wid.getDialog().exec_()
        
##############################################################################

class DisplayImage:
    def __init__(self,image=[[0.0]],title=''):
        from NodeEditor.modules.Nifti.sources.DispNifti import DispNifti
        self.wid = DispNifti(image,[1.0,1.0],title)
        self.wid.getDialog().exec_()
        
###############################################################################

class array_to_NumpyArray():
    def __init__(self, array_in=[[0.0]]):
        import numpy as np
        self.out_array=np.array(array_in)
        
    def out_array(self:'array_float'):
        return self.out_array
    
###############################################################################

class NumpyArray_to_array():
    def __init__(self, array_in=[[0.0]]):
        self.out_array=array_in.tolist()
        
    def out_array(self:'array_float'):
        return self.out_array
       

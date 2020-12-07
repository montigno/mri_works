class Save_NiiGz:
    def __init__(self, image=[[0.0]], filepath='path', **options):
        import nibabel as nib
        import numpy as np
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        if type(image).__name__ == 'list':
            image = np.array(image) 
        if filepath == 'path':
            self.fileSaved = filedialog.asksaveasfile(**options).name
        else:
            if '.nii.gz' in filepath:
                self.fileSaved = filepath
            elif '.nii' in filepath:
                self.fileSaved = filepath + '.gz'
            else:
                self.fileSaved = filepath + '.nii.gz'
        img = nib.Nifti1Image(image, np.eye(4))
        nib.save(img, self.fileSaved)

    def pathFile(self: 'path'):
        return self.fileSaved

##############################################################################


class Save_NiiGz_header:
    def __init__(self,
                 image=[[0.0]], filepath='path', new_header='', **options):
        import nibabel as nib
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        if type(image).__name__ == 'list':
            image = np.array(image) 
        if filepath == 'path':
            self.fileSaved = filedialog.asksaveasfile(**options).name
        else:
            if filepath.endswith('.nii.gz'):
                self.fileSaved = filepath
            elif filepath.endswith('.nii'):
                self.fileSaved = filepath + '.gz'
            else:
                self.fileSaved = filepath + '.nii.gz'
        img = nib.Nifti1Image(image, None, header=new_header)
        nib.save(img, self.fileSaved)

    def pathFile(self: 'path'):
        return self.fileSaved
    
    
##############################################################################

class Save_Nifti:
    def __init__(self, image=[[0.0]], filepath='path', out_type="enumerate(('nii','nii.gz'))", **options):
        import nibabel as nib
        import numpy as np
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        if type(image).__name__ == 'list':
            image = np.array(image) 
        if filepath == 'path':
            self.fileSaved = filedialog.asksaveasfile(**options).name
        else:
            if filepath.endswith('.nii') or filepath.endswith('.nii.gz'):
                self.fileSaved = filepath[0:filepath.index('.nii')] + '.' + out_type
            else:
                self.fileSaved = filepath + '.' + out_type
        img = nib.Nifti1Image(image, np.eye(4))
        nib.save(img, self.fileSaved)

    def pathFile(self: 'path'):
        return self.fileSaved
    
##############################################################################


class Save_Nifti_header:
    def __init__(self,
                 image=[[0.0]], filepath='path', new_header='', out_type="enumerate(('nii','nii.gz'))", **options):
        import nibabel as nib
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        if type(image).__name__ == 'list':
            image = np.array(image) 
        if filepath == 'path':
            self.fileSaved = filedialog.asksaveasfile(**options).name
        else:
            if filepath.endswith('.nii') or filepath.endswith('.nii.gz'):
                self.fileSaved = filepath[0:filepath.index('.nii')] + '.' + out_type
            else:
                self.fileSaved = filepath + '.' + out_type
        img = nib.Nifti1Image(image, None, header=new_header)
        nib.save(img, self.fileSaved)
        

    def pathFile(self: 'path'):
        return self.fileSaved
    
##############################################################################

class Create_gzip:
    def __init__(self, file_in='path', delete_file=False):
        import gzip
        import shutil
        import os
        self.out_gz = ''
        with open(file_in, 'rb') as f_in:
            with gzip.open(file_in+'.gz', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                self.out_gz = file_in+'.gz'
        if delete_file:
            try:
                os.remove(file_in)
            except OSError as e:
                print("Error : %s : %s" % (input_file, e.strerror))
    
    def out_file(self:'path'):
        return self.out_gz

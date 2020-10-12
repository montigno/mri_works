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
        print("file saved", self.fileSaved)
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
            if 'nii.gz' in filepath:
                self.fileSaved = filepath
            else:
                self.fileSaved = filepath + '.nii.gz'
        print("file saved", self.fileSaved)
        img = nib.Nifti1Image(image, None, header=new_header)
        nib.save(img, self.fileSaved)

    def pathFile(self: 'path'):
        return self.fileSaved

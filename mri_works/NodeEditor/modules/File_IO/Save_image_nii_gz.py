class Save_NiiGz:
    def __init__(self, image=[[0.0]], filepath='path', **options):
        import nibabel as nib
        from tkinter import filedialog

        if filepath is 'path':
            self.fileSaved = filedialog.asksaveasfile(**options).name
        else:
            if 'nii.gz' in filepath:
                self.fileSaved = filepath
            else:
                self.fileSaved = filepath + '.nii.gz'
        print("file saved", self.fileSaved)
        img = nib.Nifti1Image(image, np.eye(4))
        nib.save(img, self.fileSaved)

    def pathFile(self: 'path'):
        return self.fileSaved
    
##############################################################################

class Save_NiiGz_header:
    def __init__(self, image=[[0.0]], filepath='path', new_header='', **options):
        import nibabel as nib
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        if filepath is 'path':
            self.fileSaved = filedialog.asksaveasfile(**options).name
        else:
            if 'nii.gz' in filepath:
                self.fileSaved = filepath
            else:
                self.fileSaved = filepath + '.nii.gz'
        print("file saved", self.fileSaved)
        img = nib.Nifti1Image(image, None,header=new_header )
        nib.save(img, self.fileSaved)

    def pathFile(self: 'path'):
        return self.fileSaved

class ants_N4BiasFieldCorrection():
    def __init__(self, input_image='path', save_bias=False, copy_header=False, **options):
        from nipype.interfaces.ants import N4BiasFieldCorrection
        n4 = N4BiasFieldCorrection()
        n4.inputs.input_image = input_image
        n4.inputs.save_bias = save_bias
        n4.inputs.copy_header = copy_header
        for ef in options:
            setattr(n4.inputs, ef, options[ef])
        self.res = n4.run()
        
    def output_image(self:'path'):
        return self.res.outputs.output_image
    
    def bias_image(self:'path'):
        return self.res.outputs.bias_image


class fsl_FAST:
    def __init__(self, in_files=['path'], **options):
        from nipype.interfaces import fsl
        fastr = fsl.FAST()
        fastr.inputs.in_files = in_files
        for ef in options:
            setattr(fastr.inputs, ef, options[ef])
        self.res = fastr.run()
        
    def tissue_class_map(self:'path'): 
        return self.res.outputs.tissue_class_map
    
    def tissue_class_files(self:'list_path'):
        return self.res.outputs.tissue_class_files
    
    def restored_image(self:'list_path'):
        return self.res.outputs.restored_image
    
    def mixeltype(self:'path'):
        return self.res.outputs.mixeltype
    
    def partial_volume_map(self:'path'):
        return self.res.outputs.partial_volume_map
    
    def partial_volume_files(self:'list_path'):
        return self.res.outputs.partial_volume_files
    
    def bias_field(self:'list_path'):
        return self.res.outputs.bias_field
    
    def probability_maps(self:'list_path'):
        return self.res.outputs.probability_maps


class Print_Path:
    def __init__(self,comment='',inPath='path'):
        print('\033[92m' + comment, inPath)


class askopenfilename():
    def __init__(self,extension='*.*',title='choose your file'):
        import tkinter as tk
        from tkinter import filedialog
        root=tk.Tk()
        root.withdraw()
        self.filename = filedialog.askopenfilename(title=title,filetypes=[('', extension)])
        
    def filePath(self:'path'):
        return self.filename


class Print_list_Path:
    def __init__(self,comment='',in_list_Path=['path']):
        print('\033[92m' + comment, in_list_Path)



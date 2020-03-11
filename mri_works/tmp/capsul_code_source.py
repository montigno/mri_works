class fsl_UnaryMaths():
    def __init__(self,in_file='path',
                 operation="enumerate(('exp','log','sin','cos','tan','asin','acos','atan',"+
                            "'sqr','sqrt','recip','abs','bin','binv','fillh',"+
                            "'fillh26','index','edge','nan','nanm','rand',"+
                            "'randn','range'))",**options):
        from nipype.interfaces.fsl import UnaryMaths
        mf = UnaryMaths()
        mf.inputs.in_file=in_file
        mf.inputs.operation=operation
        for ef in options:
            setattr(mf.inputs,ef,options[ef])
        self.res=mf.run()  
    
    def out_file(self:'path'):
        return self.res.outputs.out_file


class MatPlotLib:
    def __init__(self,sourceFile='path', title='original',display_mode="enumerate(('ortho', 'x', 'y', 'z', 'yx', 'xz', 'yz'))", 
                                                dim=1,draw_cross=False,annotate=False):
        from nilearn import plotting
        plotting.plot_anat(sourceFile,title=title,display_mode=display_mode,dim=dim,draw_cross=draw_cross,annotate=annotate)
        plotting.show()


class askopenfilename():
    def __init__(self,extension='*.*',title='choose your file'):
        import tkinter as tk
        from tkinter import filedialog
        root=tk.Tk()
        root.withdraw()
        self.filename = filedialog.askopenfilename(title=title,filetypes=[('', extension)])
        
    def filePath(self:'path'):
        return self.filename



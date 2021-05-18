class nipy_FmriRealign4d():
    def __init__(self, in_file=['path'], tr=1.0, **options):
        from nipype.interfaces.nipy.preprocess import FmriRealign4d
        realigner = FmriRealign4d()
        realigner.inputs.in_file = in_file
        realigner.inputs.tr = tr
        for ef in options:
            setattr(realigner.inputs, ef, options[ef])
        self.res = realigner.run()
        
    def out_file(self:'list_path'):
        return self.res.outputs.out_file
    
    def par_file(self:'list_path'):
        return self.res.outputs.par_file

###############################################################################

class nipy_SpaceTimeRealigner():
    def __init__(self, in_file=['path'], **options):
        from nipype.interfaces.nipy.preprocess import SpaceTimeRealigner
        realigner = SpaceTimeRealigner()
        realigner.inputs.in_file = in_file
        for ef in options:
            setattr(realigner.inputs, ef, options[ef])
        self.res = realigner.run()
        
    def out_file(self:'list_path'):
        return self.res.outputs.out_file
    
    def par_file(self:'list_path'):
        return self.res.outputs.par_file
    
###############################################################################

class nipy_Trim():
    def __init__(self, in_file='path', **options):
        from nipype.interfaces.nipy.preprocess import Trim
        trim = Trim()
        trim.inputs.in_file = in_file
        for ef in options:
            setattr(trim.inputs, ef, options[ef])
        self.res = trim.run() 
        
    def out_file(self:'path'):
        return self.res.outputs.out_file

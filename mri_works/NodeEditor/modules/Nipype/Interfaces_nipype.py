class smoothing():
    def __init__(self, fwhm=[4, 8]):
        from nipype.interfaces.spm import Smooth
        from nipype import Workflow, Node
        smooth = Node(Smooth(), name="smooth")
        smooth.iterables = ("fwhm", fwhm)

##############################################################################

class SplitNifti():
    def __init__(self, in_file='path', **options):
        from nipype.interfaces.dcmstack import SplitNifti
        split = SplitNifti()
        split.inputs.in_file = in_file
        for ef in options:
            setattr(split.inputs, ef, options[ef])
        self.res = split.run()
        
    def out_list(self:'list_path'):
        return self.res.outputs.out_list
    
    
class fsl_Merge():
    def __init__(self, in_files=['path'],
                 dimension="enumerate(('t','x','y','z','a'))", **options):
        from nipype.interfaces.fsl import Merge
        fu = Merge()
        fu.inputs.in_files = in_files
        fu.inputs.dimension = dimension
        for ef in options:
            setattr(fu.inputs, ef, options[ef])
        self.res = fu.run()

    def merged_file(self: 'path'):
        return self.res.outputs.merged_file

##############################################################################


class fsl_Split():
    def __init__(self, in_file='path',
                 dimension="enumerate(('t','x','y','z'))", **options):
        from nipype.interfaces.fsl import Split
        fu = Split()
        fu.inputs.in_file = in_file
        fu.inputs.dimension = dimension
        for ef in options:
            setattr(fu.inputs, ef, options[ef])
        self.res = fu.run()

    def out_files(self: 'path'):
        return self.res.outputs.out_files

##############################################################################


class fsl_SwapDimensions():
    def __init__(self, in_file='path', new_dims=('x', 'y', 'z'), **options):
        from nipype.interfaces.fsl import SwapDimensions
        fu = SwapDimensions()
        fu.inputs.in_file = in_file
        fu.inputs.new_dims = new_dims
        for ef in options:
            setattr(fu.inputs, ef, options[ef])
        self.res = fu.run()

    def out_file(self: 'path'):
        return self.res.outputs.out_file

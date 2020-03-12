class image_Reorient():
    def __init__(self, in_file='path', **options):
        import numpy as np
        from nipype.interfaces.image import Reorient
        reorient = Reorient()
        reorient.inputs.in_file = in_file
        for ef in options:
            setattr(reorient.inputs, ef, options[ef])
        self.res = reorient.run()

    def out_file(self: 'path'):
        return self.res.outputs.out_file

    def transform(self: 'path'):
        return self.res.outputs.transform

##############################################################################


class image_Rescale():
    def __init__(self, in_file='path', ref_file='path', **options):
        from nipype.interfaces.image import Rescale
        invert_t1w = Rescale(invert=True)
        invert_t1w.inputs.in_file = in_file
        invert_t1w.inputs.ref_file = ref_file
        for ef in options:
            setattr(invert_t1w.inputs, ef, options[ef])
        self.res = invert_t1w.run()

    def out_file(self: 'path'):
        return self.res.outputs.out_file

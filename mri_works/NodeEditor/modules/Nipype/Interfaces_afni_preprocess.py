class afni_Seg():
    def __init__(self, in_file='path', mask='AUTO', **options):
        from nipype.interfaces.afni import preprocess
        seg = preprocess.Seg()
        seg.inputs.in_file = in_file
        seg.inputs.mask = mask
        for ef in options:
            setattr(seg.inputs, ef, options[ef])
        self.res = seg.run()

    def out_file(self: 'path'):
        return self.res.outputs.out_file

##############################################################################

class afni_SkullStrip():
    def __init__(self, in_file='path', **options):
        from nipype.interfaces import afni as afni
        skullstrip = afni.SkullStrip()
        skullstrip.inputs.in_file = in_file
        for ef in options:
            setattr(skullstrip.inputs, ef, options[ef])
        self.res = skullstrip.run()
        
    def out_file(self: 'path'):
        return self.res.outputs.out_file

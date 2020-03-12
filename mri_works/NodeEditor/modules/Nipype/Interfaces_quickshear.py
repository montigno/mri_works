class quickshear_Quickshear():
    def __init__(self, in_file='path', mask_file='path', **options):
        from nipype.interfaces.quickshear import Quickshear
        qs = Quickshear(in_file=in_file, mask_file=mask_file)
        for ef in options:
            setattr(qs.inputs, ef, options[ef])
        self.res = qs.run()

    def out_file(self: 'path'):
        return self.res.outputs.out_file

class afni_ZCutUp():
    def __init__(self, in_file='path', **options):
        from nipype.interfaces.afni import ZCutUp
        zcutup = ZCutUp()
        zcutup.inputs.in_file = in_file
        for ef in options:
            setattr(zcutup.inputs, ef, options[ef])
        self.res = zcutup.run()
        
    def out_file(self:'path'):
        return self.res.outputs.out_file

##############################################################################

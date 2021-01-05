class mrtrix3_DWIExtract():
    def __init__(self, in_file='path', out_file='path', **options):
        from nipype.interfaces.mrtrix3 import DWIExtract
        dwiextract = DWIExtract()
        dwiextract.inputs.in_file = in_file
        dwiextract.out_file = out_file
        for ef in options:
            setattr(dwiextract.inputs, ef, options[ef])
        self.res = dwiextract.run()
        
    def out_file(self:'path'):
        return self.res.outputs.out_file

##############################################################################
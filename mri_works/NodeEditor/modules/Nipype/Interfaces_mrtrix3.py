class mrtrix3_DWIDenoise():
    def __init__(self, in_file='path', **options):
        from nipype.interfaces.mrtrix3 import DWIDenoise
        denoise = DWIDenoise()
        denoise.inputs.in_file = in_file
        for ef in options:
            setattr(denoise.inputs, ef, options[ef])
        self.res = denoise.run()
        
    def noise(self:'path'):
        return self.res.outputs.noise
    
    def out_file(self:'path'):
        return self.res.outputs.out_file
class Fourier():
    def __init__(self, in_file='path', lowpass=0.005, highpass=0.1, **options):
        from nipype.interfaces import afni
        fourier = afni.Fourier()
        fourier.inputs.in_file = in_file
        fourier.inputs.lowpass = lowpass
        fourier.inputs.highpass = highpass
        for ef in options:
            setattr(fourier.inputs, ef, options[ef])
        self.res = fourier.run()

    def out_file(self: 'path'):
        return self.res.outputs.out_file

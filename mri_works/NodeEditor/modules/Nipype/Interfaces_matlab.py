class MatlabCommand():
    def __init__(self, script='', **options):
        import nipype.interfaces.matlab as matlab
        mlab = matlab.MatlabCommand(mfile=False)
        mlab.inputs.script = script
        for ef in options:
            setattr(mlab.inputs, ef, options[ef])
        self.res = mlab.run()

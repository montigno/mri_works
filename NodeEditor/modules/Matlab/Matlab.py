class MatlabCommand:
    def __init__(self,cmd=""):
        import nipype.interfaces.matlab as matlab
        mlab = matlab.MatlabCommand(mfile=False)
        mlab.inputs.script = cmd
        out=mlab.run()
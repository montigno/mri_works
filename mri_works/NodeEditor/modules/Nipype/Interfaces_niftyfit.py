class niftyfit_FitAsl():
    def __init__(self, source_file='path', **options):
        from nipype.interfaces import niftyfit
        node = niftyfit.FitAsl()
        node.inputs.source_file = source_file
        for ef in options:
            setattr(node.inputs, ef, options[ef])
        self.res = node.run()

    def cbf_file(self: 'path'):
        return self.res.outputs.cbf_file

    def error_file(self: 'path'):
        return self.res.outputs.error_file

    def syn_file(self: 'path'):
        return self.res.outputs.syn_file

##############################################################################


class niftyfit_DwiTool():
    def __init__(self, source_file='path', **options):
        from nipype.interfaces import niftyfit
        dwi_tool = niftyfit.DwiTool(dti_flag=True)
        dwi_tool.inputs.source_file = source_file
        for ef in options:
            setattr(dwi_tool.inputs, ef, options[ef])
        self.res = node.run()

    def mcmap_file(self: 'path'):
        return self.res.outputs.mcmap_file

    def syn_file(self: 'path'):
        return self.res.outputs.syn_file

    def mdmap_file(self: 'path'):
        return self.res.outputs.mdmap_file

    def famap_file(self: 'path'):
        return self.res.outputs.famap_file

    def v1map_file(self: 'path'):
        return self.res.outputs.v1map_file

    def rgbmap_file(self: 'path'):
        return self.res.outputs.rgbmap_file

    def logdti_file(self: 'path'):
        return self.res.outputs.logdti_file

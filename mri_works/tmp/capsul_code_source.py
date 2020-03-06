class build_list_path_dyn:
    def __init__(self,in_path='path',in_path_0='path',**dynamicsInputs):
        self.pathList = [in_path,in_path_0]
        for di in dynamicsInputs:
            self.pathList.append(dynamicsInputs[di])
    
    def path_list(self:'list_path'):
        return self.pathList


class spm_Smooth():
    def __init__(self,in_files=['path'],**options):
        import nipype.interfaces.spm as spm
        smooth=spm.Smooth()
        smooth.inputs.in_files=in_files
        for ef in options:
            setattr(smooth.inputs,ef,options[ef])
        self.res=smooth.run()
        
    def smoothed_files(self:'list_path'):
        return self.res.outputs.smoothed_files



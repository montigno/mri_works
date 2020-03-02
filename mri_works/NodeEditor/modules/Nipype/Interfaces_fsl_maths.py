class fsl_ApplyMask():
    def __init__(self,in_file='path',mask_file='path',**options):
        from nipype.interfaces.fsl import ApplyMask
        mf = ApplyMask()
        mf.inputs.in_file=in_file
        mf.inputs.mask_file=mask_file
        for ef in options:
            setattr(mf.inputs,ef,options[ef])
        self.res=mf.run()
        
    def out_file(self:'path'):
        return self.res.outputs.out_file
    
##############################################################################

class fsl_BinaryMaths():
    def __init__(self,in_file='path',operand_value=0.0,operand_file='path',
                 operation="enumerate(('add','sub','mul','div','rem','max','min'))",**options):
        from nipype.interfaces.fsl import BinaryMaths
        mf=BinaryMaths()
        mf.inputs.in_file=in_file
        mf.inputs.operand_value=operand_value
        mf.inputs.operand_file=operand_file
        mf.inputs.operation=operation
        for ef in options:
            setattr(mf.inputs,ef,options[ef])
        self.res=mf.run()
        
    def out_file(self:'path'):
        return self.res.outputs.out_file


##############################################################################
    
class fsl_Threshold():
    def __init__(self,in_file='path',thresh=0.0,**options):
        from nipype.interfaces.fsl import Threshold
        mf = Threshold()
        mf.inputs.in_file=in_file
        mf.inputs.thresh=thresh
        for ef in options:
            setattr(mf.inputs,ef,options[ef])
        self.res=mf.run()
        
    def out_file(self:'path'):
        return self.res.outputs.out_file    
##############################################################################

class fsl_UnaryMaths():
    def __init__(self,in_file='path',
                 operation="enumerate(('exp','log','sin','cos','tan','asin','acos','atan',"+
                            "'sqr','sqrt','recip','abs','bin','binv','fillh',"+
                            "'fillh26','index','edge','nan','nanm','rand',"+
                            "'randn','range'))",**options):
        from nipype.interfaces.fsl import UnaryMaths
        mf = UnaryMaths()
        mf.inputs.in_file=in_file
        mf.inputs.operation=operation
        for ef in options:
            setattr(mf.inputs,ef,options[ef])
        self.res=mf.run()  
    
    def out_file(self:'path'):
        return self.res.outputs.out_file

##############################################################################


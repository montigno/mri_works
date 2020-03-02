class spm_Coregister():
    def __init__(self,target='path',source='path',**options):
        import nipype.interfaces.spm as spm
        coreg = spm.Coregister()
        coreg.inputs.target = target
        coreg.inputs.source = source
        for ef in options:
            setattr(coreg.inputs,ef,options[ef])
        self.res=coreg.run()
        
    def coregistered_source(self:'list_path'):
        return self.res.outputs.coregistered_source
    
    def coregistered_files(self:'list_path'):
        return self.res.outputs.coregistered_files
    
##################################################################

class spm_Normalize():
    def __init__(self,parameter_file='path',source=['path'],template='path',**options):
        import nipype.interfaces.spm as spm
        norm = spm.Normalize()
        norm.inputs.parameter_file = parameter_file
        norm.inputs.source = source
        norm.inputs.template = template
        for ef in options:
            setattr(norm.inputs,ef,options[ef])
        self.res=norm.run()
        
    def normalization_parameters(self:'path'):
        return self.res.outputs.normalization_parameters
    
    def normalized_files(self:'path'):
        return self.res.outputs.normalized_files
    
    def normalized_source(self:'path'):
        return self.res.outputs.normalized_source
    
##################################################################

class spm_NewSegment():
    def __init__(self,channel_files=['path'],**options):
        import nipype.interfaces.spm as spm
        seg = spm.NewSegment()
        seg.inputs.channel_files=channel_files
        for ef in options:
            setattr(seg.inputs,ef,options[ef])
        self.res=seg.run()
        
    def native_class_images(self:'array_path'):
        return self.res.outputs.native_class_images
    
    def forward_deformation_field(self:'list_path'):
        return self.res.outputs.forward_deformation_field

    def dartel_input_images(self:'array_path'):
        return self.res.outputs.dartel_input_images
    
    def inverse_deformation_field(self:'list_path'):
        return self.res.outputs.inverse_deformation_field
    
    def bias_field_images(self:'list_path'):
        return self.res.outputs.bias_field_images

    def normalized_class_images(self:'array_path'):
        return self.res.outputs.normalized_class_images
    
    def transformation_mat(self:'list_path'):
        return self.res.outputs.inverse_transformation_mat 
    
    def modulated_class_images(self:'array_path'):
        return self.res.outputs.modulated_class_images
    
    def bias_corrected_images(self:'list_path'):
        return self.res.outputs.bias_corrected_images
    
##################################################################

class spm_Segment():
    def __init__(self,data=['path'],**options):
        import nipype.interfaces.spm as spm
        seg = spm.Segment()
        seg.inputs.data = data
        for ef in options:
            setattr(seg.inputs,ef,options[ef])
        self.res=seg.run()
        
    def native_gm_image(self:'path'):
        return self.res.outputs.native_gm_image
    
    def normalized_gm_image(self:'path'):
        return self.res.outputs.normalized_gm_image
    
    def modulated_gm_image(self:'path'):
        return self.res.outputs.normalized_gm_image
    
    def native_wm_image(self:'path'):
        return self.res.outputs.native_wm_image
    
    def normalized_wm_image(self:'path'):
        return self.res.outputs.normalized_wm_image
    
    def modulated_wm_image(self:'path'):
        return self.res.outputs.modulated_wm_image
    
    def native_csf_image(self:'path'):
        return self.res.outputs.native_csf_image
    
    def normalized_csf_image(self:'path'):
        return self.res.outputs.normalized_csf_image
    
    def modulated_csf_image(self:'path'):
        return self.res.outputs.modulated_csf_image
    
    def modulated_input_image(self:'path'):
        return self.res.outputs.modulated_input_image
    
    def bias_corrected_image(self:'path'):
        return self.res.outputs.bias_corrected_image
    
    def transformation_mat(self:'path'):
        return self.res.outputs.transformation_mat
    
    def inverse_transformation_mat(self:'path'):
        return self.res.outputs.inverse_transformation_mat
    

##################################################################

class spm_Realign():
    def __init__(self,in_files=['path'],**options):
        import nipype.interfaces.spm as spm
        realign = spm.Realign()
        realign.inputs.in_files=in_files
        for ef in options:
            setattr(realign.inputs,ef,options[ef])
        self.res=realign.run()
        
    def mean_image(self:'path'):
        return self.res.outputs.mean_image
    
    def modified_in_files(self:'list_path'):
        return self.res.outputs.modified_in_files
    
    def realigned_files(self:'list_path'):
        return self.res.outputs.realigned_files
    
    def realignment_parameters(self:'path'):
        return self.res.outputs.realignment_parameters
    
##################################################################

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
    
##################################################################

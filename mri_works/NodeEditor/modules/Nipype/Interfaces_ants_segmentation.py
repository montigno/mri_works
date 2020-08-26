class ants_AntsJointFusion():

    def __init__(self, atlas_segmentation_image=['path', 'path'],
                 atlas_image=[['path']], target_image=['path'], **options):
        from nipype.interfaces.ants import AntsJointFusion
        antsjointfusion = AntsJointFusion()
        antsjointfusion.inputs.atlas_segmentation_image = atlas_segmentation_image
        antsjointfusion.inputs.atlas_image = atlas_image
        antsjointfusion.inputs.target_image = target_image
        for ef in options:
            setattr(antsjointfusion.inputs, ef, options[ef])
        self.res = antsjointfusion.run()

    def out_label_post_prob_name_format(self: 'str'):
        return self.res.outputs.out_label_post_prob_name_format

    def out_label_fusion(self: 'path'):
        return self.res.outputs.out_label_fusion

    def out_atlas_voting_weight_name_format(self: 'str'):
        return self.res.outputs.out_atlas_voting_weight_name_format

    def out_intensity_fusion_name_format(self: 'str'):
        return self.res.outputs.out_intensity_fusion_name_format

###############################################################################


class ants_BrainExtraction():

    def __init__(self, anatomical_image='path', brain_template='path',
                 brain_probability_mask='path', **options):
        from nipype.interfaces.ants.segmentation import BrainExtraction
        brainextraction = BrainExtraction()
        brainextraction.inputs.anatomical_image = anatomical_image
        brainextraction.inputs.brain_template = brain_template
        brainextraction.inputs.brain_probability_mask = brain_probability_mask
        for ef in options:
            setattr(brainextraction.inputs, ef, options[ef])
        self.res = brainextraction.run()

    def BrainExtractionMask(self: 'path'):
        return self.res.outputs.BrainExtractionMask

    def BrainExtractionBrain(self: 'path'):
        return self.res.outputs.BrainExtractionBrain

    def BrainExtractionCSF(self: 'path'):
        return self.res.outputs.BrainExtractionCSF

    def BrainExtractionGM(self: 'path'):
        return self.res.outputs.BrainExtractionGM

    def BrainExtractionInitialAffine(self: 'path'):
        return self.res.outputs.BrainExtractionInitialAffine

    def BrainExtractionInitialAffineFixed(self: 'path'):
        return self.res.outputs.BrainExtractionInitialAffineFixed

    def BrainExtractionInitialAffineMoving(self: 'path'):
        return self.res.outputs.BrainExtractionInitialAffineMoving

    def BrainExtractionLaplacian(self: 'path'):
        return self.res.outputs.BrainExtractionLaplacian

    def BrainExtractionPrior0GenericAffine(self: 'path'):
        return self.res.outputs.BrainExtractionPrior0GenericAffine

    def BrainExtractionPrior1InverseWarp(self: 'path'):
        return self.res.outputs.BrainExtractionPrior1InverseWarp

    def BrainExtractionPrior1Warp(self: 'path'):
        return self.res.outputs.BrainExtractionPrior1Warp

    def BrainExtractionPriorWarped(self: 'path'):
        return self.res.outputs.BrainExtractionPriorWarped

    def BrainExtractionSegmentation(self: 'path'):
        return self.res.outputs.BrainExtractionSegmentation

    def BrainExtractionTemplateLaplacian(self: 'path'):
        return self.res.outputs.BrainExtractionTemplateLaplacian

    def BrainExtractionTmp(self: 'path'):
        return self.res.outputs.BrainExtractionTmp

    def BrainExtractionWM(self: 'path'):
        return self.res.outputs.BrainExtractionWM

    def N4Corrected0(self: 'path'):
        return self.res.outputs.N4Corrected0

    def N4Truncated0(self: 'path'):
        return self.res.outputs.N4Truncated0
    
##############################################################################


class ants_JointFusion():

    def __init__(self, warped_label_images=['path'], warped_intensity_images=['path'],
                       output_label_image='path', target_image=['path'],
                       modalities=1, dimension=3, **options):
        
        from nipype.interfaces.ants import JointFusion
        at = JointFusion()
        at.inputs.warped_label_images = warped_label_images
        at.inputs.warped_intensity_images = warped_intensity_images
        at.inputs.output_label_image = output_label_image
        at.inputs.target_image = target_image
        at.inputs.modalities = modalities
        at.inputs.dimension = dimension
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()
        
    def output_label_image(self:'path'):
        return self.res.outputs.output_label_image

##############################################################################


class ants_N4BiasFieldCorrection():

    def __init__(self, input_image='path', save_bias=False,
                 copy_header=False, **options):
        from nipype.interfaces.ants import N4BiasFieldCorrection
        n4 = N4BiasFieldCorrection()
        n4.inputs.input_image = input_image
        n4.inputs.save_bias = save_bias
        n4.inputs.copy_header = copy_header
        for ef in options:
            setattr(n4.inputs, ef, options[ef])
        self.res = n4.run()

    def output_image(self: 'path'):
        return self.res.outputs.output_image

    def bias_image(self: 'path'):
        return self.res.outputs.bias_image

##############################################################################

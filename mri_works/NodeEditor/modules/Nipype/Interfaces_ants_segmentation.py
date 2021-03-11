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

    def BrainExtractionBrain(self: 'path'):
        return self.res.outputs.BrainExtractionBrain

    def BrainExtractionMask(self: 'path'):
        return self.res.outputs.BrainExtractionMask

##############################################################################


class ants_JointFusion():

    def __init__(self, atlas_segmentation_image=['path', 'path'],
                 atlas_image=[['path']], target_image=['path'], **options):

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

    def out_atlas_voting_weight_name_format(self: 'str'):
        return self.res.outputs.out_atlas_voting_weight_name_format

    def out_intensity_fusion_name_format(self: 'str'):
        return self.res.outputs.out_intensity_fusion_name_format

    def out_label_fusion(self: 'path'):
        return self.res.outputs.out_label_fusion

    def out_label_post_prob_name_format(self: 'str'):
        return self.res.outputs.out_label_post_prob_name_format
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

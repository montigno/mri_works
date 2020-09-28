class ants_MeasureImageSimilarity():

    def __init__(self,
                 moving_image='path',
                 fixed_image='path',
                 metric="enumerate(('CC', 'MeanSquares', 'Demons'))",
                 sampling_percentage=0.0,
                 radius_or_number_of_bins=0,
                 **options):

        from nipype.interfaces.ants import MeasureImageSimilarity
        sim = MeasureImageSimilarity()
        sim.inputs.moving_image = moving_image
        sim.inputs.fixed_image = fixed_image
        sim.inputs.metric = metric
        sim.inputs.sampling_percentage = sampling_percentage
        sim.inputs.radius_or_number_of_bins = radius_or_number_of_bins
        for ef in options:
            setattr(sim.inputs, ef, options[ef])
        self.res = sim.run()

    def similarity(self: 'float'):
        return self.res.outputs.similarity

###############################################################################


class ants_Registration():

    def __init__(self,
                 moving_image=['path'],
                 fixed_image=['path'],
                 metric=['CC', 'MeanSquares', 'Demons'], metric_weight=[1.0],
                 transforms=['Affine', 'BSplineSyN'],
                 shrink_factors=[[2, 1], [3, 2, 1]],
                 smoothing_sigmas=[[1, 0], [2, 1, 0]], **options):

        from nipype.interfaces.ants import Registration
        reg = Registration()
        reg.inputs.moving_image = moving_image
        reg.inputs.fixed_image = fixed_image
        reg.inputs.metric = metric
        reg.inputs.metric_weight = metric_weight
        reg.inputs.transforms = transforms
        reg.inputs.shrink_factors = shrink_factors
        reg.inputs.smoothing_sigmas = smoothing_sigmas
        for ef in options:
            setattr(reg.inputs, ef, options[ef])
        self.res = reg.run()

    def warped_image(self: 'path'):
        return self.res.outputs.warped_image

    def inverse_warped_image(self: 'path'):
        return self.res.outputs.inverse_warped_image

    def composite_transform(self: 'path'):
        return self.res.outputs.composite_transform

    def inverse_composite_transform(self: 'path'):
        return self.res.outputs.inverse_composite_transform

    def save_state(self: 'path'):
        return self.res.outputs.save_state

    def forward_transforms(self: 'list_path'):
        return self.res.outputs.forward_transforms

    def reverse_transforms(self: 'list_path'):
        return self.res.outputs.reverse_transforms

    def elapsed_time(self: 'float'):
        return self.res.outputs.elapsed_time

    def metric_value(self: 'float'):
        return self.res.outputs.metric_value

    def forward_invert_flags(self: 'list_bool'):
        return self.res.outputs.forward_invert_flags

    def reverse_invert_flags(self: 'list_bool'):
        return self.res.outputs.reverse_invert_flags

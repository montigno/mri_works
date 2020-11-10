class binarize_with_threshold():
    def __init__(self,
                 image='path',
                 threshold=1.0,
                 val_below = 0.0,
                 val_equal_above = 1.0,
                 output_file='path'):
        import nibabel
        import os
        self.outFile = output_file
        localizer_img = nibabel.load(image)
        localizer =  localizer_img.get_data()
        localizer[localizer >= 1.0] = 1.0
        locmask = nibabel.Nifti1Image(localizer, localizer_img.get_affine())
        nibabel.save(locmask, output_file)
        
    def outfile(self:'path'):
        return self.outFile
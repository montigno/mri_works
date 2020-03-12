class dcm2nii_Dcm2nii():
    def __init__(self, source_names=['path'], source_dir='path', **options):
        from nipype.interfaces.dcm2nii import Dcm2nii
        self.converter = Dcm2nii()
        self.converter.inputs.source_names = source_names
        self.converter.inputs.source_dir = source_dir
        for ef in options:
            setattr(self.converter.inputs, ef, options[ef])
        self.converter.run()

    def converted_files(self: 'list_path'):
        return self.converter.outputs.converted_files

    def reoriented_files(self: 'list_path'):
        return self.converter.outputs.reoriented_files

    def reoriented_and_cropped_files(self: 'list_path'):
        return self.converter.outputs.reoriented_and_cropped_files

    def bvecs(self: 'list_path'):
        return self.converter.outputs.bvecs

    def bvals(self: 'list_path'):
        return self.converter.outputs.bvals

class Bru2Nii:
    def __init__(self, dirSource='path'):
        from nipype.interfaces.bru2nii import Bru2
        converter = Bru2()
        converter.inputs.input_dir = dirSource
#         converter.cmdline
#         self.outfile = converter._list_outputs()
        res = converter.run()

#     def nii_file(self:'path'):
#         return self.outfile

##############################################################################


class Dcm2nii:
    def __init__(self, source_names=['', '']):
        from nipype.interfaces.dcm2nii import Dcm2nii
        converter = Dcm2nii()
        converter.inputs.source_names = source_names
        converter.inputs.gzip_output = True
        converter.inputs.output_dir = '.'
        converter.cmdline
        converter.run()

    def dicom_file(self: 'path'):
        return self.outfile

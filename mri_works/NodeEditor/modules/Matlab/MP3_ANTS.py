class MP3_Atlas_ANTS():
    def __init__(self,
                 mat_eng='',
                 Nifti_in='path',
                 Ref_in='path',
                 file_out1='path',
                 file_out2='path',
                 **options):
        import matlab.engine
        import os
        files_in, files_out = {}, {}
        options['flag_test'] = 0
        options['Table_in'] = {}
        base = os.path.basename(Nifti_in)
        options['Table_in']['Filename'] = os.path.splitext(base)[0]
        files_in['In1'] = [Nifti_in]
        files_in['In2'] = [Ref_in]
        files_out['In1'] = [file_out1]
        files_out['In2'] = [file_out2]
        mat_eng.Module_Atlas_ANTs(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out

    def mat_eng(self: 'str'):
        return self.mat_eng
    
    def file_out1(self: 'path'):
        return self.map[0]

    def file_out2(self: 'path'):
        return self.map[1]

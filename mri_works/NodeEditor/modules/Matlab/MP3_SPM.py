class MP3_SPM_reorient():
    def __init__(self,
                 mat_eng='',
                 file_in='path',
                 file_out='path',
                 **options):
        import matlab.engine
        files_in, files_out = {}, {}
        options['flag_test'] = 0
        files_in['In1'] = [file_in]
        files_out['In1'] = [file_out]
        mat_eng.Module_SPM_reorient(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out
        
    def mat_eng(self: 'str'):
        return self.mat_eng

    def file_out(self: 'path'):
        return self.map

##############################################################################

class MP3_SPM_Coreg_Est_Res():
    def __init__(self,
                 mat_eng='',
                 file_ref='path',
                 file_source='path',
                 files_other=['path'],
                 file_out='path',
                 files_out_other=['path'],
                 **options):
        import matlab.engine
        files_in, files_out = {}, {}
        options['flag_test'] = 0
        files_in['In1'] = [file_ref]
        files_in['In2'] = [file_source]
        files_out['In1'] = [file_out]
        files_out['In2'] = [file_out]
        if files_other[0] != 'path':
            files_in['In3'] = files_other
            files_out['In3'] = files_out_other
        mat_eng.Module_Coreg_Est_Res(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out
        
    def mat_eng(self: 'str'):
        return self.mat_eng

    def file_out(self: 'path'):
        return self.map

##############################################################################

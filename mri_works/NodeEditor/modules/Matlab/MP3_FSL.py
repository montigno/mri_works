class MP3_FLIRT():
    def __init__(self,
                 mat_eng='',
                 reference='path',
                 file_in='path',
                 file_out='path',
                 **options):
        import matlab.engine
        files_in, files_out = {}, {}
        options['flag_test'] = 0
        files_in['In1'] = [reference]
        files_in['In2'] = [file_in]
        files_out['In1'] = [file_out]
        mat_eng.Module_FSL_FLIRT(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out

    def mat_eng(self: 'str'):
        return self.mat_eng

    def file_out1(self: 'path'):
        return self.map[0]

    def file_out2(self: 'path'):
        return self.map[1]

    def file_out3(self: 'path'):
        return self.map[2]

##############################################################################

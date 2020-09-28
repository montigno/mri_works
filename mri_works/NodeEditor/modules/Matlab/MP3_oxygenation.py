class MP3_CMRO2():
    def __init__(self,
                 mat_eng='',
                 file_CBF='path',
                 file_SO2='path',
                 file_out='path',
                 **options):
        import matlab.engine
        files_in, files_out = {}, {}
        options['flag_test'] = 0
        files_in['In1'] = [file_CBF]
        files_in['In2'] = [file_SO2]
        files_out['In1'] = [file_out]
        mat_eng.Module_CMRO2(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out

    def mat_eng(self: 'str'):
        return self.mat_eng

    def file_out(self: 'path'):
        return self.map

##############################################################################


class MP3_R2Prim():
    def __init__(self,
                 mat_eng='',
                 file_T2Map='path',
                 file_T2StarCorr3D='path',
                 file_out='path',
                 **options):
        import matlab.engine
        files_in, files_out = {}, {}
        options['flag_test'] = 0
        files_in['In1'] = [file_T2Map]
        files_in['In2'] = [file_T2StarCorr3D]
        files_out['In1'] = [file_out]
        mat_eng.Module_CMRO2(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out

    def mat_eng(self: 'str'):
        return self.mat_eng

    def file_out(self: 'path'):
        return self.map

##############################################################################


class MP3_SO2():
    def __init__(self,
                 mat_eng='',
                 file_R2Prim='path',
                 file_BVf='path',
                 file_out='path',
                 **options):
        import matlab.engine
        files_in, files_out = {}, {}
        options['flag_test'] = 0
        files_in['In1'] = [file_R2Prim]
        files_in['In2'] = [file_BVf]
        files_out['In1'] = [file_out]
        mat_eng.Module_CMRO2(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out

    def mat_eng(self: 'str'):
        return self.mat_eng

    def file_out(self: 'path'):
        return self.map

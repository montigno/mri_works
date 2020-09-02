class MP3_T2map():
    def __init__(self, mat_eng='', file_in='path', file_out='path', **options):
        import matlab.engine
        files_in , files_out = {}, {}
        options['flag_test'] = 0
        files_in['In1'] = [file_in]
        files_out['In1'] = [file_out]
        mat_eng.Module_T2map(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out

    def mat_eng(self:'str'):
        return self.mat_eng

    def file_out(self:'path'):
        return self.map

##############################################################################


class MP3_DeltaR2():
    def __init__(self, mat_eng='', file_in_pre='path', file_in_post = 'path', file_out='path', **options):
        import matlab.engine
        files_in , files_out = {}, {}
        options['flag_test'] = 0
        files_in['In1'] = [file_in_pre]
        files_in['In2'] = [file_in_post]
        files_out['In1'] = [file_out]
        mat_eng.Module_DeltaR2(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out
        
    def mat_eng(self:'str'):
        return self.mat_eng

    def file_out(self:'path'):
        return self.map

##############################################################################


class MP3_T1map_MultiAngles():
    def __init__(self, mat_eng='', file_in=['path'], file_out='path', **options):
        import matlab.engine
        files_in , files_out = {}, {}
        options['flag_test'] = 0
        files_in['In1'] = list(file_in)
        files_out['In1'] = [file_out]
        mat_eng.Module_T1map_MultiAngles(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out
        
    def mat_eng(self:'str'):
        return self.mat_eng

    def file_out(self:'path'):
        return self.map

##############################################################################


class MP3_MGE2Dfrom3D():
    def __init__(self, mat_eng='', file_in='path', file_out='path', **options):
        import matlab.engine
        files_in , files_out = {}, {}
        options['flag_test'] = 0
        files_in['In1'] = [file_in]
        files_out['In1'] = [file_out]
        mat_eng.Module_MGE2Dfrom3D(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out

    def mat_eng(self:'str'):
        return self.mat_eng

    def file_out(self:'path'):
        return self.map

##############################################################################


class MP3_T1map_MIT():
    def __init__(self, mat_eng='', file_in='path', file_out='path', **options):
        import matlab.engine
        files_in , files_out = {}, {}
        options['flag_test'] = 0
        files_in['In1'] = [file_in]
        files_out['In1'] = [file_out]
        mat_eng.Module_T1map_MIT(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out

    def mat_eng(self:'str'):
        return self.mat_eng

    def file_out(self:'path'):
        return self.map

##############################################################################


class MP3_Slice_Sum():
    def __init__(self, mat_eng='', file_in='path', file_out='path', **options):
        import matlab.engine
        files_in , files_out = {}, {}
        options['flag_test'] = 0
        files_in['In1'] = [file_in]
        files_out['In1'] = [file_out]
        mat_eng.Module_Slice_Sum(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out

    def mat_eng(self:'str'):
        return self.mat_eng

    def file_out(self:'path'):
        return self.map

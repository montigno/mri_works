class MP3_Brain_Mask_PCNN3D():
    def __init__(self, mat_eng='', file_in='path', file_out='path', **options):
        import matlab.engine
        files_in , files_out = {}, {}
        options['flag_test'] = 0
        files_in['In1'] = [file_in]
        files_out['In1'] = [file_out]
        mat_eng.Module_Brain_Mask_PCNN3D(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out

    def mat_eng(self:'str'):
        return self.mat_eng

    def file_out(self:'path'):
        return self.map

##############################################################################

class MP3_Arithmetic():
    def __init__(self, mat_eng='', img1='path', img2='path',file_out='path', **options):
        import matlab.engine
        files_in , files_out = {}, {}
        options['flag_test'] = 0
#         options['Table_in']['Type'] = 'ROI'
        setattr(options['Table_in'], 'Type', 'ROI')        
        files_in['In1'] = [img1]
        files_in['In2'] = [img2]
        files_out['In1'] = [file_out]
        mat_eng.Module_Brain_Arithmetic(files_in, files_out, options)
        self.mat_eng = mat_eng
        self.map = file_out

    def mat_eng(self:'str'):
        return self.mat_eng

    def file_out(self:'path'):
        return self.map
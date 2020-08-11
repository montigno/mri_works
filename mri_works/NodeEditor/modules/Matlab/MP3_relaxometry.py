class Module_T2map():
    def __init__(self, mat_eng='', files_in=['path'], files_out=['path'], **options):
        import matlab.engine
        self.map = mat_eng.Module_T2map(files_in, '', '')
        self.mat_eng = mat_eng

    def mat_eng(self:'str'):
        return self.mat_eng

    def files_out(self:'list_path'):
        return self.map
class create_directory:
    def __init__(self, dir_in='path'):
        import os
        self.dir_out = ''
        if not os.path.exists(dir_in):
            os.makedirs(dir_in)
            self.dir_out = dir_in
            
    def out_dir(self:'path'):
        return self.dir_out
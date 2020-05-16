class deleting_folder:
    def __init__(self, input_folder='path', ignore_errors=False):
        import shutil
        shutil.rmtree(input_folder, ignore_errors=ignore_errors)
        
##############################################################################

class deleting_file:
    def __init__(self, input_file='path'):
        import os
        os.remove(input_file)

class deleting_folder:
    def __init__(self, input_folder='path', ignore_errors=False):
        import shutil
        shutil.rmtree(input_folder, ignore_errors=ignore_errors)
        
##############################################################################

class deleting_file:
    def __init__(self, input_file='path'):
        import os
        try:
            os.remove(input_file)
        except OSError as e:
            print("Error : %s : %s" % (input_file, e.strerror))
            
##############################################################################

class deleting_files_model:
    def __init__(self, input_dir='path', model='*.txt'):
        import os
        import glob

        files = glob.glob(os.path.join(input_dir,model))

        for f in files:
            try:
                os.remove(f)
            except OSError as e:
                print('Error : %s : %s' %(f, e.strerror))

##############################################################################

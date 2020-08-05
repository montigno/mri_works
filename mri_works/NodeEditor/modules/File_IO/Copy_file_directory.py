class copy_file():
    def __init__(self, src_file='path', dest_file='path'):
        from shutil import copyfile
        copyfile(src_file, dest_file)
        
###############################################################################

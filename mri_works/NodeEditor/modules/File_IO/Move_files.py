class move_files:
    def __init__(self, files_input=['path'], move_to_dir='path'):
        import shutil
        import os
        if not os.path.exists(move_to_dir):
            os.makedirs(move_to_dir)
        for lst in files_input:
            shutil.move(lst, move_to_dir)
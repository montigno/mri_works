class dcm2niix():
    def __init__(self, sourcedir='path', **options):
        from subprocess import run        
        import os
        if 'o' in options.keys():
            listRep1 = os.listdir(options['o'])
        else:
            listRep1 = os.listdir(sourcedir)
        list_options = []
        for op in options:
            list_options.append('-'+op)
            list_options.append(options[op])
        command = ['dcm2niix']
        command.extend(list_options)
        command.append(sourcedir)
        result = run(command, shell=False, check=True)
        if 'o' in options.keys():
            listRep2 = os.listdir(options['o'])
        else:
            listRep2 = os.listdir(sourcedir)
        self.listfiles = [os.path.join(options['o'], item) for item in listRep2 if item not in listRep1]

    def list_files(self:'list_path'):
        return self.listfiles

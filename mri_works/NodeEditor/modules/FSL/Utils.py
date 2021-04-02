class fslsplit():
    def __init__(self, input='path', output_basename='path', dimension= "enumerate(('-t', '-x', '-y', '-z'))"):
        from subprocess import run
        import glob
        list_options = []
        list_options.append(input)
        list_options.append(output_basename)
        list_options.append(dimension)
        command = ["fslsplit"]
        command.extend(list_options)
        print('command : ', command)
        result = run(command, shell=False, check=True)
        self.outfile = glob.glob(output_basename+'*.nii.gz')
        self.outfile = sorted(self.outfile, reverse=False)
        
    def output_file(self:'list_path'):
        return self.outfile
    
###############################################################################

class fslmerge():
    def __init__(self, dimension= "enumerate(('-t', '-x', '-y', '-z', '-a', 'tr'))", output='path', in_files=['path'], **options):
        from subprocess import run
        list_options = []
        list_options.append(dimension)
        list_options.append(output)
        list_options.extend(in_files)
        for op in options:
            list_options.append(op)
            if options[op]:
                list_options.append(str(options[op]))
        command = ["fslmerge"]
        command.extend(list_options)
        print('command : ', command)
        result = run(command, shell=False, check=True)
        self.outfile = output
        
    def output_file(self:'path'):
        return self.outfile
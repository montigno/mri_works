class antsRegistration():
    def __init__(self, output='', **options):
        from subprocess import run
        list_options = []
        list_options.append('--output')
        list_options.append(output)
        for op in options:
            list_options.append(op)
            if options[op]:
                list_options.append(str(options[op]))
        command = ['antsRegistration']
        command.extend(list_options)            
        result = run(command, shell=False, check=True)
        self.res = output.strip('][').split(',')

    def outputWarpedImage(self:'path'):
        return self.res[1]

    def outputInverseWarpedImage(self:'path'):
        return self.res[2]
    
###############################################################################

class antsApplyTransforms():
    def __init__(self, output='path', **options):
        from subprocess import run
        list_options = []
        list_options.append('--output')
        list_options.append(output)
        for op in options:
            list_options.append(op)
            if options[op]:
                list_options.append(str(options[op]))
        command = ['antsApplyTransforms']
        command.extend(list_options)            
        result = run(command, shell=False, check=True)
        self.res = output

    def outputWarpedImage(self:'path'):
        return self.res
    
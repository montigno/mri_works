class antsMotionCorr:
    def __init__(self, output='', **options):
        from subprocess import run
        list_options = []
        list_options.append('--output')
        list_options.append(output)
        for op in options:
            list_options.append('--' + op)
            list_options.append(options[op])
        command = ['antsMotionCorr']
        command.extend(list_options)            
        result = run(command, shell=False, check=True)
        self.res = output.strip('][').split(',')

    def outputWarpedImage(self:'path'):
        return self.res[1]

    def outputAverageImage(self:'path'):
        return self.res[2]
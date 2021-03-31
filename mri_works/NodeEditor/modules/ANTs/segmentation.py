class N4BiasFieldCorrection:
    def __init__(self, **options):
        from subprocess import run
        list_options = []
        for op in options:
            list_options.append('--' + op)
            if options[op]:
                list_options.append(options[op])
        command = ["N4BiasFieldCorrection"]
        command.extend(list_options)
        print('command : ', command)
        result = run(command, shell=False, check=True)
        self.outfile = output_file
        
    def output_file(self:'path'):
        return self.outfile
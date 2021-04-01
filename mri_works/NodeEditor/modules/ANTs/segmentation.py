class N4BiasFieldCorrection:
    def __init__(self, input_image='path', output='path', **options):
        from subprocess import run
        list_options = []
        list_options.append('--input-image')
        list_options.append(input_image)
        list_options.append('--output')
        list_options.append(output)
        for op in options:
            list_options.append('--' + op)
            if options[op]:
                list_options.append(options[op])
        command = ["N4BiasFieldCorrection"]
        command.extend(list_options)
        print('command : ', command)
        result = run(command, shell=False, check=True)
        self.outfile = output
        
    def output_file(self:'path'):
        return self.outfile
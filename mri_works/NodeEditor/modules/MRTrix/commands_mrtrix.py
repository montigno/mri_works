class mrconvert:
    def __init__(self, input='path', output='path', **options):
        from subprocess import Popen
        list_options = []
        list_options.append(input)
        list_options.append(output)
        for op in options:
            list_options.append('-' + op)
            list_options.append(options[op])
        command = ["mrconvert"]
        command.extend(list_options)
        proc = Popen(command)
        self.outfile = output
        
    def output_file(self:'path'):
        return self.outfile

###############################################################################

class mrview:
    def __init__(self, list_images = ['path'], **options):
        from subprocess import Popen
        list_options = []
        list_options.extend(list_images)
        for op in options:
            list_options.append('-' + op)
            list_options.append(options[op])
        command = ['mrview']
        command.extend(list_options)
        proc = Popen(command)

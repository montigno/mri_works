class bet2:
    def __init__(self, input_file='path', output_file='path', **options):
        from subprocess import run
        list_options = []
        list_options.append(input_file)
        list_options.append(output_file)
        for op in options:
            list_options.append(op)
            if options[op]:
                list_options.append(str(options[op]))
        command = ["bet2"]
        command.extend(list_options)
        print('command : ', command)
        result = run(command, shell=False, check=True)
        self.outfile = output_file
        
    def output_file(self:'path'):
        return self.outfile
        
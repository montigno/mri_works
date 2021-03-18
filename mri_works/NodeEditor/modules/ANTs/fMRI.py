class antsMotionCorr:
    def __init__(self, fixed_image='path', moved_image='path', **options):
        from subprocess import run
        list_options = []
        for op in options:
            list_options.append('-'+op)
            list_options.append(options[op])
        command = ['antsMotionCorr']
        command.extend(list_options)            
        result = run(command, shell=False, check=True)
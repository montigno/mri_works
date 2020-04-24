class mrconvert:
    def __init__(self, input='path', output='path'):
        import subprocess
        import os
        lso = ("mrconvert", input, output)
        command = " ".join(lso)
        subprocess.run(command, shell=True, check=True)
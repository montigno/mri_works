class Plot_profil():
    def __init__(self, cmd_ant='', coord=[0, 0, 0, 0]):
        coords = tuple(coord)
        txt = ','.join(str(x) for x in coords)
        self.cmd = cmd_ant + "\nselectWindow(imageCurrent);makeLine(" + txt + ");run(\"Plot Profile\");"

    def cmd_post(self: 'str'):
        return self.cmd
    
##############################################################################

class Atlas_reg():
    def __init__(self, file_in='path', atlas_template='path', atlas_label='path', label_txt='path'):
        import subprocess
        from subprocess import Popen
        import os
        scriptfile = 'open("' + file_in + '");run(\"Enhance Contrast\", \"saturated=0.35\");\n'\
                     'open("' + atlas_label + '");run(\"Enhance Contrast\", \"saturated=0.35\");\n'\
                     'open("' + atlas_template + '");run(\"Enhance Contrast\", \"saturated=0.35\");\n'
        script = 'var lines=split(File.openAsString("' + label_txt + '"), "\\n");\n ij.run("Synchronize Windows"); \n'
        filemacro = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'macros', 'Atlas.txt')
        scriptmacro = open(filemacro, 'r').read()
        script += scriptmacro + '\n'

        
        file_tmp = open("/tmp/tmp.txt", "w")
        file_tmp.write(script)
        script = 'run("Install...", "install=/tmp/tmp.txt");'
        subprocess.Popen(['ImageJ', '-eval', scriptfile, '-eval', script], shell=False)

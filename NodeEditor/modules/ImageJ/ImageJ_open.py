##########################################################################################

class ImageJ_load_Image():
    def __init__(self, file='path'):
        import os
        img_current = os.path.basename(file)
        script = "fileCurrent = " + "\"" + file + "\"" + ";imageCurrent = " + "\"" + img_current + "\";open(fileCurrent);run('Enhance Contrast', 'saturated=0.35');"
        self.cmd = script
   
    def cmd_post(self:'str'):
        return self.cmd
    
##########################################################################################

class ImageJ_load_multiImages():
    def __init__(self, file=['path']):
        self.currentImg = file
   
    def currentImage(self:'list_str'):
        return self.currentImg

##########################################################################################

class openImageJ():

    def __init__(self, file='path'):
        from NodeEditor.python.configStandalone import ConfigModuls
        import subprocess
        from subprocess import Popen
        import os
        if file == 'path':
            file = ''
        pathImageJ = os.path.normpath(ConfigModuls().getPathConfig('ImageJ'))
        pathPlugIns = os.path.join(os.path.dirname(pathImageJ), 'plugins')
        script_macro = "run(\"Appearance...\", \"interpolate auto menu=15 gui=1 16-bit=Automatic\");"\
                       "run(\"Brightness/Contrast...\");"\
                       "run(\"Enhance Contrast\", \"saturated=0.35\");"
        subprocess.Popen(['java', '-jar', pathImageJ, file, '-ijpath', pathPlugIns,'-eval',script_macro], shell=False)
        tmp = os.path.basename(file)
        self.currentImg = ('.').join(tmp.split('.')[:-1])
                
    def currentImage(self:'str'):
        return self.currentImg
    
##########################################################################################

class openImagej_multiFiles():

    def __init__(self, file=['path']):
        from NodeEditor.python.configStandalone import ConfigModuls
        import subprocess
        from subprocess import Popen
        import os
        pathImageJ = os.path.normpath(ConfigModuls().getPathConfig('ImageJ'))
        pathPlugIns = os.path.join(os.path.dirname(pathImageJ), 'plugins')
        list_files = '|||'.join(file)
        script_macro = "run(\"Appearance...\", \"interpolate auto menu=15 gui=1 16-bit=Automatic\");"\
                       "run(\"Brightness/Contrast...\");"
        script_macro1 = "arg=" + "\"" + list_files + "\"" + ";"\
                        "list=split(arg,\"|||\");"\
                        "for (i=0;i<list.length;i++) {"\
                        "open(list[i]);"\
                        "run(\"Enhance Contrast\", \"saturated=0.35\");"\
                        "};"
        proc = subprocess.Popen(['java', '-jar', pathImageJ, '-ijpath', pathPlugIns, '-eval', script_macro1+script_macro])
        
##########################################################################################

class ImageJ_macro():

    def __init__(self, file_macro='path'):
        from NodeEditor.python.configStandalone import ConfigModuls
        import subprocess
        from subprocess import Popen
        import os
        pathImageJ = os.path.normpath(ConfigModuls().getPathConfig('ImageJ'))
        pathPlugIns = os.path.join(os.path.dirname(pathImageJ), 'plugins')
        option = '-macro'
        subprocess.Popen(['java', '-jar', pathImageJ, '-ijpath', pathPlugIns, option, file_macro])
        
##########################################################################################

class ImageJ_macrofile():

    def __init__(self, pathImage='path', filemacro='path'):
        from NodeEditor.python.configStandalone import ConfigModuls
        import subprocess
        from subprocess import Popen
        import os
        pathImageJ = os.path.normpath(ConfigModuls().getPathConfig('ImageJ'))
        pathPlugIns = os.path.join(os.path.dirname(pathImageJ), 'plugins')
        option = '-macro'
#         subprocess.call(['java','-jar',pathImageJ,pathImage,option,filemacro], shell=False)
        subprocess.Popen(['java', '-jar', pathImageJ, '-ijpath', pathPlugIns, pathImage, option, filemacro])
        
##########################################################################################

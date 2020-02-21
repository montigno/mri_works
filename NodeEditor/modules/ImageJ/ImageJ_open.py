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
        import subprocess
        from subprocess import Popen
        import os
        if file == 'path':
            file = ''
        script_macro = "run(\"Appearance...\", \"interpolate auto menu=15 gui=1 16-bit=Automatic\");"\
                       "run(\"Brightness/Contrast...\");"\
                       "run(\"Enhance Contrast\", \"saturated=0.35\");"
        subprocess.Popen(['ImageJ', file, '-eval',script_macro], shell=False)
        tmp = os.path.basename(file)
        self.currentImg = ('.').join(tmp.split('.')[:-1])
                
    def currentImage(self:'str'):
        return self.currentImg
    
##########################################################################################

class openImagej_multiFiles():

    def __init__(self, file=['path']):
        import subprocess
        from subprocess import Popen
        import os
        list_files = '|||'.join(file)
        script_macro = "run(\"Appearance...\", \"interpolate auto menu=15 gui=1 16-bit=Automatic\");"\
                       "run(\"Brightness/Contrast...\");"
        script_macro1 = "arg=" + "\"" + list_files + "\"" + ";"\
                        "list=split(arg,\"|||\");"\
                        "for (i=0;i<list.length;i++) {"\
                        "open(list[i]);"\
                        "run(\"Enhance Contrast\", \"saturated=0.35\");"\
                        "};"
        proc = subprocess.Popen(['ImageJ', '-eval', script_macro1+script_macro])
        
##########################################################################################

class ImageJ_macro():

    def __init__(self, file_macro='path'):
        import subprocess
        from subprocess import Popen
        import os
        option = '-macro'
        subprocess.Popen(['ImageJ', option, file_macro])
        
##########################################################################################

class ImageJ_macrofile():

    def __init__(self, pathImage='path', filemacro='path'):
        import subprocess
        from subprocess import Popen
        import os
        option = '-macro'
#         subprocess.call(['java','-jar',pathImageJ,pathImage,option,filemacro], shell=False)
        subprocess.Popen(['ImageJ', pathImage, option, filemacro])
        
##########################################################################################

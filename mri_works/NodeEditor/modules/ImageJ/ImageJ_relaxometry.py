class ImageJ_RelaxationTime_profil():

    def __init__(self, image='path', relax_Time='path', Intensity='path', Shift='path', 
                        ListTime=[0.0], time_type="enumerate(('EchoTime','RepetitionTime','InversionTime'))"):
        import subprocess
        from subprocess import Popen
        import os
        scriptfile= 'open("'+image+'");run(\"Enhance Contrast\", \"saturated=0.35\");\n'\
                    'open("'+relax_Time+'");run(\"Enhance Contrast\", \"saturated=0.35\");\n'\
                    'open("'+Intensity+'");run(\"Enhance Contrast\", \"saturated=0.35\");\n'
        script='var img1="'+os.path.basename(image)+'"; var img2="'+os.path.basename(relax_Time)+'"; var img3="'+os.path.basename(Intensity)+'";'
        if Shift!='path':
            scriptfile+='open("'+Shift+'");run(\"Enhance Contrast\", \"saturated=0.35\");\n'
            script+='var img4="'+os.path.basename(Shift)+'";'
            if time_type=='EchoTime':
                filemacro = os.path.join(os.path.dirname(os.path.abspath(__file__)),'macros', 'Macro_Profil_T2_with_shift.txt')
            elif time_type=='RepetitionTime':
                filemacro = os.path.join(os.path.dirname(os.path.abspath(__file__)),'macros', 'Macro_Profil_T1_with_shift.txt')
            elif time_type=='InversionTime':
                filemacro = os.path.join(os.path.dirname(os.path.abspath(__file__)),'macros', 'Macro_Profil_TInv_with_shift.txt')
        else:
            if time_type=='EchoTime':
                filemacro = os.path.join(os.path.dirname(os.path.abspath(__file__)),'macros', 'Macro_Profil_T2.txt')
            elif time_type=='RepetitionTime':
                filemacro = os.path.join(os.path.dirname(os.path.abspath(__file__)),'macros', 'Macro_Profil_T1.txt')
            elif time_type=='InversionTime':
                filemacro = os.path.join(os.path.dirname(os.path.abspath(__file__)),'macros', 'Macro_Profil_TInv.txt')
        
        scriptmacro = open(filemacro, 'r').read()
        script+='\nvar Times=newArray('+str(ListTime).strip('[]')+');\n'+scriptmacro+'\n'
        
        file_tmp = open("/tmp/tmp.txt", "w")
        file_tmp.write(script)
        script='run("Install...", "install=/tmp/tmp.txt");'
        subprocess.Popen(['ImageJ', '-eval', scriptfile, '-eval', script], shell=False)
        
##############################################################################


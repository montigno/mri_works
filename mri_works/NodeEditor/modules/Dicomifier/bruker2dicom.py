
##########################################################################################

class bruker2dicom_convert():
    def __init__(self, rep_data_bruker='path', rep_out='path'):
        import subprocess, os
        listRep1 = os.listdir(rep_out)
        lso = ("bruker2dicom convert", rep_data_bruker, rep_out)
        command = " ".join(lso)
        subprocess.run(command, shell=True, check=True)
        listRep2 = os.listdir(rep_out)
        tmp = [item for item in listRep2 if item not in listRep1]
        try:
            self.output_directory = os.path.join(rep_out,tmp[0])
        except:
            self.output_directory=''
        
    def out_diretory(self:'path'):
        return self.output_directory
        
##########################################################################################

class bruker2dicom_list():
    def __init__(self,rep_data_bruker='path'):
        from subprocess import Popen, PIPE
        lso = ("bruker2dicom list", rep_data_bruker)
        command = " ".join(lso)
        p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        txt, error = p.communicate()
        self.txt = txt.decode("utf-8")
        
    def outText(self:'str'):
        return self.txt
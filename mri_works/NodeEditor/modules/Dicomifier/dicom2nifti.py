class dicom2nifti_convert():
    def __init__(self,rep_data_dicom='path', rep_out='path'):
        import subprocess, os
        listRep1 = os.listdir(rep_out)
        lso = ("dicom2nifti", rep_data_dicom, rep_out)
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
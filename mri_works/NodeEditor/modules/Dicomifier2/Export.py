class bruker_to_dicom():
    def __init__(self, rep_data_bruker='path', rep_out='path'):
        import subprocess
        import os
        listRep1 = os.listdir(rep_out)
        lso = ("dicomifier to-dicom", rep_data_bruker, rep_out)
        command = " ".join(lso)
        subprocess.run(command, shell=True, check=True)
        listRep2 = os.listdir(rep_out)
        tmp = [item for item in listRep2 if item not in listRep1]
        try:
            self.output_directory = os.path.join(rep_out, tmp[0])
        except Exception as e:
            self.output_directory = ''

    def out_diretory(self: 'path'):
        return self.output_directory
    
##############################################################################

class dicom_to_nifti():
    def __init__(self, rep_data_dicom='path', rep_out='path'):
        import subprocess
        import os
        listRep1 = os.listdir(rep_out)
        lso = ("dicomifier to-nifti", rep_data_dicom, rep_out)
        command = " ".join(lso)
        subprocess.run(command, shell=True, check=True)
        listRep2 = os.listdir(rep_out)
        tmp = [item for item in listRep2 if item not in listRep1]
        try:
            self.output_directory = os.path.join(rep_out, tmp[0])
        except Exception as e:
            self.output_directory = ''

    def out_diretory(self: 'path'):
        return self.output_directory
    
##############################################################################

class bruker_to_nifti():
    def __init__(self, rep_data_bruker='path', rep_out='path'):
        import subprocess
        import os
        listRep1 = os.listdir(rep_out)
        lso = ("dicomifier to-nifti", rep_data_bruker, rep_out)
        command = " ".join(lso)
        subprocess.run(command, shell=True, check=True)
        listRep2 = os.listdir(rep_out)
        tmp = [item for item in listRep2 if item not in listRep1]
        try:
            self.output_directory = os.path.join(rep_out, tmp[0])
        except Exception as e:
            self.output_directory = ''

    def out_diretory(self: 'path'):
        return self.output_directory

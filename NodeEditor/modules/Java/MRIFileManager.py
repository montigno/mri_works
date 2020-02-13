############################################################################################################################

class BrukerToNifti:
    def __init__(self, Bruker_files=['path'],
                       naming='PatientName/StudyName/CreationDate-SeqNumber-Protocol-SequenceName-AcquisitionTime',
                       path_export='path',
                       bvals_bvecs=False):
        import os, sys
        from subprocess import Popen, PIPE
        from NodeEditor.python.configStandalone import ConfigModuls
        listBruker = ''
        for ls in Bruker_files:
            listBruker += ls + ";"            
        listBruker = listBruker[0:-1]
        options_export = "00000"
        if bvals_bvecs:
            options_export = "00013"
        command = 'java -classpath ' + ConfigModuls().getPathConfig('MRIFileManager') + \
                  ' BrukerToNifti \"' + listBruker + '\" ' + path_export + ' ' + naming + ' [ExportOptions] ' + options_export
        p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        txt, error = p.communicate()
        rc = p.returncode
        txt = txt.decode("utf-8") 
        txt = txt[txt.index("exported to ") + 12:]
        self.output = []
        for val in txt.split("exported to "):
            self.output.append(val[0:val.index("\n")])
    
    def list_files_exported(self:'list_path'):    
        return self.output

############################################################################################################################

class PhilipsToNifti:
    def __init__(self, Philips_files=['path'],
                       naming='PatientName/StudyName/CreationDate-SeqNumber-Protocol-SequenceName-AcquisitionTime',
                       path_export='path',
                       bvals_bvecs=False):
        import os, sys
        from subprocess import Popen, PIPE
        from NodeEditor.python.configStandalone import ConfigModuls
        listPhilips = ''
        for ls in Philips_files:
            listPhilips += ls + ";"
        listPhilips = listPhilips[0:-1]
        options_export = "00000"
        if bvals_bvecs:
            options_export = "00013"
        command = 'java -classpath ' + ConfigModuls().getPathConfig('MRIFileManager') + \
                  ' PhilipsToNifti \"' + listPhilips + '\" ' + path_export + ' ' + naming + ' [ExportOptions] ' + options_export
        p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        txt, error = p.communicate()
        rc = p.returncode
        txt = txt.decode("utf-8") 
        txt = txt[txt.index("exported to ") + 12:]
        self.output = []
        for val in txt.split("exported to "):
            self.output.append(val[0:val.index("\n")])
    
    def list_files_exported(self:'list_path'):    
        return self.output
    
############################################################################################################################

class BidsToNifti:
    def __init__(self, Bids_dir=['path'],
                       naming='PatientName/StudyName/CreationDate-SeqNumber-Protocol-SequenceName-AcquisitionTime',
                       path_export='path',
                       bvals_bvecs=False):
        import os, sys
        from subprocess import Popen, PIPE
        from NodeEditor.python.configStandalone import ConfigModuls
        listBids = ''
        for ls in Bids_dir:
            listBids += ls + ";"
        listBids = listBids[0:-1]
        options_export = "00000"
        if bvals_bvecs:
            options_export = "00013"
        command = 'java -classpath ' + ConfigModuls().getPathConfig('MRIFileManager') + \
                  ' BidsToNifti \"' + listBids + '\" ' + path_export + ' ' + naming + ' [ExportOptions] ' + options_export
        p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        txt, error = p.communicate()
        rc = p.returncode
        txt = txt.decode("utf-8") 
        txt = txt[txt.index("exported to ") + 12:]
        self.output = []
        for val in txt.split("exported to "):
            self.output.append(val[0:val.index("\n")])
    
    def list_files_exported(self:'list_path'):    
        return self.output
    

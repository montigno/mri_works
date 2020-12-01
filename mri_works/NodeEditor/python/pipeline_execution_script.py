##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

class executionScript:
    def __init__(self, txt, listDynamicValue, textEditor):
        self.listDynamicValueToReturn = {}
        inputsList = eval(txt[0:txt.index('\n')])
        textScript = '\n'.join(txt.split('\n')[1:-2])
        outputsList = eval(txt.splitlines()[-1])
        code = ''
        for lst in inputsList:
            az = lst.split('=')
            if ':' in az[1]:
                if type(listDynamicValue[az[1]]).__name__ == 'str':
                    code += az[0]+' = "'+str(listDynamicValue[az[1]])+'"\n'
                elif type(listDynamicValue[az[1]]).__name__ in ['float', 'int', 'bool', 'list', 'range', 'array']:
                    code += az[0]+' = '+str(listDynamicValue[az[1]])+'\n'
                elif type(listDynamicValue[az[1]]).__name__ in ['memmap']:
                    code += az[0]+' = '+str(listDynamicValue[az[1]].tolist())+'\n'
                elif type(listDynamicValue[az[1]]).__name__ in ['ndarray']:
                    code += az[0]+' = '+str(list(listDynamicValue[az[1]]))+'\n'
            else:
                code += lst+'\n'
        code += textScript+'\n'
        for lst in outputsList:
            az = lst.split(':')
            code += 'self.listDynamicValueToReturn["'+lst+'"]='+az[1]+'\n'
#         print(code)
        try:
            exec(code)
        except Exception as e:
            print("Script error: {0}".format(e))

    def getOutValues(self):
        return self.listDynamicValueToReturn

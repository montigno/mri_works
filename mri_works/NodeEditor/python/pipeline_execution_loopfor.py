##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################


import os
import ast
import numpy as np
from NodeEditor.python.PipeLine_Execution_SubMod import executionSubmod


class executionFor:
    def __init__(self, txt, listDynamicValue, textEditor, txtfull):

#         print('txt pipeline for : ')
#         print(txt)
#         print('txtfull pipeline for : ')
#         print(txtfull)
#         print('listDynamicValue : ')
#         print(listDynamicValue)

        listConnctIn = []
        listBlockExecution = []
        listBlock = {}
        listOut = []
        listModul = {}
        listConnctOut = []

        for i, ln in enumerate(txt.splitlines()):
            if i == 0:
                ln = ln.replace('\\', '\\\\')
                try:
                    listConnctIn.append(ast.literal_eval(ln))
                except Exception as e:
                    listConnctIn.append(ln)
                listConnctIn = listConnctIn[0]
            if i == 1:
                listBlockExecution.append(ast.literal_eval(ln))
                listBlockExecution = listBlockExecution[0]
            if i == 2:
                listBlock = ast.literal_eval(ln)
            if i == 3:
                listOut.append(ast.literal_eval(ln))
                listOut = listOut[0]
            if i == 4:
                listModul = ast.literal_eval(ln)
            if i == 5:
                listConnctOut.append(ast.literal_eval(ln))
                listConnctOut = listConnctOut[0]
            if i == 6:
                break

        listNodeValue = list(set(listOut))

        # listModulExecution={}
        for ls in listModul.keys():
            tmp = txtfull[txtfull.index('[submod '+ls):len(txtfull)]
            tmp1 = ''
            for i, ln in enumerate(tmp.splitlines()):
                if i < 7:
                    tmp1 += ln + '\n'
                elif i > 6:
                    break
#             listModulExecution[ls]=tmp1
            txt += '\n' + tmp1
            
        # listScriptExecution
        for ls in listBlockExecution:
            if 'S' in ls:
                tmp2 = txtfull[txtfull.index('[source '+ls):txtfull.index('[/source '+ls)+10+len(ls)]
                txt += '\n' + tmp2
                

        ######################################################################
        self.listDynamicValueSubToReturn = {}

        for kj in listConnctOut:
            tmp = kj[0:kj.index('=')]
            self.listDynamicValueSubToReturn[tmp] = []

        firstIndex = listConnctIn[0]
        firstIndex = firstIndex[0:firstIndex.index('=')]

        listDynamicValueSub = listDynamicValue.copy()

        tmp = []
        lengthEnter = range(len(listDynamicValue[firstIndex]))

        for ele in lengthEnter:
            for keyDyn, valDyn in listDynamicValue.items():
                if 'F' in keyDyn[0:keyDyn.index(':')]:
                    listDynamicValueSub[keyDyn] = valDyn[ele]
                    # print(self)
                    # print('listDynamicValueSub',listDynamicValueSub)

            try:
                a = executionSubmod(txt,
                                    listDynamicValueSub.copy(),
                                    textEditor,
                                    None)
                for keyR, valueR in a.getOutValues().items():
                    if 'ndarray' in type(valueR).__name__:
                        if ele == 0:
                            tmp = np.array(valueR)
                        else:
                            tmp = self.listDynamicValueSubToReturn[keyR]
                            tmp = np.vstack((tmp, valueR))
                    else:
                        tmp = self.listDynamicValueSubToReturn[keyR]
                        tmp.append(valueR)

                    self.listDynamicValueSubToReturn[keyR] = tmp

            except Exception as e:
                textEditor.append("<span style=\" \
                                   font-size:10pt; \
                                   font-weight:600; \
                                   color:#cc0000;\" \
                                   > Pipeline Execution For Loop  stopped : " +
                                    str(e) + "</span>")
                return

    def getOutValues(self):
        return self.listDynamicValueSubToReturn

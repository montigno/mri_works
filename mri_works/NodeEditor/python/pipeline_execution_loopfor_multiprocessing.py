##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################


import ast
import sys
import numpy as np
from multiprocessing import Process
from NodeEditor.python.PipeLine_Execution_SubMod import executionSubmod


class executionFor_proc:
    def __init__(self, txt, listDynamicValue, txtfull, modejoin):

        # print('txt pipeline for',txt)
        # print('txtfull pipeline for',txtfull)
        # print('list Dynamic Value multiprocess : ',listDynamicValue.keys())

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

#         listModulExecution = {}
        for ls in listModul.keys():
            tmp = txtfull[txtfull.index('[submod '+ls):len(txtfull)]
            tmp1 = ''
            for i, ln in enumerate(tmp.splitlines()):
                if i < 7:
                    tmp1 += ln+'\n'
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

        firstIndex = listConnctIn[0]
        firstIndex = firstIndex[0:firstIndex.index('=')]

        process = []

        listDynamicValueSub = listDynamicValue.copy()
        lengthEnter = range(len(listDynamicValue[firstIndex]))

        for ele in lengthEnter:
            for keyDyn, valDyn in listDynamicValue.items():
                if 'F' in keyDyn[0:keyDyn.index(':')]:
                    listDynamicValueSub[keyDyn] = valDyn[ele]
            process.append(Process(target=executionSubmod,
                                   args=(txt,
                                         listDynamicValueSub,
                                         None,
                                         None)))
            process[-1].start()

        if modejoin:
            for p in process:
                p.join()

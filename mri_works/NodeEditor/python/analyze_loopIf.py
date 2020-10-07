##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

import re
import ast
from NodeEditor.python.analyze_loopFor import analyzeLoopFor


class analyzeLoopIf:

    def __init__(self, keyF, valueF, listBlock,
                 listModul, ModulExecution, listArrowExtern, listConstants, listProbes):

        # valueF[0] : inputs
        # valueF[1] : outputs
        # valueF[2] : list of blocks
        # valueF[3] : list of arrows
        # valueF[4] : list of direct and intern arrows
        # print("analyzeLoopIf : ")
        # print("keyF : ",keyF)
        # print("valueF : ",valueF)
        # print("listBlock : ",listBlock)
        # print("listModul : ",listModul)
        # print("ModulExecution : ",ModulExecution)
        # print("listArrowExtern : ",listArrowExtern)
        # print("listConstants : ",listConstants)

        self.unit = keyF
        self.listBlockExecution = [[], []]

        listConstantsTrue = {}
        listConstantsFalse = {}

        if listConstants:
            for keyC, valC in listConstants.items():
                if keyF + ':out' in keyC:
                    try:
                        listConstantsTrue[keyC] = valC[0][0]
                    except Exception as e:
                        pass
                    try:
                        listConstantsFalse[keyC] = valC[1][0]
                    except Exception as e:
                        pass
                elif ':out' not in keyC:
                    listConstantsTrue[keyC] = valC
                    listConstantsFalse[keyC] = valC
        # print('listConstantsTrue : ',listConstantsTrue)
        # print('listConstantsFalse : ',listConstantsFalse)

        tmpvalueF3 = valueF[3].copy()
        for lb in eval(valueF[2])[1]:
            for keyl, vall in valueF[3].items():
                tmpUnitAmont = vall[0:vall.index(':')]
                tmpUnitAval = vall[vall.index('#Node#') + 6:]
                tmpUnitAval = tmpUnitAval[0:tmpUnitAval.index(':')]
                if lb == tmpUnitAmont or lb == tmpUnitAval:
                    try:
                        del tmpvalueF3[keyl]
                    except Exception as e:
                        pass
        tmpValueF = [valueF[0], valueF[1], str(eval(valueF[2])[0]), tmpvalueF3, valueF[4][0]]
        tmp = analyzeLoopFor(keyF, tmpValueF, listBlock, listModul, ModulExecution, listArrowExtern, listConstantsTrue, listProbes)
        self.listBlockExecution[0] = tmp.getListBlockExecution()
        self.executionTrue = tmp.getListForExecution()

        tmpvalueF3 = valueF[3].copy()
        for lb in eval(valueF[2])[0]:
            for keyl, vall in valueF[3].items():
                tmpUnitAmont = vall[0:vall.index(':')]
                tmpUnitAval = vall[vall.index('#Node#') + 6:]
                tmpUnitAval = tmpUnitAval[0:tmpUnitAval.index(':')]
                if lb == tmpUnitAmont or lb == tmpUnitAval:
                    try:
                        del tmpvalueF3[keyl]
                    except Exception as e:
                        pass
        tmpValueF = [valueF[0], valueF[1], str(eval(valueF[2])[1]), tmpvalueF3, valueF[4][1]]
        tmp = analyzeLoopFor(keyF, tmpValueF, listBlock, listModul, ModulExecution, listArrowExtern, listConstantsFalse, listProbes)
        self.listBlockExecution[1] = tmp.getListBlockExecution()
        self.executionFalse = tmp.getListForExecution()

    def getListIfExecution(self):
        txtTrue, txtFalse = '', ''
        txtTrue = '[loopif ' + self.unit + ' True]\n' + self.executionTrue
        txtFalse = '[loopif ' + self.unit + ' False]\n' + self.executionFalse
        return txtTrue + txtFalse

    def getListBlockExecution(self):
        return self.listBlockExecution

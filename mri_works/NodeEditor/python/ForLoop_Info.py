##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

import ast


class ForLoopInfo:
    def __init__(self, txt, txtfull):

        # print('txt in ForLoopInfo',txt)
        # print('txtfull in ForLoopInfo',txtfull)

        self.listConnctIn = []
        self.listBlockExecution = []
        self.listBlock = {}
        self.listOut = []
        self.listModul = {}
        self.listConnctOut = []

        for i, ln in enumerate(txt.splitlines()):
            if i == 0:
                ln = ln.replace('\\', '\\\\')
                try:
                    self.listConnctIn.append(ast.literal_eval(ln))
                except Exception as e:
                    self.listConnctIn.append(ln)
                self.listConnctIn = self.listConnctIn[0]
            if i == 1:
                self.listBlockExecution.append(ast.literal_eval(ln))
                self.listBlockExecution = self.listBlockExecution[0]
            if i == 2:
                self.listBlock = ast.literal_eval(ln)
            if i == 3:
                self.listOut.append(ast.literal_eval(ln))
                self.listOut = self.listOut[0]
            if i == 4:
                self.listModul = ast.literal_eval(ln)
            if i == 5:
                self.listConnctOut.append(ast.literal_eval(ln))
                self.listConnctOut = self.listConnctOut[0]
            if i == 6:
                break

        listNodeValue = list(set(self.listOut))

        self.txt = ''
        self.listModulExecution = {}

        for ls in self.listModul.keys():
            tmp = txtfull[txtfull.index('[submod '+ls):len(txtfull)]
            tmp1 = ''
            for i, ln in enumerate(tmp.splitlines()):
                if i < 7:
                    tmp1 += ln+'\n'
                elif i > 6:
                    break
            # self.listModulExecution[ls]=tmp1
            self.txt += '\n'+tmp1

        # print('self.txt in ForLoopInfo',self.txt)

    def getListInfo(self):
        return (self.listConnctIn,
                self.listBlockExecution,
                self.listBlock,
                self.listOut,
                self.listModul,
                self.listConnctOut,
                self.txt)

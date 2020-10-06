##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

import re
import ast
import sys
import os
from NodeEditor.python.analyze_loopFor import analyzeLoopFor
from NodeEditor.python.analyze_loopIf import analyzeLoopIf


class analyze:

    def __init__(self, txt, textEditor, mode):

        # initialize variables ##########################
        listArrow = {}
        self.listBlock, self.listModul = {}, {}
        self.listLoopFor, self.listLoopIf = {}, {}
        self.listModExecution = {}
        self.listConstantLoop = {}
        self.listScript = []
        listConnectInPos, listConnectOutPos = {}, {}
        listConstant, listProbe = {}, {}
        listConstantInLoopIf, listConstantInLoopFor = {}, {}
        tmpIn, tmpOut = {}, {}
        self.listOut = []
        self.listConnectIn, self.listConnectOut = [], []
        listBlockStart, listBlockRemaining, listBlockStop = [], [], []

        tmp = txt.splitlines()
        tmp.reverse()

        connectItem = False

        # create list ######################################
        for line in tmp:
            if line[0:4] == 'link':
                nameNode = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                nameNode = 'Node(' + nameNode + ')'
                line = line[line.index('node=') + 6:len(line) - 1]
                listArrow[nameNode] = line
                a, b, c, d = line.replace('#Node#',':').split(':')
                self.listOut.append(a+':'+b)
                if 'A' not in a :
                    if 'I' not in a and 'F' not in a:
                        listBlockStart.append(a)
                    elif 'in' not in b:
                        listBlockStart.append(a)
                    if 'C' not in c and 'P' not in c:
                        if 'I' not in c and 'F' not in c:
                            listBlockStop.append(c)
                        elif 'out' not in d:
                            listBlockStop.append(c)
                else:
                    listBlockStart.append(c)
 
            elif line[0:5] == 'block':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('category') + 10:len(line)]
                cat = line[0:line.index(']')]
                line = line[line.index('class') + 7:len(line)]
                classs = line[0:line.index(']')]
                line = line[line.index('valInputs') + 11:len(line)]
                Vinput = line[0:line.index('] RectF')]
                self.listBlock[unit] = (cat, classs, Vinput)

            elif line[0:6] == 'submod':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('nameMod') + 9:len(line)]
                nameMod = line[0:line.index(']')]
                line = line[line.index('valInputs') + 11:len(line)]
                Vinput = line[0:line.index('] RectF')]
                self.listModul[unit] = (nameMod, Vinput)
                path_submod = os.path.dirname(os.path.realpath(__file__))
                file = os.path.join(path_submod,
                                    '../submodules',
                                    nameMod + '.mod')
                f = open(file, 'r')
                txt = f.read()
                f.close()
                txt = txt[txt.index('[execution]') + 12:len(txt)]
                tmp1 = ''
                for i, ln in enumerate(txt.splitlines()):
                    if i < 6:
                        tmp1 += ln + '\n'
                self.listModExecution[unit] = tmp1

            elif line[0:7] == 'loopFor':
                unit = re.search(r"\[([A-Za-z0-9*_]+)\]", line).group(1)
                line = line[line.index('inputs') + 8:len(line)]
                vinput = line[0:line.index('] outputs')]
                line = line[line.index('outputs') + 9:len(line)]
                voutputs = line[0:line.index('] listItems')]
                line = line[line.index('listItems') + 11:len(line)]
                listItems = line[0:line.index('] RectF')]
                listTmp = []
                tmplistConstantInLoopFor = []
                for el in eval(listItems):
                    if 'A' not in el:
                        listTmp.append(el)
                    else:
                        tmplistConstantInLoopFor.append(el)
                listItems = str(listTmp)
                self.listLoopFor[unit] = [vinput, voutputs, listItems, {}]
                listConstantInLoopFor[unit] = tmplistConstantInLoopFor

            elif line[0:6] == 'loopIf':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('inputs') + 8:len(line)]
                vinput = line[0:line.index('] outputs')]
                line = line[line.index('outputs') + 9:len(line)]
                voutputs = line[0:line.index('] listItems')]
                line = line[line.index('listItems') + 11:len(line)]
                listItems = line[0:line.index('] RectF')]
                listTmp = [[], []]
                listLinkDirectIntern = [[], []]
                tmplistConstantInLoopIf = [[], []]
                for el in eval(listItems)[0]:
                    if 'A' not in el and 'N' not in el:
                        listTmp[0].append(el)
                    elif 'N' in el:
                        listLinkDirectIntern[0].append(el)
                    elif 'A' in el:
                        tmplistConstantInLoopIf[0].append(el)
                for el in eval(listItems)[1]:
                    if 'A' not in el and 'N' not in el:
                        listTmp[1].append(el)
                    elif 'N' in el:
                        listLinkDirectIntern[1].append(el)
                    elif 'A' in el:
                        tmplistConstantInLoopIf[1].append(el)
                listItems = str(listTmp)
                self.listLoopIf[unit] = [vinput,
                                         voutputs,
                                         listItems,
                                         {},
                                         listLinkDirectIntern]
                listConstantInLoopIf[unit] = tmplistConstantInLoopIf

            elif line[0:5] == 'connt':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('name') + 6:len(line)]
                nameConn = line[0:line.index(']')]
                line = line[line.index('type') + 6:len(line)]
                typInOut = line[0:line.index(']')]
                line = line[line.index('] RectF') + 6:len(line)]
                line = line[line.index(',') + 2:len(line)]
                posY = line[0:line.index(',')]
                connectItem = True

                if 'in' in typInOut:
                    tmpIn[unit] = nameConn
                    listConnectInPos[unit] = posY
                else:
                    tmpOut[unit] = nameConn
                    listConnectOutPos[unit] = posY

            elif line[0:8] == 'constant':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('value=') + 7:len(line)]
                vout = line[0:line.index('] format')]
                line = line[line.index('format=') + 8:len(line)]
                fort = line[0:line.index('] label')]
                if not fort:
                    fort = ''
                elif fort == 'path':
                    vout = vout.replace('\\n', '')
                elif fort == 'bool':
                    vout = eval(vout)
                try:
                    listConstant[unit] = (eval(vout), fort)
                except Exception as e:
                    listConstant[unit] = (vout, fort)

            elif line[0:6] == 'script':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                self.listScript.append(unit)
                
            elif line[0:5] == 'probe':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('label=') + 7:len(line)]
                lab = line[0:line.index(']')]
                line = line[line.index('format=') + 8:len(line)]
                form = line[0:line.index('] RectF')]
                listProbe[unit] = (form, lab) 

        # sort of connectors list ##########################

        if tmpIn:
            sorted_by_pos_In = sorted(listConnectInPos.items(),
                                      key=lambda kv: eval(kv[1]))
            for elem in sorted_by_pos_In:
                self.listConnectIn.append(elem[0] + ":" + tmpIn[elem[0]] + "=")

        if tmpOut:
            sorted_by_pos_Out = sorted(listConnectOutPos.items(),
                                       key=lambda kv: eval(kv[1]))
            for elem in sorted_by_pos_Out:
                self.listConnectOut.append(elem[0] + ":" + tmpOut[elem[0]])

        # attribute constants to elements #############################

        tmplistArrow = listArrow.copy()
        for keyArr, valueArr in tmplistArrow.items():
            tmp = valueArr
            tmpUnitstart = tmp[0:tmp.index(':')]
            if 'A' in tmpUnitstart:
                tmpUnitend = tmp[tmp.index('#Node#') + 6:len(tmp)]
                tmpUnitend = tmpUnitend[0:tmpUnitend.index(':')]
                tmpEntend = tmp[tmp.index('#Node#') + 6:len(tmp)]
                tmpEntend = tmpEntend[tmpEntend.index(':') + 1:len(tmpEntend)]
                if 'U' in tmpUnitend:
                    listInBl = self.listBlock[tmpUnitend]
                    listVal = listInBl[2]
                    nameEnter = eval(listVal)[0]
                    valEnter = eval(listVal)[1]
                    nameOut = eval(listVal)[2]
                    valOut = eval(listVal)[3]
                    ind = 0
                    for i, el in enumerate(nameEnter):
                        if el == tmpEntend:
                            ind = i
                            break
                    valEnter[ind] = listConstant[tmpUnitstart][0]
                    del self.listBlock[tmpUnitend]
                    self.listBlock[tmpUnitend] = (listInBl[0],
                                                  listInBl[1],
                                                  str((nameEnter,
                                                       valEnter,
                                                       nameOut,
                                                       valOut)))
                elif 'M' in tmpUnitend:
                    listInBl = self.listModul[tmpUnitend]
                    listVal = listInBl[1]
                    nameEnter = eval(listVal)[0]
                    valEnter = eval(listVal)[1]
                    nameOut = eval(listVal)[2]
                    valOut = eval(listVal)[3]
                    ind = 0
                    for i, el in enumerate(nameEnter):
                        if el == tmpEntend:
                            ind = i
                            break
                    valEnter[ind] = listConstant[tmpUnitstart][0]
                    del self.listModul[tmpUnitend]
                    self.listModul[tmpUnitend] = (listInBl[0],
                                                  str((nameEnter,
                                                       valEnter,
                                                       nameOut,
                                                       valOut)))
                elif 'I' in tmpUnitend:
                    tmpKey = tmpUnitend + ":" + tmpEntend
                    if 'out' in tmpEntend:
                        if tmpKey in self.listConstantLoop:  # already exist ?
                            tmpVal = self.listConstantLoop[tmpKey]
                        else:
                            tmpVal = [[], []]
                        if tmpUnitstart in listConstantInLoopIf[tmpUnitend][0]:
                            tmpVal[0].append(listConstant[tmpUnitstart][0])
                        elif tmpUnitstart in listConstantInLoopIf[tmpUnitend][1]:
                            tmpVal[1].append(listConstant[tmpUnitstart][0])
                        self.listConstantLoop[tmpKey] = tmpVal
                    else:
                        self.listConstantLoop[tmpKey] = listConstant[tmpUnitstart][0]

                elif 'F' in tmpUnitend:
                    tmpKey = tmpUnitend + ":" + tmpEntend
                    if 'out' in tmpEntend:
                        if tmpKey in self.listConstantLoop:  # already exist ?
                            tmpVal = self.listConstantLoop[tmpKey]
                        else:
                            tmpVal = []
                        if tmpUnitstart in listConstantInLoopFor[tmpUnitend]:
                            tmpVal.append(listConstant[tmpUnitstart][0])
                        self.listConstantLoop[tmpKey] = tmpVal[0]
                    else:
                        self.listConstantLoop[tmpKey] = listConstant[tmpUnitstart][0]

                # links from constants deleted from the listArrow
                del listArrow[keyArr]

        # search arrows within loop For ##########################

        listBlockStart = list(set(listBlockStart))
        listBlockStop = list(set(listBlockStop))

#         print('listBlockStart 0 : ', listBlockStart)
#         print('listBlockStop 0 : ', listBlockStop)
#         print('listConstantLoop 0 : ', self.listConstantLoop)
#         print('listArrow :  ', listArrow)

        if self.listLoopFor:
            for keyF, valueF in self.listLoopFor.items():
                tmplistItem = eval(valueF[2])
                listBlockStart = (list(set(listBlockStart) - set(tmplistItem)))
                listBlockStop = (list(set(listBlockStop) - set(tmplistItem)))

            listArrowFor = {}
            tmplistArrow = listArrow.copy()
            for keyA, valueA in tmplistArrow.items():
                a, b, c, d = valueA.replace('#Node#',':').split(':')
                for keyF, valueF in self.listLoopFor.items():
                    if keyF + ':in' in a + ':' + b or \
                        keyF + ':out' in c + ':' + d or \
                        (a in eval(self.listLoopFor[keyF][2]) and
                            keyF == a) or \
                            c in eval(self.listLoopFor[keyF][2]):
                        if keyA in listArrow.keys():
                            # links from LoopFor deleted from the listArrow
                            del listArrow[keyA]
                            listArrowFor = self.listLoopFor[keyF][3]
                            listArrowFor[keyA] = valueA
                            self.listLoopFor[keyF][3] = listArrowFor

        # search arrows within loop If ###############

        if self.listLoopIf:
            for keyF, valueF in self.listLoopIf.items():
                tmplistItem = eval(valueF[2])[0]
                listBlockStart = (list(set(listBlockStart) - set(tmplistItem)))
                listBlockStop = (list(set(listBlockStop) - set(tmplistItem)))
#             for keyF, valueF in self.listLoopIf.items():
                tmplistItem = eval(valueF[2])[1]
                listBlockStart = (list(set(listBlockStart) - set(tmplistItem)))
                listBlockStop = (list(set(listBlockStop) - set(tmplistItem)))

            listArrowIf = {}
            tmplistArrow = listArrow.copy()
            for keyA, valueA in tmplistArrow.items():
                a, b, c, d = valueA.replace('#Node#',':').split(':')
                for keyF, valueF in self.listLoopIf.items():
                    if (keyF + ':in' in a + ':' + b) or (
                        keyF + ':out' in c + ':' + d) or (
                        a in eval(self.listLoopIf[keyF][2])[0]) or (
                        c in eval(self.listLoopIf[keyF][2])[0]) or (
                        a in eval(self.listLoopIf[keyF][2])[1]) or (
                            c in eval(self.listLoopIf[keyF][2])[1]):
                        if keyA in listArrow.keys():
                            # links from LoopIf deleted from the listArrow
                            del listArrow[keyA]
                            listArrowIf = self.listLoopIf[keyF][3]
                            listArrowIf[keyA] = valueA
                            self.listLoopIf[keyF][3] = listArrowIf

        #######################################################################

#         print('listBlockStart 1 : ', listBlockStart)
#         print('listBlockStop 1 : ', listBlockStop)

        for i, lin in enumerate(self.listConnectOut):
            for lan in listArrow.values():
                if lin in lan:
                    tmp = lin + "=" + lan[0:lan.index('#Node#')]
                    self.listConnectOut[i] = tmp

        # search start and finish blocks ###################

        if len(listArrow) != 0:
            tmp = listBlockStart
            listBlockStart = (list(set(listBlockStart) - set(listBlockStop)))
            listBlockStop = (list(set(listBlockStop) - set(tmp)))
            listBlockRemaining = (list(set(tmp) - set(listBlockStart)))
        else:
            if len(self.listBlock) != 0:
                listBlockStart.extend(self.listBlock.keys())
            if len(self.listModul) != 0:
                listBlockStart.extend(self.listModul.keys())
            if len(self.listScript) != 0:
                listBlockStart.extend(self.listScript)
            listBlockStart = list(set(listBlockStart))

        listBlockStart = ReorderList(listBlockStart).getNewList()
        listBlockStop = ReorderList(listBlockStop).getNewList()

        # print('listBlockStart 2 : ', listBlockStart)
        # print('listBlockStop 2 : ', listBlockStop)

        self.textExecutionInLoopFor = {}
        self.listBlockExecutionInLoopFor = []
        if self.listLoopFor:
            for keyF, valueF in self.listLoopFor.items():
                tmplistItem = valueF[2]
                listBlockStart = (list(set(listBlockStart) - set(tmplistItem)))
                listBlockStop = (list(set(listBlockStop) - set(tmplistItem)))
                listBlockRemaining = (list(set(listBlockRemaining) - set(tmplistItem)))
                tmp = analyzeLoopFor(keyF,
                                     valueF,
                                     self.listBlock,
                                     self.listModul,
                                     self.listModExecution,
                                     listArrow,
                                     self.listConstantLoop)
                self.listBlockExecutionInLoopFor.append(keyF + ':' + str(tmp.getListBlockExecution()))
                self.textExecutionInLoopFor[keyF] = tmp.getListForExecution()
#                 print('getListForExecution : ',tmp.getListForExecution())

        self.textExecutionInLoopIf = {}
        self.listBlockExecutionInLoopIf = []
        if self.listLoopIf:
            for keyF, valueF in self.listLoopIf.items():
                tmplistItem = eval(valueF[2])[0]
                listBlockStart = (list(set(listBlockStart) - set(tmplistItem)))
                listBlockStop = (list(set(listBlockStop) - set(tmplistItem)))
                listBlockRemaining = (list(set(listBlockRemaining) - set(tmplistItem)))
                tmplistItem = eval(valueF[2])[1]
                listBlockStart = (list(set(listBlockStart) - set(tmplistItem)))
                listBlockStop = (list(set(listBlockStop) - set(tmplistItem)))
                listBlockRemaining = (list(set(listBlockRemaining) - set(tmplistItem)))
                tmp = analyzeLoopIf(keyF,
                                    valueF,
                                    self.listBlock,
                                    self.listModul,
                                    self.listModExecution,
                                    listArrow,
                                    self.listConstantLoop)
                self.listBlockExecutionInLoopIf.append(keyF + ':' + str(tmp.getListBlockExecution()))
                self.textExecutionInLoopIf[keyF] = tmp.getListIfExecution()

        #######################################################################

        # print('listLoopFor : ', self.listLoopFor)
        # print('listLoopIf : ', self.listLoopIf)
        # print('listArrow : ', listArrow)
        # print('listBlockStart : ', listBlockStart)
        # print('listBlockStop : ', listBlockStop)
        # print('listBlockRemaining 1 : ', listBlockRemaining)
        # print('textExecutionInLoopFor : ',self.textExecutionInLoopFor)
        # print('loopFor_values : ' , self.listLoopFor.values())

        # create list of remaining Block to execute in order ###########

        self.listBlockExecution = []
        listNodeValue = []
        tmpListBlock = []

        for startBlock in listBlockStart:
            if 'C' not in startBlock:
                tmpListBlock.append(startBlock)
            listValue = {}
            for ln in listArrow.keys():
                tmp = listArrow[ln]
                tmp = tmp[0:tmp.index("#Node#")]
                if startBlock + ':' in tmp:
                    outUnit = tmp[tmp.index(':') + 1:len(tmp)]
                    listNodeValue.append(tmp)
        if connectItem and len(tmpListBlock) > 1 and mode:
            self.listBlockExecution.append('ThreadOn')
            self.listBlockExecution.extend(tmpListBlock)
            self.listBlockExecution.append('ThreadOff')
        else:
            self.listBlockExecution.extend(tmpListBlock)

        listNodeValue = list(set(listNodeValue))

        # print('listBlockRemaining',listBlockRemaining)
        # print('listNodeValue',listNodeValue)

        listBlockRemainingNodeNeed1 = {}
        listBlockRemainingNodeGen1 = {}
        for ln in listArrow.values():
            tmpNeed = []
            tmpGen = []
            startArrow = ln[0:ln.index("#Node#")]
            endArrow = ln[ln.index("#Node#") + 6:len(ln)]
            startUnit = startArrow[0:startArrow.index(":")]
            endUnit = endArrow[0:endArrow.index(":")]
            # print("start & end : ",startArrow,",",endArrow,",",startUnit,",",endUnit)
            if endUnit in listBlockRemaining:
                try:
                    tmpNeed = listBlockRemainingNodeNeed1[endUnit]
                except Exception as e:
                    pass
                tmpNeed.append(startArrow)
                listBlockRemainingNodeNeed1[endUnit] = tmpNeed

            if startUnit in listBlockRemaining:
                try:
                    tmpGen = listBlockRemainingNodeGen1[startUnit]
                except Exception as e:
                    pass
                tmpGen.append(startArrow)
                listBlockRemainingNodeGen1[startUnit] = tmpGen

        # search block/subMod extern that loopfor is depending ############
        if self.listLoopFor:
            tmpList = []
            for key, val in self.listLoopFor.items():
                ggg = val[3].values()
                tmpList = [e[0:e.index('#Node#')] for e in ggg if [f for f in listBlockRemaining if (f + ":" in e) and (f != key)]]
                if tmpList:
                    if key in listBlockRemainingNodeNeed1:
                        tmpVal = listBlockRemainingNodeNeed1[key]
                        tmpVal.extend(tmpList)
                        listBlockRemainingNodeNeed1[key] = tmpVal
                    else:
                        listBlockRemainingNodeNeed1[key] = tmpList
                    for ele in tmpList:
                        unit = ele[0:ele.index(':')]
                        if unit in listBlockRemainingNodeGen1:
                            tmpVal = []
                            tmpVal.extend(listBlockRemainingNodeGen1[unit])
                            tmpVal.extend(ele)
                            listBlockRemainingNodeGen1[unit] = tmpVal
                        else:
                            try:
                                listBlockRemainingNodeGen1[unit] = tmpVal
                            except Exception as e:
                                listBlockRemainingNodeGen1[unit] = ele

        # search block/subMod extern that loopif is depending ############
        if self.listLoopIf:
            tmpList = []
            for key, val in self.listLoopIf.items():
                ggg = val[3].values()
                tmpList = [e[0:e.index('#Node#')] for e in ggg if [f for f in listBlockRemaining if (f + ":" in e) and (f != key)]]
                if tmpList:
                    if key in listBlockRemainingNodeNeed1:
                        tmpVal = listBlockRemainingNodeNeed1[key]
                        tmpVal.extend(tmpList)
                        listBlockRemainingNodeNeed1[key] = tmpVal
                    else:
                        listBlockRemainingNodeNeed1[key] = tmpList
                    for ele in tmpList:
                        unit = ele[0:ele.index(':')]
                        if unit in listBlockRemainingNodeGen1:
                            tmpVal = listBlockRemainingNodeGen1[unit]
                            tmpVal.append(ele)
                            listBlockRemainingNodeGen1[unit] = tmpVal
                        else:
                            try:
                                listBlockRemainingNodeGen1[unit] = tmpVal
                            except Exception as e:
                                listBlockRemainingNodeGen1[unit] = ele

        # print('listBlockRemainingNodeNeed1 2', len(listBlockRemainingNodeNeed1), listBlockRemainingNodeNeed1)
        # print('listBlockRemainingNodeGen1 2', len(listBlockRemainingNodeGen1), listBlockRemainingNodeGen1)
        # print('listBlockRemaining 2 : ', listBlockRemaining)

        while len(listBlockRemaining) != 0:
            tmpListlistBlockRemaining = listBlockRemaining.copy()
            tmpListNodeValue = []
            tmpListBlock = []
            # print('listBlockRemainingNodeNeed1 = ',listBlockRemainingNodeNeed1)
            for remainingBlock in tmpListlistBlockRemaining:
                # print('remainingBlock',remainingBlock)
                if all(x in listNodeValue for x in listBlockRemainingNodeNeed1[remainingBlock]):
                    # print('remainingBlock selected',remainingBlock)
                    # self.listBlockExecution.append(remainingBlock)
                    tmpListBlock.append(remainingBlock)
                    try:
                        tmpListNodeValue.extend(listBlockRemainingNodeGen1[remainingBlock])
                    except Exception as e:
                        pass
                    listBlockRemaining.remove(remainingBlock)
            # print('tmpListBlock : ',tmpListBlock)

            if len(tmpListBlock) > 1 and mode:
                # to avoid to put block/subMod and loopfor in same thread if forloop depending of this block/subMod #
                listF = [e for e in tmpListBlock if 'F' in e]
                listI = [e for e in tmpListBlock if 'I' in e]
                listB = [e for e in tmpListBlock if 'U' in e]
                listB.extend([e for e in tmpListBlock if 'M' in e])
                # print('listF & listB : ',listF,' , ',listB)

                if listF and listB:
                    tmpListBlock1 = []
                    tmpListBlock2 = []
                    for i in range(len(listF)):
                        ggg = self.listLoopFor[listF[i]][3].values()
                        tmpListBlock1.extend([e for e in listB if [f for f in ggg if e + ":" in f]])
                    if tmpListBlock1:
                        tmpListBlock1 = list(set(tmpListBlock1))
                        tmpListBlock2 = list(set(tmpListBlock) - set(tmpListBlock1))
                        if len(tmpListBlock1) > 1 and mode:
                            tmpListBlock = ['ThreadOn']
                            tmpListBlock.extend(tmpListBlock1)
                            tmpListBlock.append('ThreadOff')
                        else:
                            tmpListBlock = tmpListBlock1
                        if len(tmpListBlock2) > 1 and mode:
                            tmpListBlock.append('ThreadOn')
                            tmpListBlock.extend(tmpListBlock2)
                            tmpListBlock.append('ThreadOff')
                        else:
                            tmpListBlock.extend(tmpListBlock2)
                        self.listBlockExecution.extend(tmpListBlock)
                    else:
                        self.listBlockExecution.append('ThreadOn')
                        self.listBlockExecution.extend(tmpListBlock)
                        self.listBlockExecution.append('ThreadOff')
                else:
                    self.listBlockExecution.append('ThreadOn')
                    self.listBlockExecution.extend(tmpListBlock)
                    self.listBlockExecution.append('ThreadOff')

                # self.listBlockExecution.append('ThreadOn')
                # self.listBlockExecution.extend(tmpListBlock)
                # self.listBlockExecution.append('ThreadOff')

            else:  # if len(tmpListBlock) == 1
                self.listBlockExecution.extend(tmpListBlock)
            if tmpListNodeValue:
                listNodeValue.extend(tmpListNodeValue)

        listBlockStop.sort()
        tmpListBlock = []
        for endBlocks in listBlockStop:
            tmpListBlock.append(endBlocks)
            # self.listBlockExecution.append(endBlocks)
        if connectItem and len(tmpListBlock) > 1 and mode:
            self.listBlockExecution.append('ThreadOn')
            self.listBlockExecution.extend(tmpListBlock)
            self.listBlockExecution.append('ThreadOff')
        else:
            self.listBlockExecution.extend(tmpListBlock)
            
        
        ######################################################

        # replace Node() by listOut corresponding ###################################################
        for listB in self.listBlock.keys():
            tmp = eval(self.listBlock[listB][2])
            if tmp[1] is not None:
                for index, item in enumerate(tmp[1]):
                    if type(item).__name__ == 'str':
                        if 'Node' in item:
                            try:
                                st = listArrow[item]
                                st = st[0:st.index('#Node#')]
                                tmp[1][index] = st
                                self.listBlock[listB] = (self.listBlock[listB][0], self.listBlock[listB][1], str(tmp))
                            except Exception as e:
                                pass

        # delete in listBlock of diagram elements which are in loopfor yet ##
        tmp1 = self.listBlock.copy()
        tmp = tmp1.keys()
        for el in tmp:
            if el not in self.listBlockExecution:
                del self.listBlock[el]
                for fg in self.listOut:
                    if el + ':' in fg:
                        self.listOut.remove(fg)

        # delete in listModul of diagram elements which are in loopfor yet ###
        tmp2 = self.listModul.copy()
        tmp = tmp2.keys()
        for el in tmp:
            if el not in self.listBlockExecution:
                del self.listModul[el]
                del self.listModExecution[el]
                for fg in self.listOut:
                    if el + ':' in fg:
                        self.listOut.remove(fg)

        # detect input and ouput of submodul and erase output not used #####
        for listM in self.listModul.keys():
            tmp = eval(self.listModul[listM][1])
            for index, item in enumerate(tmp[1]):
                if type(item).__name__ == 'str':
                    if 'Node' in item:
                        try:
                            st = listArrow[item]
                            st = st[0:st.index('#Node#')]
                            tmp[1][index] = st
                            self.listModul[listM] = (self.listModul[listM][0], str(tmp))
                        except Exception as e:
                            pass
            tmp = eval(self.listModul[listM][1])

            txtExc = self.listModExecution[listM]

            listConnctIn = []
            listConnctOut = []
            for i, ln in enumerate(txtExc.splitlines()):
                if i == 0:
                    tss = ast.literal_eval(ln)
                    listConnctIn.append(tss)
                if i == 5:
                    listConnctOut.append(ast.literal_eval(ln))

            for li in listConnctIn[0]:
                for i, hh in enumerate(tmp[0]):
                    if hh in li:
                        tmpa = li + str(tmp[1][i])
                txtExc = txtExc.replace(str(li), tmpa)
                liq = li[0:len(li) - 1]
                tmps = listM + ':' + liq[liq.index(':') + 1:len(liq)]
                # txtExc=txtExc.replace(str(liq),tmps)
                # txtExc=txtExc.replace('\\','\\\\')

            for li in listConnctOut[0]:
                txtExc = txtExc.replace(li, listM + ':' + li[li.index(':') + 1:len(li)])

            self.listModExecution[listM] = txtExc
            
        # place list probe in listBlockExecution #############
        if listProbe:
            for klink, vlink in listArrow.items():
                a, b, c, d = vlink.replace("#Node#",':').split(':')
                if 'P' in c:
                    indx = self.listBlockExecution.index(a)
                    if 'ThreadOn' in self.listBlockExecution:
                        for i in range(indx, len(self.listBlockExecution)):
                            if self.listBlockExecution[i] == 'ThreadOn':
                                break
                            elif self.listBlockExecution[i] == 'ThreadOff':
                                indx=i
                                break
                    self.listBlockExecution.insert(indx+1, c)
                    self.listBlock[c] = (listProbe[c][0], listProbe[c][1], a+':'+b)

######################################################################

        textEditor.clear()
        textEditor.append("<span style=\" \
                           font-size:10pt; \
                           font-weight:600; \
                           color:#000000;\" >Sequence of tasks :</span>")
        textEditor.append("<span style=\" \
                           font-size:8pt; \
                           font-weight:600; \
                           color:#000000;\" >" + str(self.listBlockExecution) + "</span>")
        textEditor.append("<span style=\" \
                           font-size:8pt; \
                           font-weight:600; \
                           color:#000000;\" >" + str(self.listBlockExecutionInLoopFor) + "</span>")
        textEditor.append("<span style=\" \
                           font-size:8pt; \
                           font-weight:600; \
                           color:#000000;\" >" + str(self.listBlockExecutionInLoopIf) + "</span>")

    def getListForExecution(self):
        txtlist = str(self.listConnectIn) + '\n' + \
                    str(self.listBlockExecution) + '\n' + \
                    str(self.listBlock) + '\n' + \
                    str(self.listOut) + '\n' + \
                    str(self.listModul) + '\n' + \
                    str(self.listConnectOut) + '\n'
        txt2, txt3, txt4 = '', '', ''
        for df in self.listModExecution:
            txt2 += '[submod ' + df + ']\n' + self.listModExecution[df]
        for db in self.textExecutionInLoopFor:
            txt3 += '[loopfor ' + db + ']\n' + self.textExecutionInLoopFor[db]
        for de in self.textExecutionInLoopIf:
            txt4 += self.textExecutionInLoopIf[de]
        return txtlist + txt2 + txt3 + txt4


class ReorderList:

    def __init__(self, list):
        listOrder = self.sorted_nicely(list)
        self.list = listOrder

    def sorted_nicely(self, lst):
        convert = lambda text: int(text) if text.isdigit() else text
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        return sorted(lst, key=alphanum_key)

    def getNewList(self):
        return self.list

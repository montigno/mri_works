##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

import re
import ast


class analyzeLoopFor:

    def __init__(self, keyF, valueF, listBlock,
                 listModul, ModulExecution, listArrowExtern, listConstants, listProbes):

        # valueF[0] : inputs
        # valueF[1] : outputs
        # valueF[2] : list of blocks
        # valueF[3] : list of arrows
        # valueF[4] : list of arrows

        # print('keyF', keyF)
        # print('valueF', valueF)
        # print('listBlock', listBlock)
        # print('listModul', listModul)
        # print('ModulExecution', ModulExecution)
        # print('listArrowExtern', listArrowExtern)
        # print('listConstants', listConstants)

        listBlockStart = []
        listBlockRemaining = []
        listBlockStop = []

        self.listBlock = {}
        self.listModul = {}
        self.listModExecution = ModulExecution.copy()

        listBlockIntern = eval(valueF[2])
        self.listOut = []

        self.listConnectIn = []
        self.listConnectOut = []

# search listBlock and listModul in Loop ###########################
        for keyLb, valueLb in listBlock.items():
            if keyLb in listBlockIntern:
                self.listBlock[keyLb] = valueLb
        for keyLm, valueLm in listModul.items():
            if keyLm in listBlockIntern:
                self.listModul[keyLm] = valueLm

# search value ForLoop inputs and outputs #########################
        for keyAe, valueAe in listArrowExtern.items():
            tmp1 = valueAe
            tmp1 = tmp1[tmp1.index('#Node#') + 6:len(tmp1)]
            if keyF + ':in' in tmp1 or keyF+':val' in tmp1:
                self.listConnectIn.append(tmp1 +
                                          '=' +
                                          valueAe[0:valueAe.index('#Node#')])
        #     tmp2 = valueAe
        #     tmp2=tmp2[tmp2.index('#Node#')+6:len(tmp2)]
        #     if keyF+':out' in tmp1:
        #          self.listConnectOut.append(tmp1+'='+valueAe[0:valueAe.index('#Node#')])

        listArrowIntern = valueF[3]
        for keyAi, valueAi in listArrowIntern.items():
            tmp1 = valueAi[valueAi.index('#Node#') + 6:len(valueAi)]
            unittmp1 = tmp1[0:tmp1.index(':')]
            tmp2 = valueAi[0:valueAi.index('#Node#')]
            unittmp2 = tmp2[0:tmp2.index(':')]
            if keyF + ':out' in tmp1 and unittmp1 != unittmp2:
                # if unittmp1 == unittmp2 => link direct in loopIf
                self.listConnectOut.append(tmp1 + '=' + tmp2)

        if listConstants:
            for keyConst, valConst in listConstants.items():
                if ':in' in keyConst or ':val' in keyConst:
                    self.listConnectIn.append(keyConst+'='+str(valConst))
                else:
                    self.listConnectOut.append(keyConst+'='+str(valConst))

# search direct link in loop If ###############################
        # in case of loopIf
        if len(valueF) == 5:
            tmpVal = valueF[4]
            for el in tmpVal:
                tmpArrow = listArrowIntern['Node('+el+')']
                tmp1 = tmpArrow[tmpArrow.index('#Node#') + 6:]
                tmp2 = tmpArrow[0:tmpArrow.index('#Node#')]
                self.listConnectOut.append(tmp1 + '=' + tmp2)

# search sequence of stacks #####################################
        tmplistArrowIntern = {}
        for keyAi, valueAi in listArrowIntern.items():
            tmp = valueAi
            de = tmp[0:tmp.index(':')]
            self.listOut.append(tmp[0:tmp.index('#Node#')])
            tmp = tmp[tmp.index('#Node#') + 6:len(tmp)]
            df = tmp[0:tmp.index(':')]

            if keyF not in de and \
               keyF not in df and \
               ((de in self.listBlock.keys() or
                de in self.listModul.keys()) and \
               (df in self.listBlock.keys() or df in self.listModul.keys()) or \
               (de in listBlockIntern and df in listBlockIntern)):
                listBlockStart.append(de)
                listBlockStop.append(df)
                tmplistArrowIntern[keyAi] = valueAi
                        

#         print(self)
#         print('listBlockStart LoopFor',listBlockStart)
#         print('listBlockRemaining LoppFor',listBlockRemaining)
#         print('listBlockStop LoopFor',listBlockStop)
#         print('tmplistArrowIntern',tmplistArrowIntern)
#         print('listArrowIntern',listArrowIntern)

        tmp = (list(set(listBlockIntern) -
                    set(listBlockStart) -
                    set(listBlockStop)))
       
        for lb in tmp:
            listBlockStart.append(lb)

        if tmplistArrowIntern:
            tmp = listBlockStart
            listBlockStart = (list(set(listBlockStart) - set(listBlockStop)))
            listBlockStop = (list(set(listBlockStop) - set(tmp)))
        #      listBlockRemaining = (list(set(tmp)-set(listBlockStart)))
            listBlockRemaining = (list(set(listBlockIntern) -
                                       set(listBlockStart) -
                                       set(listBlockStop)))

        elif listBlockIntern:
            listBlockStart = list(set(listBlockIntern))
        #     listBlockStart=list(set(listBlockIntern.keys()))
        # else:
        #     listBlockStart=list(set(self.listModul.keys()))

        # print('listBlockStart LoopFor',listBlockStart)
        # print('listBlockRemaining',listBlockRemaining)
        # print('listBlockStop LoopFor',listBlockStop)

        listBlockStart = ReorderList(listBlockStart).getNewList()
        listBlockStop = ReorderList(listBlockStop).getNewList()

        # print('listBlockStart LoopFor',listBlockStart)
        # print('listBlockRemaining LoopFor',listBlockRemaining)
        # print('listBlockStop LoopFor',listBlockStop)

# create list of Block to execute in order###########
        self.listBlockExecution = []
        listNodeValue = []

        for startBlock in listBlockStart:
            self.listBlockExecution.append(startBlock)
            listValue = {}
            for ln in tmplistArrowIntern.keys():
                tmp = tmplistArrowIntern[ln]
                tmp = tmp[0:tmp.index("#Node#")]
                if startBlock + ':' in tmp:
                    outUnit = tmp[tmp.index(':') + 1:len(tmp)]
                    listNodeValue.append(tmp)
        if len(self.listBlockExecution) > 1:
            self.listBlockExecution = ['ThreadOn'] + \
                                      self.listBlockExecution + \
                                      ['ThreadOff']

        listNodeValue = list(set(listNodeValue))

        if len(listBlockRemaining) > 1:
            listBlockRemainingNodeNeed1 = {}
            listBlockRemainingNodeGen1 = {}
            for ln in tmplistArrowIntern.values():
                tmpNeed = []
                tmpGen = []
                startArrow = ln[0:ln.index("#Node#")]
                endArrow = ln[ln.index("#Node#") + 6:len(ln)]
                startUnit = startArrow[0:startArrow.index(":")]
                endUnit = endArrow[0:endArrow.index(":")]

                if endUnit in listBlockRemaining and 'F' not in startUnit:
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

        #     print(self)
        #     print('listBlockRemainingNodeNeed1',len(listBlockRemainingNodeNeed1),listBlockRemainingNodeNeed1)
        #     print('listBlockRemainingNodeGen1',len(listBlockRemainingNodeGen1),listBlockRemainingNodeGen1)
        #     print('listBlockRemaining',listBlockRemaining)
        #     print('listNodeValue',listNodeValue)
        #     print('listArrowIntern',listArrowIntern)

            while len(listBlockRemaining) != 0:
                tmpListlistBlockRemaining = listBlockRemaining.copy()
                tmpListNodeValue = []
        #         self.listBlockExecution.append('ThreadOn')
                for remainingBlock in tmpListlistBlockRemaining:
                    tmp = []
                    if all(x in listNodeValue for x in listBlockRemainingNodeNeed1[remainingBlock]):
                        tmp.append(remainingBlock)
        #                 self.listBlockExecution.append(remainingBlock)
                        try:
                            tmpListNodeValue.extend(listBlockRemainingNodeGen1[remainingBlock])
                        except Exception as e:
                            pass
                        listBlockRemaining.remove(remainingBlock)
        #         self.listBlockExecution.append('ThreadOff')
                        if len(tmp) > 1:
                            tmp = ['ThreadOn'] + tmp + ['ThreadOff']
                        self.listBlockExecution.extend(tmp)
                if tmpListNodeValue:
                    listNodeValue.extend(tmpListNodeValue)

#             if len(tmp) > 1:
#                 tmp = ['ThreadOn'] + tmp + ['ThreadOff']
#             self.listBlockExecution.extend(tmp)

        elif len(listBlockRemaining) == 1:
            self.listBlockExecution.append(listBlockRemaining[0])

#         self.listBlockExecution.append('ThreadOn')
        tmp = []
        for endBlocks in listBlockStop:
            tmp.append(endBlocks)
#             self.listBlockExecution.append(endBlocks)
#         self.listBlockExecution.append('ThreadOff')
        if len(tmp) > 1:
            tmp = ['ThreadOn'] + tmp + ['ThreadOff']
        self.listBlockExecution.extend(tmp)

# replace Node() by listOut corresponding #######################
        for listB in self.listBlock.keys():
            tmp = eval(self.listBlock[listB][2])
            if tmp[1] is not None:
                for index, item in enumerate(tmp[1]):
                    if type(item).__name__ == 'str':
                        if 'Node' in item:
                            try:
                                st = listArrowIntern[item]
                                st = st[0:st.index('#Node#')]
                                tmp[1][index] = st
                                self.listBlock[listB] = (self.listBlock[listB][0],
                                                         self.listBlock[listB][1],
                                                         str(tmp))
                            except Exception as e:
                                pass
# relist listModExecution ##################################
        tmp2 = self.listModExecution.copy()
        tmp = tmp2.keys()
        for el in tmp:
            if el not in self.listBlockExecution:
                del self.listModExecution[el]

# detect input and ouput of submodul and erase output not used ####
        for listM in self.listModul.keys():
            tmp = eval(self.listModul[listM][1])
            for index, item in enumerate(tmp[1]):
                if type(item).__name__ == 'str':
                    if 'Node' in item:
                        try:
                            st = listArrowIntern[item]
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
#                 txtExc=txtExc.replace(str(liq),tmps)
#                 txtExc=txtExc.replace('\\','\\\\')

            for li in listConnctOut[0]:
                txtExc = txtExc.replace(li, listM + ':' + li[li.index(':') + 1:len(li)])

            self.listModExecution[listM] = txtExc

# end of analyze for loop #######################

        # place list probe in listBlockExecution #############
        if listProbes:
            for klink, vlink in listArrowIntern.items():
                a, b, c, d = vlink.replace("#Node#", ':').split(':')
                if 'P' in c:
                    self.listBlockExecution.remove(c)
                    if keyF == a:
                        self.listBlockExecution.insert(0, c)
                    else:
                        indx = self.listBlockExecution.index(a)
                        if 'ThreadOn' in self.listBlockExecution:
                            for i in range(indx, len(self.listBlockExecution)):
                                if self.listBlockExecution[i] == 'ThreadOn':
                                    break
                                elif self.listBlockExecution[i] == 'ThreadOff':
                                    indx = i
                                    break
                        self.listBlockExecution.insert(indx+1, c)
                    self.listBlock[c] = (listProbes[c][0], listProbes[c][1], a+':'+b)

    def getListForExecution(self):
        txtlist = str(self.listConnectIn) + '\n' + \
                    str(self.listBlockExecution) + '\n' + \
                    str(self.listBlock) + '\n' + \
                    str(self.listOut) + '\n' + \
                    str(self.listModul) + '\n' + \
                    str(self.listConnectOut) + '\n'
        txt2 = ''
        for df in self.listModExecution:
            txt2 += '[submod ' + df + ']\n' + self.listModExecution[df]
#         print("listForExecution : ",txtlist + txt2)
        return txtlist + txt2

    def getListBlockExecution(self):
        return self.listBlockExecution


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

#!/usr/bin/python
##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

import importlib
import re
import ast
import sys
import os
import threading
import numpy as np
from PyQt5.QtCore import QDir
from NodeEditor.python.ForLoop_Info import ForLoopInfo


class executionSubmod:

    def __init__(self, txt, listDynamicValue, textEditor, modul):

        # print('txt execution SubMod ')
        # print(txt)
        # print(listDynamicValue)

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

        listModExecution = {}

        if modul:
            for ls in listModul.keys():
                file = os.path.join(QDir.currentPath(),
                                    'NodeEditor',
                                    'submodules',
                                    modul[0] + '.mod')
                f = open(file, 'r')
                txt = f.read()
                f.close()
                tmp = txt[txt.index('[submod ' + ls):len(txt)]
                tmp1 = ''
                for i, ln in enumerate(tmp.splitlines()):
                    if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                        tmp1 += ln + '\n'
                listModExecution[ls] = tmp1
        else:
            for ls in listModul.keys():
                tmp = txt[txt.index('[submod ' + ls):len(txt)]
                tmp1 = ''
                for i, ln in enumerate(tmp.splitlines()):
                    if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                        tmp1 += ln + '\n'
                    elif i > 6:
                        break
                listModExecution[ls] = tmp1

        listForExecution = {}
        listIfExecution = {}
        for ls in listBlockExecution:
            if 'F' in ls:
                file = os.path.join(QDir.currentPath(),
                                    'NodeEditor',
                                    'submodules',
                                    modul[0] + '.mod')
                f = open(file, 'r')
                txt = f.read()
                f.close()
                tmp = txt[txt.index('[loopfor ' + ls):len(txt)]
                tmp1 = ''
                for i, ln in enumerate(tmp.splitlines()):
                    if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                        tmp1 += ln + '\n'
                    elif i > 6:
                        break
                listForExecution[ls] = tmp1
            elif 'I' in ls:
                file = os.path.join(QDir.currentPath(),
                                    'NodeEditor',
                                    'submodules',
                                    modul[0] + '.mod')
                f = open(file, 'r')
                txt = f.read()
                f.close()
                tmp = txt[txt.index('[loopif ' + ls + ' True]'):len(txt)]
                tmp1 = ''
                for i, ln in enumerate(tmp.splitlines()):
                    if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                        tmp1 += ln + '\n'
                    elif i > 6:
                        break
                listIfExecution[ls + '-true'] = tmp1
                tmp = txt[txt.index('[loopif ' + ls + ' False]'):len(txt)]
                tmp2 = ''
                for i, ln in enumerate(tmp.splitlines()):
                    if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                        tmp2 += ln + '\n'
                    elif i > 6:
                        break
                listIfExecution[ls + '-false'] = tmp2

        ######################################################################

        threadcurrent = False
        threads = []

        for execution in listBlockExecution:
            if 'ThreadOn' in execution:
                threadcurrent = True
                threads = []
            elif 'ThreadOff' in execution:
                if threads:
                    [thread.start() for thread in threads]
                    [listDynamicValue.update(thread.join()) for thread in threads]
                threadcurrent = False
            if ('M' not in execution and
                    'Thread' not in execution and
                    'F' not in execution and 'I' not in execution):
                category = listBlock[execution][0]
                classes = listBlock[execution][1]
                module = importlib.import_module('NodeEditor.modules.' + category)
                MyClass = getattr(module, classes)
                tmp = eval(listBlock[execution][2])
                Enters = tmp[0]
                outUnit = []
                for lsi in listNodeValue:
                    if execution + ':' in lsi:
                        outUnit.append(lsi)
                if tmp[1] is None:
                    if threadcurrent:
                        threads.append(ThreadClass(MyClass, None, outUnit))
                    else:
                        a = MyClass()
                else:
                    for index, item in enumerate(tmp[1]):
                        if type(item).__name__ == 'str':
                            try:
                                gg = tmp[1][index]
                                tmp[1][index] = listDynamicValue[tmp[1][index]]
                        # try delete nodes which are no longer useful
                                if gg in listOut:
                                    listOut.remove(gg)
                                if gg not in listOut:
                                    del listDynamicValue[gg]
                            except Exception as e:
                                pass
                    try:
                        list3 = dict(zip(Enters, tmp[1]))
                        if threadcurrent:
                            threads.append(ThreadClass(MyClass,
                                                       list3,
                                                       outUnit))
                        else:
                            a = MyClass(**list3)
                    except Exception as e:
                        return
                if not threadcurrent:
                    for lsi in listNodeValue:
                        if execution + ':' in lsi:
                            outUnit = lsi[lsi.index(':') + 1:len(lsi)]
                            value = getattr(a, outUnit)
                            try:
                                listDynamicValue[lsi] = value()
                            except Exception as e:
                                listDynamicValue[lsi] = value

            elif 'M' in execution:
                listDynamicValueSub2 = {}
                txtCurrentSubmod = listModExecution[execution].splitlines()[0]
                txtCurrentSubmod = txtCurrentSubmod.replace('\\', '\\\\')
                txtCurrentSubmod = txtCurrentSubmod[1:len(txtCurrentSubmod) - 1]
                for li in txtCurrentSubmod.split(','):
                    st = li[li.index("'") + 1:li.index('=')]
                    ed = li[li.index('=') + 1:len(li) - 1]
                    if ':' in ed and '\\' not in ed:
                        listDynamicValueSub2[st] = listDynamicValue[ed]
                    else:
                        try:
                            listDynamicValueSub2[st] = eval(ed)
                        except Exception as e:
                            listDynamicValueSub2[st] = ed
                try:
                    a = executionSubmod(listModExecution[execution],
                                        listDynamicValueSub2,
                                        None,
                                        listModul[execution])
                    for uj in a.getOutValues().keys():
                        listDynamicValue[uj] = a.getOutValues()[uj]
                except Exception as e:
                    return

            elif 'I' in execution:
                self.listDynamicValueIf = {}
                txtIf = listIfExecution[execution + '-true']
                txtCurrentIf = txtIf.splitlines()[0]
                txtCurrentIf = txtCurrentIf.replace('\\', '\\\\')
                txtCurrentIf = eval(txtCurrentIf)
                for indif in txtCurrentIf:
                    if execution + ':val' in indif:
                        tmpVal = indif[indif.index('=') + 1:]
                        txtCurrentIf.remove(indif)
                for li in txtCurrentIf:
                    st = li[0:li.index('=')]
                    ed = li[li.index('=') + 1:len(li)]
                    self.listDynamicValueIf[st] = listDynamicValue[ed]
                try:
                    if not listDynamicValue[tmpVal]:
                        txtIf = listIfExecution[execution + '-false']
                except Exception as e:
                    pass

                tmpMod = eval(txtIf.split('\n')[4]).keys()
                for mod in tmpMod:
                    tmp = txt[txt.index('[submod ' + mod):len(txt)]
                    tmp1 = ''
                    for i, ln in enumerate(tmp.splitlines()):
                        if i < 7:
                            tmp1 += ln + '\n'
                        elif i > 6:
                            break
                    txtIf += '\n' + tmp1
                a = executionSubmod(txtIf,
                                    self.listDynamicValueIf.copy(),
                                    textEditor,
                                    None)
                for uj in a.getOutValues().keys():
                    listDynamicValue[uj] = a.getOutValues()[uj]

            elif 'F' in execution:
                listDynamicValueFor = {}
                txtCurrentFor = listForExecution[execution].splitlines()[0]
                txtCurrentFor = txtCurrentFor.replace('\\', '\\\\')
                txtCurrentFor = txtCurrentFor[2:len(txtCurrentFor) - 2]
                for li in txtCurrentFor.split("\', \'"):
                    st = li[0:li.index('=')]
                    ed = li[li.index('=') + 1:len(li)]
                    if ':' in ed and '\\' not in ed:
                        listDynamicValueFor[st] = listDynamicValue[ed]
                    else:
                        try:
                            listDynamicValueFor[st] = eval(ed)
                        except Exception as e:
                            listDynamicValueFor[st] = ed
                listBlockInFor = eval(listForExecution[execution].splitlines()[1])
                txtCurrentFor = listForExecution[execution].splitlines()[3]
                txtCurrentFor = txtCurrentFor[2:len(txtCurrentFor) - 2]
                if txtCurrentFor:
                    for li in txtCurrentFor.split("\', \'"):
                        st = li[0:li.index(':')]
                        if st not in listBlockInFor and 'F' not in st:
                            listDynamicValueFor[li] = listDynamicValue[li]
                try:
                    if 'm' in execution:
                        executionFor_proc(listForExecution[execution],
                                          listDynamicValueFor,
                                          txt)
                    else:
                        a, b, c, d, e, f, g = ForLoopInfo(listForExecution[execution],
                                                          txt).getListInfo()

                        listDynamicValueSubToReturn = {}

                        for kj in f:
                            tmpf = kj[0:kj.index('=')]
                            listDynamicValueSubToReturn[tmpf] = []
                        firstIndex = a[0]
                        firstIndex = firstIndex[0:firstIndex.index('=')]

                        listDynamicValueSub = listDynamicValueFor.copy()
                        tmp = []
                        lengthEnter = len(listDynamicValueFor[firstIndex])
                        for ele in range(lengthEnter):
                            for keyDyn, valDyn in listDynamicValueFor.items():
                                if 'F' in keyDyn[0:keyDyn.index(':')]:
                                    listDynamicValueSub[keyDyn] = valDyn[ele]
                            try:
                                es = executionSubmod(listForExecution[execution],
                                                     listDynamicValueSub.copy(),
                                                     textEditor,
                                                     modul)
                                for keyR, valueR in es.getOutValues().items():
                                    if 'ndarray' in type(valueR).__name__:
                                        if ele == 0:
                                            tmp = np.array(valueR)
                                        else:
                                            tmp = listDynamicValueSubToReturn[keyR]
                                            tmp = np.vstack((tmp, valueR))
                                    else:
                                        tmp = listDynamicValueSubToReturn[keyR]
                                        tmp.append(valueR)

                                    listDynamicValueSubToReturn[keyR] = tmp
                            except Exception as e:
                                textEditor.append("<span style=\" \
                                                  font-size:10pt; \
                                                  font-weight:600; \
                                                  color:#cc0000;\" \
                                                  > Pipeline Execution \
                                                  For Loop  stopped : " +
                                                  str(e) + "</span>")
                                return
                        for uj in listDynamicValueSubToReturn.keys():
                            listDynamicValue[uj] = listDynamicValueSubToReturn[uj]
                except Exception as e:
                    textEditor.append("<span style=\" \
                                      font-size:10pt; \
                                      font-weight:600; \
                                      color:#cc0000;\" \
                                      > Pipeline Execution " +
                                      execution +
                                      " stopped <br>" +
                                      execution + ' : ' + str(e) + "</span>")
                    return

        self.listValueDynamicToReturn = {}
        for ln in listConnctOut:
            st = ln[0:ln.index('=')]
            ed = ln[ln.index('=') + 1:len(ln)]
            if ':' in ed and '\\' not in ed:
                self.listValueDynamicToReturn[st] = listDynamicValue[ed]
            else:
                try:
                    self.listValueDynamicToReturn[st] = eval(ed)
                except Exception as e:
                    self.listValueDynamicToReturn[st] = ed

    def getOutValues(self):
        return self.listValueDynamicToReturn


class ThreadClass(threading.Thread):

    def __init__(self, classs, inp, outp):
        threading.Thread.__init__(self)
        self.classs = classs
        self.inp = inp
        self.outp = outp

    def run(self):
        self._return = {}
        if self.inp:
            a = self.classs(**self.inp)
        else:
            a = self.classs()
        if self.outp:
            for el in self.outp:
                unit = el[0:el.index(':')]
                val = el[el.index(':') + 1:len(el)]
                value = getattr(a, val)
                try:
                    self._return[el] = value()
                except Exception as e:
                    self._return[el] = value

    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return

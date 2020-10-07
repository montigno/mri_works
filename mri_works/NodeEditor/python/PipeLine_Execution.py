##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

import ast
import importlib
import sys
import time
import threading
import gc
from builtins import getattr

from PyQt5.QtWidgets import QProgressDialog
from PyQt5.Qt import Qt

from NodeEditor.python.PipeLine_Execution_SubMod import executionSubmod
from NodeEditor.python.pipeline_execution_loopfor import executionFor
from NodeEditor.python.pipeline_execution_loopfor_multiprocessing import executionFor_proc
from NodeEditor.python.pipeline_execution_script import executionScript
from NodeEditor.python.progressBar import progressBar
from NodeEditor.python.classForProbe import printProbe


class execution:

    def __init__(self, txt, textEditor):

        # print('txt')
        # print(txt)

        self.progress = QProgressDialog("Please wait while \
                                        the pipeline is being run...",
                                        None,
                                        0,
                                        100,
                                        None)
        self.progress.setWindowTitle("Pipeline running ....")
        self.progress.setWindowModality(Qt.WindowModal)
        self.progress.setModal(True)
        self.progress.forceShow()
        # self.progress.show()
        self.execution(txt, textEditor)
        self.progress.close()

    def execution(self, txt, textEditor):

        # compiles a list of items
        listConnctIn = []
        listBlockExecution = []
        listBlock = {}
        listOut = []
        listModul = {}
        listConnctOut = []

        for i, ln in enumerate(txt.splitlines()):
            if i == 0:
                listConnctIn.append(ast.literal_eval(ln))
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

        listModExecution = {}
        for ls in listModul.keys():
            tmp = txt[txt.index('[submod ' + ls):len(txt)]
            tmp1 = ''
            for i, ln in enumerate(tmp.splitlines()):
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    tmp1 += ln + '\n'
                elif i > 6:
                    break
            listModExecution[ls] = tmp1

#         print('PipeLine_Execution')
#         print(listModul)

        listForExecution = {}
        listIfExecution = {}
        listScriptExecution = {}

        for ls in listBlockExecution:
            if 'F' in ls:
                tmp = txt[txt.index('[loopfor ' + ls):len(txt)]
                tmp1 = ''
                for i, ln in enumerate(tmp.splitlines()):
                    if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                        tmp1 += ln + '\n'
                    elif i > 6:
                        break
                listForExecution[ls] = tmp1

            elif 'I' in ls:
                tmp = txt[txt.index('[loopif ' + ls + ' True'):len(txt)]
                tmp1 = ''
                for i, ln in enumerate(tmp.splitlines()):
                    if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                        tmp1 += ln + '\n'
                    elif i > 6:
                        break
                listIfExecution[ls + '-true'] = tmp1
                tmp = txt[txt.index('[loopif ' + ls + ' False'):len(txt)]
                tmp1 = ''
                for i, ln in enumerate(tmp.splitlines()):
                    if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                        tmp1 += ln + '\n'
                    elif i > 6:
                        break
                listIfExecution[ls + '-false'] = tmp1

            elif 'S' in ls:
                tmp = txt[txt.index('[source ' + ls):txt.index('[/source ' + ls)]
                tmp = tmp[tmp.index('\n') + 1:]
                listScriptExecution[ls] = tmp

        listNodeValue = list(set(listOut))
        self.listDynamicValue = {}
        start = time.time()
        start_sum = 0.00
        i = 0
        n = len(listBlockExecution)

        threadcurrent = False
        threads = []
        listInThread = []

        for execution in listBlockExecution:

            if 'ThreadOn' in execution:
                threadcurrent = True
                threads = []
                listInThread = []

            elif 'ThreadOff' in execution:
                self.progress.setLabelText('['+' , '.join(listInThread)+'] running')
                self.progress.setValue(i)
                i += 100 / n
                [thread.start() for thread in threads]
                [self.listDynamicValue.update(thread.join()) for thread in threads]
                threadcurrent = False
                start_sum += (time.time() - start_bb)
                textEditor.append("<span style=\" \
                                  font-size:8pt; \
                                  font-weight:600; \
                                  color:#006600;\" >[" +
                                  ' , '.join(listInThread) +
                                  "] --- time : %.2f seconds ---"
                                  % (time.time() - start_bb) + "</span>")
#                 print("thread lisdynamicvalue", self.listDynamicValue.keys())
            else:
                if not threadcurrent:
                    self.progress.setLabelText(execution+' running')
                self.progress.setValue(i)
                i += 100 / n
                start_bb = time.time()

            if ('M' not in execution and
                'F' not in execution and
                'I' not in execution and
                'S' not in execution and
                'P' not in execution and
                'Thread' not in execution):
                category = listBlock[execution][0]
                classes = listBlock[execution][1]
                module = importlib.import_module('NodeEditor.modules.' +
                                                 category)
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
                        listInThread.append(execution)
                    else:
                        a = MyClass()
                else:
                    for index, item in enumerate(tmp[1]):
                        if type(item).__name__ == 'str':
                            try:
                                gg = tmp[1][index]
                                tmp[1][index] = self.listDynamicValue[tmp[1][index]]
                        # try delete nodes which are no longer useful
                                if gg in listOut:
                                    listOut.remove(gg)
                                if gg not in listOut:
                                    del self.listDynamicValue[gg]
                            except Exception as e:
                                pass

#                     gc.collect()
                    try:
                        list3 = dict(zip(Enters, tmp[1]))
#                         print('list3 = ',list3)
                        if threadcurrent:
                            threads.append(ThreadClass(MyClass, list3, outUnit))
                            listInThread.append(execution)
                        else:
                            a = MyClass(**list3)
                            start_sum += (time.time() - start_bb)
                            textEditor.append("<span style=\" \
                                              font-size:8pt; \
                                              font-weight:600; \
                                              color:#006600;\" >" +
                                              execution +
                                              " --- time : %.2f seconds ---"
                                              % (time.time() - start_bb) +
                                              "</span>")
                    except Exception as e:
                        textEditor.append("<span style=\" \
                                          font-size:8pt; \
                                          font-weight:600; \
                                          color:#cc0000;\" \
                                          > Pipeline Execution \
                                          stopped <br>" +
                                          execution + ' : ' + str(e) +
                                          "</span>")
                        return
                if not threadcurrent:
                    for lsi in listNodeValue:
                        if execution + ':' in lsi:
                            outUnit = lsi[lsi.index(':') + 1:len(lsi)]
                            value = getattr(a, outUnit)
                            try:
                                self.listDynamicValue[lsi] = value()
                            except Exception as e:
                                self.listDynamicValue[lsi] = value

                # print('list3 & outUnit : ', list3,' , ',outUnit)
                
            elif 'P' in execution:
                valToPrint = self.listDynamicValue[listBlock[execution][2]]
                printProbe(execution, listBlock[execution][2],listBlock[execution][0], listBlock[execution][1],valToPrint)

            elif 'M' in execution:
                self.listDynamicValueSub = {}
                txtCurrentSubmod = listModExecution[execution].splitlines()[0]
                txtCurrentSubmod = txtCurrentSubmod.replace('\\', '\\\\')
                txtCurrentSubmod = txtCurrentSubmod[2:len(txtCurrentSubmod) - 2]
                outUnit = []
                for lsi in listNodeValue:
                    if execution + ':' in lsi:
                        outUnit.append(lsi)
                for li in txtCurrentSubmod.split("\', \'"):
                    st = li[0:li.index('=')]
                    ed = li[li.index('=') + 1:len(li)]
                    if ':' in ed and '\\' not in ed:
                        self.listDynamicValueSub[st] = self.listDynamicValue[ed]
                    else:
                        try:
                            self.listDynamicValueSub[st] = eval(ed)
                        except Exception as e:
                            self.listDynamicValueSub[st] = ed

                try:
                    if threadcurrent:
                        threads.append(ThreadSubMod(listModExecution[execution],
                                                    self.listDynamicValueSub,
                                                    listModul[execution]))
                        listInThread.append(execution)
                    else:
                        a = executionSubmod(listModExecution[execution],
                                            self.listDynamicValueSub,
                                            textEditor,
                                            listModul[execution])
                        start_sum += (time.time() - start_bb)
                        textEditor.append("<span style=\" \
                                          font-size:8pt; \
                                          font-weight:600; \
                                          color:#006600;\" >" +
                                          execution + " --- time : %.2f seconds ---"
                                          % (time.time() - start_bb) + "</span>")
                        for uj in a.getOutValues().keys():
                            self.listDynamicValue[uj] = a.getOutValues()[uj]
                except Exception as e:
                    textEditor.append("<span style=\" \
                                      font-size:10pt; \
                                      font-weight:600; \
                                      color:#cc0000;\" \
                                      > Pipeline Execution \
                                      SubMod stopped <br>" +
                                      execution + ' : ' + str(e) + "</span>")
                    return

            elif 'F' in execution:
                self.listDynamicValueFor = {}
                # search outs from extern pass by connectin (outs indexed)###
                txtCurrentFor = listForExecution[execution].splitlines()[0]
                txtCurrentFor = txtCurrentFor.replace('\\', '\\\\')
                txtCurrentFor = txtCurrentFor[2:len(txtCurrentFor) - 2]
                for li in txtCurrentFor.split("\', \'"):
                    st = li[0:li.index('=')]
                    ed = li[li.index('=') + 1:len(li)]
                    if ':' in ed and '\\' not in ed:
                        self.listDynamicValueFor[st] = self.listDynamicValue[ed]
                    else:
                        try:
                            self.listDynamicValueFor[st] = eval(ed)
                        except Exception as e:
                            self.listDynamicValueFor[st] = ed

                # search outs from extern no pass by connectin (outs no indexed)###
                listBlockInFor = eval(listForExecution[execution].splitlines()[1])
                txtCurrentFor = listForExecution[execution].splitlines()[3]
                txtCurrentFor = txtCurrentFor[2:len(txtCurrentFor) - 2]
                if txtCurrentFor:
                    for li in txtCurrentFor.split("\', \'"):
                        st = li[0:li.index(':')]
                        if st not in listBlockInFor and 'F' not in st:
                            self.listDynamicValueFor[li] = self.listDynamicValue[li]
                try:
                    if 'm' in execution:  # multiprocessing LoopFor
                        executionFor_proc(listForExecution[execution],
                                          self.listDynamicValueFor,
                                          txt, '*' in execution)
                    else:
                        a = executionFor(listForExecution[execution],
                                         self.listDynamicValueFor,
                                         textEditor,
                                         txt)
                        for uj in a.getOutValues().keys():
                            self.listDynamicValue[uj] = a.getOutValues()[uj]

                    start_sum += (time.time() - start_bb)
                    textEditor.append("<span style=\" \
                                      font-size:8pt; \
                                      font-weight:600; \
                                      color:#006600;\" >" +
                                      execution +
                                      " --- time : %.2f seconds ---"
                                      % (time.time() - start_bb) + "</span>")

                except Exception as e:
                    textEditor.append("<span style=\" \
                                      font-size:10pt; \
                                      font-weight:600; \
                                      color:#cc0000;\" \
                                      > Pipeline Execution " +
                                      execution +
                                      " stopped <br>" +
                                      execution + ' : ' +
                                      str(e) + "</span>")
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
                        try:
                            tmpVal = eval(tmpVal)
                        except Exception as e:
                            pass
                        txtCurrentIf.remove(indif)
                for li in txtCurrentIf:
                    st = li[0:li.index('=')]
                    ed = li[li.index('=') + 1:len(li)]
                    if ':' in ed and '\\' not in ed:
                        self.listDynamicValueIf[st] = self.listDynamicValue[ed]
                    else:
                        try:
                            self.listDynamicValueIf[st] = eval(ed)
                        except Exception as e:
                            self.listDynamicValueIf[st] = ed

                try:
                    if not tmpVal:
                        txtIf = listIfExecution[execution + '-false']
                except Exception as e:
                    pass
                try:
                    if not self.listDynamicValue[tmpVal]:
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

                for ls in eval(txtIf.splitlines()[1]):
                    if 'S' in ls:
                        tmp2 = txt[txt.index('[source ' + ls):txt.index('[/source ' + ls) + 10 + len(ls)]
                        txtIf += '\n' + tmp2

                a = executionSubmod(txtIf,
                                    self.listDynamicValueIf.copy(),
                                    textEditor,
                                    None)
                start_sum += (time.time() - start_bb)
                textEditor.append("<span style=\" \
                                  font-size:8pt; \
                                  font-weight:600; \
                                  color:#006600;\" >" +
                                  execution +
                                  " --- time : %.2f seconds ---"
                                  % (time.time() - start_bb) + "</span>")
                for uj in a.getOutValues().keys():
                    self.listDynamicValue[uj] = a.getOutValues()[uj]

            elif 'S' in execution:
                a = executionScript(listScriptExecution[execution], self.listDynamicValue, textEditor)
                start_sum += (time.time() - start_bb)
                textEditor.append("<span style=\" \
                                  font-size:8pt; \
                                  font-weight:600; \
                                  color:#006600;\" >" +
                                  execution +
                                  " --- time : %.2f seconds ---"
                                  % (time.time() - start_bb) + "</span>")
                for uj in a.getOutValues().keys():
                    self.listDynamicValue[uj] = a.getOutValues()[uj]

        # try:
        #     print("lenght value listDynamicValue",
        #            len(self.listDynamicValue))
        # except:
        #     pass
        # try:
        #     print("lenght value listDynamicValueFor",
        #            len(self.listDynamicValueFor))
        # except:
        #     pass
        # try:
        #     print("lenght value listDynamicValueIf",
        #            len(self.listDynamicValueIf))
        # except:
        #     pass
        # try:
        #     print("lenght value listDynamicValueSub",
        #            len(self.listDynamicValueSub))
        # except:
        #     pass

        textEditor.append("<span style=\" \
                          font-size:10pt; \
                          font-weight:600; \
                          color:#0000CC;\" \
                          >Pipeline finished ! \
                          --- Total time : %s seconds ---"
                          % (time.time() - start) +
                          " : " + str(start_sum) + "</span>")

        gc.collect()


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
                # print('unit , val',el,unit,val)
                value = getattr(a, val)
                try:
                    self._return[el] = value()
                except Exception as e:
                    self._return[el] = value

    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return


class ThreadSubMod(threading.Thread):

    def __init__(self, listModExc, listDynVal, listModul):
        threading.Thread.__init__(self)
        self.listModExc = listModExc
        self.listDynVal = listDynVal
        self.listModul = listModul

    def run(self):
        self._return = {}
        a = executionSubmod(self.listModExc,
                            self.listDynVal,
                            None,
                            self.listModul)
        for el in a.getOutValues().keys():
            self._return[el] = a.getOutValues()[el]

    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return

##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################


import xml.etree.cElementTree as ET
from xml.etree import ElementTree
from xml.dom import minidom
import os
import re
from importlib import reload
import importlib
import inspect
import subprocess
from shutil import copyfile
from NodeEditor.python.Capsul.Generate_moduls_py import CodeGenerator


class exportCapsul():

    def __init__(self, diagram, repertory, doExecution, textEditor):

        listUnit = {}
        listClass = {}
        listConstant = {}
        listArrow = {}
        listInputs = {}
        listValParam = {}
        listCategory, listDoublon_InOut = [], []

        tmp = diagram.splitlines()
        tmp.reverse()

        pipeline = ET.Element("pipeline")
        gui = ET.SubElement(pipeline, "gui")
        ET.SubElement(gui, "position", name="inputs", x="0", y="0")

        for line in tmp:
            if line[0:5] == 'block':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('category') + 10:len(line)]
                cat = line[0:line.index(']')]
                line = line[line.index('class') + 7:len(line)]
                classs = line[0:line.index(']')]
                line = line[line.index('valInputs') + 11:len(line)]
                Vinput = line[0:line.index('] RectF')]
                line = line[line.index('RectF') + 7:len(line)]
                posi = eval(line[0:line.index(']')])
                tmpVal = eval(Vinput)
                if '_dyn' in classs:
                    classs += str(len(tmpVal[0]))
                try:
#                     tmpDoub = str(list(set(tmpVal[0]) & set(tmpVal[2]))[0])
#                     if tmpDoub:
#                         newTmpVal0 = [w.replace(tmpDoub, tmpDoub + '_xx') for w in tmpVal[0]]
#                         tmpVal = (newTmpVal0, tmpVal[1], tmpVal[2], tmpVal[3])
#                         listDoublon_InOut.append(unit + '.' + tmpDoub)                        
                    
                    tmpDoub = list(set(tmpVal[0]) & set(tmpVal[2]))
                    if tmpDoub:
                        for elem in tmpDoub:
                            newTmpVal0 = [w.replace(elem, elem + '_xx') for w in tmpVal[0]]
                            tmpVal = (newTmpVal0, tmpVal[1], tmpVal[2], tmpVal[3])
                            listDoublon_InOut.append(unit + '.' + elem)
                            
                except Exception as e:
                    pass
                listUnit[unit] = tmpVal
                listClass[classs] = (cat, tmpVal)
                listCategory.append(cat + '.' + classs)
                ET.SubElement(pipeline, "process", module="capsul_moduls." + classs, name=unit)
                ET.SubElement(gui, "position", name=unit, x=str(posi[0]), y=str(posi[1]))

                for i in range(0, len(tmpVal[1])):
                    if 'Node' not in str(tmpVal[1][i]):
                        ET.SubElement(pipeline, "link", source=unit + "_" + tmpVal[0][i], dest=unit + "." + tmpVal[0][i])
                        listValParam[unit + "_" + tmpVal[0][i]] = tmpVal[1][i]

            elif line[0:4] == 'link':
                nameNode = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                nameNode = 'Node(' + nameNode + ')'
                line = line[line.index('node=') + 6:len(line) - 1]
                a = line[0:line.index(':')]
                b = line[line.index(':') + 1:line.index('#Node#')]
                line = line[line.index('#Node#') + 6:len(line)]
                c = line[0:line.index(':')]
                d = line[line.index(':') + 1:]

                if c + '.' + d in listDoublon_InOut:
                    d += '_xx'

                if 'A' not in a:
                    ET.SubElement(pipeline, "link", source=a + "." + b, dest=c + "." + d)

                listArrow[nameNode] = (a, b, c, d)

            elif line[0:8] == 'constant':
                unit = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
                line = line[line.index('value=') + 7:len(line)]
                vout = line[0:line.index(']')]
                line = line[line.index('format=') + 8:len(line)]
                fort = line[0:line.index('] label')]
                line = line[line.index('label=') + 7:len(line)]
                lab = line[0:line.index('] RectF')]
                try:
                    listConstant[unit] = (lab, eval(vout))
                except Exception as e:
                    listConstant[unit] = (lab, vout)

        for keyLink, valLink in listArrow.items():
            if 'A' in valLink[0]:
                listInputs[listConstant[valLink[0]][0]] = listConstant[valLink[0]][1]
                ET.SubElement(pipeline, "link", source=listConstant[valLink[0]][0], dest=valLink[2] + "." + valLink[3])
#                 listInputs[valLink[0]] = listConstant[valLink[0]]

        for keyUnit, valUnit in listUnit.items():
            for listOut in valUnit[2]:
                isYet = False
                for keyLink, valLink in listArrow.items():
                    if keyUnit + ':' + listOut in valLink[0] + ':' + valLink[1]:
                        isYet = True
                        break
                if not isYet:
                    ET.SubElement(pipeline, "link", source=keyUnit + '.' + listOut, dest=keyUnit + '_' + listOut)

        # generate xml pipeline ##############""

        f = open(os.path.join(repertory, "capsul_pipeline.xml"), 'w')
        f.write(self.prettify(pipeline))
        f.close()

        # generate capsul_moduls.py ##############
        codeModuls = CodeGenerator()
        codeModuls += 'from capsul.process.xml import xml_process\n'
        codeModuls += 'import capsul_code_source as cs\n'
        codeModuls += '\n'

        for keyClass, valClass in listClass.items():
            codeModuls += "@xml_process('''\n"
            codeModuls += '<process capsul_xml="2.0">\n'
            codeModuls.indent()

            for i in range(0, len(valClass[1][0])):
                typeVal = ''
                if 'Node' in str(valClass[1][1][i]):
                    tmp = listArrow[valClass[1][1][i]]
                    if 'A' in tmp[0]:
                        typeVal = type(listConstant[str(tmp[0])][1]).__name__
                    else:
                        tmpType = listUnit[str(tmp[0])]
                        ind = 0
                        for lst in tmpType[2]:
                            if lst == tmp[1]:
                                typeVal = tmpType[3][ind]
                            else:
                                ind += 1
                else:
                    tmp = valClass[1][1][i]
                    if isinstance(tmp, list):
                        if isinstance(tmp[0], list):
                            typeVal = 'list_' + type(tmp[0][0]).__name__
                        else:
                            typeVal = 'list_' + type(tmp[0]).__name__
                    else:
                        typeVal = type(tmp).__name__

                typeVal = typeVal.replace('str', 'string')
                typeVal = typeVal.replace('path', 'file')
                typeVal = typeVal.replace('array', 'list')
                codeModuls += '<input name="' + valClass[1][0][i] + '" type="' + str(typeVal) + '" doc=""/>\n'

            if len(valClass[1][2]) == 1:
                typeOut = valClass[1][3][0]
                typeOut = typeOut.replace('str', 'string')
                typeOut = typeOut.replace('path', 'file')
                typeOut = typeOut.replace('array', 'list')
                codeModuls += '<return name="' + valClass[1][2][0] + '" type="' + typeOut + '" doc=""/>\n'
            elif len(valClass[1][2]) > 1:
                codeModuls += '<return>\n'
                codeModuls.indent()
                for i in range(0, len(valClass[1][2])):
                    typeOut = valClass[1][3][i]
                    typeOut = typeOut.replace('str', 'string')
                    typeOut = typeOut.replace('path', 'file')
                    typeOut = typeOut.replace('array', 'list')
                    codeModuls += '<output name="' + valClass[1][2][i] + '" type="' + typeOut + '" doc=""/>\n'
                codeModuls.dedent()
                codeModuls += '</return>\n'
                codeModuls.dedent()

            codeModuls.dedent()
            codeModuls += '</process>\n'
            codeModuls += "''')\n"
            tmp = str(tuple(valClass[1][0]))
            tmpw = tmp.replace("'", "")
            codeModuls += 'def ' + keyClass + tmpw + ':\n'
            codeModuls.indent()
            codeModuls += 'listInputs=dict(zip(' + tmp + ',' + str(tmpw) + '))\n'
            
            tmpkeyClass = keyClass
            if '_dyn' in tmpkeyClass:
                tmpkeyClass = tmpkeyClass[0:tmpkeyClass.index('_dyn')+4]

            if len(valClass[1][2]) < 2:
                tmp2 = 'return cs.' + tmpkeyClass + '(**listInputs)'
                try:
                    codeModuls += tmp2 + '.' + str(valClass[1][2][0]) + '()\n'
                except Exception as e:
                    codeModuls += tmp2 + '\n'

            elif len(valClass[1][2]) > 1:
                codeModuls += 'z=cs.' + tmpkeyClass + '(**listInputs)\n'
                codeModuls += 'return {\n'
                codeModuls.indent()
                for i in range(0, len(valClass[1][2])):
                    codeModuls += "'" + str(valClass[1][2][i]) + "':" + ' z.' + valClass[1][2][i] + '(),\n'
                codeModuls.dedent()
                codeModuls += '}\n'
            codeModuls.dedent()
            codeModuls += '\n'

        f = open(os.path.join(repertory, "capsul_moduls.py"), 'w')
        f.write(str(codeModuls))
        f.close()

        # generate capsul_code_source.py ##############
        listCategory = set(list(listCategory))
        listSources = []
        src = ''
        for listcode in listCategory:
            filePy = 'NodeEditor.modules.' + listcode[0:listcode.rfind('.')]
            classPy = listcode[listcode.rfind('.') + 1:]
            if 'dyn' in classPy:
                classPy = classPy[0:classPy.index('_dyn')+4]
            imp = importlib.import_module(filePy)
            importlib.reload(imp)
            for nameClass, obj in inspect.getmembers(imp):
                if nameClass == classPy:
                    srcTmp = inspect.getsource(obj)
                    for line in self.lines_that_contain("NodeEditor", srcTmp.splitlines()):
                        listSources.append(line)
                    src += srcTmp + '\n\n'
        
        if listSources:
            src = src.replace('NodeEditor.modules.','')
            if not os.path.isdir(os.path.join(repertory, "sources")):
                os.mkdir(os.path.join(repertory, "sources"))
            for lst in listSources:
                filepy = lst.strip()[32:lst.strip().index('import')-1]
                copyfile(os.path.join("NodeEditor","modules","sources",filepy+'.py'),
                         os.path.join(repertory, "sources",filepy+'.py'))
        
        f = open(os.path.join(repertory, "capsul_code_source.py"), 'w')
        f.write(src)
        f.close()

        # generate capsul_main.py ##############
        codeMain = CodeGenerator()
        codeMain += 'import sys, time\n'
        codeMain += 'from capsul.api import get_process_instance\n'
        codeMain += 'from PyQt5.Qt import QApplication\n'
        codeMain += '\n'
        codeMain += self.PipelineGetArguments() + '\n'
        codeMain += 'try:\n'
        codeMain.indent()
        codeMain += 'xmlpipe = get_process_instance("capsul_pipeline")\n'

        for keyInput, valInput in listInputs.items():
            if type(valInput).__name__ == 'str':
                codeMain += 'xmlpipe.' + keyInput + '=\"' + str(valInput) + '\"\n'
            else:
                codeMain += 'xmlpipe.' + keyInput + '=' + str(valInput) + '\n'

        for keyParam, valParam in listValParam.items():
            if type(valParam).__name__ == 'str':
                if valParam == '':
                    valParam = ' '
                codeMain += 'xmlpipe.' + keyParam + "=\"" + str(valParam) + '\"\n'
            else:
                codeMain += 'xmlpipe.' + keyParam + "=" + str(valParam) + '\n'
        codeMain += 'if sys.argv[1] == "runPipeline":\n'
        codeMain.indent()
        codeMain += 'app = QApplication.instance()\n'
        codeMain += 'if app is None:\n'
        codeMain.indent()
        codeMain += 'app = QApplication(sys.argv)\n'
        codeMain.dedent()
        codeMain += 'start=time.time()\n'
        codeMain += 'if parameter_dict:\n'
        codeMain.indent()
        codeMain += 'xmlpipe(**parameter_dict)\n'
        codeMain.dedent()
        codeMain += 'else:\n'
        codeMain.indent()
        codeMain += 'xmlpipe()\n'
        codeMain.dedent()
        codeMain += 'print("Capsul execution time = ",time.time()-start)\n'
        codeMain.dedent()
        codeMain.dedent()
        codeMain += 'except Exception as e:\n'
        codeMain.indent()
        codeMain += 'print("error execution pipeline : ",e)\n'
        codeMain.dedent()

        codeMain += self.PipelineShowingCode()

        pathMain = os.path.join(repertory, "capsul_main.py")
        f = open(pathMain, 'w')
        os.chmod(pathMain, 0o777)
        f.write(str(codeMain))
        f.close()

        # execute capsul_main.py ##############
        if doExecution:
            textEditor.append("<span style=\" \
                              font-size:10pt; \
                              font-weight:600; \
                              color:#006600;\" \
                              > Pipeline running \
                              by Capsul </span>")
            subprocess.Popen(['python3', pathMain, 'runPipeline'], shell=False)

    def prettify(self, elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
    
    def lines_that_contain(self, string, fp):
        return [line for line in fp if string in line]

    def PipelineGetArguments(self):
        txt = """
parameter_dict={}
if len(sys.argv) > 2:
    for user_input in sys.argv[2:]:
        varname = user_input.split("=")[0]
        varvalue = user_input.split("=")[1]
        try:
            varvalue = eval(varvalue)
        except:
            pass
        parameter_dict[varname] = varvalue
        """
        return txt

    def PipelineShowingCode(self):
        txt = """
try:
    if sys.argv[1] == 'showInputs':
        for key_s,val_s in xmlpipe.get_inputs().items():
            if 'nodes_activation' not in key_s:
                print(key_s,'= ',val_s)
except:
    pass

try:
    if sys.argv[1] == 'showOutputs':
        for key_s,val_s in xmlpipe.get_outputs().items():
            print(key_s,'= ',val_s)
except:
    pass

try:
    if sys.argv[1] in ['-help','-h'] :
        print(\"""
        usage:  python3 capsul_main.py runPipeline [attributs=value] (1)
                python3 capsul_main.py showPipeline                  (2)
                python3 capsul_main.py showInputs                    (3)
                python3 capsul_main.py showOutputs                   (4)

        (1) - run pipeline : - with default values of inputs if no option
                             - with value assigned to certain (or all) inputs
                                    (ex : python3 capsul_main.py executionPipeline X=10.0 Y=[5.6])
        (2) - show pipeline developper view
        (3) - show pipeline inputs with default values
        (4) - show pipeline outputs
        \""")
except:
    pass

try:
    if sys.argv[1] == "showPipeline":
        if globals().get('use_gui', True):
            from capsul.qt_gui.widgets import PipelineDevelopperView
            run_qt_loop=False
            if QApplication.instance() is None:
                app=QApplication(sys.argv)
                run_qt_loop=True
            else:
                app = QApplication.instance()

            view4 = PipelineDevelopperView(xmlpipe, allow_open_controller=True, show_sub_pipelines=True)
            view4.show()

            if run_qt_loop:
                print('close window to gon on ...')
                app.exec_()
except Exception as e:
    print("error show pipeline : ",e)
              """
        return txt

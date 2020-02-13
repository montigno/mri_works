import yaml
import inspect

interf = 'utility'

exec('from nipype.interfaces import '+interf)
lis = inspect.getmembers(eval(interf), lambda a:not(inspect.isroutine(a)))
list_cat=[]
list_fct=[]
dict_cat_fct={}

for nameClass in lis :
    try:
        if '__' not in nameClass[0]:
            fct = nameClass[0]
            txt = str(nameClass[1])
            cat = 'type' in str(type(nameClass[1]))
            if cat :
                txt = txt[txt.index(interf)+len(interf)+1:-1]
                txt1 = txt[0:txt.index('.')]
                txt2 = txt[txt.index('.'):]
                txt2 = txt2[txt2.index('.')+1:]
#                 print(txt," , ",txt1," , ",txt2)
                if txt1 in dict_cat_fct.keys():
                    list_fct=dict_cat_fct[txt1]
                else:
                    list_fct=[]
                if txt2 not in list_fct:
                    list_fct.append(txt2)
                    dict_cat_fct[txt1] = list_fct
    except:
        pass


TxtToImport = interf

for elem in dict_cat_fct.keys():
    
    dataAll={}
    doc=''

    for elemVal in dict_cat_fct[elem]:
        TxtToExecute = elemVal[0:-1]
#         print(TxtToImport," : ",elem," , ",TxtToExecute)
        try:
            doc = eval(TxtToImport+"."+TxtToExecute+"().help(True)")
            doc=doc[doc.index('[Optional]'):doc.index('Outputs')]
        except:
            doc=''
        
        if doc :
            list_inputs={}
            descript=''
            label=None

            for ele in doc.split('\n'):
                
                leading_spaces = len(ele) - len(ele.lstrip())
#                 print(ele," , ",leading_spaces)
                if leading_spaces == 8:
                    label=ele[8:ele.index(':')]
                    list_inputs[label]=''
#                     print(label)
        
            b=dict()

            for key,val in list_inputs.items():
                print(key)
                c=''
                b[key]=dict(c)
     
            tag=TxtToImport+"_"+TxtToExecute

            data = dict({tag : dict(b)})
            dataAll[tag] = dict(b)
     
        with open('Interfaces_'+TxtToImport+'_'+elem+'.yml', 'w') as outfile:
            yaml.dump(dataAll, outfile, default_flow_style=False)

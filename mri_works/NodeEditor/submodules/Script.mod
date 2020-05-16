[diagram]
link=[N7] node=[U1:arrayFloat#Node#C2:arrayFloat]
link=[N6] node=[C0:inBool#Node#U1:inBool]
link=[N5] node=[C1:arrayInt#Node#U1:arrayInt]
link=[N4] node=[U1:arrayBool#Node#U2:in_array_Bool]
link=[N1] node=[U1:outInt#Node#S0:in0]
link=[N2] node=[U1:outFloat#Node#S0:in1]
link=[N3] node=[U1:outBool#Node#S0:in3]
link=[N0] node=[S0:out5#Node#C3:out5]
link=[N8] node=[U1:listInt#Node#S1:in0]
script=[S1] inputs=[['in0', 'in', 'list_int']] outputs=[] code=[your code] RectF=[(172.15668304457336, 238.0253269920624, 200.0, 200.0)]
connt=[C2] name=[arrayFloat] type=[out] format=[array_float] RectF=[(327.28268807932574, 147.89674151876557, 70, 24)]
connt=[C1] name=[arrayInt] type=[in] format=[array_int] valOut=[[[0]]] RectF=[(-763.234197912879, 216.95060229210273, 70, 24)]
connt=[C0] name=[inBool] type=[in] format=[bool] valOut=[True] RectF=[(-767.1963650847226, 67.51486107760866, 70, 24)]
block=[U2] category=[Tools.Print] class=[Print_array_bool] valInputs=[(['comment', 'in_array_Bool'], ['', 'Node(N4)'], [], [])] RectF=[(-84.93945239765338, 401.28269167629935, 150.0, 80.0)]
script=[S0] inputs=[['in0', 'in', 'int'], ['in1', 'in', 'float'], ['in3', 'in', 'bool']] outputs=[['out5', 'out', 'list_path']] code=[your code] RectF=[(-231.3666265608741, -34.856513397502596, 200.0, 200.0)]
block=[U1] category=[Demos.Models] class=[AllTypes] valInputs=[(['inInt', 'inFloat', 'inString', 'inBool', 'inPath', 'listInt', 'listFloat', 'listString', 'listBool', 'listPath', 'arrayInt', 'arrayFloat', 'arrayString', 'arrayBool', 'arrayPath', 'inDict', 'inTuple'], [0, 0.0, '', 'Node(N6)', 'path', [0, 1], [0.0], [''], [False], ['path'], 'Node(N5)', [[0.0]], [['']], [[False]], [['path']], {}, ('',)], ['outInt', 'outFloat', 'outString', 'outBool', 'outPath', 'listInt', 'listFloat', 'listString', 'listBool', 'listPath', 'arrayInt', 'arrayFloat', 'arrayString', 'arrayBool', 'arrayPath', 'dictionary', 'tuple'], ['int', 'float', 'str', 'bool', 'path', 'list_int', 'list_float', 'list_str', 'list_bool', 'list_path', 'array_int', 'array_float', 'array_str', 'array_bool', 'array_path', 'dict', 'tuple_str'])] RectF=[(-604.7463088237325, -4.026514317567319, 244.12152198992362, 474.0295915550822)]
connt=[C3] name=[out5] type=[out] format=[list_path] RectF=[(285.5318617333265, 53.44931401904634, 70, 24)]
[source S0]
['in3=U1:outBool', 'in1=U1:outFloat', 'in0=U1:outInt']
out5=['path']
def method():
    print('hello')
    for i in range(0, 10):
        p = i * i
method()
['S0:out5']
[/source S0]
[source S1]
['in0=U1:listInt']
print('Script 2')
[]
[/source S1]

[execution]
['C0:inBool=', 'C1:arrayInt=']
['U1', 'S0', 'ThreadOn', 'S1', 'U2', 'ThreadOff']
{'U1': ('Demos.Models', 'AllTypes', "(['inInt', 'inFloat', 'inString', 'inBool', 'inPath', 'listInt', 'listFloat', 'listString', 'listBool', 'listPath', 'arrayInt', 'arrayFloat', 'arrayString', 'arrayBool', 'arrayPath', 'inDict', 'inTuple'], [0, 0.0, '', 'C0:inBool', 'path', [0, 1], [0.0], [''], [False], ['path'], 'C1:arrayInt', [[0.0]], [['']], [[False]], [['path']], {}, ('',)], ['outInt', 'outFloat', 'outString', 'outBool', 'outPath', 'listInt', 'listFloat', 'listString', 'listBool', 'listPath', 'arrayInt', 'arrayFloat', 'arrayString', 'arrayBool', 'arrayPath', 'dictionary', 'tuple'], ['int', 'float', 'str', 'bool', 'path', 'list_int', 'list_float', 'list_str', 'list_bool', 'list_path', 'array_int', 'array_float', 'array_str', 'array_bool', 'array_path', 'dict', 'tuple_str'])"), 'U2': ('Tools.Print', 'Print_array_bool', "(['comment', 'in_array_Bool'], ['', 'U1:arrayBool'], [], [])")}
['U1:listInt', 'S0:out5', 'U1:outBool', 'U1:outFloat', 'U1:outInt', 'U1:arrayBool', 'C1:arrayInt', 'C0:inBool', 'U1:arrayFloat']
{}
['C3:out5=S0:out5', 'C2:arrayFloat=U1:arrayFloat']

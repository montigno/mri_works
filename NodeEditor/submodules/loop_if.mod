[diagram]
link=[N16] node=[C6:y#Node#U5:y]
link=[N15] node=[C5:x#Node#U5:x]
link=[N14] node=[I0:out1#Node#C4:out1]
link=[N13] node=[I0:out0#Node#C3:out0]
link=[N12] node=[C2:arrayInt_2#Node#U3:arrayInt]
link=[N11] node=[C1:arrayInt_1#Node#U2:arrayInt]
link=[N10] node=[C0:arrayInt#Node#U1:arrayInt]
link=[N7] node=[U3:outArrayInt#Node#I0:in2]
link=[N6] node=[U2:outArrayInt#Node#I0:in1]
link=[N5] node=[U1:outArrayInt#Node#I0:in0]
link=[N3] node=[U0:outArrayInt#Node#I0:out1]
link=[N2] node=[I0:in2#Node#U0:arrayInt]
link=[N0] node=[I0:in1#Node#U4:arrayInt]
link=[N1] node=[U4:outArrayInt#Node#I0:out0]
link=[N4] node=[I0:in0#Node#I0:out1]
link=[N8] node=[I0:in1#Node#I0:out0]
link=[N9] node=[U5:out#Node#I0:val]
block=[U0] category=[Tools.Constants] class=[Constant_int_array] valInputs=[(['arrayInt'], ['Node(N2)'], ['outArrayInt'], ['array_int'])] RectF=[(-180.4883369831437, 57.50532896130562, 170.046875, 80.0)]
block=[U4] category=[Tools.Constants] class=[Constant_int_array] valInputs=[(['arrayInt'], ['Node(N0)'], ['outArrayInt'], ['array_int'])] RectF=[(-226.67368793898277, 67.38485827904711, 170.046875, 80.0)]
connt=[C6] name=[y] type=[in] format=[float] valOut=[0.0] RectF=[(-785.0002081351803, -188.4879313281513, 70, 24)]
connt=[C5] name=[x] type=[in] format=[float] valOut=[0.0] RectF=[(-785.8379322744169, -256.0643452265404, 70, 24)]
connt=[C4] name=[out1] type=[out] format=[array_int] RectF=[(253.95536489245654, 85.19985849831978, 70, 24)]
connt=[C3] name=[out0] type=[out] format=[array_int] RectF=[(251.13952283802524, -74.502782459077, 70, 24)]
connt=[C2] name=[arrayInt_2] type=[in] format=[array_int] valOut=[[[0]]] RectF=[(-769.9211736289283, 168.10331060673647, 70, 24)]
connt=[C1] name=[arrayInt_1] type=[in] format=[array_int] valOut=[[[0]]] RectF=[(-774.1097943251094, 36.02213798715782, 70, 24)]
connt=[C0] name=[arrayInt] type=[in] format=[array_int] valOut=[[[0]]] RectF=[(-778.0191736415454, -92.98737945522132, 70, 24)]
block=[U3] category=[Tools.Constants] class=[Constant_int_array] valInputs=[(['arrayInt'], ['Node(N12)'], ['outArrayInt'], ['array_int'])] RectF=[(-626.9517194493476, 143.70746878820987, 170.046875, 80.0)]
block=[U2] category=[Tools.Constants] class=[Constant_int_array] valInputs=[(['arrayInt'], ['Node(N11)'], ['outArrayInt'], ['array_int'])] RectF=[(-626.4732723832474, 7.6399179558932655, 172.85412627778067, 82.80725127778062)]
block=[U1] category=[Tools.Constants] class=[Constant_int_array] valInputs=[(['arrayInt'], ['Node(N10)'], ['outArrayInt'], ['array_int'])] RectF=[(-623.567937217414, -118.05956278774914, 170.046875, 78.59637436110968)]
block=[U5] category=[Tools.Comparison_operations] class=[x_Equal_y] valInputs=[(['x', 'y'], ['Node(N15)', 'Node(N16)'], ['out'], ['bool'])] RectF=[(-631.0464682504744, -249.6172216901047, 173.86163586113537, 80.0)]
loopIf=[I0] inputs=[[[['in0', 'in', 'array_int'], ['in0', 'out', 'array_int']], [['in1', 'in', 'array_int'], ['in1', 'out', 'array_int']], [['in2', 'in', 'array_int'], ['in2', 'out', 'array_int']]]] outputs=[[[['out0', 'in', 'array_int'], ['out0', 'out', 'array_int']], [['out1', 'in', 'array_int'], ['out1', 'out', 'array_int']]]] listItems=[[['N4', 'U4'], ['U0', 'N8']]] RectF=[(-304.9957774653224, -165.46511869195947, 431.7474414777878, 348.54340936702886)]
[execution]
['C5:x=', 'C6:y=', 'C0:arrayInt=', 'C1:arrayInt_1=', 'C2:arrayInt_2=']
['ThreadOn', 'U5', 'U3', 'U2', 'U1', 'ThreadOff', 'I0']
{'U5': ('Tools.Comparison_operations', 'x_Equal_y', "(['x', 'y'], ['C5:x', 'C6:y'], ['out'], ['bool'])"), 'U1': ('Tools.Constants', 'Constant_int_array', "(['arrayInt'], ['C0:arrayInt'], ['outArrayInt'], ['array_int'])"), 'U2': ('Tools.Constants', 'Constant_int_array', "(['arrayInt'], ['C1:arrayInt_1'], ['outArrayInt'], ['array_int'])"), 'U3': ('Tools.Constants', 'Constant_int_array', "(['arrayInt'], ['C2:arrayInt_2'], ['outArrayInt'], ['array_int'])")}
['U5:out', 'I0:in1', 'I0:in0', 'I0:in1', 'I0:in2', 'U1:outArrayInt', 'U2:outArrayInt', 'U3:outArrayInt', 'C0:arrayInt', 'C1:arrayInt_1', 'C2:arrayInt_2', 'I0:out0', 'I0:out1', 'C5:x', 'C6:y']
{}
['C3:out0=I0:out0', 'C4:out1=I0:out1']
[loopif I0 True]
['I0:val=U5:out', 'I0:in0=U1:outArrayInt', 'I0:in1=U2:outArrayInt', 'I0:in2=U3:outArrayInt']
['U4']
{'U4': ('Tools.Constants', 'Constant_int_array', "(['arrayInt'], ['I0:in1'], ['outArrayInt'], ['array_int'])")}
['I0:in1', 'I0:in0', 'U4:outArrayInt', 'I0:in1']
{}
['I0:out0=U4:outArrayInt', 'I0:out1=I0:in0']
[loopif I0 False]
['I0:val=U5:out', 'I0:in0=U1:outArrayInt', 'I0:in1=U2:outArrayInt', 'I0:in2=U3:outArrayInt']
['U0']
{'U0': ('Tools.Constants', 'Constant_int_array', "(['arrayInt'], ['I0:in2'], ['outArrayInt'], ['array_int'])")}
['I0:in1', 'I0:in0', 'I0:in2', 'U0:outArrayInt']
{}
['I0:out1=U0:outArrayInt', 'I0:out0=I0:in1']
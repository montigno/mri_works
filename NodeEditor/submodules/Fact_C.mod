[diagram]
constant=[A1] value=[' != '] format=[str] label=[A1] RectF=[(-45.17327014145877, 202.11665099458745, 45.0, 33.0)]
link=[N3] node=[A1:#Node#U1:stringIn_0]
link=[N1] node=[C0:enter_int#Node#U3:inInt]
link=[N0] node=[C0:enter_int#Node#U0:enter_int]
link=[N2] node=[U0:factorial#Node#C1:factorial]
link=[N4] node=[U3:outString#Node#U1:stringIn]
link=[N6] node=[U1:str_conc#Node#C2:str_conc]
connt=[C2] name=[str_conc] type=[out] format=[str] RectF=[(318.3523019643369, 132.82731080888303, 70, 24)]
connt=[C1] name=[factorial] type=[out] format=[int] RectF=[(126.33296849506976, -47.75986963638484, 70, 24)]
connt=[C0] name=[enter_int] type=[in] format=[int] valOut=[0] RectF=[(-376.29386560583464, 34.81352786349757, 70, 24)]
block=[U0] category=[C.Maths] class=[fact] valInputs=[(['enter_int'], ['Node(N0)'], ['factorial'], ['int'])] RectF=[(-120.0, -58.047319606824175, 148.34375, 72.07157842908865)]
block=[U3] category=[Tools.Conversion] class=[IntToString] valInputs=[(['inInt'], ['Node(N1)'], ['outString'], ['str'])] RectF=[(-124.60437254937096, 83.41868823518871, 153.58131176481135, 70.79245293896287)]
block=[U1] category=[Tools.StringManipulation] class=[string_concatenat_dyn] valInputs=[(['stringIn', 'stringIn_0'], ['Node(N4)', 'Node(N3)'], ['str_conc'], ['str'])] RectF=[(111.90051695642126, 108.69594677486276, 156.71875, 78.69901176301931)]
[execution]
['C0:enter_int=']
['ThreadOn', 'U0', 'U3', 'ThreadOff', 'U1']
{'U3': ('Tools.Conversion', 'IntToString', "(['inInt'], ['C0:enter_int'], ['outString'], ['str'])"), 'U0': ('C.Maths', 'fact', "(['enter_int'], ['C0:enter_int'], ['factorial'], ['int'])"), 'U1': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0'], ['U3:outString', ' != '], ['str_conc'], ['str'])")}
['U1:str_conc', 'U3:outString', 'U0:factorial', 'C0:enter_int', 'C0:enter_int', 'A1:']
{}
['C1:factorial=U0:factorial', 'C2:str_conc=U1:str_conc']
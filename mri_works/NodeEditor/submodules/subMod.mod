[diagram]
link=[N26] node=[C26:sigma3#Node#M2:sigma3]
link=[N25] node=[C25:sigma2#Node#M2:sigma2]
link=[N24] node=[C24:sigma1#Node#M2:sigma1]
link=[N23] node=[C23:fileSource#Node#M2:fileSource]
link=[N22] node=[M2:label3#Node#C22:label3]
link=[N21] node=[M2:CannyEdge3#Node#C21:CannyEdge3]
link=[N20] node=[M2:label2#Node#C20:label2]
link=[N19] node=[M2:CannyEdge2#Node#C19:CannyEdge2]
link=[N18] node=[M2:label1#Node#C18:label1]
link=[N17] node=[M2:CannyEdge1#Node#C17:CannyEdge1]
link=[N16] node=[M1:label2#Node#C16:label2]
link=[N15] node=[M1:CannyEdge2#Node#C15:CannyEdge2]
link=[N14] node=[M1:label1#Node#C14:label1]
link=[N13] node=[M1:CannyEdge1#Node#C13:CannyEdge1]
link=[N12] node=[M0:label3#Node#C12:label3]
link=[N11] node=[M0:CannyEdge3#Node#C11:CannyEdge3]
link=[N10] node=[M0:label2#Node#C10:label2]
link=[N9] node=[M0:CannyEdge2#Node#C9:CannyEdge2]
link=[N8] node=[M0:label1#Node#C8:label1]
link=[N7] node=[M0:CannyEdge1#Node#C7:CannyEdge1]
link=[N6] node=[C6:sigma2#Node#M1:sigma2]
link=[N5] node=[C5:sigma1#Node#M1:sigma1]
link=[N4] node=[C4:fileSource#Node#M1:fileSource]
link=[N0] node=[C0:fileSource#Node#M0:fileSource]
link=[N1] node=[C1:sigma1#Node#M0:sigma1]
link=[N2] node=[C2:sigma2#Node#M0:sigma2]
link=[N3] node=[C3:sigma3#Node#M0:sigma3]
connt=[C26] name=[sigma3] type=[in] format=[int] valOut=[3] RectF=[(-1563.6868855033683, -16.248761398930526, 70, 24)]
connt=[C25] name=[sigma2] type=[in] format=[int] valOut=[3] RectF=[(-1563.6868855033683, -101.24876139893053, 70, 24)]
connt=[C24] name=[sigma1] type=[in] format=[int] valOut=[3] RectF=[(-1563.6868855033683, -186.24876139893053, 70, 24)]
connt=[C23] name=[fileSource] type=[in] format=[path] valOut=[path] RectF=[(-1563.6868855033683, -271.2487613989305, 70, 24)]
connt=[C22] name=[label3] type=[out] format=[str] RectF=[(-1081.1400105033683, 0.7750481248789924, 70, 24)]
connt=[C21] name=[CannyEdge3] type=[out] format=[array_float] RectF=[(-1081.1400105033683, -57.03447568464482, 70, 24)]
connt=[C20] name=[label2] type=[out] format=[str] RectF=[(-1081.1400105033683, -114.84399949416864, 70, 24)]
connt=[C19] name=[CannyEdge2] type=[out] format=[array_float] RectF=[(-1081.1400105033683, -172.65352330369242, 70, 24)]
connt=[C18] name=[label1] type=[out] format=[str] RectF=[(-1081.1400105033683, -230.46304711321625, 70, 24)]
connt=[C17] name=[CannyEdge1] type=[out] format=[array_float] RectF=[(-1081.1400105033683, -288.27257092274004, 70, 24)]
submod=[M2] nameMod=[canny_3_modules] valInputs=[(['fileSource', 'sigma1', 'sigma2', 'sigma3'], ['Node(N23)', 'Node(N24)', 'Node(N25)', 'Node(N26)'], ['CannyEdge1', 'label1', 'CannyEdge2', 'label2', 'CannyEdge3', 'label3'], ['array_float', 'str', 'array_float', 'str', 'array_float', 'str'])] RectF=[(-1363.6868855033683, -203.74876139893053, 182.546875, 120.0)]
connt=[C16] name=[label2] type=[out] format=[str] RectF=[(-225.453125, 135.5, 70, 24)]
connt=[C15] name=[CannyEdge2] type=[out] format=[array_float] RectF=[(-225.453125, 78.5, 70, 24)]
connt=[C14] name=[label1] type=[out] format=[str] RectF=[(-225.453125, 21.5, 70, 24)]
connt=[C13] name=[CannyEdge1] type=[out] format=[array_float] RectF=[(-225.453125, -35.5, 70, 24)]
connt=[C12] name=[label3] type=[out] format=[str] RectF=[(-245.453125, -115.4761904761905, 70, 24)]
connt=[C11] name=[CannyEdge3] type=[out] format=[array_float] RectF=[(-245.453125, -173.28571428571428, 70, 24)]
connt=[C10] name=[label2] type=[out] format=[str] RectF=[(-245.453125, -231.0952380952381, 70, 24)]
connt=[C9] name=[CannyEdge2] type=[out] format=[array_float] RectF=[(-245.453125, -288.90476190476187, 70, 24)]
connt=[C8] name=[label1] type=[out] format=[str] RectF=[(-245.453125, -346.7142857142857, 70, 24)]
connt=[C7] name=[CannyEdge1] type=[out] format=[array_float] RectF=[(-245.453125, -404.5238095238095, 70, 24)]
connt=[C6] name=[sigma2] type=[in] format=[int] valOut=[3] RectF=[(-708.0, 124.66666666666666, 70, 24)]
connt=[C5] name=[sigma1] type=[in] format=[int] valOut=[3] RectF=[(-708.0, 50.0, 70, 24)]
connt=[C4] name=[fileSource] type=[in] format=[path] valOut=[path] RectF=[(-708.0, -24.666666666666664, 70, 24)]
submod=[M0] nameMod=[canny_3_modules] valInputs=[(['fileSource', 'sigma1', 'sigma2', 'sigma3'], ['Node(N0)', 'Node(N1)', 'Node(N2)', 'Node(N3)'], ['CannyEdge1', 'label1', 'CannyEdge2', 'label2', 'CannyEdge3', 'label3'], ['array_float', 'str', 'array_float', 'str', 'array_float', 'str'])] RectF=[(-536.9363491841636, -364.6817459208181, 195.05776385782906, 216.5125711889671)]
submod=[M1] nameMod=[canny_2_modules] valInputs=[(['fileSource', 'sigma1', 'sigma2'], ['Node(N4)', 'Node(N5)', 'Node(N6)'], ['CannyEdge1', 'label1', 'CannyEdge2', 'label2'], ['array_float', 'str', 'array_float', 'str'])] RectF=[(-538.3835872261566, -47.192634778647175, 196.84503369466177, 208.6834282519561)]
connt=[C0] name=[fileSource] type=[in] format=[path] valOut=[path] RectF=[(-728.0, -387.5, 70, 24)]
connt=[C1] name=[sigma1] type=[in] format=[int] valOut=[3] RectF=[(-728.0, -302.5, 70, 24)]
connt=[C2] name=[sigma2] type=[in] format=[int] valOut=[3] RectF=[(-728.0, -217.5, 70, 24)]
connt=[C3] name=[sigma3] type=[in] format=[int] valOut=[3] RectF=[(-728.0, -132.5, 70, 24)]
[execution]
['C0:fileSource=', 'C1:sigma1=', 'C23:fileSource=', 'C2:sigma2=', 'C24:sigma1=', 'C3:sigma3=', 'C25:sigma2=', 'C4:fileSource=', 'C26:sigma3=', 'C5:sigma1=', 'C6:sigma2=']
['ThreadOn', 'M0', 'M1', 'M2', 'ThreadOff']
{}
['C3:sigma3', 'C2:sigma2', 'C1:sigma1', 'C0:fileSource', 'C4:fileSource', 'C5:sigma1', 'C6:sigma2', 'M0:CannyEdge1', 'M0:label1', 'M0:CannyEdge2', 'M0:label2', 'M0:CannyEdge3', 'M0:label3', 'M1:CannyEdge1', 'M1:label1', 'M1:CannyEdge2', 'M1:label2', 'M2:CannyEdge1', 'M2:label1', 'M2:CannyEdge2', 'M2:label2', 'M2:CannyEdge3', 'M2:label3', 'C23:fileSource', 'C24:sigma1', 'C25:sigma2', 'C26:sigma3']
{'M1': ('canny_2_modules', "(['fileSource', 'sigma1', 'sigma2'], ['C4:fileSource', 'C5:sigma1', 'C6:sigma2'], ['CannyEdge1', 'label1', 'CannyEdge2', 'label2'], ['array_float', 'str', 'array_float', 'str'])"), 'M0': ('canny_3_modules', "(['fileSource', 'sigma1', 'sigma2', 'sigma3'], ['C0:fileSource', 'C1:sigma1', 'C2:sigma2', 'C3:sigma3'], ['CannyEdge1', 'label1', 'CannyEdge2', 'label2', 'CannyEdge3', 'label3'], ['array_float', 'str', 'array_float', 'str', 'array_float', 'str'])"), 'M2': ('canny_3_modules', "(['fileSource', 'sigma1', 'sigma2', 'sigma3'], ['C23:fileSource', 'C24:sigma1', 'C25:sigma2', 'C26:sigma3'], ['CannyEdge1', 'label1', 'CannyEdge2', 'label2', 'CannyEdge3', 'label3'], ['array_float', 'str', 'array_float', 'str', 'array_float', 'str'])")}
['C7:CannyEdge1=M0:CannyEdge1', 'C8:label1=M0:label1', 'C9:CannyEdge2=M0:CannyEdge2', 'C17:CannyEdge1=M2:CannyEdge1', 'C10:label2=M0:label2', 'C18:label1=M2:label1', 'C11:CannyEdge3=M0:CannyEdge3', 'C19:CannyEdge2=M2:CannyEdge2', 'C12:label3=M0:label3', 'C20:label2=M2:label2', 'C21:CannyEdge3=M2:CannyEdge3', 'C13:CannyEdge1=M1:CannyEdge1', 'C22:label3=M2:label3', 'C14:label1=M1:label1', 'C15:CannyEdge2=M1:CannyEdge2', 'C16:label2=M1:label2']
[submod M1]
['C0:fileSource=C4:fileSource', 'C5:sigma1=C5:sigma1', 'C6:sigma2=C6:sigma2']
['ThreadOn', 'U7', 'U8', 'U1', 'ThreadOff', 'ThreadOn', 'U3', 'U5', 'ThreadOff']
{'U5': ('Numpy.Image_filters', 'CannyEdge_Filter', "(['image', 'sigma'], ['U1:image', 'C6:sigma2'], ['CannyEdge'], ['array_float'])"), 'U3': ('Numpy.Image_filters', 'CannyEdge_Filter', "(['image', 'sigma'], ['U1:image', 'C5:sigma1'], ['CannyEdge'], ['array_float'])"), 'U1': ('Nifti.Nifti', 'Open_Nifti', "(['fileSource'], ['C0:fileSource'], ['image', 'dim', 'filePath'], ['array_float', 'int', 'path'])"), 'U8': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0'], ['canny=', 'C6:sigma2'], ['str_conc'], ['str'])"), 'U7': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0'], ['canny=', 'C5:sigma1'], ['str_conc'], ['str'])")}
['C6:sigma2', 'C5:sigma1', 'U8:str_conc', 'U5:CannyEdge', 'U7:str_conc', 'U3:CannyEdge', 'C0:fileSource', 'A2:', 'A2:', 'U1:image', 'U1:image', 'C5:sigma1', 'C6:sigma2']
{}
['M1:CannyEdge1=U3:CannyEdge', 'M1:label1=U7:str_conc', 'M1:CannyEdge2=U5:CannyEdge', 'M1:label2=U8:str_conc']
[submod M0]
['C0:fileSource=C0:fileSource', 'C1:sigma1=C1:sigma1', 'C2:sigma2=C2:sigma2', 'C3:sigma3=C3:sigma3']
['ThreadOn', 'U5', 'U0', 'U6', 'U4', 'ThreadOff', 'ThreadOn', 'U2', 'U1', 'U3', 'ThreadOff']
{'U0': ('Nifti.Nifti', 'Open_Nifti', "(['fileSource'], ['C0:fileSource'], ['image', 'dim', 'filePath'], ['array_float', 'int', 'path'])"), 'U1': ('Numpy.Image_filters', 'CannyEdge_Filter', "(['image', 'sigma'], ['U0:image', 'C1:sigma1'], ['CannyEdge'], ['array_float'])"), 'U2': ('Numpy.Image_filters', 'CannyEdge_Filter', "(['image', 'sigma'], ['U0:image', 'C2:sigma2'], ['CannyEdge'], ['array_float'])"), 'U3': ('Numpy.Image_filters', 'CannyEdge_Filter', "(['image', 'sigma'], ['U0:image', 'C3:sigma3'], ['CannyEdge'], ['array_float'])"), 'U5': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0'], ['canny=', 'C2:sigma2'], ['str_conc'], ['str'])"), 'U4': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0'], ['canny=', 'C1:sigma1'], ['str_conc'], ['str'])"), 'U6': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0'], ['canny=', 'C3:sigma3'], ['str_conc'], ['str'])")}
['U0:image', 'C0:fileSource', 'C1:sigma1', 'C2:sigma2', 'C3:sigma3', 'U0:image', 'U0:image', 'A0:', 'A0:', 'A0:', 'C1:sigma1', 'C2:sigma2', 'C3:sigma3', 'U1:CannyEdge', 'U4:str_conc', 'U2:CannyEdge', 'U5:str_conc', 'U3:CannyEdge', 'U6:str_conc']
{}
['M0:CannyEdge1=U1:CannyEdge', 'M0:label1=U4:str_conc', 'M0:CannyEdge2=U2:CannyEdge', 'M0:label2=U5:str_conc', 'M0:CannyEdge3=U3:CannyEdge', 'M0:label3=U6:str_conc']
[submod M2]
['C0:fileSource=C23:fileSource', 'C1:sigma1=C24:sigma1', 'C2:sigma2=C25:sigma2', 'C3:sigma3=C26:sigma3']
['ThreadOn', 'U5', 'U0', 'U6', 'U4', 'ThreadOff', 'ThreadOn', 'U2', 'U1', 'U3', 'ThreadOff']
{'U0': ('Nifti.Nifti', 'Open_Nifti', "(['fileSource'], ['C0:fileSource'], ['image', 'dim', 'filePath'], ['array_float', 'int', 'path'])"), 'U1': ('Numpy.Image_filters', 'CannyEdge_Filter', "(['image', 'sigma'], ['U0:image', 'C1:sigma1'], ['CannyEdge'], ['array_float'])"), 'U2': ('Numpy.Image_filters', 'CannyEdge_Filter', "(['image', 'sigma'], ['U0:image', 'C2:sigma2'], ['CannyEdge'], ['array_float'])"), 'U3': ('Numpy.Image_filters', 'CannyEdge_Filter', "(['image', 'sigma'], ['U0:image', 'C3:sigma3'], ['CannyEdge'], ['array_float'])"), 'U5': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0'], ['canny=', 'C2:sigma2'], ['str_conc'], ['str'])"), 'U4': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0'], ['canny=', 'C1:sigma1'], ['str_conc'], ['str'])"), 'U6': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0'], ['canny=', 'C3:sigma3'], ['str_conc'], ['str'])")}
['U0:image', 'C0:fileSource', 'C1:sigma1', 'C2:sigma2', 'C3:sigma3', 'U0:image', 'U0:image', 'A0:', 'A0:', 'A0:', 'C1:sigma1', 'C2:sigma2', 'C3:sigma3', 'U1:CannyEdge', 'U4:str_conc', 'U2:CannyEdge', 'U5:str_conc', 'U3:CannyEdge', 'U6:str_conc']
{}
['M2:CannyEdge1=U1:CannyEdge', 'M2:label1=U4:str_conc', 'M2:CannyEdge2=U2:CannyEdge', 'M2:label2=U5:str_conc', 'M2:CannyEdge3=U3:CannyEdge', 'M2:label3=U6:str_conc']

[diagram]
constant=[A12] value=['For Philips '] format=[str] label=[comment] RectF=[(2577.2369268827797, -50.02361534280867, 100.0, 33.0)]
constant=[A10] value=['False'] format=[bool] label=[bvals_bvecs] RectF=[(-947.7746922432048, 276.3859820378634, 79.0, 31.0)]
constant=[A9] value=['/tmp/'] format=[path] label=[path_export] RectF=[(-941.7750045474854, 194.2010717495753, 65.0, 33.0)]
constant=[A8] value=['PatientName-StudyName-CreationDate-SeqNumber-Protocol-SequenceName-AcquisitionTime'] format=[str] label=[naming] RectF=[(-1618.9047052133715, 129.56721078030307, 665.0, 33.0)]
constant=[A2] value=['True'] format=[bool] label=[recursive] RectF=[(-1061.2384647628871, -106.0111400593953, 79.0, 31.0)]
constant=[A1] value=['*.nii'] format=[str] label=[filter] RectF=[(-1018.2771504372251, -187.64194643449324, 53.0, 33.0)]
link=[N49] node=[A12:#Node#U25:comment]
link=[N48] node=[I0:out0#Node#U25:in_String]
link=[N47] node=[A3:#Node#I0:out0]
constant=[A3] value=['error !'] format=[str] label=[A3] RectF=[(2484.7833989737887, 94.98073625251303, 68.0, 33.0)]
link=[N46] node=[A0:#Node#I0:out0]
constant=[A0] value=["it's all good !"] format=[str] label=[A0] RectF=[(2469.0715620206033, 91.94018823952348, 111.0, 33.0)]
link=[N45] node=[U24:out#Node#I0:val]
link=[N44] node=[F0:out0#Node#U24:list_bool]
link=[N43] node=[U22:out#Node#F0:out0]
link=[N21] node=[C1:path_raw_Philips#Node#U16:in_file]
link=[N42] node=[A11:#Node#U21:y]
link=[N27] node=[A2:#Node#U13:recursive]
link=[N19] node=[A1:#Node#U13:filter]
link=[N18] node=[U15:list_out#Node#F0:in1]
link=[N16] node=[U0:list_out#Node#F0:in0]
link=[N11] node=[U13:listFiles#Node#U0:files_list]
link=[N7] node=[F0:in1#Node#U3:fileSource]
link=[N4] node=[F0:in1#Node#U5:nii_image]
link=[N1] node=[F0:in0#Node#U2:fileSource]
link=[N0] node=[F0:in0#Node#U7:nii_image]
link=[N13] node=[U5:nii_quaternions#Node#U10:list2]
link=[N12] node=[U7:nii_quaternions#Node#U10:list1]
link=[N8] node=[U5:nii_affine#Node#U8:image2]
link=[N6] node=[U7:nii_affine#Node#U8:image1]
link=[N5] node=[U4:image#Node#U6:y]
link=[N2] node=[U2:image#Node#U4:image1]
link=[N3] node=[U3:image#Node#U4:image2]
link=[N9] node=[F0:in0#Node#U9:inPath]
link=[N14] node=[A4:#Node#U9:comment]
link=[N25] node=[U6:rms#Node#U14:inFloat]
link=[N26] node=[A7:#Node#U14:comment]
link=[N15] node=[U8:image#Node#U12:y]
link=[N22] node=[U10:listSub#Node#U11:y]
link=[N23] node=[U12:rms#Node#U17:inFloat]
link=[N24] node=[A5:#Node#U17:comment]
link=[N28] node=[U11:rms#Node#U18:inFloat]
link=[N29] node=[A6:#Node#U18:comment]
link=[N33] node=[U22:out#Node#U23:inBool]
link=[N34] node=[U12:rms#Node#U19:x]
link=[N35] node=[U11:rms#Node#U20:x]
link=[N36] node=[U6:rms#Node#U21:x]
link=[N37] node=[A11:#Node#U19:y]
link=[N38] node=[A11:#Node#U20:y]
link=[N39] node=[U19:out#Node#U22:in_0]
link=[N40] node=[U20:out#Node#U22:in_1]
link=[N41] node=[U21:out#Node#U22:in_2]
link=[N10] node=[U1:list_files_exported#Node#U15:files_list]
link=[N20] node=[U16:ListPath#Node#U1:Philips_files]
link=[N30] node=[A8:#Node#U1:naming]
link=[N31] node=[A9:#Node#U1:path_export]
link=[N32] node=[A10:#Node#U1:bvals_bvecs]
link=[N17] node=[C0:path_Nifti_reference#Node#U13:RepDefault]
block=[U10] category=[Tools.ListOperation] class=[subtractListValues] valInputs=[(['list1', 'list2'], ['Node(N12)', 'Node(N13)'], ['listSub'], ['list_float'])] RectF=[(499.21512782549473, 13.221579478066374, 150.0, 80.0)]
block=[U8] category=[Numpy.Image_operations] class=[subtractImage_dyn] valInputs=[(['image1', 'image2'], ['Node(N6)', 'Node(N8)'], ['image'], ['array_float'])] RectF=[(511.4698078663197, -213.77009945065038, 152.0, 82.0)]
block=[U7] category=[Nifti.Info_Nifti] class=[Nifti_affine_quaternion] valInputs=[(['nii_image'], ['Node(N0)'], ['nii_affine', 'nii_quaternions'], ['array_float', 'list_float'])] RectF=[(63.13330872552214, -160.08891805676225, 201.171875, 82.0)]
block=[U5] category=[Nifti.Info_Nifti] class=[Nifti_affine_quaternion] valInputs=[(['nii_image'], ['Node(N4)'], ['nii_affine', 'nii_quaternions'], ['array_float', 'list_float'])] RectF=[(-8.473899024092816, -22.602376272504955, 199.171875, 80.0)]
block=[U6] category=[Numpy.Maths] class=[numpy_mean_array] valInputs=[(['y'], ['Node(N5)'], ['rms'], ['float'])] RectF=[(721.9668855573468, 225.25224410109865, 150.0, 80.0)]
block=[U2] category=[Nifti.Nifti] class=[Open_Nifti] valInputs=[(['fileSource'], ['Node(N1)'], ['image', 'dim', 'pixdim', 'filePath'], ['array_float', 'int', 'list_float', 'path'])] RectF=[(-20.060037381089614, 126.04741086467425, 150.0, 80.0)]
block=[U3] category=[Nifti.Nifti] class=[Open_Nifti] valInputs=[(['fileSource'], ['Node(N7)'], ['image', 'dim', 'pixdim', 'filePath'], ['array_float', 'int', 'list_float', 'path'])] RectF=[(-16.970746170656042, 285.20111737732634, 152.0, 82.0)]
block=[U4] category=[Numpy.Image_operations] class=[subtractImage_dyn] valInputs=[(['image1', 'image2'], ['Node(N2)', 'Node(N3)'], ['image'], ['array_float'])] RectF=[(456.5846341025416, 225.80099537883558, 150.0, 80.0)]
block=[U9] category=[Tools.Print] class=[Print_path] valInputs=[(['comment', 'inPath'], ['Node(N14)', 'Node(N9)'], [], [])] RectF=[(151.5865083076657, -299.0816819304356, 150.0, 80.0)]
constant=[A4] value=['\n********************************\nfile : '] format=[str] label=[comment] RectF=[(-144.38143073186797, -329.2833137068768, 255.0, 67.0)]
constant=[A5] value=['difference affine :'] format=[str] label=[comment] RectF=[(718.4721047399199, -309.2294410913576, 147.0, 33.0)]
constant=[A6] value=['difference quaternions : '] format=[str] label=[comment] RectF=[(694.933144948529, -68.79748631806777, 192.0, 33.0)]
block=[U14] category=[Tools.Print] class=[Print_float] valInputs=[(['comment', 'inFloat'], ['Node(N26)', 'Node(N25)'], [], [])] RectF=[(1061.697263635381, 184.21264606772706, 150.0, 80.0)]
constant=[A7] value=['mean of difference image : '] format=[str] label=[comment] RectF=[(684.4828211236038, 154.7777252696521, 211.0, 33.0)]
block=[U11] category=[Numpy.Maths] class=[numpy_mean_array] valInputs=[(['y'], ['Node(N22)'], ['rms'], ['float'])] RectF=[(733.1496505050468, 14.291641646548953, 152.0, 82.0)]
block=[U12] category=[Numpy.Maths] class=[numpy_mean_array] valInputs=[(['y'], ['Node(N15)'], ['rms'], ['float'])] RectF=[(730.4050193894789, -213.5127409456108, 152.0, 82.0)]
block=[U17] category=[Tools.Print] class=[Print_float] valInputs=[(['comment', 'inFloat'], ['Node(N24)', 'Node(N23)'], [], [])] RectF=[(1076.5619621536744, -297.8697733806796, 150.0, 80.0)]
block=[U18] category=[Tools.Print] class=[Print_float] valInputs=[(['comment', 'inFloat'], ['Node(N29)', 'Node(N28)'], [], [])] RectF=[(1065.9004761869633, -67.05385018091226, 150.0, 80.0)]
block=[U19] category=[Tools.Comparison_operations] class=[x_Equal_y] valInputs=[(['x', 'y'], ['Node(N34)', 'Node(N37)'], ['out'], ['bool'])] RectF=[(1350.5693766410611, -206.75069234632153, 150.0, 80.0)]
block=[U20] category=[Tools.Comparison_operations] class=[x_Equal_y] valInputs=[(['x', 'y'], ['Node(N35)', 'Node(N38)'], ['out'], ['bool'])] RectF=[(1333.4152152569243, 67.08994982834434, 152.0, 82.0)]
block=[U21] category=[Tools.Comparison_operations] class=[x_Equal_y] valInputs=[(['x', 'y'], ['Node(N36)', 'Node(N42)'], ['out'], ['bool'])] RectF=[(1341.8292885179724, 300.69316237634746, 152.0, 82.0)]
block=[U23] category=[Tools.Print] class=[Print_bool] valInputs=[(['comment', 'inBool'], ['', 'Node(N33)'], [], [])] RectF=[(1879.2860958218987, -101.35166728330393, 150.0, 80.0)]
constant=[A11] value=[0.0] format=[float] label=[y] RectF=[(1098.4429198704868, -148.99537475519512, 135.0, 31.0)]
block=[U22] category=[Tools.Logical_operations] class=[AND_dyn] valInputs=[(['in_0', 'in_1', 'in_2'], ['Node(N39)', 'Node(N40)', 'Node(N41)'], ['out'], ['bool'])] RectF=[(1616.4077573717145, -65.64632611507892, 173.6642992252182, 245.65009457652798)]
block=[U25] category=[Tools.Print] class=[Print_str] valInputs=[(['comment', 'in_String'], ['Node(N49)', 'Node(N48)'], [], [])] RectF=[(2739.415289513563, -24.337512784124215, 150.0, 80.0)]
block=[U24] category=[Tools.Comparison_operations] class=[all_iterable] valInputs=[(['list_bool'], ['Node(N44)'], ['out'], ['bool'])] RectF=[(2162.2894863718784, 6.72609017257669, 150.0, 80.0)]
loopIf=[I0] inputs=[[]] outputs=[[[['out0', 'in', 'str'], ['out0', 'out', 'str']]]] listItems=[[['A0'], ['A3']]] RectF=[(2425.6563897809947, 32.79004147492856, 219.0844931380011, 152.02685482192925)]
block=[U16] category=[Tools.PathManipulation] class=[ToListPath] valInputs=[(['in_file'], ['Node(N21)'], ['ListPath'], ['list_path'])] RectF=[(-892.387380257137, 31.740180419542497, 150.0, 80.0)]
block=[U15] category=[Tools.PathManipulation] class=[order_name_files] valInputs=[(['files_list', 'reverse'], ['Node(N10)', False], ['list_out'], ['list_path'])] RectF=[(-370.7442712138309, 143.49514818422108, 152.0, 82.0)]
block=[U0] category=[Tools.PathManipulation] class=[order_name_files] valInputs=[(['files_list', 'reverse'], ['Node(N11)', False], ['list_out'], ['list_path'])] RectF=[(-415.8762119702619, -177.15724927259603, 150.0, 80.0)]
block=[U13] category=[File_IO.Dialog_files_directories] class=[list_files_in_directory] valInputs=[(['RepDefault', 'title', 'filter', 'recursive'], ['Node(N17)', 'Select a directory', 'Node(N19)', 'Node(N27)'], ['listFiles'], ['list_path'])] RectF=[(-882.9122971258648, -210.05733503484817, 158.328125, 120.2043785309045)]
loopFor=[F0] inputs=[[[['in0', 'in', 'list_path'], ['in0', 'out', 'path']], [['in1', 'in', 'list_path'], ['in1', 'out', 'path']]]] outputs=[[[['out0', 'in', 'bool'], ['out0', 'out', 'list_bool']]]] listItems=[['U3', 'U5', 'A11', 'U22', 'U6', 'U17', 'U2', 'U18', 'U21', 'U14', 'U23', 'U4', 'U7', 'U12', 'U9', 'U8', 'A5', 'U10', 'U19', 'A6', 'A4', 'U20', 'A7', 'U11']] RectF=[(-153.37921366106298, -354.55724789635144, 2227.213494213255, 804.4447196579645)]
block=[U1] category=[Java.MRIFileManager] class=[PhilipsToNifti] valInputs=[(['Philips_files', 'naming', 'path_export', 'bvals_bvecs'], ['Node(N20)', 'Node(N30)', 'Node(N31)', 'Node(N32)'], ['list_files_exported'], ['list_path'])] RectF=[(-668.0533490242233, 69.00081539217331, 230.78125, 204.41056108588822)]
connt=[C0] name=[path_Nifti_reference] type=[in] format=[path] valOut=[path] RectF=[(-1106.6059044489791, -237.9912329003485, 70, 24)]
connt=[C1] name=[path_raw_Philips] type=[in] format=[path] valOut=[path] RectF=[(-1097.5597442756848, 5.801497229542893, 70, 24)]
[execution]
['C0:path_Nifti_reference=', 'C1:path_raw_Philips=']
['ThreadOn', 'U16', 'U13', 'ThreadOff', 'ThreadOn', 'U0', 'U1', 'ThreadOff', 'U15', 'F0', 'U24', 'I0', 'U25']
{'U0': ('Tools.PathManipulation', 'order_name_files', "(['files_list', 'reverse'], ['U13:listFiles', False], ['list_out'], ['list_path'])"), 'U15': ('Tools.PathManipulation', 'order_name_files', "(['files_list', 'reverse'], ['U1:list_files_exported', False], ['list_out'], ['list_path'])"), 'U16': ('Tools.PathManipulation', 'ToListPath', "(['in_file'], ['C1:path_raw_Philips'], ['ListPath'], ['list_path'])"), 'U24': ('Tools.Comparison_operations', 'all_iterable', "(['list_bool'], ['F0:out0'], ['out'], ['bool'])"), 'U1': ('Java.MRIFileManager', 'PhilipsToNifti', "(['Philips_files', 'naming', 'path_export', 'bvals_bvecs'], ['U16:ListPath', 'PatientName-StudyName-CreationDate-SeqNumber-Protocol-SequenceName-AcquisitionTime', '/tmp/', False], ['list_files_exported'], ['list_path'])"), 'U13': ('File_IO.Dialog_files_directories', 'list_files_in_directory', "(['RepDefault', 'title', 'filter', 'recursive'], ['C0:path_Nifti_reference', 'Select a directory', '*.nii', True], ['listFiles'], ['list_path'])"), 'U25': ('Tools.Print', 'Print_str', "(['comment', 'in_String'], ['For Philips ', 'I0:out0'], [], [])")}
['C0:path_Nifti_reference', 'A10:', 'A9:', 'A8:', 'U16:ListPath', 'U1:list_files_exported', 'A11:', 'A11:', 'A6:', 'A5:', 'A7:', 'A4:', 'F0:in0', 'U7:nii_quaternions', 'F0:in0', 'F0:in0', 'F0:in1', 'F0:in1', 'U13:listFiles', 'U0:list_out', 'U15:list_out', 'A1:', 'A2:', 'A11:', 'C1:path_raw_Philips', 'F0:out0', 'U24:out', 'A0:', 'A3:', 'I0:out0', 'A12:']
{}
[]
[loopfor F0]
['F0:in0=U0:list_out', 'F0:in1=U15:list_out']
['ThreadOn', 'U2', 'U3', 'U5', 'U7', 'U9', 'ThreadOff', 'U10', 'U4', 'U8', 'U12', 'U11', 'U6', 'U20', 'U21', 'U19', 'U22', 'ThreadOn', 'U14', 'U17', 'U18', 'U23', 'ThreadOff']
{'U22': ('Tools.Logical_operations', 'AND_dyn', "(['in_0', 'in_1', 'in_2'], ['U19:out', 'U20:out', 'U21:out'], ['out'], ['bool'])"), 'U23': ('Tools.Print', 'Print_bool', "(['comment', 'inBool'], ['', 'U22:out'], [], [])"), 'U12': ('Numpy.Maths', 'numpy_mean_array', "(['y'], ['U8:image'], ['rms'], ['float'])"), 'U11': ('Numpy.Maths', 'numpy_mean_array', "(['y'], ['U10:listSub'], ['rms'], ['float'])"), 'U4': ('Numpy.Image_operations', 'subtractImage_dyn', "(['image1', 'image2'], ['U2:image', 'U3:image'], ['image'], ['array_float'])"), 'U3': ('Nifti.Nifti', 'Open_Nifti', "(['fileSource'], ['F0:in1'], ['image', 'dim', 'pixdim', 'filePath'], ['array_float', 'int', 'list_float', 'path'])"), 'U2': ('Nifti.Nifti', 'Open_Nifti', "(['fileSource'], ['F0:in0'], ['image', 'dim', 'pixdim', 'filePath'], ['array_float', 'int', 'list_float', 'path'])"), 'U6': ('Numpy.Maths', 'numpy_mean_array', "(['y'], ['U4:image'], ['rms'], ['float'])"), 'U5': ('Nifti.Info_Nifti', 'Nifti_affine_quaternion', "(['nii_image'], ['F0:in1'], ['nii_affine', 'nii_quaternions'], ['array_float', 'list_float'])"), 'U7': ('Nifti.Info_Nifti', 'Nifti_affine_quaternion', "(['nii_image'], ['F0:in0'], ['nii_affine', 'nii_quaternions'], ['array_float', 'list_float'])"), 'U8': ('Numpy.Image_operations', 'subtractImage_dyn', "(['image1', 'image2'], ['U7:nii_affine', 'U5:nii_affine'], ['image'], ['array_float'])"), 'U10': ('Tools.ListOperation', 'subtractListValues', "(['list1', 'list2'], ['U7:nii_quaternions', 'U5:nii_quaternions'], ['listSub'], ['list_float'])"), 'U20': ('Tools.Comparison_operations', 'x_Equal_y', "(['x', 'y'], ['U11:rms', 0.0], ['out'], ['bool'])"), 'U19': ('Tools.Comparison_operations', 'x_Equal_y', "(['x', 'y'], ['U12:rms', 0.0], ['out'], ['bool'])"), 'U18': ('Tools.Print', 'Print_float', "(['comment', 'inFloat'], ['difference quaternions : ', 'U11:rms'], [], [])"), 'U17': ('Tools.Print', 'Print_float', "(['comment', 'inFloat'], ['difference affine :', 'U12:rms'], [], [])"), 'U14': ('Tools.Print', 'Print_float', "(['comment', 'inFloat'], ['mean of difference image : ', 'U6:rms'], [], [])"), 'U9': ('Tools.Print', 'Print_path', "(['comment', 'inPath'], ['\\n********************************\\nfile : ', 'F0:in0'], [], [])"), 'U21': ('Tools.Comparison_operations', 'x_Equal_y', "(['x', 'y'], ['U6:rms', 0.0], ['out'], ['bool'])")}
['U21:out', 'U20:out', 'U19:out', 'U6:rms', 'U11:rms', 'U12:rms', 'U22:out', 'U11:rms', 'U12:rms', 'U10:listSub', 'U8:image', 'U6:rms', 'F0:in0', 'U3:image', 'U2:image', 'U4:image', 'U7:nii_affine', 'U5:nii_affine', 'U7:nii_quaternions', 'U5:nii_quaternions', 'F0:in0', 'F0:in0', 'F0:in1', 'F0:in1', 'U22:out']
{}
['F0:out0=U22:out', 'I0:out0=[["it\'s all good !"], [\'error !\']]']
[loopif I0 True]
['I0:val=U24:out']
[]
{}
[]
{}
["I0:out0=it's all good !"]
[loopif I0 False]
['I0:val=U24:out']
[]
{}
[]
{}
['I0:out0=error !']

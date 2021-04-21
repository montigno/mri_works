[diagram]
link=[N43] node=[A19:#Node#U0:--use-histogram-matching]
link=[N32] node=[F0:out0#Node#C1:GenericAffine_mat]
link=[N31] node=[F0:out1#Node#C2:out_warped_image]
link=[N30] node=[F0:out2#Node#C5:out_inverse_warped_image]
link=[N29] node=[U0:outputWarpedImage#Node#F0:out1]
link=[N42] node=[U0:outputInverseWarpedImage#Node#F0:out2]
link=[N27] node=[A15:#Node#U2:stringIn_3]
link=[N20] node=[U9:str_conc#Node#U2:stringIn_2]
link=[N18] node=[A14:#Node#U2:stringIn_1]
link=[N39] node=[A12:#Node#U9:stringIn_2]
link=[N25] node=[A17:#Node#U9:stringIn_0]
link=[N38] node=[U6:str_conc#Node#U9:stringIn]
link=[N37] node=[U8:str_conc#Node#U2:stringIn_0]
link=[N23] node=[U6:str_conc#Node#U8:stringIn]
link=[N21] node=[A16:#Node#U8:stringIn_0]
link=[N35] node=[U3:nameFile#Node#U8:stringIn_1]
link=[N36] node=[A4:#Node#U8:stringIn_2]
link=[N34] node=[U7:outString#Node#U0:--masks]
link=[N14] node=[C4:mean_brain_extraction#Node#U7:inPath]
link=[N33] node=[U5:outString#Node#U1:stringIn_0]
link=[N5] node=[C3:mean_N4bias#Node#U5:inPath]
link=[N17] node=[F0:in0#Node#U3:inPath]
link=[N15] node=[U2:str_conc#Node#U0:output]
link=[N13] node=[A11:#Node#U0:--winsorize-image-intensities]
link=[N12] node=[A10:#Node#U0:--smoothing-sigmas]
link=[N11] node=[A9:#Node#U0:--shrink-factors]
link=[N10] node=[A8:#Node#U1:stringIn_3]
link=[N3] node=[U1:str_conc#Node#U0:--metric]
link=[N2] node=[A2:#Node#U0:--initial-moving-transform]
link=[N1] node=[A1:#Node#U0:--interpolation]
link=[N0] node=[A0:#Node#U0:--dimensionality]
link=[N4] node=[A3:#Node#U1:stringIn]
link=[N6] node=[A5:#Node#U1:stringIn_1]
link=[N7] node=[F0:in0#Node#U1:stringIn_2]
link=[N8] node=[A6:#Node#U0:--transform]
link=[N9] node=[A7:#Node#U0:--convergence]
link=[N16] node=[A13:#Node#U2:stringIn]
link=[N19] node=[U4:out_sep#Node#U6:stringIn_0]
link=[N22] node=[U3:directory#Node#U6:stringIn]
link=[N24] node=[C0:files_in#Node#F0:in0]
link=[N26] node=[U3:nameFile#Node#U9:stringIn_1]
link=[N28] node=[U8:str_conc#Node#U10:stringIn]
link=[N40] node=[A18:#Node#U10:stringIn_0]
link=[N41] node=[U10:str_conc#Node#F0:out0]
block=[U0] category=[ANTs.registration] class=[antsRegistration] valInputs=[(['output', '--dimensionality', '--interpolation', '--initial-moving-transform', '--metric', '--transform', '--convergence', '--smoothing-sigmas', '--shrink-factors', '--use-histogram-matching', '--winsorize-image-intensities', '--masks'], ['Node(N15)', 'Node(N0)', 'Node(N1)', 'Node(N2)', 'Node(N3)', 'Node(N8)', 'Node(N9)', 'Node(N12)', 'Node(N11)', 'Node(N43)', 'Node(N13)', 'Node(N34)'], ['outputWarpedImage', 'outputInverseWarpedImage'], ['path', 'path'])] RectF=[(513.658355012704, 150.18739477429818, 405.5951728636444, 474.5796803640836)]
constant=[A19] value=['0'] format=[str] label=[--use-histogram-matching] RectF=[(408.65835501270396, 491.3545502294294, 34.0, 33.0)]
constant=[A12] value=['_wrpd.nii.gz'] format=[str] label=[stringIn_2] RectF=[(-629.1892301737394, 102.15504441418864, 107.0, 33.0)]
block=[U9] category=[Tools.StringManipulation] class=[string_concatenat_dyn] valInputs=[(['stringIn', 'stringIn_0', 'stringIn_1', 'stringIn_2'], ['Node(N38)', 'Node(N25)', 'Node(N26)', 'Node(N39)'], ['str_conc'], ['str'])] RectF=[(-445.84468228952994, 40.081772562689196, 156.71875, 80.0)]
block=[U8] category=[Tools.StringManipulation] class=[string_concatenat_dyn] valInputs=[(['stringIn', 'stringIn_0', 'stringIn_1', 'stringIn_2'], ['Node(N23)', 'Node(N21)', 'Node(N35)', 'Node(N36)'], ['str_conc'], ['str'])] RectF=[(-396.24211397913996, -178.05067671532754, 156.71875, 80.0)]
constant=[A17] value=['a_'] format=[str] label=[stringIn_5] RectF=[(-588.255707487212, 9.856183977257729, 42.0, 33.0)]
block=[U3] category=[Tools.PathManipulation] class=[separatePath_2ext] valInputs=[(['inPath'], ['Node(N17)'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])] RectF=[(-982.226984885303, -158.93026933976608, 154.83244523182987, 80.99865395760085)]
constant=[A11] value=['[0.0005,0.9995]'] format=[str] label=[--winsorize-image-intensities] RectF=[(89.07599758235267, 504.19523553958135, 131.0, 33.0)]
constant=[A10] value=['2x0vox'] format=[str] label=[--smoothing-sigmas] RectF=[(157.734619723184, 416.69890569348007, 74.0, 33.0)]
constant=[A9] value=['2x1'] format=[str] label=[--shrink-factors] RectF=[(332.3211119529652, 439.1908101854691, 50.0, 33.0)]
constant=[A8] value=[',1,4,Regular,0.5]'] format=[str] label=[stringIn_3] RectF=[(-505.4822025451881, 445.6765061515294, 135.0, 33.0)]
block=[U1] category=[Tools.StringManipulation] class=[string_concatenat_dyn] valInputs=[(['stringIn', 'stringIn_0', 'stringIn_1', 'stringIn_2', 'stringIn_3'], ['Node(N4)', 'Node(N33)', 'Node(N6)', 'Node(N7)', 'Node(N10)'], ['str_conc'], ['str'])] RectF=[(-289.19597496361905, 186.7208651684743, 156.71875000000003, 323.6878459568727)]
constant=[A2] value=['Identity'] format=[str] label=[--initial-moving-transform] RectF=[(111.31717396556826, 292.0927003687405, 80.0, 33.0)]
constant=[A1] value=['Linear'] format=[str] label=[--interpolation] RectF=[(-11.887107226300259, 235.2767662861649, 68.0, 33.0)]
constant=[A0] value=[3] format=[int] label=[--dimensionality] RectF=[(144.5287154891488, 197.76914390717906, 98.0, 31.0)]
constant=[A3] value=['GC['] format=[str] label=[stringIn] RectF=[(-419.34343638535347, 213.98617555062953, 50.0, 33.0)]
constant=[A5] value=[','] format=[str] label=[stringIn_1] RectF=[(-365.88792642794033, 331.6976033149546, 29.0, 33.0)]
constant=[A6] value=['Rigid[0.05]'] format=[str] label=[--transform] RectF=[(279.2848290484506, 347.8081379853221, 99.0, 33.0)]
constant=[A7] value=['[800x800,1e-7]'] format=[str] label=[--convergence] RectF=[(-9.830581099139351, 383.5703290944204, 127.0, 33.0)]
constant=[A13] value=['['] format=[str] label=[stringIn] RectF=[(-239.00611298400247, -40.0333650240172, 30.0, 33.0)]
constant=[A14] value=[','] format=[str] label=[stringIn_1] RectF=[(-246.70435831555278, 29.376765553997075, 29.0, 33.0)]
constant=[A15] value=[']'] format=[str] label=[stringIn_3] RectF=[(-243.95940219639078, 117.51303554834789, 30.0, 33.0)]
constant=[A16] value=['x_'] format=[str] label=[stringIn_1] RectF=[(-559.1409719228856, -247.71996008229678, 42.0, 33.0)]
block=[U4] category=[Tools.Os] class=[separator_path] valInputs=[([], [], ['out_sep'], ['str'])] RectF=[(-975.5032342344876, 14.335737522408408, 159.46823240634632, 45.626363554063516)]
block=[U6] category=[Tools.StringManipulation] class=[string_concatenat_dyn] valInputs=[(['stringIn', 'stringIn_0'], ['Node(N22)', 'Node(N19)'], ['str_conc'], ['str'])] RectF=[(-756.7961352215453, -223.94517357029514, 156.71875, 50.81512508723489)]
constant=[A4] value=['_'] format=[str] label=[stringIn_1] RectF=[(-480.11108697005113, -98.89787924664739, 34.0, 33.0)]
block=[U2] category=[Tools.StringManipulation] class=[string_concatenat_dyn] valInputs=[(['stringIn', 'stringIn_0', 'stringIn_1', 'stringIn_2', 'stringIn_3'], ['Node(N16)', 'Node(N37)', 'Node(N18)', 'Node(N20)', 'Node(N27)'], ['str_conc'], ['str'])] RectF=[(-70.93254626647024, -56.018622207991314, 212.00673888772502, 217.48697638641562)]
block=[U10] category=[Tools.StringManipulation] class=[string_concatenat_dyn] valInputs=[(['stringIn', 'stringIn_0'], ['Node(N28)', 'Node(N40)'], ['str_conc'], ['str'])] RectF=[(234.53107555979216, -207.27995217000387, 159.71875, 83.0)]
constant=[A18] value=['0GenericAffine.mat'] format=[str] label=[stringIn_0] RectF=[(26.828257806995907, -132.45293654457657, 159.0, 33.0)]
connt=[C5] name=[out_inverse_warped_image] type=[out] format=[list_path] RectF=[(1171.5146638296749, 421.745278978683, 70, 24)]
block=[U7] category=[Tools.Conversion] class=[PathToString] valInputs=[(['inPath'], ['Node(N14)'], ['outString'], ['str'])] RectF=[(-1323.5897373997386, 510.69169423441303, 153.0, 83.0)]
block=[U5] category=[Tools.Conversion] class=[PathToString] valInputs=[(['inPath'], ['Node(N5)'], ['outString'], ['str'])] RectF=[(-1325.3907266187898, 253.17985521815984, 150.0, 80.0)]
connt=[C4] name=[mean_brain_extraction] type=[in] format=[path] valOut=[path] RectF=[(-1449.5687673352336, 540.5404766250512, 70, 24)]
connt=[C3] name=[mean_N4bias] type=[in] format=[path] valOut=[path] RectF=[(-1456.625363512034, 281.2974977123084, 70, 24)]
loopFor=[F0] inputs=[[[['in0', 'in', 'list_path'], ['in0', 'out', 'path']]]] outputs=[[[['out0', 'in', 'path'], ['out0', 'out', 'list_path']], [['out1', 'in', 'path'], ['out1', 'out', 'list_path']], [['out2', 'in', 'path'], ['out2', 'out', 'list_path']]]] listItems=[['A13', 'A2', 'U10', 'A14', 'A16', 'A10', 'A15', 'A8', 'U6', 'U9', 'U0', 'A9', 'A18', 'A11', 'U1', 'U8', 'U4', 'U2', 'A4', 'A12', 'A19', 'A5', 'A0', 'A6', 'A3', 'A17', 'U3', 'A1', 'A7']] RectF=[(-1109.7810695634453, -274.49996197859525, 2152.650328028871, 947.2033812081128)]
connt=[C0] name=[files_in] type=[in] format=[list_path] valOut=[['path']] RectF=[(-1461.8582911797746, 187.32382312882174, 70, 24)]
connt=[C1] name=[GenericAffine_mat] type=[out] format=[list_path] RectF=[(1170.5875760877661, -46.23536890615159, 70, 24)]
connt=[C2] name=[out_warped_image] type=[out] format=[list_path] RectF=[(1154.0696479005576, 186.41763084554574, 70, 24)]
[execution]
['C0:files_in=', 'C3:mean_N4bias=', 'C4:mean_brain_extraction=']
['ThreadOn', 'U7', 'U5', 'ThreadOff', 'F0']
{'U5': ('Tools.Conversion', 'PathToString', "(['inPath'], ['C3:mean_N4bias'], ['outString'], ['str'])"), 'U7': ('Tools.Conversion', 'PathToString', "(['inPath'], ['C4:mean_brain_extraction'], ['outString'], ['str'])")}
['A18:', 'C0:files_in', 'A13:', 'A7:', 'A6:', 'F0:in0', 'A5:', 'A3:', 'A0:', 'A1:', 'A2:', 'A8:', 'A9:', 'A10:', 'A11:', 'F0:in0', 'C3:mean_N4bias', 'U5:outString', 'C4:mean_brain_extraction', 'U7:outString', 'A4:', 'A16:', 'A17:', 'A12:', 'A14:', 'A15:', 'U0:outputWarpedImage', 'F0:out2', 'F0:out1', 'F0:out0', 'A19:']
{}
['C1:GenericAffine_mat=F0:out0', 'C2:out_warped_image=F0:out1', 'C5:out_inverse_warped_image=F0:out2']
[loopfor F0]
['F0:in0=C0:files_in']
['ThreadOn', 'U1', 'U3', 'U4', 'ThreadOff', 'U6', 'U8', 'U9', 'U2', 'ThreadOn', 'U0', 'U10', 'ThreadOff']
{'U6': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0'], ['U3:directory', 'U4:out_sep'], ['str_conc'], ['str'])"), 'U4': ('Tools.Os', 'separator_path', "([], [], ['out_sep'], ['str'])"), 'U3': ('Tools.PathManipulation', 'separatePath_2ext', "(['inPath'], ['F0:in0'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])"), 'U10': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0'], ['U8:str_conc', '0GenericAffine.mat'], ['str_conc'], ['str'])"), 'U1': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0', 'stringIn_1', 'stringIn_2', 'stringIn_3'], ['GC[', 'U5:outString', ',', 'F0:in0', ',1,4,Regular,0.5]'], ['str_conc'], ['str'])"), 'U8': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0', 'stringIn_1', 'stringIn_2'], ['U6:str_conc', 'x_', 'U3:nameFile', '_'], ['str_conc'], ['str'])"), 'U9': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0', 'stringIn_1', 'stringIn_2'], ['U6:str_conc', 'a_', 'U3:nameFile', '_wrpd.nii.gz'], ['str_conc'], ['str'])"), 'U2': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0', 'stringIn_1', 'stringIn_2', 'stringIn_3'], ['[', 'U8:str_conc', ',', 'U9:str_conc', ']'], ['str_conc'], ['str'])"), 'U0': ('ANTs.registration', 'antsRegistration', "(['output', '--dimensionality', '--interpolation', '--initial-moving-transform', '--metric', '--transform', '--convergence', '--smoothing-sigmas', '--shrink-factors', '--use-histogram-matching', '--winsorize-image-intensities', '--masks'], ['U2:str_conc', 3, 'Linear', 'Identity', 'U1:str_conc', 'Rigid[0.05]', '[800x800,1e-7]', '2x0vox', '2x1', '0', '[0.0005,0.9995]', 'U7:outString'], ['outputWarpedImage', 'outputInverseWarpedImage'], ['path', 'path'])")}
['U10:str_conc', 'U8:str_conc', 'U3:nameFile', 'U3:directory', 'U4:out_sep', 'F0:in0', 'U1:str_conc', 'U2:str_conc', 'F0:in0', 'U5:outString', 'U7:outString', 'U3:nameFile', 'U6:str_conc', 'U8:str_conc', 'U6:str_conc', 'U9:str_conc', 'U0:outputInverseWarpedImage', 'U0:outputWarpedImage']
{}
['F0:out0=U10:str_conc', 'F0:out2=U0:outputInverseWarpedImage', 'F0:out1=U0:outputWarpedImage']
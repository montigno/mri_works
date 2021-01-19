[diagram]
constant=[A1] value=[15] format=[int] label=[index_start] RectF=[(-142.06140212283708, 106.87278449610281, 87.0, 31.0)]
constant=[A2] value=[249] format=[int] label=[index_end] RectF=[(-149.64817612566327, 196.11287360473432, 87.0, 31.0)]
constant=[A7] value=['listStructures'] format=[str] label=[fileName] RectF=[(1007.6625850735186, -706.9583773585431, 100.0, 33.0)]
link=[N36] node=[U7:out_dir#Node#C3:out_dir_structures]
link=[N29] node=[C2:files_name_prefix#Node#U15:fileName]
link=[N0] node=[C1:Atlas_labels#Node#U0:file]
link=[N34] node=[A17:#Node#U16:delete_file]
link=[N33] node=[U12:outfile#Node#U16:file_in]
link=[N35] node=[U15:outFile#Node#U9:file_path]
link=[N28] node=[U7:out_dir#Node#U15:inPath]
link=[N32] node=[U13:newString#Node#U9:new_str]
link=[N31] node=[A15:#Node#U13:newCharact]
link=[N30] node=[A14:#Node#U13:charactToreplace]
link=[N25] node=[U11:newString#Node#U13:string_in]
link=[N27] node=[U10:outFloat#Node#U12:threshold_low]
link=[N16] node=[U9:newPath#Node#U12:output_file]
link=[N17] node=[U4:outInt#Node#U10:inInt]
link=[N11] node=[U5:out_element#Node#U4:inString]
link=[N4] node=[U1:out_subarray#Node#F0:in0]
link=[N1] node=[U0:array_csv#Node#U1:in_string_array]
link=[N2] node=[A1:#Node#U1:index_start]
link=[N3] node=[A2:#Node#U1:index_end]
link=[N5] node=[F0:in0#Node#U2:in_string_list]
link=[N6] node=[A3:#Node#U2:index]
link=[N7] node=[U2:out_element#Node#U3:in_string]
link=[N8] node=[A4:#Node#U3:expr]
link=[N9] node=[U3:list_string#Node#U5:in_string_list]
link=[N10] node=[U3:list_string#Node#U6:in_string_list]
link=[N14] node=[A5:#Node#U5:index]
link=[N15] node=[A6:#Node#U6:index]
link=[N18] node=[U6:out_element#Node#U8:in_string]
link=[N21] node=[A10:#Node#U8:start]
link=[N22] node=[A11:#Node#U8:end]
link=[N20] node=[U8:substring#Node#U11:string_in]
link=[N23] node=[A12:#Node#U11:charactToreplace]
link=[N24] node=[A13:#Node#U11:newCharact]
link=[N12] node=[U10:outFloat#Node#U12:threshold_high]
link=[N19] node=[U14:directory#Node#U18:inPath]
link=[N38] node=[U18:outFile#Node#U7:dir_in]
link=[N39] node=[A7:#Node#U18:fileName]
link=[N26] node=[C0:Label_registred#Node#U12:image]
link=[N13] node=[C0:Label_registred#Node#U14:inPath]
constant=[A17] value=['True'] format=[bool] label=[delete_file] RectF=[(2827.3042518723287, 132.02143530304986, 73.0, 31.0)]
block=[U16] category=[File_IO.Save_image_nii_gz] class=[Create_gzip] valInputs=[(['file_in', 'delete_file'], ['Node(N33)', 'Node(N34)'], [], [])] RectF=[(2938.524162017845, 53.72203433294004, 150.0, 80.0)]
constant=[A15] value=['_'] format=[str] label=[newCharact] RectF=[(1807.4013071528257, 333.0562197650401, 32.0, 33.0)]
constant=[A14] value=['/'] format=[str] label=[charactToreplace] RectF=[(1679.8403932463384, 295.8350600010005, 31.0, 33.0)]
block=[U13] category=[Tools.StringManipulation] class=[string_replace] valInputs=[(['string_in', 'charactToreplace', 'newCharact'], ['Node(N25)', 'Node(N30)', 'Node(N31)'], ['newString'], ['str'])] RectF=[(2006.9957489749545, 247.97751254637285, 216.15625, 82.0)]
block=[U12] category=[Nifti.process_Nifti] class=[threshold_low_high] valInputs=[(['image', 'threshold_low', 'threshold_high', 'output_file'], ['Node(N26)', 'Node(N27)', 'Node(N12)', 'Node(N16)'], ['outfile'], ['path'])] RectF=[(2620.64258254536, -67.1087154137835, 198.72032299819648, 172.37072571343592)]
block=[U10] category=[Tools.Conversion] class=[IntToFloat_simple] valInputs=[(['inInt'], ['Node(N17)'], ['outFloat'], ['float'])] RectF=[(1633.8163367202278, -86.8325878301383, 150.0, 80.0)]
block=[U9] category=[Tools.PathManipulation] class=[add_suffixprefix_file] valInputs=[(['file_path', 'new_str', 'place'], ['Node(N35)', 'Node(N32)', 'suffix'], ['newPath'], ['path'])] RectF=[(2391.1894151817005, 222.54623192056272, 150.0, 80.0)]
block=[U4] category=[Tools.Conversion] class=[StringToInt] valInputs=[(['inString'], ['Node(N11)'], ['outInt'], ['int'])] RectF=[(1290.8682929396996, -97.8167907926287, 150.0, 80.0)]
block=[U2] category=[Tools.StringManipulation] class=[string_index_list] valInputs=[(['in_string_list', 'index'], ['Node(N5)', 'Node(N6)'], ['out_element'], ['str'])] RectF=[(541.0788918799954, -11.87532711457753, 198.296875, 80.0)]
constant=[A3] value=[0] format=[int] label=[index] RectF=[(409.18823148907995, 174.09215920015563, 87.0, 31.0)]
block=[U3] category=[Tools.StringManipulation] class=[string_split] valInputs=[(['in_string', 'expr'], ['Node(N7)', 'Node(N8)'], ['list_string'], ['list_str'])] RectF=[(782.8400295713541, -1.5567328679622392, 157.515625, 80.0)]
constant=[A4] value=['\t'] format=[str] label=[expr] RectF=[(708.7452331417696, 108.57254462658562, 29.0, 33.0)]
block=[U5] category=[Tools.StringManipulation] class=[string_index_list] valInputs=[(['in_string_list', 'index'], ['Node(N9)', 'Node(N14)'], ['out_element'], ['str'])] RectF=[(1017.1013064454678, -99.94955159379043, 200.296875, 82.0)]
block=[U6] category=[Tools.StringManipulation] class=[string_index_list] valInputs=[(['in_string_list', 'index'], ['Node(N10)', 'Node(N15)'], ['out_element'], ['str'])] RectF=[(1022.4090718958446, 64.5911773678904, 202.296875, 84.0)]
constant=[A5] value=[0] format=[int] label=[index] RectF=[(836.9474728963582, -86.44351247964585, 87.0, 31.0)]
constant=[A6] value=[7] format=[int] label=[index] RectF=[(816.07209597683, 142.19292231264438, 87.0, 31.0)]
block=[U8] category=[Tools.StringManipulation] class=[string_substring] valInputs=[(['in_string', 'start', 'end'], ['Node(N18)', 'Node(N21)', 'Node(N22)'], ['substring'], ['str'])] RectF=[(1348.3951963471604, 157.77037457195223, 153.375, 80.0)]
constant=[A10] value=[1] format=[int] label=[start] RectF=[(1178.71823086196, 188.46250943927674, 87.0, 31.0)]
constant=[A11] value=[-1] format=[int] label=[end] RectF=[(1177.64017056347, 256.5221262800341, 87.0, 31.0)]
block=[U11] category=[Tools.StringManipulation] class=[string_replace] valInputs=[(['string_in', 'charactToreplace', 'newCharact'], ['Node(N20)', 'Node(N23)', 'Node(N24)'], ['newString'], ['str'])] RectF=[(1697.071406136079, 172.59708298658273, 214.15625, 80.0)]
constant=[A12] value=[' '] format=[str] label=[charactToreplace] RectF=[(1521.957532648426, 229.74998700974305, 29.0, 33.0)]
constant=[A13] value=['_'] format=[str] label=[newCharact] RectF=[(1511.6680487043045, 304.2077415073772, 32.0, 33.0)]
connt=[C3] name=[out_dir_structures] type=[out] format=[path] RectF=[(1985.4609363574868, -925.0243157874559, 70, 24)]
connt=[C2] name=[files_name_prefix] type=[in] format=[str] valOut=[] RectF=[(628.3405030643389, -465.45411494403527, 70, 24)]
connt=[C1] name=[Atlas_labels] type=[in] format=[path] valOut=[path] RectF=[(-371.8478433599204, -4.733650950742808, 70, 24)]
block=[U15] category=[Tools.PathManipulation] class=[joinPath] valInputs=[(['inPath', 'fileName'], ['Node(N28)', 'Node(N29)'], ['outFile'], ['path'])] RectF=[(1685.387170158063, -725.2728917497268, 150.0, 80.0)]
block=[U14] category=[Tools.PathManipulation] class=[separatePath] valInputs=[(['inPath'], ['Node(N13)'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])] RectF=[(887.9715628150578, -825.2623063162976, 150.0, 80.0)]
block=[U7] category=[File_IO.Create_files_directories] class=[create_directory] valInputs=[(['dir_in'], ['Node(N38)'], ['out_dir'], ['path'])] RectF=[(1416.3915017859156, -833.4069633140617, 150.0, 80.0)]
loopFor=[F0] inputs=[[[['in0', 'in', 'array_str'], ['in0', 'out', 'list_str']]]] outputs=[[]] listItems=[['A5', 'U2', 'A3', 'U16', 'U6', 'U5', 'U9', 'A17', 'U3', 'A15', 'A13', 'A6', 'U13', 'U11', 'A4', 'U10', 'A11', 'U12', 'U4', 'A12', 'A10', 'U8', 'A14']] RectF=[(381.2195290628247, -153.55997876617346, 2732.806174129159, 581.0120395506447)]
block=[U0] category=[CSV.csv_file] class=[csv_reader_file] valInputs=[(['file'], ['Node(N0)'], ['array_csv'], ['array_str'])] RectF=[(-167.10847061287075, -28.18325008291876, 150.0, 80.0)]
block=[U1] category=[Tools.StringManipulation] class=[string_index_subarray] valInputs=[(['in_string_array', 'index_start', 'index_end'], ['Node(N1)', 'Node(N2)', 'Node(N3)'], ['out_subarray'], ['array_str'])] RectF=[(86.85075962638561, 63.557901033309975, 223.359375, 134.22367069766167)]
block=[U18] category=[Tools.PathManipulation] class=[joinPath] valInputs=[(['inPath', 'fileName'], ['Node(N19)', 'Node(N39)'], ['outFile'], ['path'])] RectF=[(1173.5919915473742, -837.1122867620893, 152.0, 82.0)]
connt=[C0] name=[Label_registred] type=[in] format=[path] valOut=[path] RectF=[(615.8320758264053, -580.6991954003995, 70, 24)]
[execution]
['C0:Label_registred=', 'C2:files_name_prefix=', 'C1:Atlas_labels=']
['ThreadOn', 'U0', 'U14', 'ThreadOff', 'ThreadOn', 'U18', 'U1', 'ThreadOff', 'U7', 'U15', 'F0']
{'U0': ('CSV.csv_file', 'csv_reader_file', "(['file'], ['C1:Atlas_labels'], ['array_csv'], ['array_str'])"), 'U7': ('File_IO.Create_files_directories', 'create_directory', "(['dir_in'], ['U18:outFile'], ['out_dir'], ['path'])"), 'U14': ('Tools.PathManipulation', 'separatePath', "(['inPath'], ['C0:Label_registred'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])"), 'U15': ('Tools.PathManipulation', 'joinPath', "(['inPath', 'fileName'], ['U7:out_dir', 'C2:files_name_prefix'], ['outFile'], ['path'])"), 'U18': ('Tools.PathManipulation', 'joinPath', "(['inPath', 'fileName'], ['U14:directory', 'listStructures'], ['outFile'], ['path'])"), 'U1': ('Tools.StringManipulation', 'string_index_subarray', "(['in_string_array', 'index_start', 'index_end'], ['U0:array_csv', 15, 249], ['out_subarray'], ['array_str'])")}
['C0:Label_registred', 'C0:Label_registred', 'A7:', 'U18:outFile', 'U14:directory', 'A13:', 'A12:', 'A11:', 'A10:', 'A6:', 'A5:', 'U3:list_string', 'A4:', 'A3:', 'F0:in0', 'A2:', 'A1:', 'U0:array_csv', 'U1:out_subarray', 'A14:', 'A15:', 'U7:out_dir', 'U15:outFile', 'A17:', 'C1:Atlas_labels', 'C2:files_name_prefix', 'U7:out_dir']
{}
['C3:out_dir_structures=U7:out_dir']
[loopfor F0]
['F0:in0=U1:out_subarray']
['U2', 'U3', 'U6', 'U5', 'U4', 'U8', 'U11', 'U10', 'U13', 'U9', 'U12', 'U16']
{'U4': ('Tools.Conversion', 'StringToInt', "(['inString'], ['U5:out_element'], ['outInt'], ['int'])"), 'U9': ('Tools.PathManipulation', 'add_suffixprefix_file', "(['file_path', 'new_str', 'place'], ['U15:outFile', 'U13:newString', 'suffix'], ['newPath'], ['path'])"), 'U10': ('Tools.Conversion', 'IntToFloat_simple', "(['inInt'], ['U4:outInt'], ['outFloat'], ['float'])"), 'U12': ('Nifti.process_Nifti', 'threshold_low_high', "(['image', 'threshold_low', 'threshold_high', 'output_file'], ['C0:Label_registred', 'U10:outFloat', 'U10:outFloat', 'U9:newPath'], ['outfile'], ['path'])"), 'U11': ('Tools.StringManipulation', 'string_replace', "(['string_in', 'charactToreplace', 'newCharact'], ['U8:substring', ' ', '_'], ['newString'], ['str'])"), 'U8': ('Tools.StringManipulation', 'string_substring', "(['in_string', 'start', 'end'], ['U6:out_element', 1, -1], ['substring'], ['str'])"), 'U6': ('Tools.StringManipulation', 'string_index_list', "(['in_string_list', 'index'], ['U3:list_string', 7], ['out_element'], ['str'])"), 'U5': ('Tools.StringManipulation', 'string_index_list', "(['in_string_list', 'index'], ['U3:list_string', 0], ['out_element'], ['str'])"), 'U3': ('Tools.StringManipulation', 'string_split', "(['in_string', 'expr'], ['U2:out_element', '\\t'], ['list_string'], ['list_str'])"), 'U2': ('Tools.StringManipulation', 'string_index_list', "(['in_string_list', 'index'], ['F0:in0', 0], ['out_element'], ['str'])"), 'U13': ('Tools.StringManipulation', 'string_replace', "(['string_in', 'charactToreplace', 'newCharact'], ['U11:newString', '/', '_'], ['newString'], ['str'])"), 'U16': ('File_IO.Save_image_nii_gz', 'Create_gzip', "(['file_in', 'delete_file'], ['U12:outfile', True], [], [])")}
['C0:Label_registred', 'U10:outFloat', 'U8:substring', 'U6:out_element', 'U3:list_string', 'U3:list_string', 'U2:out_element', 'F0:in0', 'U5:out_element', 'U4:outInt', 'U9:newPath', 'U10:outFloat', 'U11:newString', 'U13:newString', 'U15:outFile', 'U12:outfile']
{}
[]

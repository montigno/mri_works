[diagram]
constant=[A3] value=[0] format=[int] label=[index] RectF=[(68.52906996396752, 453.0128605572943, 98.0, 31.0)]
constant=[A8] value=['SIGMA_Anatomical_Brain_Atlas_Labels.txt'] format=[str] label=[fileName] RectF=[(-71.24987233827608, 205.45890781109082, 314.0, 33.0)]
constant=[A4] value=['.json'] format=[str] label=[new_extension] RectF=[(-558.0460378181394, -291.66370173565434, 57.0, 33.0)]
constant=[A5] value=['StudyName'] format=[str] label=[tag] RectF=[(-283.6004011016642, -191.2582438039809, 104.0, 33.0)]
constant=[A6] value=['_analyse.txt'] format=[str] label=[stringIn_0] RectF=[(278.5025992742215, -415.790757730046, 107.0, 33.0)]
constant=[A7] value=['_mask_.nii'] format=[str] label=[stringIn_0] RectF=[(252.55853033925956, -176.00773793516797, 95.0, 33.0)]
link=[N33] node=[U12:outPath#Node#M5:Diff MD Nifti]
link=[N32] node=[A3:#Node#U12:index]
link=[N20] node=[M2:out_image_transformed#Node#U12:listPath]
link=[N19] node=[M2:out_image_registred#Node#M5:Diff FA Nifti]
link=[N7] node=[U11:outFile#Node#M3:Atlas_labels]
link=[N31] node=[A8:#Node#U11:fileName]
link=[N30] node=[U10:directory#Node#U11:inPath]
link=[N29] node=[U9:projet_path#Node#U10:inPath]
link=[N3] node=[M0:output_file#Node#M1:image_fixed]
link=[N8] node=[M1:out_label_registred#Node#M3:Label_registred]
link=[N10] node=[A4:#Node#U3:new_extension]
link=[N11] node=[U3:newPath#Node#U2:jsonFile]
link=[N12] node=[A5:#Node#U2:tag]
link=[N13] node=[U2:ValueTag#Node#U4:in_string]
link=[N16] node=[M3:out_dir_structures#Node#M4:structures_directory]
link=[N17] node=[M4:list_outfiles#Node#M5:list_structures]
link=[N21] node=[U3:newPath#Node#U5:inPath]
link=[N22] node=[U4:substring#Node#U6:stringIn]
link=[N23] node=[A6:#Node#U6:stringIn_0]
link=[N24] node=[U5:directory#Node#U7:inPath]
link=[N25] node=[U6:str_conc#Node#U7:fileName]
link=[N26] node=[U7:outFile#Node#M5:outfile_result_name]
link=[N15] node=[U4:substring#Node#U8:stringIn]
link=[N27] node=[U8:str_conc#Node#M3:files_name_prefix]
link=[N28] node=[A7:#Node#U8:stringIn_0]
link=[N9] node=[C0:T1_Flash_3D#Node#U3:file_path]
link=[N18] node=[C0:T1_Flash_3D#Node#M5:T1_Flash Nifti]
link=[N0] node=[C0:T1_Flash_3D#Node#M0:input_nifti]
link=[N4] node=[C0:T1_Flash_3D#Node#M2:reference_nifti]
link=[N1] node=[C1:Diffusion_nifti#Node#M2:Diffusion_nifti]
block=[U12] category=[Tools.PathManipulation] class=[indexListPath] valInputs=[(['listPath', 'index'], ['Node(N20)', 'Node(N32)'], ['outPath'], ['path'])] RectF=[(272.3216951300698, 383.698906549115, 150.0, 80.0)]
submod=[M2] nameMod=[IG_Registration_diffusion] valInputs=[(['reference_nifti', 'Diffusion_nifti'], ['Node(N4)', 'Node(N1)'], ['out_image_registred', 'out_image_transformed'], ['path', 'list_path'])] RectF=[(-290.68399914868576, 320.40673011317807, 284.03125, 80.0)]
block=[U11] category=[Tools.PathManipulation] class=[joinPath] valInputs=[(['inPath', 'fileName'], ['Node(N30)', 'Node(N31)'], ['outFile'], ['path'])] RectF=[(412.42649364216936, 70.50025532344776, 150.0, 80.0)]
block=[U10] category=[Tools.PathManipulation] class=[separatePath] valInputs=[(['inPath'], ['Node(N29)'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])] RectF=[(21.150076597034342, 78.7252851111833, 150.0, 80.0)]
block=[U9] category=[Tools.Os] class=[projet_path] valInputs=[([], [], ['projet_path'], ['path'])] RectF=[(-247.92589788745792, 79.90028936657416, 150.0, 80.0)]
submod=[M0] nameMod=[IG_N4bias_segmentation] valInputs=[(['input_nifti'], ['Node(N0)'], ['output_file'], ['path'])] RectF=[(-336.86632539925824, -49.83848871735306, 174.140625, 80.0)]
submod=[M1] nameMod=[IG_Registration_Atlas] valInputs=[(['image_fixed'], ['Node(N3)'], ['out_template_registred', 'out_label_registred'], ['path', 'path'])] RectF=[(-56.12868182277953, -48.8083611377491, 262.40625, 80.0)]
submod=[M3] nameMod=[IG_list_structures] valInputs=[(['Label_registred', 'files_name_prefix', 'Atlas_labels'], ['Node(N8)', 'Node(N27)', 'Node(N7)'], ['out_dir_structures'], ['path'])] RectF=[(729.3139984850711, -236.66055273470852, 269.890625, 110.26579341109039)]
block=[U2] category=[Irmage.Json_Irmage] class=[Json_File] valInputs=[(['jsonFile', 'tag'], ['Node(N11)', 'Node(N12)'], ['hasJson', 'jsonFile', 'ValueTag'], ['bool', 'path', 'str'])] RectF=[(-59.306039287236594, -348.1194034344567, 150.0, 80.0)]
block=[U3] category=[Tools.PathManipulation] class=[change_extension] valInputs=[(['file_path', 'new_extension'], ['Node(N9)', 'Node(N10)'], ['newPath'], ['path'])] RectF=[(-391.49773279221915, -328.68502044364806, 186.03125, 80.0)]
block=[U4] category=[Tools.StringManipulation] class=[string_substring] valInputs=[(['in_string', 'start', 'end'], ['Node(N13)', 2, -2], ['substring'], ['str'])] RectF=[(160.90424598460683, -305.0078719824859, 153.375, 80.0)]
submod=[M4] nameMod=[IG_erosion_1px] valInputs=[(['structures_directory'], ['Node(N16)'], ['list_outfiles'], ['list_path'])] RectF=[(1067.009937841174, -222.71612352752015, 240.71875, 80.0)]
submod=[M5] nameMod=[IG_calculs] valInputs=[(['list_structures', 'T1_Flash Nifti', 'Diff FA Nifti', 'Diff MD Nifti', 'outfile_result_name'], ['Node(N17)', 'Node(N18)', 'Node(N19)', 'Node(N33)', 'Node(N26)'], [], [])] RectF=[(1698.4996150199079, -181.65417302132528, 203.05640548283895, 301.80202793779017)]
block=[U5] category=[Tools.PathManipulation] class=[separatePath] valInputs=[(['inPath'], ['Node(N21)'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])] RectF=[(-47.06281718521691, -516.3027073275023, 150.0, 80.0)]
block=[U6] category=[Tools.StringManipulation] class=[string_concatenat_dyn] valInputs=[(['stringIn', 'stringIn_0'], ['Node(N22)', 'Node(N23)'], ['str_conc'], ['str'])] RectF=[(508.79148806512967, -452.9040139769363, 156.71875, 80.0)]
block=[U7] category=[Tools.PathManipulation] class=[joinPath] valInputs=[(['inPath', 'fileName'], ['Node(N24)', 'Node(N25)'], ['outFile'], ['path'])] RectF=[(788.8116396303526, -524.1447135319402, 150.0, 80.0)]
block=[U8] category=[Tools.StringManipulation] class=[string_concatenat_dyn] valInputs=[(['stringIn', 'stringIn_0'], ['Node(N15)', 'Node(N28)'], ['str_conc'], ['str'])] RectF=[(452.94655800065595, -293.28642496369594, 158.71875, 82.0)]
connt=[C0] name=[T1_Flash_3D] type=[in] format=[path] valOut=[path] RectF=[(-684.1535201625746, -107.1310193799307, 70, 24)]
connt=[C1] name=[Diffusion_nifti] type=[in] format=[path] valOut=[path] RectF=[(-694.7694642279189, 357.18997846096806, 70, 24)]
comments=[] RectF=[(1121.217262074671, 494.2028163953311, 977.7971839372578, 10.0)] text=['This pipeline requires 3 files which must be placed in the same project directory :\n    - SIGMA_Anatomical_Brain_Atlas.nii\n    - SIGMA_ExVivo_Brain_Template_Masked.nii\n    - SIGMA_Anatomical_Brain_Atlas_Labels.txt\n ']
[execution]
['C0:T1_Flash_3D=', 'C1:Diffusion_nifti=']
['U9', 'ThreadOn', 'M2', 'M0', 'U3', 'U10', 'ThreadOff', 'ThreadOn', 'U2', 'U5', 'U11', 'M1', 'U12', 'ThreadOff', 'U4', 'ThreadOn', 'U8', 'U6', 'ThreadOff', 'ThreadOn', 'U7', 'M3', 'ThreadOff', 'M4', 'M5']
{'U7': ('Tools.PathManipulation', 'joinPath', "(['inPath', 'fileName'], ['U5:directory', 'U6:str_conc'], ['outFile'], ['path'])"), 'U5': ('Tools.PathManipulation', 'separatePath', "(['inPath'], ['U3:newPath'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])"), 'U4': ('Tools.StringManipulation', 'string_substring', "(['in_string', 'start', 'end'], ['U2:ValueTag', 2, -2], ['substring'], ['str'])"), 'U9': ('Tools.Os', 'projet_path', "([], [], ['projet_path'], ['path'])"), 'U10': ('Tools.PathManipulation', 'separatePath', "(['inPath'], ['U9:projet_path'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])"), 'U8': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0'], ['U4:substring', '_mask_.nii'], ['str_conc'], ['str'])"), 'U6': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0'], ['U4:substring', '_analyse.txt'], ['str_conc'], ['str'])"), 'U2': ('Irmage.Json_Irmage', 'Json_File', "(['jsonFile', 'tag'], ['U3:newPath', 'StudyName'], ['hasJson', 'jsonFile', 'ValueTag'], ['bool', 'path', 'str'])"), 'U3': ('Tools.PathManipulation', 'change_extension', "(['file_path', 'new_extension'], ['C0:T1_Flash_3D', '.json'], ['newPath'], ['path'])"), 'U11': ('Tools.PathManipulation', 'joinPath', "(['inPath', 'fileName'], ['U10:directory', 'SIGMA_Anatomical_Brain_Atlas_Labels.txt'], ['outFile'], ['path'])"), 'U12': ('Tools.PathManipulation', 'indexListPath', "(['listPath', 'index'], ['M2:out_image_transformed', 0], ['outPath'], ['path'])")}
['C1:Diffusion_nifti', 'C0:T1_Flash_3D', 'C0:T1_Flash_3D', 'C0:T1_Flash_3D', 'C0:T1_Flash_3D', 'A7:', 'U8:str_conc', 'U4:substring', 'U7:outFile', 'U6:str_conc', 'U5:directory', 'A6:', 'U4:substring', 'U3:newPath', 'M4:list_outfiles', 'M3:out_dir_structures', 'U2:ValueTag', 'A5:', 'U3:newPath', 'A4:', 'M1:out_label_registred', 'M0:output_file', 'U9:projet_path', 'U10:directory', 'A8:', 'U11:outFile', 'M2:out_image_registred', 'M2:out_image_transformed', 'A3:', 'U12:outPath']
{'M5': ('IG_calculs', "(['list_structures', 'T1_Flash Nifti', 'Diff FA Nifti', 'Diff MD Nifti', 'outfile_result_name'], ['M4:list_outfiles', 'C0:T1_Flash_3D', 'M2:out_image_registred', 'U12:outPath', 'U7:outFile'], [], [])"), 'M4': ('IG_erosion_1px', "(['structures_directory'], ['M3:out_dir_structures'], ['list_outfiles'], ['list_path'])"), 'M3': ('IG_list_structures', "(['Label_registred', 'files_name_prefix', 'Atlas_labels'], ['M1:out_label_registred', 'U8:str_conc', 'U11:outFile'], ['out_dir_structures'], ['path'])"), 'M1': ('IG_Registration_Atlas', "(['image_fixed'], ['M0:output_file'], ['out_template_registred', 'out_label_registred'], ['path', 'path'])"), 'M0': ('IG_N4bias_segmentation', "(['input_nifti'], ['C0:T1_Flash_3D'], ['output_file'], ['path'])"), 'M2': ('IG_Registration_diffusion', "(['reference_nifti', 'Diffusion_nifti'], ['C0:T1_Flash_3D', 'C1:Diffusion_nifti'], ['out_image_registred', 'out_image_transformed'], ['path', 'list_path'])")}
[]
[submod M5]
['C0:list_structures=M4:list_outfiles', 'C1:T1_Flash Nifti=C0:T1_Flash_3D', 'C2:Diff FA Nifti=M2:out_image_registred', 'C3:Diff MD Nifti=U12:outPath', 'C4:outfile_result_name=U7:outFile']
['ThreadOn', 'U2', 'U0', 'ThreadOff', 'S0']
{'U0': ('Tools.PathManipulation', 'build_list_path_dyn', "(['in_path', 'in_path_0', 'in_path_1'], ['C1:T1_Flash Nifti', 'C2:Diff FA Nifti', 'C3:Diff MD Nifti'], ['path_list'], ['list_path'])"), 'U2': ('Tools.PathManipulation', 'order_name_files', "(['files_list', 'reverse'], ['C0:list_structures', False], ['list_out'], ['list_path'])")}
['U0:path_list', 'U2:list_out', 'C0:list_structures', 'C3:Diff MD Nifti', 'C2:Diff FA Nifti', 'C1:T1_Flash Nifti', 'C4:outfile_result_name']
{}
[]
[submod M4]
['C0:structures_directory=M3:out_dir_structures']
['U0', 'F0', 'U9', 'P0']
{'U9': ('Tools.PathManipulation', 'concat_list_path_dyn', "(['list_files', 'list_files_0'], ['U0:listFiles', 'F0:out0'], ['path_list'], ['list_path'])"), 'U0': ('File_IO.Dialog_files_directories', 'list_files_in_directory', "(['RepDefault', 'title', 'filter', 'recursive'], ['C0:structures_directory', 'Select a directory', '*', True], ['listFiles'], ['list_path'])"), 'P0': ('list_path', 'Length', 'U9:path_list')}
['U9:path_list', 'F0:out0', 'U0:listFiles', 'A2:', 'F0:in0', 'U0:listFiles', 'F0:in0', 'F0:in0', 'U6:nameFile', 'A1:', 'A3:', 'C0:structures_directory', 'U9:path_list']
{}
['M4:list_outfiles=U9:path_list']
[submod M3]
['C0:Label_registred=M1:out_label_registred', 'C2:files_name_prefix=U8:str_conc', 'C1:Atlas_labels=U11:outFile']
['ThreadOn', 'U0', 'U14', 'ThreadOff', 'ThreadOn', 'U18', 'U1', 'ThreadOff', 'U7', 'U15', 'F0']
{'U0': ('CSV.csv_file', 'csv_reader_file', "(['file'], ['C1:Atlas_labels'], ['array_csv'], ['array_str'])"), 'U7': ('File_IO.Create_files_directories', 'create_directory', "(['dir_in'], ['U18:outFile'], ['out_dir'], ['path'])"), 'U14': ('Tools.PathManipulation', 'separatePath', "(['inPath'], ['C0:Label_registred'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])"), 'U15': ('Tools.PathManipulation', 'joinPath', "(['inPath', 'fileName'], ['U7:out_dir', 'C2:files_name_prefix'], ['outFile'], ['path'])"), 'U18': ('Tools.PathManipulation', 'joinPath', "(['inPath', 'fileName'], ['U14:directory', 'listStructures'], ['outFile'], ['path'])"), 'U1': ('Tools.StringManipulation', 'string_index_subarray', "(['in_string_array', 'index_start', 'index_end'], ['U0:array_csv', 15, 249], ['out_subarray'], ['array_str'])")}
['C0:Label_registred', 'C0:Label_registred', 'A7:', 'U18:outFile', 'U14:directory', 'A13:', 'A12:', 'A11:', 'A10:', 'A6:', 'A5:', 'U3:list_string', 'A4:', 'A3:', 'F0:in0', 'A2:', 'A1:', 'U0:array_csv', 'U1:out_subarray', 'A14:', 'A15:', 'U7:out_dir', 'U15:outFile', 'A17:', 'C1:Atlas_labels', 'C2:files_name_prefix', 'U7:out_dir']
{}
['M3:out_dir_structures=U7:out_dir']
[submod M1]
['C0:image_fixed=M0:output_file']
['U8', 'ThreadOn', 'U4', 'U1', 'U9', 'ThreadOff', 'ThreadOn', 'U10', 'U5', 'U11', 'U2', 'ThreadOff', 'U0', 'ThreadOn', 'U6', 'U3', 'ThreadOff', 'U7', 'U12']
{'U9': ('Tools.PathManipulation', 'separatePath', "(['inPath'], ['U8:projet_path'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])"), 'U8': ('Tools.Os', 'projet_path', "([], [], ['projet_path'], ['path'])"), 'U11': ('Tools.PathManipulation', 'joinPath', "(['inPath', 'fileName'], ['U9:directory', 'SIGMA_Anatomical_Brain_Atlas.nii'], ['outFile'], ['path'])"), 'U10': ('Tools.PathManipulation', 'joinPath', "(['inPath', 'fileName'], ['U9:directory', 'SIGMA_ExVivo_Brain_Template_Masked.nii'], ['outFile'], ['path'])"), 'U5': ('Tools.PathManipulation', 'change_extension', "(['file_path', 'new_extension'], ['U4:newPath', '.mat'], ['newPath'], ['path'])"), 'U4': ('Tools.PathManipulation', 'add_suffixprefix_file', "(['file_path', 'new_str', 'place'], ['C0:image_fixed', '_RegLinLab', 'suffix'], ['newPath'], ['path'])"), 'U3': ('Nipype.Interfaces_fsl_preprocess', 'fsl_FLIRT', "(['in_file', 'reference', 'apply_xfm', 'in_matrix_file', 'interp', 'out_file', 'out_matrix_file', 'output_type'], ['U11:outFile', 'U0:out_file', True, 'U0:out_matrix_file', 'nearestneighbour', 'U4:newPath', 'U5:newPath', 'NIFTI'], ['out_file', 'out_log', 'out_matrix_file'], ['path', 'path', 'path'])"), 'U1': ('Tools.PathManipulation', 'add_suffixprefix_file', "(['file_path', 'new_str', 'place'], ['C0:image_fixed', '_RegLinTemp', 'suffix'], ['newPath'], ['path'])"), 'U2': ('Tools.PathManipulation', 'change_extension', "(['file_path', 'new_extension'], ['U1:newPath', '.mat'], ['newPath'], ['path'])"), 'U0': ('Nipype.Interfaces_fsl_preprocess', 'fsl_FLIRT', "(['in_file', 'reference', 'cost_func', 'interp', 'out_file', 'out_matrix_file', 'output_type'], ['U10:outFile', 'C0:image_fixed', 'normcorr', 'nearestneighbour', 'U1:newPath', 'U2:newPath', 'NIFTI'], ['out_file', 'out_log', 'out_matrix_file'], ['path', 'path', 'path'])"), 'U6': ('Tools.PathManipulation', 'add_suffixprefix_file', "(['file_path', 'new_str', 'place'], ['U0:out_file', '_regNoLin_Template', 'suffix'], ['newPath'], ['path'])"), 'U7': ('Tools.PathManipulation', 'add_suffixprefix_file', "(['file_path', 'new_str', 'place'], ['U3:out_file', '_regNoLin_Label', 'suffix'], ['newPath'], ['path'])"), 'U12': ('Irmage.Registration', 'Non_linear_registration_for_Atlases', "(['image_fixed', 'atlas_template_moved', 'atlas_label_moved', 'output_template_name', 'output_label_name', 'interpolator', 'transform'], ['C0:image_fixed', 'U0:out_file', 'U3:out_file', 'U6:newPath', 'U7:newPath', 'nearestNeighbor', 'SyNOnly'], ['out_template_registred', 'out_label_registred'], ['path', 'path'])")}
['A7:', 'U11:outFile', 'U9:directory', 'A0:', 'U10:outFile', 'U9:directory', 'U8:projet_path', 'A6:', 'U5:newPath', 'A11:', 'U4:newPath', 'A10:', 'U4:newPath', 'A9:', 'U0:out_matrix_file', 'A8:', 'U0:out_file', 'A2:', 'A3:', 'A4:', 'U1:newPath', 'U1:newPath', 'U2:newPath', 'A5:', 'A6:', 'U0:out_file', 'U3:out_file', 'U0:out_file', 'A12:', 'U6:newPath', 'U3:out_file', 'A13:', 'U7:newPath', 'A14:', 'A15:', 'C0:image_fixed', 'C0:image_fixed', 'C0:image_fixed', 'C0:image_fixed', 'U12:out_template_registred', 'U12:out_label_registred']
{}
['M1:out_template_registred=U12:out_template_registred', 'M1:out_label_registred=U12:out_label_registred']
[submod M0]
['C0:input_nifti=C0:T1_Flash_3D']
['U3', 'U2', 'U4', 'U0']
{'U2': ('Nipype.Interfaces_ants_segmentation', 'ants_N4BiasFieldCorrection', "(['input_image', 'save_bias', 'copy_header', 'output_image'], ['C0:input_nifti', False, False, 'U3:newPath'], ['output_image', 'bias_image'], ['path', 'path'])"), 'U3': ('Tools.PathManipulation', 'add_suffixprefix_file', "(['file_path', 'new_str', 'place'], ['C0:input_nifti', '_N4bias', 'suffix'], ['newPath'], ['path'])"), 'U0': ('Irmage.Segmentation', 'Seg_conv3D', "(['file_in', 'file_out_name', 'threshold', 'radius'], ['U2:output_image', 'U4:newPath', 1.0, 8], ['output_file'], ['path'])"), 'U4': ('Tools.PathManipulation', 'add_suffixprefix_file', "(['file_path', 'new_str', 'place'], ['U2:output_image', '_seg', 'suffix'], ['newPath'], ['path'])")}
['U3:newPath', 'A0:', 'C0:input_nifti', 'A2:', 'A3:', 'U2:output_image', 'C0:input_nifti', 'U2:output_image', 'U4:newPath', 'A1:', 'U0:output_file']
{}
['M0:output_file=U0:output_file']
[submod M2]
['C0:reference_nifti=C0:T1_Flash_3D', 'C1:Diffusion_nifti=C1:Diffusion_nifti']
['U14', 'U1', 'ThreadOn', 'U2', 'U13', 'U6', 'ThreadOff', 'ThreadOn', 'U7', 'U16', 'U3', 'ThreadOff', 'ThreadOn', 'U4', 'U8', 'U17', 'ThreadOff', 'U0', 'ThreadOn', 'U5', 'U12', 'ThreadOff', 'ThreadOn', 'U19', 'U10', 'ThreadOff', 'U18', 'F0']
{'U14': ('Tools.PathManipulation', 'separatePath', "(['inPath'], ['C1:Diffusion_nifti'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])"), 'U1': ('Nifti.funcs', 'four_to_three', "(['image_nii_4D', 'out_directory'], ['C1:Diffusion_nifti', 'U14:directory'], ['list_3D_images'], ['list_path'])"), 'U19': ('Tools.PathManipulation', 'ToListPath', "(['in_file'], ['U5:out_file'], ['ListPath'], ['list_path'])"), 'U17': ('Tools.PathManipulation', 'change_extension', "(['file_path', 'new_extension'], ['U16:newPath', '.mat'], ['newPath'], ['path'])"), 'U13': ('Tools.PathManipulation', 'indexListPath', "(['listPath', 'index'], ['U1:list_3D_images', 0], ['outPath'], ['path'])"), 'U16': ('Tools.PathManipulation', 'add_suffixprefix_file', "(['file_path', 'new_str', 'place'], ['U13:outPath', '_RegLinFA', 'suffix'], ['newPath'], ['path'])"), 'U10': ('Tools.PathManipulation', 'add_suffixprefix_file', "(['file_path', 'new_str', 'place'], ['U12:out_file', '_NoLinFA', 'suffix'], ['newPath'], ['path'])"), 'U8': ('Tools.PathManipulation', 'change_extension', "(['file_path', 'new_extension'], ['U7:newPath', '.mat'], ['newPath'], ['path'])"), 'U7': ('Tools.PathManipulation', 'add_suffixprefix_file', "(['file_path', 'new_str', 'place'], ['U6:outPath', '_RegLinMD', 'suffix'], ['newPath'], ['path'])"), 'U5': ('Nipype.Interfaces_fsl_preprocess', 'fsl_FLIRT', "(['in_file', 'reference', 'apply_xfm', 'in_matrix_file', 'interp', 'out_file', 'out_matrix_file', 'output_type'], ['U6:outPath', 'U0:out_file', True, 'U0:out_matrix_file', 'nearestneighbour', 'U7:newPath', 'U8:newPath', 'NIFTI'], ['out_file', 'out_log', 'out_matrix_file'], ['path', 'path', 'path'])"), 'U2': ('Tools.PathManipulation', 'indexListPath', "(['listPath', 'index'], ['U1:list_3D_images', 0], ['outPath'], ['path'])"), 'U3': ('Tools.PathManipulation', 'add_suffixprefix_file', "(['file_path', 'new_str', 'place'], ['U2:outPath', '_RegLinInt', 'suffix'], ['newPath'], ['path'])"), 'U4': ('Tools.PathManipulation', 'change_extension', "(['file_path', 'new_extension'], ['U3:newPath', '.mat'], ['newPath'], ['path'])"), 'U0': ('Nipype.Interfaces_fsl_preprocess', 'fsl_FLIRT', "(['in_file', 'reference', 'cost_func', 'interp', 'out_file', 'out_matrix_file', 'output_type'], ['U2:outPath', 'C0:reference_nifti', 'mutualinfo', 'nearestneighbour', 'U3:newPath', 'U4:newPath', 'NIFTI'], ['out_file', 'out_log', 'out_matrix_file'], ['path', 'path', 'path'])"), 'U6': ('Tools.PathManipulation', 'indexListPath', "(['listPath', 'index'], ['U1:list_3D_images', 1], ['outPath'], ['path'])"), 'U12': ('Nipype.Interfaces_fsl_preprocess', 'fsl_FLIRT', "(['in_file', 'reference', 'apply_xfm', 'in_matrix_file', 'interp', 'out_file', 'out_matrix_file', 'output_type'], ['U13:outPath', 'U0:out_file', True, 'U0:out_matrix_file', 'nearestneighbour', 'U16:newPath', 'U17:newPath', 'NIFTI'], ['out_file', 'out_log', 'out_matrix_file'], ['path', 'path', 'path'])"), 'U18': ('Irmage.Registration', 'Non_linear_registration_multiple_Images', "(['image_fixed', 'image_moved', 'images_apply_transform', 'output_moved_name', 'suffix_transformed_name', 'interpolator', 'transform'], ['C0:reference_nifti', 'U12:out_file', 'U19:ListPath', 'U10:newPath', '_NoLinMD', 'nearestNeighbor', 'SyN'], ['out_image_registred', 'out_image_transformed'], ['path', 'list_path'])")}
['C0:reference_nifti', 'U12:out_file', 'U13:outPath', 'U0:out_file', 'U0:out_matrix_file', 'A10:', 'A11:', 'U16:newPath', 'U17:newPath', 'A3:', 'U16:newPath', 'A1:', 'U1:list_3D_images', 'U13:outPath', 'A0:', 'F0:in0', 'U1:list_3D_images', 'U14:directory', 'C1:Diffusion_nifti', 'C0:reference_nifti', 'A15:', 'A14:', 'U8:newPath', 'A13:', 'U7:newPath', 'U7:newPath', 'A12:', 'U6:outPath', 'A11:', 'U0:out_matrix_file', 'A10:', 'U0:out_file', 'U1:list_3D_images', 'A2:', 'U2:outPath', 'A4:', 'A5:', 'U2:outPath', 'U3:newPath', 'A6:', 'U3:newPath', 'U4:newPath', 'A7:', 'A8:', 'U1:list_3D_images', 'A9:', 'U6:outPath', 'C1:Diffusion_nifti', 'A14:', 'U12:out_file', 'U19:ListPath', 'U5:out_file', 'U10:newPath', 'A16:', 'A17:', 'A18:', 'U18:out_image_registred', 'U18:out_image_transformed']
{}
['M2:out_image_registred=U18:out_image_registred', 'M2:out_image_transformed=U18:out_image_transformed']
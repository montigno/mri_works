[diagram]
constant=[A3] value=[0] format=[int] label=[index] RectF=[(68.52906996396752, 453.0128605572943, 98.0, 31.0)]
constant=[A8] value=['SIGMA_Anatomical_Brain_Atlas_Labels.txt'] format=[str] label=[fileName] RectF=[(-71.24987233827608, 205.45890781109082, 314.0, 33.0)]
constant=[A4] value=['.json'] format=[str] label=[new_extension] RectF=[(-558.0460378181394, -291.66370173565434, 57.0, 33.0)]
constant=[A5] value=['StudyName'] format=[str] label=[tag] RectF=[(-283.6004011016642, -191.2582438039809, 104.0, 33.0)]
constant=[A6] value=['_analyse.txt'] format=[str] label=[stringIn_0] RectF=[(278.5025992742215, -415.790757730046, 107.0, 33.0)]
link=[N32] node=[A3:#Node#U12:index]
link=[N20] node=[M2:out_image_transformed#Node#U12:listPath]
link=[N31] node=[A8:#Node#U11:fileName]
link=[N30] node=[U10:directory#Node#U11:inPath]
link=[N29] node=[U9:projet_path#Node#U10:inPath]
link=[N3] node=[M0:output_file#Node#M1:image_fixed]
link=[N10] node=[A4:#Node#U3:new_extension]
link=[N11] node=[U3:newPath#Node#U2:jsonFile]
link=[N12] node=[A5:#Node#U2:tag]
link=[N13] node=[U2:ValueTag#Node#U4:in_string]
link=[N21] node=[U3:newPath#Node#U5:inPath]
link=[N22] node=[U4:substring#Node#U6:stringIn]
link=[N23] node=[A6:#Node#U6:stringIn_0]
link=[N24] node=[U5:directory#Node#U7:inPath]
link=[N25] node=[U6:str_conc#Node#U7:fileName]
link=[N9] node=[C0:T1_Flash_3D#Node#U3:file_path]
link=[N0] node=[C0:T1_Flash_3D#Node#M0:input_nifti]
link=[N4] node=[C0:T1_Flash_3D#Node#M2:reference_nifti]
link=[N1] node=[C1:Diffusion_nifti#Node#M2:Diffusion_nifti]
link=[N2] node=[C0:T1_Flash_3D#Node#M6:T1_Flash Nifti]
link=[N5] node=[M2:out_image_registred#Node#M6:Diff FA Nifti]
link=[N6] node=[U12:outPath#Node#M6:Diff MD Nifti]
link=[N14] node=[U11:outFile#Node#M6:Atlas_label_text]
link=[N34] node=[U7:outFile#Node#M6:output_result]
link=[N35] node=[M1:out_label_registred#Node#M6:Atlas_label_nifti]
block=[U12] category=[Tools.PathManipulation] class=[indexListPath] valInputs=[(['listPath', 'index'], ['Node(N20)', 'Node(N32)'], ['outPath'], ['path'])] RectF=[(272.3216951300698, 383.698906549115, 150.0, 80.0)]
submod=[M2] nameMod=[IG_Registration_diffusion] valInputs=[(['reference_nifti', 'Diffusion_nifti'], ['Node(N4)', 'Node(N1)'], ['out_image_registred', 'out_image_transformed'], ['path', 'list_path'])] RectF=[(-290.68399914868576, 320.40673011317807, 284.03125, 80.0)]
block=[U11] category=[Tools.PathManipulation] class=[joinPath] valInputs=[(['inPath', 'fileName'], ['Node(N30)', 'Node(N31)'], ['outFile'], ['path'])] RectF=[(361.59169021328466, 72.92096024863275, 150.0, 80.0)]
block=[U10] category=[Tools.PathManipulation] class=[separatePath] valInputs=[(['inPath'], ['Node(N29)'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])] RectF=[(21.150076597034342, 78.7252851111833, 150.0, 80.0)]
block=[U9] category=[Tools.Os] class=[projet_path] valInputs=[([], [], ['projet_path'], ['path'])] RectF=[(-247.92589788745792, 79.90028936657416, 150.0, 80.0)]
submod=[M0] nameMod=[IG_N4bias_segmentation] valInputs=[(['input_nifti'], ['Node(N0)'], ['output_file'], ['path'])] RectF=[(-336.86632539925824, -49.83848871735306, 174.140625, 80.0)]
submod=[M1] nameMod=[IG_Registration_Atlas] valInputs=[(['image_fixed'], ['Node(N3)'], ['out_template_registred', 'out_label_registred'], ['path', 'path'])] RectF=[(-56.12868182277953, -48.8083611377491, 262.40625, 80.0)]
block=[U2] category=[Irmage.Json_Irmage] class=[Json_File] valInputs=[(['jsonFile', 'tag'], ['Node(N11)', 'Node(N12)'], ['hasJson', 'jsonFile', 'ValueTag'], ['bool', 'path', 'str'])] RectF=[(-59.306039287236594, -348.1194034344567, 150.0, 80.0)]
block=[U3] category=[Tools.PathManipulation] class=[change_extension] valInputs=[(['file_path', 'new_extension'], ['Node(N9)', 'Node(N10)'], ['newPath'], ['path'])] RectF=[(-391.49773279221915, -328.68502044364806, 186.03125, 80.0)]
block=[U4] category=[Tools.StringManipulation] class=[string_substring] valInputs=[(['in_string', 'start', 'end'], ['Node(N13)', 2, -2], ['substring'], ['str'])] RectF=[(160.90424598460683, -305.0078719824859, 153.375, 80.0)]
block=[U5] category=[Tools.PathManipulation] class=[separatePath] valInputs=[(['inPath'], ['Node(N21)'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])] RectF=[(-47.06281718521691, -516.3027073275023, 150.0, 80.0)]
block=[U6] category=[Tools.StringManipulation] class=[string_concatenat_dyn] valInputs=[(['stringIn', 'stringIn_0'], ['Node(N22)', 'Node(N23)'], ['str_conc'], ['str'])] RectF=[(508.79148806512967, -452.9040139769363, 156.71875, 80.0)]
block=[U7] category=[Tools.PathManipulation] class=[joinPath] valInputs=[(['inPath', 'fileName'], ['Node(N24)', 'Node(N25)'], ['outFile'], ['path'])] RectF=[(788.8116396303526, -524.1447135319402, 150.0, 80.0)]
connt=[C0] name=[T1_Flash_3D] type=[in] format=[path] valOut=[path] RectF=[(-684.1535201625746, -107.1310193799307, 70, 24)]
connt=[C1] name=[Diffusion_nifti] type=[in] format=[path] valOut=[path] RectF=[(-694.7694642279189, 357.18997846096806, 70, 24)]
submod=[M6] nameMod=[IG_calculs_2] valInputs=[(['T1_Flash Nifti', 'Diff FA Nifti', 'Diff MD Nifti', 'Atlas_label_nifti', 'Atlas_label_text', 'output_result'], ['Node(N2)', 'Node(N5)', 'Node(N6)', 'Node(N35)', 'Node(N14)', 'Node(N34)'], [], [])] RectF=[(1131.838703223739, -124.25833426483393, 164.73143126581112, 255.85653278470244)]
comments=[] RectF=[(841.9207904990565, 445.97896518803077, 977.7971839372578, 10.0)] text=['This pipeline requires 3 files which must be placed in the same project directory :\n    - SIGMA_Anatomical_Brain_Atlas.nii\n    - SIGMA_ExVivo_Brain_Template_Masked.nii\n    - SIGMA_Anatomical_Brain_Atlas_Labels.txt\n ']
[execution]
['C0:T1_Flash_3D=', 'C1:Diffusion_nifti=']
['U9', 'ThreadOn', 'M2', 'U3', 'M0', 'U10', 'ThreadOff', 'ThreadOn', 'U11', 'U12', 'U5', 'U2', 'M1', 'ThreadOff', 'U4', 'U6', 'U7', 'M6']
{'U7': ('Tools.PathManipulation', 'joinPath', "(['inPath', 'fileName'], ['U5:directory', 'U6:str_conc'], ['outFile'], ['path'])"), 'U5': ('Tools.PathManipulation', 'separatePath', "(['inPath'], ['U3:newPath'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])"), 'U4': ('Tools.StringManipulation', 'string_substring', "(['in_string', 'start', 'end'], ['U2:ValueTag', 2, -2], ['substring'], ['str'])"), 'U9': ('Tools.Os', 'projet_path', "([], [], ['projet_path'], ['path'])"), 'U10': ('Tools.PathManipulation', 'separatePath', "(['inPath'], ['U9:projet_path'], ['directory', 'nameFile', 'extension'], ['path', 'str', 'str'])"), 'U6': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0'], ['U4:substring', '_analyse.txt'], ['str_conc'], ['str'])"), 'U2': ('Irmage.Json_Irmage', 'Json_File', "(['jsonFile', 'tag'], ['U3:newPath', 'StudyName'], ['hasJson', 'jsonFile', 'ValueTag'], ['bool', 'path', 'str'])"), 'U3': ('Tools.PathManipulation', 'change_extension', "(['file_path', 'new_extension'], ['C0:T1_Flash_3D', '.json'], ['newPath'], ['path'])"), 'U11': ('Tools.PathManipulation', 'joinPath', "(['inPath', 'fileName'], ['U10:directory', 'SIGMA_Anatomical_Brain_Atlas_Labels.txt'], ['outFile'], ['path'])"), 'U12': ('Tools.PathManipulation', 'indexListPath', "(['listPath', 'index'], ['M2:out_image_transformed', 0], ['outPath'], ['path'])")}
['M1:out_label_registred', 'U7:outFile', 'U11:outFile', 'U12:outPath', 'M2:out_image_registred', 'C0:T1_Flash_3D', 'C1:Diffusion_nifti', 'C0:T1_Flash_3D', 'C0:T1_Flash_3D', 'C0:T1_Flash_3D', 'U6:str_conc', 'U5:directory', 'A6:', 'U4:substring', 'U3:newPath', 'U2:ValueTag', 'A5:', 'U3:newPath', 'A4:', 'M0:output_file', 'U9:projet_path', 'U10:directory', 'A8:', 'M2:out_image_transformed', 'A3:']
{'M6': ('IG_calculs_2', "(['T1_Flash Nifti', 'Diff FA Nifti', 'Diff MD Nifti', 'Atlas_label_nifti', 'Atlas_label_text', 'output_result'], ['C0:T1_Flash_3D', 'M2:out_image_registred', 'U12:outPath', 'M1:out_label_registred', 'U11:outFile', 'U7:outFile'], [], [])"), 'M1': ('IG_Registration_Atlas', "(['image_fixed'], ['M0:output_file'], ['out_template_registred', 'out_label_registred'], ['path', 'path'])"), 'M0': ('IG_N4bias_segmentation', "(['input_nifti'], ['C0:T1_Flash_3D'], ['output_file'], ['path'])"), 'M2': ('IG_Registration_diffusion', "(['reference_nifti', 'Diffusion_nifti'], ['C0:T1_Flash_3D', 'C1:Diffusion_nifti'], ['out_image_registred', 'out_image_transformed'], ['path', 'list_path'])")}
[]
[submod M6]
['C1:T1_Flash Nifti=C0:T1_Flash_3D', 'C2:Diff FA Nifti=M2:out_image_registred', 'C3:Diff MD Nifti=U12:outPath', 'C4:Atlas_label_nifti=M1:out_label_registred', 'C0:Atlas_label_text=U11:outFile', 'C5:output_result=U7:outFile']
['U0', 'S0']
{'U0': ('Tools.PathManipulation', 'build_list_path_dyn', "(['in_path', 'in_path_0', 'in_path_1'], ['C1:T1_Flash Nifti', 'C2:Diff FA Nifti', 'C3:Diff MD Nifti'], ['path_list'], ['list_path'])")}
['C5:output_result', 'C0:Atlas_label_text', 'C4:Atlas_label_nifti', 'U0:path_list', 'C3:Diff MD Nifti', 'C2:Diff FA Nifti', 'C1:T1_Flash Nifti']
{}
[]
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

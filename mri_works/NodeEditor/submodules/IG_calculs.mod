[diagram]
link=[N4] node=[C4:outfile_result_name#Node#S0:output_result]
link=[N2] node=[C1:T1_Flash Nifti#Node#U0:in_path]
link=[N1] node=[C2:Diff FA Nifti#Node#U0:in_path_0]
link=[N0] node=[C3:Diff MD Nifti#Node#U0:in_path_1]
link=[N3] node=[C0:list_structures#Node#U2:files_list]
link=[N7] node=[U2:list_out#Node#S0:list_masks]
link=[N5] node=[U0:path_list#Node#S0:list_files]
connt=[C4] name=[outfile_result_name] type=[in] format=[path] valOut=[path] RectF=[(-206.3301628712638, 212.97620685775584, 70, 24)]
connt=[C3] name=[Diff MD Nifti] type=[in] format=[path] valOut=[path] RectF=[(-453.94120312879824, 72.32990797016276, 70, 24)]
connt=[C2] name=[Diff FA Nifti] type=[in] format=[path] valOut=[path] RectF=[(-455.82166796026706, -7.369810096133431, 70, 24)]
connt=[C1] name=[T1_Flash Nifti] type=[in] format=[path] valOut=[path] RectF=[(-451.34029307621864, -92.30110518459833, 70, 24)]
connt=[C0] name=[list_structures] type=[in] format=[list_path] valOut=[['path']] RectF=[(-307.1121313741944, -209.83041528740227, 70, 24)]
block=[U2] category=[Tools.PathManipulation] class=[order_name_files] valInputs=[(['files_list', 'reverse'], ['Node(N3)', False], ['list_out'], ['list_path'])] RectF=[(-21.69589698480131, -186.55469191160077, 150.0, 80.0)]
script=[S0] title=[Script_editor] inputs=[['list_masks', 'in', 'list_path'], ['list_files', 'in', 'list_path'], ['output_result', 'in', 'path']] outputs=[] code=[your code] RectF=[(230.67553884337556, -260.5514686018141, 537.7032895347078, 541.5114194704972)]
block=[U0] category=[Tools.PathManipulation] class=[build_list_path_dyn] valInputs=[(['in_path', 'in_path_0', 'in_path_1'], ['Node(N2)', 'Node(N1)', 'Node(N0)'], ['path_list'], ['list_path'])] RectF=[(-275.0386837364293, -61.729310250010684, 159.890625, 133.0)]
[source S0]
['list_files=U0:path_list', 'list_masks=U2:list_out', 'output_result=C4:outfile_result_name']
import numpy as np
import nibabel as nib
import os
import pathlib

fileSet = {}
for seq in list_files:
    base_seq = os.path.basename(seq)
    base_seq=('.').join(base_seq.split('.')[:-1])
    fileSet[base_seq] = nib.load(seq).get_fdata()  

with open(output_result, 'w') as results:
    results.write('Labels|Sequences|Vol(mm3)|Mean|Stdv\n')
    for mask in list_masks:
        base_mask = os.path.basename(mask)
        base_mask=('.').join(base_mask.split('.')[:-1])
        tmpmask = nib.load(mask).get_fdata()
        hdr =  nib.load(mask).header
        list_dim = (hdr['pixdim']).tolist()
        voxel_dim = list_dim[1] * list_dim[2] * list_dim[3]
        sum_mask = np.sum(tmpmask)
        results.write(base_mask + '||' + str(round(sum_mask*voxel_dim, 2)) + '||\n')
        for seq_k, seq_v in fileSet.items():
            mul = np.multiply(seq_v, tmpmask)
            mul[mul == 0.0] = 'nan'
            mean = np.nanmean(mul)
            stdv = np.nanstd(mul)
            results.write( '|' + seq_k + '|''|' + str(mean) + '|' + str(stdv) + '\n')
results.close()
[]
[/source S0]

[execution]
['C0:list_structures=', 'C1:T1_Flash Nifti=', 'C2:Diff FA Nifti=', 'C3:Diff MD Nifti=', 'C4:outfile_result_name=']
['ThreadOn', 'U2', 'U0', 'ThreadOff', 'S0']
{'U0': ('Tools.PathManipulation', 'build_list_path_dyn', "(['in_path', 'in_path_0', 'in_path_1'], ['C1:T1_Flash Nifti', 'C2:Diff FA Nifti', 'C3:Diff MD Nifti'], ['path_list'], ['list_path'])"), 'U2': ('Tools.PathManipulation', 'order_name_files', "(['files_list', 'reverse'], ['C0:list_structures', False], ['list_out'], ['list_path'])")}
['U0:path_list', 'U2:list_out', 'C0:list_structures', 'C3:Diff MD Nifti', 'C2:Diff FA Nifti', 'C1:T1_Flash Nifti', 'C4:outfile_result_name']
{}
[]

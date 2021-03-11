[diagram]
link=[N6] node=[C5:output_result#Node#S0:output_result]
link=[N4] node=[C0:Atlas_label_text#Node#S0:Atlas_label_text]
link=[N3] node=[C4:Atlas_label_nifti#Node#S0:Atlas_label_nifti]
link=[N5] node=[U0:path_list#Node#S0:list_files]
link=[N0] node=[C3:Diff MD Nifti#Node#U0:in_path_1]
link=[N1] node=[C2:Diff FA Nifti#Node#U0:in_path_0]
link=[N2] node=[C1:T1_Flash Nifti#Node#U0:in_path]
connt=[C5] name=[output_result] type=[in] format=[path] valOut=[path] RectF=[(-185.0092220251627, 315.0129956079193, 70, 24)]
connt=[C0] name=[Atlas_label_text] type=[in] format=[path] valOut=[path] RectF=[(-180.61637864217354, 168.62919629112787, 70, 24)]
block=[U0] category=[Tools.PathManipulation] class=[build_list_path_dyn] valInputs=[(['in_path', 'in_path_0', 'in_path_1'], ['Node(N2)', 'Node(N1)', 'Node(N0)'], ['path_list'], ['list_path'])] RectF=[(-128.28218392325718, -180.89753458942587, 159.890625, 133.0)]
script=[S0] title=[Script_editor] inputs=[['list_files', 'in', 'list_path'], ['Atlas_label_nifti', 'in', 'path'], ['Atlas_label_text', 'in', 'path'], ['output_result', 'in', 'path']] outputs=[] code=[your code] RectF=[(203.3470922013654, -366.44919933960364, 666.5346560075606, 919.5032976127125)]
connt=[C1] name=[T1_Flash Nifti] type=[in] format=[path] valOut=[path] RectF=[(-392.8220604573624, -227.70874119134032, 70, 24)]
connt=[C2] name=[Diff FA Nifti] type=[in] format=[path] valOut=[path] RectF=[(-402.24503472555415, -146.38763312353308, 70, 24)]
connt=[C3] name=[Diff MD Nifti] type=[in] format=[path] valOut=[path] RectF=[(-406.27272437835984, -64.10829148167673, 70, 24)]
connt=[C4] name=[Atlas_label_nifti] type=[in] format=[path] valOut=[path] RectF=[(-190.0182653661515, 22.03509840556343, 70, 24)]
[source S0]
['list_files=U0:path_list', 'Atlas_label_nifti=C4:Atlas_label_nifti', 'Atlas_label_text=C0:Atlas_label_text', 'output_result=C5:output_result']
import numpy as np
import nibabel as nib
import os
import pathlib
import csv
import collections
from skimage.morphology import erosion


fileSet = {}
for seq in list_files:
    base_seq = os.path.basename(seq)
    base_seq=('.').join(base_seq.split('.')[:-1])
    fileSet[base_seq] = nib.load(seq).get_fdata()

base_mas = os.path.basename(Atlas_label_nifti)
base_mas=('.').join(base_mas.split('.')[:-1])
masks_struct = nib.load(Atlas_label_nifti).get_fdata()

hdr =  nib.load(Atlas_label_nifti).header
list_dim = (hdr['pixdim']).tolist()
voxel_dim = list_dim[1] * list_dim[2] * list_dim[3]

list_struct = []
with open(Atlas_label_text) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                list_struct.append(row)
list_struct = list_struct[15:249]
# list_struct = list_struct[15:20]
list_idx = {}
for lst_str in list_struct:
    elemts = lst_str[0].split('\t')
    list_idx[int(elemts[0])]= elemts[7][1:-1]

od = collections.OrderedDict(sorted(list_idx.items()))

with open(output_result, 'w') as results:
    results.write('Labels|Sequences|Vol(mm3)|Mean|Stdv\n')
    for k, v in od.items():
        tmp_masks = masks_struct.copy()
        tmp_masks[tmp_masks<k] = 0.0
        tmp_masks[tmp_masks>k] = 0.0
        tmp_masks[tmp_masks==k] = 1.0
        sum_mask = np.sum(tmp_masks)
        results.write(v + '||' + str(round(sum_mask*voxel_dim, 2)) + '||\n')
        for seq_k, seq_v in fileSet.items():
            mul = np.multiply(seq_v, tmp_masks)
            mul[mul == 0.0] = 'nan'
            mean = np.nanmean(mul)
            stdv = np.nanstd(mul)
            results.write( '|' + seq_k + '|''|' + str(mean) + '|' + str(stdv) + '\n')

        tmp_masks = erosion(np.array(tmp_masks))
        sum_mask = np.sum(tmp_masks)
        results.write(v+ '_eroded' + '||' + str(round(sum_mask*voxel_dim, 2)) + '||\n')
        for seq_k, seq_v in fileSet.items():
            mul = np.multiply(seq_v, tmp_masks)
            mul[mul == 0.0] = 'nan'
            mean = np.nanmean(mul)
            stdv = np.nanstd(mul)
            results.write( '|' + seq_k + '|''|' + str(mean) + '|' + str(stdv) + '\n')
results.close()


[]
[/source S0]

[execution]
['C1:T1_Flash Nifti=', 'C2:Diff FA Nifti=', 'C3:Diff MD Nifti=', 'C4:Atlas_label_nifti=', 'C0:Atlas_label_text=', 'C5:output_result=']
['U0', 'S0']
{'U0': ('Tools.PathManipulation', 'build_list_path_dyn', "(['in_path', 'in_path_0', 'in_path_1'], ['C1:T1_Flash Nifti', 'C2:Diff FA Nifti', 'C3:Diff MD Nifti'], ['path_list'], ['list_path'])")}
['C1:T1_Flash Nifti', 'C2:Diff FA Nifti', 'C3:Diff MD Nifti', 'U0:path_list', 'C4:Atlas_label_nifti', 'C0:Atlas_label_text', 'C5:output_result']
{}
[]

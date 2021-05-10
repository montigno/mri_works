file_txt = '/home/domicile-xubuntu/Documents/DataIRM/Atlas_Rat/SIGMA_W_Rat_Atlas_V1.1/SIGMA_Rat_Brain_Atlases/SIGMA_Anatomical_Atlas/SIGMA_Anatomical_Brain_Atlas_Labels.txt'

file_output = '/tmp/SIGMA_Anatomical_Brain_Atlas_Labels.txt'

with open(file_txt) as ts:
  data = ts.readlines()

f = open(file_output, "w+")

for i, v in enumerate(data):
    v = v.split('\t')
    if v[0][0] != '#':
        f.write(str(v[0]) + "\t" + v[7])

f.close()

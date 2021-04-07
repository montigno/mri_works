file_txt = '/tmp/label.txt'

file_output = '/tmp/SIGMA_Anatomical_Brain_Atlas_Labels.txt'

with open(file_txt) as ts:
  data = ts.readlines()

f = open(file_output, "w+")

for i, v in enumerate(data):
    v = v.split('\t')
    f.write(str(v[0]) + "\t" + v[7])

f.close()

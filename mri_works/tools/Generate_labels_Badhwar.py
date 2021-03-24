import json

file_json = '/home/omontigon/Documents/DataIRM/Atlas_mouse/Badhwar/rgb2acr.json'
# file_json = '/home/omontigon/Documents/DataIRM/Atlas_mouse/Badhwar/acr2full.json'

file_output = '/home/omontigon/Documents/mri_works_projects/Toff/bha_labels_sba.txt'

with open(file_json) as f:
  data = json.load(f)

# labels_dict ={}

f = open(file_output, "w+")

for i, (k, v) in enumerate(data.items()):
    if not v == '['+str(i)+']':
        f.write(str(i) + "\t0\t0\t0\t0\t0\t0\t" + v + "\r\n")
#         print(i,v)
#         labels_dict[i] = v

f.close()   


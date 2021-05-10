import json

file_json = '/tmp/waxhom_acr2full.json'

file_output = '/tmp/waxhom.txt'

with open(file_json) as f:
  data = json.load(f)

# labels_dict ={}

f = open(file_output, "w+")

for i, (k, v) in enumerate(data.items()):
    if not v == '['+str(i)+']':
        f.write(str(i) + "\t" + v + "\r\n")
#         print(i,v)
#         labels_dict[i] = v

f.close()   


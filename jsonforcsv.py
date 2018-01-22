import json

f = open('./images_testing/images_testing.json','r')
json_dict = json.load(f)

f2 = open('./images_testing/images_testing.csv','a')

#print(json_dict)
kigou = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
st = ""

for r in json_dict:
  count = r["num_of_points"]
  for i in range(count):
    x = r[kigou[i]]["x"]
    y = r[kigou[i]]["y"]
    if i == 0:
      st = r["filename"] + ',' + str(x) + ',' + str(y) + '\n'
      f2.write(st)
    else:
      st = ',' + str(x) + ',' + str(y) + '\n'
      f2.write(st)
  
f.close()
f2.close()

import os
import glob
import json

import test

#書き換え：inputdirectry,outputdirectry,jsonのopen
#
#

inputdirectry = './images/images_testing/*.jpg'
outputdirectry = './images/images_testing/output'

counter_1 = 0
for target in glob.glob(inputdirectry):
  counter_1 += 1
print('%d個やります（意味深）' %counter_1)

with open('./images/images_testing/output/output1.json','a') as f:
  counter_2 = 0
  f.write('[\n')
  for file in glob.glob(inputdirectry):
    name = os.path.basename(file)
    outputpass = os.path.join(outputdirectry,name)
    

    if os.path.exists(outputdirectry) == False:
      print("出力フォルダがないよ．")
      break
    else:
      dict_add = test.car_detection(file,outputpass)
      
      json.dump(dict_add, f, indent=4, separators=(',',':'))
      if counter_2 != counter_1 - 1:
        f.write(',\n')

      counter_2 += 1

      print(outputpass)
    
  f.write(']')

print('オワオワリで～す')


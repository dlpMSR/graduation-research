import os
import sys
import glob
import json

import test
import label
import jsonforcsv
import csvforarff

def main(arg1):
  inputpath = os.path.join(arg1,'*.jpg')
  outputpath = os.path.join(arg1,'output')

  if os.path.exists(outputpath) == False:
    print('出力フォルダがありません．新たに作成しますか？[y/n]')
    input_word = input('>> ')
    if input_word == 'Y' or input_word == 'y':
      os.mkdir(outputpath)
      print('出力フォルダを作成しました．%s' % outputpath)
      #matomete(inputpath,outputpath)
    elif input_word == 'N' or input_word == 'n':
      print('うんこｗ')
      pass
    else:
      print('うんこｗ')
      pass

  else:
    pass

  matomete(inputpath,outputpath)
  label.main(arg1)
  jsonforcsv.main(arg1)
  csvforarff.main(arg1)
  


def matomete(input_path,output_path):
  num_of_target = 0
  for target in glob.glob(input_path):
    num_of_target += 1
  print('%d個の画像があります．' % num_of_target)

  jsonpath = os.path.join(output_path,'output1.json')
  count = 0
  
  with open(jsonpath,'a') as f:
    f.write('[\n')
    for file in glob.glob(input_path):
      filename = os.path.basename(file)
      path = os.path.join(output_path,filename)
    
      dict_add = test.car_detection(file,path)
      json.dump(dict_add, f, indent=4, separators=(',',':'))

      if count != num_of_target - 1:
        f.write(',\n')
        count += 1
        print(path)
      else:
        pass

    f.write(']')
    print('オワオワリで～す')



if __name__ == '__main__':
  main(sys.argv[1])
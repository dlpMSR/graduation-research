import os
import glob

import test

inputdirectry = './images/images_testing/*.jpg'
outputdirectry = './images/images_testing/output'

for file in glob.glob(inputdirectry):
  name = os.path.basename(file)
  outputpass = os.path.join(outputdirectry,name)

  if os.path.exists(outputdirectry)==False:
    print("出力フォルダが見当たりません．")
    break
  else:
    test.car_detection(file,outputpass)
    #test.resize(file,outputpass)
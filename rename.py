import os
import sys
import glob

def rename(target_pass):
    number = 1
    outputdirectry = os.path.dirname(target_pass)

    for f in glob.glob(target_pass):
        newname = os.path.join(outputdirectry,'%s.jpg' % number)
        os.rename(f,newname)
        number += 1
    
    print('オワオワリで～す')


if __name__ == '__main__':
    target = './images/images_testing/*.jpg'
    rename(target)
  

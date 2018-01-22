# -*- coding: utf-8 -*-

import os
import glob
import numpy as np
import cv2


#for file in glob.glob('20171020/*'):
    #r = file
    #print r
    #for line in open(file, 'r'):
        #print line,


#print glob.glob('20171020/*')
#for file in glob.glob('20171020/*'):
    #f = cv2.imread(file,cv2.IMREAD_GRAYSCALE) 
    #cv2.imshow('image',f)
    #cv2.waitKey
    #cv2.destroyAllWindows()

#l = glob.glob('20171020/*')
#ll = l[0]
#print ll

#f = cv2.imread(ll,cv2.IMREAD_GRAYSCALE)
#cv2.imshow('image',f)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#cv2.imwrite(os.path.join('./output/','1.jpg'),f)

#f = cv2.imread(file,cv2.IMREAD_GRAYSCALE) 

i = 0

for file in glob.glob('20171020/*'):
    
    i = i + 1

    gray = cv2.imread(file,cv2.IMREAD_GRAYSCALE)
    #cv2.imshow('image',f)
    filename = str(file)
    print filename
    cv2.imwrite(os.path.join('./output/','%s.jpg'% i),gray)


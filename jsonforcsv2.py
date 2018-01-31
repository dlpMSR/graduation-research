import json
from statistics import mean, median,variance,stdev
import numpy as np

kigou = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('./images/images_testing2/output/output1.json','r') as input:
  with open('./images/images_testing2/output/output1.csv','a') as output:
    json_dict = json.load(input)

    output.write('filename,number,A,B,mean_x,mean_y,median_x,median_y,variance_x,variance_y,stdev_x,stdev_y\n')

    for item in json_dict:
      count = item["num_of_points"]
      width = item["width"]
      height = item["height"]
      list_x = np.array([])
      list_y = np.array([])
      for i in range(count):
        list_x = np.append(list_x,item[kigou[i]]["x"])
        list_y = np.append(list_y, height - item[kigou[i]]["y"])

      if len(list_x)==0:
        num_of_points = 0
        a = 0
        b = 0
        mean_x = 0
        mean_y = 0
        median_x = 0
        median_y = 0
        variance_x = 0
        variance_y = 0
        stdev_x = 0
        stdev_y = 0

      elif len(list_x)==1:
        num_of_points = 1
        a = 0
        b = 0
        variance_x = 0
        variance_y = 0
        stdev_x = 0
        stdev_y = 0
        mean_x = np.mean(list_x)
        mean_y = np.mean(list_y)
        median_x = np.median(list_x)
        median_y = np.median(list_y)
        
      else:
        num_of_points = len(list_x)

        a, b = np.polyfit(list_x,list_y,1) 

        mean_x = np.mean(list_x)
        mean_y = np.mean(list_y)
        median_x = np.median(list_x)
        median_y = np.median(list_y)
        variance_x = np.var(list_x)
        variance_y = np.var(list_y)
        stdev_x = np.std(list_x)
        stdev_y = np.std(list_y)

      output_string = item['filename'] +','+ \
                      str(num_of_points) +','+ \
                      str(a) +','+ \
                      str(b) +','+ \
                      '{0:.2f}'.format(mean_x) +','+ \
                      '{0:.2f}'.format(mean_y) +','+ \
                      '{0:.2f}'.format(median_x) +','+ \
                      '{0:.2f}'.format(median_y) +','+ \
                      '{0:.2f}'.format(variance_x) +','+ \
                      '{0:.2f}'.format(variance_y) +','+ \
                      '{0:.2f}'.format(stdev_x) +','+ \
                      '{0:.2f}'.format(stdev_y) +','+ \
                      '\n'
      output.write(output_string)
print('オワオワリで～す')


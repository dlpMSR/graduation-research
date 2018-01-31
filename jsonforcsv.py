import os
import json
import numpy as np
import math

kigou = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main(target_directry):
  path_json2 = os.path.join(target_directry,'output/output2.json')
  path_csv = os.path.join(target_directry,'output/output.csv')

  with open(path_json2,'r') as input:
    with open(path_csv,'a') as output:
      json_dict = json.load(input)

      output.write('filename,number,A,B,mean_x,mean_y,median_x,median_y,variance_x,\variance_y,stdev_x,stdev_y,range_x,center_x,range_y,center_y,ave_distance,label\n')

      for item in json_dict:
        count = item["num_of_points"]
        width = item["width"]
        height = item["height"]
        label = item["label"]
        list_x = np.array([])
        list_y = np.array([])
        for i in range(count):
          list_x = np.append(list_x,item[kigou[i]]["x"])
          list_y = np.append(list_y, height - item[kigou[i]]["y"])

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

          min_x = min(list_x)
          max_x = max(list_x)
          range_x = abs(max_x - min_x)
          center_x = int(min_x + (range_x/2))

          min_y = min(list_y)
          max_y = max(list_y)
          range_y = abs(max_y - min_y)
          center_y = int(min_y + (range_y/2))

          list_distance = []
          for j in range(len(list_x)):
            d = distance(a, b, list_x[j], list_y[j])
            list_distance = np.append(list_distance, d)
          ave_distance = int(np.mean(list_distance))


          output_string = item['filename'] +','+ \
                          str(num_of_points) +','+ \
                          '{0:.2f}'.format(a) +','+ \
                          '{0:.2f}'.format(b) +','+ \
                          '{0:.2f}'.format(mean_x) +','+ \
                          '{0:.2f}'.format(mean_y) +','+ \
                          '{0:.2f}'.format(median_x) +','+ \
                          '{0:.2f}'.format(median_y) +','+ \
                          '{0:.2f}'.format(variance_x) +','+ \
                          '{0:.2f}'.format(variance_y) +','+ \
                          '{0:.2f}'.format(stdev_x) +','+ \
                          '{0:.2f}'.format(stdev_y) +','+ \
                          str(range_x)+','+ \
                          str(center_x) +','+ \
                          str(range_y) +','+ \
                          str(center_y) +','+ \
                          str(ave_distance) +','+ \
                          str(label) + '\n'

        output.write(output_string)

      print('オワオワリで～す')


def distance(a,b,x1,y1):
  d = abs(a*x1-y1+b)/math.sqrt(a**2 + 1)
  return d


if __name__ == '__main__':
    main()

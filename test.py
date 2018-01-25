from darkflow.net.build import TFNet
import cv2

import os
import math
import json
import sys

options = {"model":"./cfg/yolo.cfg","load": "./yolo.weights", "threshold": 0.38,"gpu":1.0}
tfnet = TFNet(options)
kigou = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
threshold_distance = 150
threshold_size = 150

def car_detection(input_image,output_image):
  imgcv = cv2.imread('%s' % input_image)
  filename = os.path.basename(input_image)
  output_dict = {
                  "filename":filename,
                  "label":0,
                  "width":imgcv.shape[1],
                  "height":imgcv.shape[0],
                  "num_of_points":0
                }
                
  result = tfnet.return_predict(imgcv)

  num_of_points = 0
  list_center = []

  for item in result:
    tlx = item['topleft']['x']
    tly = item['topleft']['y']
    brx = item['bottomright']['x']
    bry = item['bottomright']['y']
    label = item['label']
    conf = item['confidence']

    center_x = int(tlx + (brx - tlx)/2)
    center_y = int(tly + (bry - tly)/2)

    dict_center = {'x':center_x,'y':center_y}
    size = distance(tlx,tly,brx,bry)

    if label == 'car' or label == 'bus' or label == 'truck':
      if num_of_points == 0:
        min_of_distance = threshold_distance + 1
      else:
        list_distance = []
        for point in list_center:
          x2 = point['x']
          y2 = point['y']
          distance_of_points = distance(center_x, center_y, x2, y2)
          list_distance.append(distance_of_points)
        min_of_distance = min(list_distance)

      if min_of_distance > threshold_distance and size > threshold_size:
    
        num_of_points += 1
        list_center.append(dict_center)
        
        output_dict["num_of_points"] = num_of_points
        output_dict["%s" % kigou[num_of_points - 1]] = {"x":center_x,"y":center_y}

        cv2.rectangle(imgcv, (tlx, tly), (brx, bry), (0,0,255), 5)
        text = label + " " + ('%.2f' % conf)
        cv2.rectangle(imgcv, (tlx, tly - 15), (tlx + 100, tly + 5), (0,0,255), -1)
        cv2.putText(imgcv, text, (tlx, tly), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)
        cv2.circle(imgcv, (center_x, center_y), 15, (255, 255, 0), -1)
      else:
        pass
    else:
      pass
  
  cv2.imwrite('%s' % output_image, imgcv)
  return output_dict


def resize(input_image,output_image):
  imgcv = cv2.imread('%s' % input_image)
  image_resized = cv2.resize(imgcv, (1080, 1440))
  cv2.imwrite('%s' % output_image, image_resized)
  print('%s' % output_image)


def distance(x1,y1,x2,y2):
    xd = x2 - x1
    yd = y2 - y1 
    distance = math.sqrt(pow(xd,2)+pow(yd,2))
    return distance






if __name__ == '__main__':
  arg = sys.argv
  car_detection(arg[1],arg[2])
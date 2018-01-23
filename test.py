from darkflow.net.build import TFNet
import cv2
import os
import json
import sys

options = {"model":"./cfg/yolo.cfg","load": "./yolo.weights", "threshold": 0.25,"gpu":1}
tfnet = TFNet(options)

def car_detection(input_image,output_image):

  filename = os.path.basename(input_image)
  output_dict = {"filename":filename,
                 "label":0,
                 "width":0,
                 "height":0,
                 "num_of_points":0}

  imgcv = cv2.imread('%s' % input_image)

  output_dict["height"] = imgcv.shape[0]
  output_dict["width"] = imgcv.shape[1]


  result = tfnet.return_predict(imgcv)

  #result = tfnet.return_predict(frame)
  
  num_of_points = 0
  kigou = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  for item in result:
    tlx = item['topleft']['x']
    tly = item['topleft']['y']
    brx = item['bottomright']['x']
    bry = item['bottomright']['y']
    label = item['label']
    conf = item['confidence']
    
    center_x = int(tlx + (brx - tlx)/2)
    center_y = int(tly + (bry - tly)/2)

    if label == 'car' or label == 'bus' or label == 'truck':
      num_of_points += 1
      
      newdict = {"%s" % kigou[num_of_points-1]:{"x":center_x,"y":center_y}}
      output_dict["num_of_points"] = num_of_points
      output_dict.update(newdict)

      cv2.rectangle(imgcv, (tlx, tly), (brx, bry), (0,0,255), 5)
      text = label + " " + ('%.2f' % conf)
      cv2.rectangle(imgcv, (tlx, tly - 15), (tlx + 100, tly + 5), (0,0,255), -1)
      cv2.putText(imgcv, text, (tlx, tly), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)
      cv2.circle(imgcv, (center_x, center_y), 15, (255, 255, 0), -1)
    else:
      pass
    
  cv2.imwrite('%s' % output_image, imgcv)

  f = open('./images_testing/images_testing.json','a')
  f.write(',\n')
  json.dump(output_dict, f, indent=2, separators=(',',':'))
  f.close()

  print('%s' % output_image)
  #print(output_dict)


def resize(input_image,output_image):
  imgcv = cv2.imread('%s' % input_image)
  #hight = imgcv.shape[0]
  #width = imgcv.shape[1]

  image_resized = cv2.resize(imgcv, (1080, 1440))
  cv2.imwrite('%s' % output_image, image_resized)


  print('%s' % output_image)


if __name__ == '__main__':
  arg = sys.argv
  car_detection(arg[1],arg[2])
  
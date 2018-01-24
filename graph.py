import os
import json 
import numpy as np 
import matplotlib.pyplot as plt

kigou = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def graph():
    with open('./images/images_testing/output1.json','r') as input:
        json_dict = json.load(input)

        for item in json_dict:
            filename = item["filename"]
            count = item["num_of_points"]
            width = item["width"]
            height = item["height"]

            list_x = []
            list_y = []
            
            for i in range(count):
                name, ext = os.path.splitext(filename)
                outputpass = os.path.join('./images/images_testing/graph','%s.png' % name)

                list_x.append(item[kigou[i]]["x"])
                list_y.append(height - item[kigou[i]]["y"])

            plt.figure(figsize=(6,8))
            plt.title(filename)
            plt.xlim([0,width])
            plt.ylim([0,height])
            plt.scatter(list_x,list_y)
            plt.savefig(outputpass)


if __name__ == '__main__':
    graph()

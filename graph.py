import os
import json 
import numpy as np 
import matplotlib.pyplot as plt

kigou = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def graph():
    with open('./images/images_testing2/output/output1.json','r') as input:
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
                outputpass = os.path.join('./images/images_testing2/graph','%s.png' % name)

                list_x = np.append(list_x, item[kigou[i]]["x"])
                list_y = np.append(list_y, height - item[kigou[i]]["y"])

            if len(list_x) == 0:
                a = 0
                b = 0

                plt.figure(figsize=(6,8))
                plt.title(filename)
                plt.xlim([0,width])
                plt.ylim([0,height])
                plt.savefig(outputpass)

            else:
                a, b = np.polyfit(list_x,list_y,1)
                y = a * list_x + b
                list_y2 = []
                list_d2 = []
                for x in list_x:
                    list_y2 = np.append(list_y2, a*x+b)
                for i in range(len(list_x)):
                    list_d2 = np.append(list_d2, np.square((list_y2[i]-list_y[i])))

                d2_average = np.average(list_d2)
                d2_average_sqrt = int(np.sqrt(d2_average))

                #mean_x = np.mean(list_x)
                min_x = min(list_x)
                max_x = max(list_x)
                center = int(min_x + (max_x - min_x)/2)
                median_x = np.median(list_x)



                plt.figure(figsize=(6,8))
                plt.title(filename)
                plt.xlim([0,width])
                plt.ylim([0,height])
                plt.scatter(list_x,list_y)
                plt.plot(list_x, y, color='black')
                plt.text(0.1,a*0.1+b, 'y='+ str(round(a,4)) +'x+'+str(round(b,4)) + '(' + str(d2_average_sqrt) + ')')
                plt.vlines(x=center, ymin=0, ymax=height, colors='r', linewidths=1)
                plt.vlines(x=median_x, ymin=0, ymax=height, colors='g', linewidths=1)
                plt.savefig(outputpass)

                print(filename)
print('オワオワリで～す')


if __name__ == '__main__':
    graph()

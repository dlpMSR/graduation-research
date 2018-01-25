import json
import math

moji = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def correction():
    with open('./images_testing/images_testing.json','r') as hoge:
        with open('./images_testing/fuga.json','w') as fuga:#???
            f = json.load(hoge)
            for item in f:
                count = item['num_of_points']
                for i in range(count):
                    x1 = item[moji[i]]['x']
                    y1 = item[moji[i]]['y']
                    for j in range(i+1,count):
                        x2 = item[moji[j]]['x']
                        y2 = item[moji[j]]['y']
                        distance(x1,y1,x2,y2)
                        
                            
            
def distance(x1,y1,x2,y2):
    xd = x2 - x1
    yd = y2 - y1 
    distance = math.sqrt(pow(xd,2)+pow(yd,2))
    return distance


if __name__ == '__main__':
    x1 = 548
    y1 = 1464
    x2 = 961
    y2 = 1490
    dist = distance(x1,y1,x2,y2)
    print(dist)


    
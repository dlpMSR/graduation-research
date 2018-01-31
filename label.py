import os
import csv
import json

def main(target_directry):
    path_label = './label.csv'
    path_json1 = os.path.join(target_directry,'output/output1.json')
    path_json2 = os.path.join(target_directry,'output/output2.json')


    with open(path_label, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        with open(path_json1,'r') as jsonfile:
            jsonfile_dict = json.load(jsonfile)
            
            num_of_target = 0
            count = 0
            for target in jsonfile_dict:
                num_of_target += 1 

            with open(path_json2,'a') as output2:
                output2.write('[\n')
                
                for row in reader:
                    image_name = row[0]
                    label = row[1]
                    
                    for item in jsonfile_dict:
                        if item['filename'] == image_name:
                            item['label'] = label
                            json.dump(item, output2, indent=4, separators=(',',':'))
                            count += 1

                            if count != num_of_target:
                                output2.write(',\n')
                            else:
                                pass

                            print('%s' % item['filename'])
                            
                        else:
                            pass
                            
                output2.write('\n]')
                    
        

if __name__ == '__main__':
    main()
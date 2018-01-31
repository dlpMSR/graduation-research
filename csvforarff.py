import os 
import csv

def main(target_directry):
    path_arff = os.path.join(target_directry,'output/output.arff')
    path_csv  = os.path.join(target_directry,'output/output.csv')

    with open(path_arff,'a') as arff:
        arff.write('@relation output1\n')
        arff.write('@attribute number numeric\n')
        arff.write('@attribute A numeric\n')
        arff.write('@attribute B    numeric\n')
        arff.write('@attribute mean_x   numeric\n')
        arff.write('@attribute mean_y   numeric\n')
        arff.write('@attribute median_x numeric\n')
        arff.write('@attribute median_y numeric\n')
        arff.write('@attribute variance_x   numeric\n')
        arff.write('@attribute variance_y   numeric\n')
        arff.write('@attribute stdev_x  numeric\n')
        arff.write('@attribute stdev_y  numeric\n')
        arff.write('@attribute range_x  numeric\n')
        arff.write('@attribute center_x numeric\n')
        arff.write('@attribute range_y  numeric\n')
        arff.write('@attribute center_y numeric\n')
        arff.write('@attribute ave_distance numeric\n')
        arff.write('@attribute label {0,1}\n')
        arff.write('\n')
        arff.write('@data\n')

        with open(path_csv,'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                row.pop(0)
                row_str = ','.join(row)
                
                arff.write(row_str + '\n')

                



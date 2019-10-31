import csv

with open('winequality-red.csv','r') as f:
    wines = list(csv.reader(f,delimiter=';'))

import numpy as np
header = np.array(wines[0],dtype=np.str)
wines = np.array(wines[1:], dtype=np.float)
acid = wines[:,2]
avg_acid = acid.mean()
ph = wines[:,-4]
avg_ph = ph.mean()
quality = wines[:,-1]
avg_quality = quality.mean()

print("Average Acid is {} ".format(avg_acid))
print("Average PH is {}".format(avg_ph))
print("Average quality is {}".format(avg_quality))

count = 0

for i,j,z in zip(range(len(acid)),range(len(ph)),range(len(quality))):
    if (acid[i] > avg_acid or ph[j] > avg_ph) and quality[z] > avg_quality :
        count += 1
print("The count = {}".format(count))
print("The data has total {} rows".format(len(wines[:,0])))
proportion = count/len(wines[:,0])
print("The proportion is {}. \nThere is no strong correlation between acid level and quality of the wine".format(proportion))



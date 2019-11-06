import numpy as np
import scipy as sp
import scipy.stats
import os
import shutil
import random as rdm
import pandas as pd

oneNine = (1,9)
tmp = np.empty((1,4),('U',18))
data = np.empty((0,4),('U',18))
countDoubles = 0

def getRand():
    a = rdm.choice(oneNine)
    b = rdm.choice(oneNine)
    c = rdm.choice(oneNine)
    d = rdm.choice(oneNine)
    letters = [a,b,c,d]
    return letters

#No change
for i in range(8):
    ind = getRand()
    fileOne = "flower1_" + str(ind[0]) + str(ind[1]) + str(ind[2]) + str(ind[3]) + "_1.png"
    while fileOne in data[:,0]: 
            ind = getRand()
            fileOne = "flower1_" + str(ind[0]) + str(ind[1]) + str(ind[2]) + str(ind[3]) + "_1.png"
            countDoubles+=1

    tmp[0,0] = fileOne
    tmp[0,1] = fileOne
    tmp[0,2] = 's'
    tmp[0,3] = '-1'
    data = np.vstack([data,tmp])

#Change each dimension; get five random images per dimension 
for i in range(4):
    for j in range(8):
        ind = getRand()
        fileOne = "flower1_" + str(ind[0]) + str(ind[1]) + str(ind[2]) + str(ind[3]) + "_1.png"
        while fileOne in data[i*4:i*4+j,i] or fileOne in data[i*4:i*4+j,i]: 
            ind = getRand()
            fileOne = "flower1_" + str(ind[0]) + str(ind[1]) + str(ind[2]) + str(ind[3]) + "_1.png"
            countDoubles+=1
        if (ind[i]==1):
            ind[i]=9
        else:
            ind[i]=1
        fileTwo = "flower1_" + str(ind[0]) + str(ind[1]) + str(ind[2]) + str(ind[3]) + "_1.png"
        tmp[0,0] = fileOne
        tmp[0,1] = fileTwo
        tmp[0,2] = 'd'
        tmp[0,3] = str(i)
        data = np.vstack([data,tmp])

dirPath = os.getcwd()
updatedData = {'img1':data[:,0],'img2':data[:,1],'response':data[:,2],'dim':data[:,3]}
df = pd.DataFrame(updatedData)
df.to_csv(dirPath + '/Output/' + 'flowerParams1.csv',index=False)
print(countDoubles)



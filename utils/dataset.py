import os
import numpy as np
from nibabel.testing import data_path
import nibabel as nib
import matplotlib.pyplot as plt
import time
from PIL import Image
import pickle

'''
Converts and saves the niftii format files to numpy arrays
'''

m = 0
n=10000
data=[]
for i in range(180,219):
    if(i<10):
        num="00"+str(i)
        file = "CTR_TRN_"+num+".nii.gz"
    elif(i<100):
        num="0"+str(i)
        file = "CTR_TRN_"+num+".nii.gz"
    else:
        num=str(i)
        file = "CTR_TRN_"+num+".nii.gz"

    epi_img_data = nib.load('TrainingSet_2_of_2/'+file)
    img_data = epi_img_data.get_data()

    np.save("img_datas/{}.npy".format(i), img_data)
    
    print(img_data.shape)
    #data.append(img_data)
    
#with open("data.txt", "wb") as fp:
    #pickle.dump(data, fp)   


# error: cannot pack 512x512 from 512x512x128
#data = np.asarray(data)
#print(data.shape)


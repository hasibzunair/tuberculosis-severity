import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import pylab
import cv2

'''
Fancy program which shows the CT scan slice by slice
'''

# the CT scan
image_number = "new"
img_3d = np.load("{}.npy".format(image_number))
print(img_3d.shape)

counter = 0
window = np.array((1,2))

while True:
    if counter >= img_3d.shape[-1]:
        break
    window = img_3d[:,:,counter]
    cv2.imshow("image 3d".format(counter), window)
    
    k = cv2.waitKey(1) & 0xff
    if k != 255: 
        if k == 112:
            print("forward")
            counter+=1
            # savea images
            #cv2.imwrite("{}.jpg".format(counter), window)
            print(counter)
            
        if k == 108:
            print("backward")
            counter-=1
            print(counter)

    if k == 27: 
        break

print("All slices shown")
cv2.destroyAllWindows()

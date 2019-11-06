########################
######Author Darshan####
########################

import numpy as np
import cv2

l = 256 #####256 for 8-bit image
def image_negative(image):
    rows,col = np.shape(image)
    output = np.zeros([rows,col])
    for i in range(rows):
        for j in range(col):
            out = int(l-1-image[i][j])
            output[i][j] = out        
    cv2.imwrite("image_negative.png",output)
    print("Check your directory for image_negative.png!!!")
    
image = cv2.imread("owl.jpg",0)
image_negative(image)

########################
#####Author Darshan#####
########################

import numpy as np
import cv2

l = 256  #Considering an 8-Bit Image
def contrast_stretching(image,r_min,r_max):
    rows,col = np.shape(image)
    output = np.zeros([rows,col])
    for i in range(rows):
        for j in range(col):
            out = int(r_min*((r_max - image[i][j])/(r_max-r_min)) + r_max*((image[i][j]-r_min)/(r_max-r_min))) #Interpolation
            if(out >= r_max):
                out = r_max         
            if(out < r_min):
                out = r_min
            output[i][j] = out      
    cv2.imwrite("contrast_stretched.png",output)
    print("Check your directory for contrast_stretched.png!!!")
    
image = cv2.imread("owl.jpg",0) #Reading the color image as Grayscale to perform Constrast Stretching
print("Enter the value of r_min:\n")
r_min = int(input())
print("Enter the value of r_max:\n")  #R_min and R_max are the bounds
r_max = int(input())                  #All the values in the image below R_min will be rounded off to R-min  
contrast_stretching(image,r_min,r_max)#All the values in the image above R_max will be rounded off to R-max

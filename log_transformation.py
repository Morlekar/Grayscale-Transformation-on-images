########################
#####Author Darshan#####
########################

import numpy as np
import cv2

def log_transformation(c,image):
    rows,col =np.shape(image)
    s2 = np.zeros([rows,col])
    
    for i in range(rows):
        for j in range(col):
            s2[i][j]= c * np.log(image[i][j]+1)
            if(s2[i][j]>=255):
                s2[i][j] = 255
            if(s2[i][j]<0):
                s2[i][j]=0
    cv2.imwrite("log_transformed.png",s2)
    print("Please Find log_transformed.png in your working directory!!")

image = cv2.imread("owl.jpg",0)
print("Enter the value of C:\n")
c = float(input())

log_transformation(c,image)

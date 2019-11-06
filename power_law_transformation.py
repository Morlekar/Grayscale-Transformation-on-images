########################
#####Author Darshan#####
########################

import numpy as np
import cv2

def power_law_transformation(c,gamma,image):
    rows,col =np.shape(image)
    s1 = np.zeros([rows,col])
    
    for i in range(rows):
        for j in range(col):
            s1[i][j]= int(c * (image[i][j] ** gamma))
            if(s1[i][j]>=255):
                s1[i][j] = 255
            if(s1[i][j]<0):
                s1[i][j]=0
    cv2.imwrite("power_law_transformed.png",s1)
    print("Check your directory for power_law_transformed.png!!!")

image = cv2.imread("owl.jpg",0)

print("Enter the value of C:\n")
c = float(input())
print("Enter the value of Gamma:\n")
gamma = float(input())

power_law_transformation(c,gamma,image)

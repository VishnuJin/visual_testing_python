import cv2
import numpy as np
import os
base_path = "baseline"
test_img = "test_imgs"

def checkpoint(img_name):
    base = cv2.imread(os.path.join(base_path,img_name+'.png'))

    if os.path.exists(test_img):
        test = cv2.imread(os.path.join(test_img,img_name+'.png'))
    else:
        return("No test_img folder is found ,First run")

    diff = cv2.subtract(base,test)
    b,g,r = cv2.split(diff)
    if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
        print("images are same")
        return("Visual Testing Pass")
    else:
        print("Images are Different")
        cv2.imshow("Difference",diff)
        imgray = cv2.cvtColor(base,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,127,255,0)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(test, contours, -1, (0,255,0), 1)
        cv2.imshow("Difference",diff)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return("Visual Testing Failed")

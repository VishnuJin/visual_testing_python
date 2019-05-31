#importing packages
import cv2 #computer vision
import numpy as np
import os
from PIL import Image, ImageChops, ImageDraw
#folder paths
base_path = "baseline"
test_img = "test_imgs"

point_table = ([0] + ([255] * 255))

def new_gray(size, color):
    img = Image.new('L',size)
    dr = ImageDraw.Draw(img)
    dr.rectangle((0,0) + size, color)
    return img

def black_or_b(base_img, test_imge, opacity=0.85):
    diff = ImageChops.difference(base_img, test_imge)
    diff = diff.convert('L')
    # Hack: there is no threshold in PILL,
    # so we add the difference with itself to do
    # a poor man's thresholding of the mask: 
    #(the values for equal pixels-  0 - don't add up)
    thresholded_diff = diff
    for repeat in range(3):
        thresholded_diff  = ImageChops.add(thresholded_diff, thresholded_diff)
    h,w = size = diff.size
    mask = new_gray(size, int(255 * (opacity)))
    shade = new_gray(size, 0)
    new = base_img.copy()
    new.paste(shade, mask=mask)
    # To have the original image show partially
    # on the final result, simply put "diff" instead of thresholded_diff bellow
    new.paste(test_imge, mask=thresholded_diff)
    return new

#function to compare the images
def checkpoint(img_name):
    """
    (image_name)->comaprision status
    This function accepts the image name as paremeter(its expected to haev the same name for 2 images in basline & test image )
    returns ->Pass or Fail(Image comparision result)
    """
    base = cv2.imread(os.path.join(base_path,img_name+'.png'))

    if os.path.exists(test_img):
        test = cv2.imread(os.path.join(test_img,img_name+'.png'))
    else:
        return("No test_img folder is found ,First run")

    diff = cv2.subtract(base,test)
    #cv2.imshow("Difference",diff)
    b,g,r = cv2.split(diff)
    if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
        print("images are same")
        return("Visual Testing Pass")
    else:
        print("Images are Different")
        #cv2.imshow("Difference",diff)
        #cv2.imwrite(os.path.join("diff_results",img_name+'.png'),diff)
        #imgray = cv2.cvtColor(test,cv2.COLOR_BGR2GRAY)
        #ret,thresh = cv2.threshold(imgray,127,255,0)
        #contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(diff, contours, -1, (0,255,0), 1)
        #cv2.imwrite(os.path.join("diff_results",img_name+'.png'),diff)
        #cv2.imshow("Difference",diff)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        base_img = Image.open(os.path.join(base_path,img_name+'.png'))
        test_imge = Image.open(os.path.join(test_img,img_name+'.png'))
        result_img = black_or_b(base_img, test_imge)
        result_img.show()
        return("Visual Testing Failed")
#img_name = "BlazeDemo"
#base_img = Image.open(os.path.join(base_path,img_name+'.png'))
#test_img = Image.open(os.path.join(test_img,img_name+'.png'))
#result_img = black_or_b(base_img, test_img)
#result_img.save(os.path.join("diff_results",img_name+'.png'))

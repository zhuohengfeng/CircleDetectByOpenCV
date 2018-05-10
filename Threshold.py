import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('33.png')
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
size = GrayImage.shape
ret,thresh1=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(GrayImage,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO_INV)
titles = ['Gray Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [GrayImage, thresh1, thresh2, thresh3, thresh4, thresh5]
#for i in range(6):
#   cv2.imshow(titles[i], images[i])  # 显示处理后的函数

# hough transform 主要调

dst_img = thresh5
dst_img = cv2.GaussianBlur(dst_img, (3, 3), 0)
dst_img = cv2.Canny(dst_img, 50, 100)  # apertureSize默认为3
cv2.imshow("calc_img", dst_img)

circles = cv2.HoughCircles(dst_img, cv2.HOUGH_GRADIENT,
                   dp=1,
                   minDist = 50,
                   param1=6, #20
                   param2=25, #25
                   minRadius=0, #20
                   maxRadius=0 )#max(size[0], size[1])

#print("circles={}, size={}".format(circles, min(size[0]/2, size[1]/2)))
if circles is not None and len(circles) != 0:
    circles = np.uint16(np.around(circles))
    # 画圆
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(GrayImage, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(GrayImage, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow("Dst Img", GrayImage)  # 显示处理后的函数
cv2.waitKey(0)
cv2.destroyAllWindows()
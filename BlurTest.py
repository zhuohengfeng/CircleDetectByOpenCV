#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 22:40
# @Author  : zhuohf1
# @File    : BlurTest.py
import cv2
import numpy as np

src_img = cv2.imread('a2.png')
dst_img = src_img.copy()

# 各种模糊，中值模糊效果比较好
#blurImg = cv2.GaussianBlur(GrayImage,(5,5),0)
#blurImg = cv2.medianBlur(GrayImage,15)
#blurImg = cv2.bilateralFilter(GrayImage,9,75,75)
#GrayImage = cv2.blur(GrayImage, (3, 3))
#Canny = cv2.Canny(blurImg, 30, 30)  # apertureSize默认为3
src_img = cv2.medianBlur(src_img,11)

# 模糊后转化成灰度图
GrayImage = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
size = GrayImage.shape

#ret, binary = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU      )
# 11为block size，2为C值
binary = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY,221,2 ) #11,2
#binary = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY,101,2)
#binary = cv2.medianBlur(binary,11)
#binary = cv2.medianBlur(binary,5)

'''
image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours2 = [x for x in contours if cv2.contourArea(x) < 50000 and cv2.contourArea(x) > 10000]

for contour in contours2:
    x, y, w, h = cv2.boundingRect(contour)
    print("rect={},{},{},{}".format(x, y, w, h))
    cv2.rectangle(dst_img, (x, y), (x + w, y + h), (255, 0, 255), 2)
'''
# hough transform 主要调
circles = cv2.HoughCircles(binary, cv2.HOUGH_GRADIENT,
                           dp=1.5,
                           minDist=500,
                           param1=130,
                           param2=38,
                           minRadius=20,
                           maxRadius=300)

print("circles={}, size={}".format(circles, min(size[0] / 2, size[1] / 2)))
if circles is not None and len(circles) != 0:
    circles = np.uint16(np.around(circles))
    # 画圆
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(dst_img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(dst_img, (i[0], i[1]), 2, (0, 0, 255), 3)



#cv2.imshow("blurImg", GrayImage)
cv2.imshow("calc_img", binary)
cv2.imshow("Dst Img", dst_img)  # 显示处理后的函数
cv2.waitKey(0)
cv2.destroyAllWindows()

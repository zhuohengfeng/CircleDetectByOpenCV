#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 10:50
# @Author  : zhuohf1
# @File    : CannyTest.py
import cv2
import numpy as np

src_img = cv2.imread('c1.png')
dst_img = src_img.copy()
graySrc = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)

# 二值化
threshold = cv2.medianBlur(graySrc,15)
threshold = cv2.adaptiveThreshold(threshold, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 221, 2)
threshold = cv2.medianBlur(threshold,5)
image, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours2 = [x for x in contours if cv2.contourArea(x) < 100000 and cv2.contourArea(x) > 5000]

copyImg = None
for contour in contours2:
    x, y, w, h = cv2.boundingRect(contour)
    print("rect={},{},{},{}".format(x, y, w, h))
    copyImg = graySrc[y -5:y + h+5 , x-5 :x + w+5 ]

copyImg = cv2.medianBlur(copyImg,9)
circles = cv2.HoughCircles(copyImg, cv2.HOUGH_GRADIENT,
                           dp=1.7,  # 1.5    2
                           minDist=480,  # 480
                           param1=100,  # 120
                           param2=52,  # 52
                           minRadius=48,  # 48
                           maxRadius=480)  # 480

print("circles={}".format(circles))
if circles is not None and len(circles) != 0:
    circles = np.uint16(np.around(circles))
    # 画圆
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(copyImg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(copyImg, (i[0], i[1]), 2, (0, 0, 255), 3)


cv2.imshow("canny", copyImg)
#cv2.imshow("Dst Img", dst_img)  # 显示处理后的函数
cv2.waitKey(0)
cv2.destroyAllWindows()

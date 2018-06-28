#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 15:58
# @Author  : zhuohf1
# @File    : FindContours.py

import cv2
import numpy as np

src_img = cv2.imread('4444.png')
dst_img = src_img.copy()
graySrc = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)

# 二值化
threshold = cv2.medianBlur(graySrc,25)
threshold = cv2.adaptiveThreshold(threshold, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 221, 2)
threshold = cv2.medianBlur(threshold,5)

'''
# hough transform 主要调 1.5, 100, 130, 38, 20, 300
circles = cv2.HoughCircles(threshold, cv2.HOUGH_GRADIENT,
                           dp=1.7,  # 1.5
                           minDist=50,  # 100
                           param1=130,  # 130
                           param2=38,  # 38
                           minRadius=200,  # 0
                           maxRadius=300)  # 0

print("circles={}".format(circles))
if circles is not None and len(circles) != 0:
    circles = np.uint16(np.around(circles))
    # 画圆
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(dst_img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(dst_img, (i[0], i[1]), 2, (0, 0, 255), 3)
'''

image, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print("contours.size = {}".format(len(contours)))
contours2 = [x for x in contours if cv2.contourArea(x) < 262144 and cv2.contourArea(x) > 16384]

for contour in contours2:
    x, y, w, h = cv2.boundingRect(contour)
    print("rect={},{},{},{}".format(x, y, w, h))
    cv2.rectangle(dst_img, (x, y), (x + w, y + h), (255, 0, 255), 2)


cv2.imshow("threshold", threshold)
cv2.imshow("Dst Img", dst_img)  # 显示处理后的函数
cv2.waitKey(0)
cv2.destroyAllWindows()

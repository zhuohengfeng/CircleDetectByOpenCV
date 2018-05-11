#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 9:29
# @Author  : zhuohf1
# @File    : OpenCV_test_UI.py


import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img=cv2.imread('33.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('image')

# create trackbars for color change
t_name = 'Threshold'
t_switch = 'T_Switch:'
cv2.createTrackbar(t_name, 'image', 0, 100, nothing)
cv2.createTrackbar(t_switch, 'image',0,1,nothing)

c_name = 'Canny'
c_switch = 'C_Switch:'
cv2.createTrackbar(c_name, 'image', 0, 100, nothing)
cv2.createTrackbar(c_switch, 'image',0,1,nothing)

h_name = 'Hough'
h_switch = 'H_Switch:'
cv2.createTrackbar(h_name, 'image', 0, 100, nothing)
cv2.createTrackbar(h_switch, 'image',0,1,nothing)


while(1):
    cv2.imshow('image',gray)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    threshold = cv2.getTrackbarPos(t_name,'image')
    isThreshold = cv2.getTrackbarPos(t_switch,'image')

    canny = cv2.getTrackbarPos(c_name,'image')
    isCanny = cv2.getTrackbarPos(c_switch,'image')
    if isCanny == 1:
        detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
        detected_edges = cv2.Canny(detected_edges, canny, canny * 3, apertureSize=3)


    hough = cv2.getTrackbarPos(h_name,'image')
    isHough = cv2.getTrackbarPos(h_switch,'image')

    print("threshold={}, isThreshold={}".format(threshold, isThreshold))

cv2.destroyAllWindows()
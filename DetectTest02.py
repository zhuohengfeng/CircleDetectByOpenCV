#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 11:48
# @Author  : zhuohf1
# @File    : DetectTest01.p

# 参考文档https://blog.csdn.net/liqiancao/article/details/55670749
import cv2

#1. 加载图片，转成灰度图
image = cv2.imread("a2.png")
#image = cv2.imread("panxie.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#2. 用Sobel算子计算x，y方向上的梯度，之后在x方向上减去y方向上的梯度，通过这个减法，我们留下具有高水平梯度和低垂直梯度的图像区域
gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

# subtract the y-gradient from the x-gradient
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)

#3. 去除图像上的噪声。首先使用低通滤泼器平滑图像（9 x 9内核）,这将有助于平滑图像中的高频噪声。
# 低通滤波器的目标是降低图像的变化率。如将每个像素替换为该像素周围像素的均值。这样就可以平滑并替代那些强度变化明显的区域。
# 然后，对模糊图像二值化。梯度图像中不大于90的任何像素都设置为0（黑色）。 否则，像素设置为255（白色）。
# blur and threshold the image
blurred = cv2.blur(gradient, (9, 9))
(_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)

#4. 在上图中我们看到蜜蜂身体区域有很多黑色的空余，我们要用白色填充这些空余，
# 使得后面的程序更容易识别昆虫区域，这需要做一些形态学方面的操作。
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

#5. 从上图我们发现图像上还有一些小的白色斑点，这会干扰之后的昆虫轮廓的检测，要把它们去掉。分别执行4次形态学腐蚀与膨胀。
# perform a series of erosions and dilations
closed = cv2.erode(closed, None, iterations=4)
closed = cv2.dilate(closed, None, iterations=4)


cv2.imshow("Image", gradient)
cv2.waitKey(0)

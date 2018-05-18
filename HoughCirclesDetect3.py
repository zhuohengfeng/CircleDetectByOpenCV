#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 15:15
# @Author  : zhuohf1
# @File    : HoughCirclesDetect.py

# pip install --upgrade setuptools
# pip install numpy Matplotlib
# pip install opencv-python
#pip install Pillow

#导入cv模块
import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
先补充下霍夫圆变换的几个参数知识：

dp，用来检测圆心的累加器图像的分辨率于输入图像之比的倒数，且此参数允许创建一个比输入图像分辨率低的累加器。
上述文字不好理解的话，来看例子吧。例如，如果dp= 1时，累加器和输入图像具有相同的分辨率。如果dp=2，累加器便有输入图像一半那么大的宽度和高度。

minDist，为霍夫变换检测到的圆的圆心之间的最小距离，即让我们的算法能明显区分的两个不同圆之间的最小距离。
这个参数如果太小的话，多个相邻的圆可能被错误地检测成了一个重合的圆。反之，这个参数设置太大的话，某些圆就不能被检测出来了。

param1，有默认值100。它是method设置的检测方法的对应的参数。对当前唯一的方法霍夫梯度法，它表示传递给canny边缘检测算子的高阈值，而低阈值为高阈值的一半。

param2，也有默认值100。它是method设置的检测方法的对应的参数。对当前唯一的方法霍夫梯度法，它表示在检测阶段圆心的累加器阈值。它越小的话，就可以检测到更多根本不存在的圆，而它越大的话，能通过检测的圆就更加接近完美的圆形了。

minRadius，默认值0，表示圆半径的最小值。

maxRadius，也有默认值0，表示圆半径的最大值。
'''

def main():
    src_img = cv2.imread("./66.png" ) #flags = cv2.IMREAD_REDUCED_COLOR_8
    dst_img = src_img.copy()

    # 灰度图像
    gray = cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY ) #cv2.COLOR_BGR2GRAY
    size = gray.shape
    # 二值化
    #ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)
    ret, binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
    #ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    #ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
    #ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)

    # 删除部分连通
    # image就是返回的原图
    image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #print("contours={}".format(contours[0]))
    contours2 = [x for x in contours if cv2.contourArea(x) < 50000 and cv2.contourArea(x) > 1000]

    for contour in contours2:
        x, y, w, h = cv2.boundingRect(contour)
        print("rect={},{},{},{}".format(x, y, w, h))
        cv2.rectangle(dst_img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        # draw the outer circle
        #cv2.circle(dst_img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        #cv2.circle(dst_img, (i[0], i[1]), 2, (0, 0, 255), 3)
    #    print("contours={}".format(cv2.contourArea(contour)))

    # 把面积小的连通的设置成白色
    #def drawContours(image, contours, contourIdx, color, thickness=None, lineType=None, hierarchy=None, maxLevel=None,
    #                 offset=None):  # real signature unknown; restored from __doc__
    #cv2.drawContours(binary, contours, -1, (255, 255, 255), 3)
    #cv2.drawContours(dst_img, contours2, -1, (0, 0, 255), 3)


    # inputImage = binary
    # # hough transform 主要调
    # circles = cv2.HoughCircles(inputImage, cv2.HOUGH_GRADIENT,
    #                    dp=1.2,
    #                    minDist= min(size[0], size[1]),
    #                    param1=15,
    #                    param2=26,
    #                    minRadius=80,
    #                    maxRadius=150 )
    #
    # print("circles={}, size={}".format(circles, min(size[0]/2, size[1]/2)))
    # if circles is not None and len(circles) != 0:
    #     circles = np.uint16(np.around(circles))
    #     # 画圆
    #     for i in circles[0, :]:
    #         # draw the outer circle
    #         cv2.circle(dst_img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    #         # draw the center of the circle
    #         cv2.circle(dst_img, (i[0], i[1]), 2, (0, 0, 255), 3)
    #
    #
    cv2.imshow("calc_img", binary)
    cv2.imshow("Dst Img", dst_img)  # 显示处理后的函数
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
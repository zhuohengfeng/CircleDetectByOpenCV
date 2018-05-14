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
    src_img = cv2.imread("./11.png")
    dst_img = src_img.copy()

    # 灰度图像
    gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    size = gray.shape
    ret, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)

    # 调节对比度
    # OpenCV中亮度和对比度应用这个公式来计算：g(x) = αf(x) + β，其中：α(>0)、β常称为增益与偏置值，分别控制图片的对比度和亮度
    #gray = np.uint8(np.clip((1.5 * gray + 10), 0, 255))
    # Canny边缘检测
    #gray = cv2.GaussianBlur(gray, (3, 3), 0)  # 高斯平滑处理原图像降噪
    #gray = cv2.Canny(gray, 80, 90)  # apertureSize默认为3

    #plt.subplot(121), plt.imshow(gray, 'gray')
    #plt.xticks([]), plt.yticks([])

    # hough transform 主要调
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,
                       dp=1.1,
                       minDist= min(size[0], size[1]),
                       param1=15,
                       param2=26,
                       minRadius=80,
                       maxRadius=150 )

    print("circles={}, size={}".format(circles, min(size[0]/2, size[1]/2)))
    if circles is not None and len(circles) != 0:
        circles = np.uint16(np.around(circles))
        # 画圆
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(dst_img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(dst_img, (i[0], i[1]), 2, (0, 0, 255), 3)


    #cv2.imshow("calc_img", gray)
    cv2.imshow("Dst Img", dst_img)  # 显示处理后的函数
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
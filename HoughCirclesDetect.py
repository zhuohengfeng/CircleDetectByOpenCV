#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 15:15
# @Author  : zhuohf1
# @File    : HoughCirclesDetect.py

# pip install --upgrade setuptools
# pip install numpy Matplotlib
# pip install opencv-python

#导入cv模块
import cv2
import numpy as np


def main():
    src_img = cv2.imread("./22.png")
    dst_img = src_img.copy()

    # 灰度图像
    gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)

    # 调节对比度
    # OpenCV中亮度和对比度应用这个公式来计算：g(x) = αf(x) + β，其中：α(>0)、β常称为增益与偏置值，分别控制图片的对比度和亮度
    # edges = np.uint8(np.clip((1.5 * gray + 10), 0, 255))
    edges = np.uint8(np.clip((1.8 * gray + 10), 0, 255))

    # # hough transform 主要调
    # circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT,
    #                    dp=1,
    #                    minDist=300,
    #                    param1=6,
    #                    param2=100,
    #                    minRadius=0,
    #                    maxRadius=0)
    #
    # print("circles={}".format(circles))
    # if circles is not None and len(circles) != 0:
    #     circles = np.uint16(np.around(circles))
    #     # 画圆
    #     for i in circles[0, :]:
    #         # draw the outer circle
    #         cv2.circle(dst_img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    #         # draw the center of the circle
    #         cv2.circle(dst_img, (i[0], i[1]), 2, (0, 0, 255), 3)


    cv2.imshow("edges", edges)
    #cv2.imshow("Dst Img", dst_img)  # 显示处理后的函数
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
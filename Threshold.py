import cv2
import numpy as np
from matplotlib import pyplot as plt

src_img=cv2.imread('a2.png')

# x0, y0(240, 165)  x1, y1(392:280) ==> [y0:y1, x0:x1]
#numpy表示的图像，高度（y坐标）在前，宽度（x坐标）在后
copyImg = src_img[165:280,240:392]




cv2.imshow("Dst ImgcopyImg", copyImg)  # 显示处理后的函数
cv2.waitKey(0)
cv2.destroyAllWindows()
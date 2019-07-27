import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("123.jpg")
img = cv2.resize(img,(640,480))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def red(img):
    #defining the range of ___color
    lower_red = np.array([0,50,0],np.uint8)
    upper_red = np.array([3, 255,255],np.uint8)
    maskr0 = cv2.inRange(hsv, lower_red, upper_red)

    # upper mask (170-180)
    lower_red = np.array([170,50,0],np.uint8)
    upper_red = np.array([180,255,255],np.uint8)
    maskr1 = cv2.inRange(hsv, lower_red, upper_red)

    # join my masks
    maskr = maskr0+maskr1


    #kernal = np.ones((5,5), "uint8")
    resr = cv2.bitwise_and(img,img, mask = maskr)
    object = "home"

    img_re = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    imgray = cv2.cvtColor(resr, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127,255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    showr=cv2.drawContours( imgray,contours, 3 , (0,255,0), 3)
    cnt = contours[0]
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    print(center[0])


    return showr,object



def blue(img):
    lower_blue = np.array([100,30,0],np.uint8)
    upper_blue = np.array([120,255,255],np.uint8)
    maskb = cv2.inRange(hsv, lower_blue, upper_blue)

    resb = cv2.bitwise_and(img,img, mask = maskb)
    object = "target"

    img_re = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    imgray = cv2.cvtColor(resb, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127,255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    showb=cv2.drawContours( imgray,contours, 0 , (0,255,0), 3)
    cnt = contours[0]
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    print(center[0])

    return showb, object


def green(img):


    lower_green = np.array([33,100,100],np.uint8)
    upper_green= np.array([83,255,255],np.uint8)
    maskg = cv2.inRange(hsv, lower_green, upper_green)


    #kernal = np.ones((5,5), "uint8")
    resg = cv2.bitwise_and(img,img, mask = maskg)
    object = "paperball"


    img_re = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    imgray = cv2.cvtColor(resg, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127,255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    showg=cv2.drawContours( imgray,contours, 0 , (0,255,0), 3)
    cnt = contours[0]
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    print(center[0])



    return  showg, object


"""""""""""""""""""""""
FIND THE COORDINATES
"""""""""""""""""""""""


# def coord(img, object):
#
#     if  object == "paperball" :
#         rob1, rob2, rob3, rob4 = fuckCVTwo(img)
#         doublecoor = rob3 + rob4
#         coor = doublecoor /2.
#         print(coor)
#
#
#
#
#     if object == "target":
#         rob1, rob2, rob3, rob4 = fuckCVTwo(img)
#         doublecoor = rob3 + rob4
#         coor = doublecoor /2.
#         print(coor)
#
#
#     if object == "point":
#         rob1, rob2, rob3, rob4 = fuckCVTwo(img)
#         doublecoor = rob3 + rob4
#         coor = doublecoor /2.
#         print(coor)
#
#
#
# def fuckCVTwo(img):
#     # print(img.shape)
#     rows, cols  = imgray.shape
#     fuckedy = False
#     find_row = 0
#     for r in range(rows):
#         for c in range(cols):
#             # print(img[r,c])
#             if(np.array_equal(img[r,c], [0,0,0]) | fuckedy):
#                 pass
#             else:
#                 fuckedy = True
#                 find_row = r
#     print(find_row)
#
#
#     fuckedy2 = False
#     find_row2 = 0
#
#     for r in reversed(range(rows)):
#         for c in reversed(range(cols)):
#             # print(img[r,c])
#             if(np.array_equal(img[r,c], [0,0,0]) | fuckedy2):
#                 pass
#             else:
#                 fuckedy2 = True
#                 find_row2 = r
#     print(find_row2)
#
#
#     fuckedx = False
#     find_col = 0
#     for c in range(cols):
#         for r in range(rows):
#             # print(img[r,c])
#             if(np.array_equal(img[r,c], [0,0,0]) | fuckedx):
#                 pass
#             else:
#                 fuckedx = True
#                 find_col = c
#     print(find_col)
#
#
#     fuckedx2 = False
#     find_col2 = 0
#
#     for c in reversed(range(cols)):
#         for r in range(rows):
#         # print(img[r,c])
#             if(np.array_equal(img[r,c], [0,0,0]) | fuckedx2):
#                 pass
#             else:
#                 fuckedx2 = True
#                 find_col2= c
#     print(find_col2)
#
#     return (find_row, find_row2, find_col, find_col2)




ffm,cls =blue(hsv)
#roco = coord(ffm, cls)



plt.imshow(ffm, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
# cv2.imshow('ffm',0)
# cv2.waitKey(0)

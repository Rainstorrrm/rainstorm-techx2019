from collections import deque
import imutils
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import time


ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help = "path to the (optional) video file")
ap.add_argument("-b", "--buffer", type = int, default = 64,
    help = "max buffer size")
args = vars(ap.parse_args())

def get_mask(object):
    lower_red1 = (0,50,0)
    upper_red1 = (3, 255,255)

    lower_red2 = (170,50,0)
    upper_red2 = (180,255,255)

    lower_blue = (100,30,0)
    upper_blue = (120,255,255)

    lower_green = (33,100,100)
    upper_green=  (83,255,255)

    mask0 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask1 = cv2.inRange(hsv, lower_red2, upper_red2)
    maskred = mask0 + mask1
    maskgreen= cv2.inRange(hsv, lower_green, upper_green)
    maskblue = cv2.inRange(hsv, lower_blue, upper_blue)
    if object == "paperball":
        mask = maskgreen
    elif object == "owner":
        mask = maskred
    elif object == "homebase" :
        mask = maskblue

    return mask



def mask_paperball():
    mask = maskred
    return mask

def mask_owner():
    mask = maskgreen
    return mask

def mask_homebase():
    mask = maskblue
    return mask




pts = deque(maxlen = args["buffer"])

if not args.get("video", False):
    vs = VideoStream(src = 0).start()

else:
    vs = cv2.VideoCapture(args["video"])

time.sleep(2.0)

while True:
    frame = vs.read()
    frame = frame[1] if  args.get("video", False) else frame

    if frame is None:
        break

    frame = imutils.resize(frame, width =600)
    blurred = cv2.GaussianBlur(frame, (11,11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = get_mask("homebase")
    mask = cv2.erode(mask, None, iterations = 2)
    mask = cv2.dilate(mask, None, iterations  = 2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    if len(cnts) > 0:
        c =max(cnts, key= cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0,0,255), -1)
            rob = center[0] - 320
            print(rob)
    pts.appendleft(center)

    for i in range(1, len(pts)):

        if pts[i - 1] is None or pts[i] is None:
            continue

        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
        cv2.line(frame,pts[i - 1], pts[i], (0,0,255), thickness)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

if not args.get("video", False):
    vs.stop()

else:
    vs.release()

cv2.destroyAllWindws()

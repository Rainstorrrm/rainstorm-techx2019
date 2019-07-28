import numpy as np
import cv2
import os
import Hack

cap = cv2.VideroCapture(0)

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')

currentframe = 0

while(True):
    #capture frame by frame
    ret, frame = cap.read()

    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

    #Our operations on the frame come here

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.resieze(hsv, (640,480))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   这里需要define什么时候call green/red/blue三个 functions
""""""""""""""""""""""""""""”“”“”“”“”“”""""""""""""""""""
    ffm,cls =green(hsv)

    #roco = coord(ffm, cls)
    #display the resulting frame
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#When everything done, release the capture
cap.release()
cv2.destroyAllWindws()

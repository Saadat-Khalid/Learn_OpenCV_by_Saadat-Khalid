# Chapter: 11
## Saving Cam Video

import cv2 as cv

cap = cv.VideoCapture(0)

# Writing format, codec, video writer object and file output
frame_width = int(cap.get(3))
frame_height = int(cv.get(4))
out = cv.VideoWriter("cam_video.mp4", cv.VideoWriter_fourcc('M', 'j', 'P', 'G'), 10, (frame_width, frame_height)) # you can control the frame rate with the number 10 mentioned like below line
# out = cv.VideoWriter("cam_video.mp4", cv.VideoWriter_fourcc('M', 'j', 'P', 'G'), 30, (frame_width, frame_height), isColor=False) # if you want to save it into gray or black and white

# Indicators
if (cap.isOpened() == False):
    print("error in reading video")

# Reading & Playing

while(True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY) # convering into Black&White

    # to show in player
    if ret == True:
        out.write(frame)
        cv.imshow("Video", frame) # COlORED 
        # cv.imshow("Video", grayframe) #GRAY
        # cv.imshow("Video", binary) #BLACK&WHITE 

        # to quit with q
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()
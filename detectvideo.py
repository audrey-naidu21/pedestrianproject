# import necessary packages
from imutils.object_detection import non_max_suppression
from imutils import paths
from collections import deque
import math
import numpy as np
import argparse
import imutils
import cv2


ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--images", required=True, help="path to images directory")
#args = vars(ap.parse_args())
ap.add_argument("-v", "--video", help = "path to the (optional) video file")
args = vars(ap.parse_args())

if not args.get("video", False):
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])

recx = 0
recy = 0
#initialize person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

boxes = []
numframe = 0
maxframe = 8



def calcdist(xa, ya, xb, yb):
    rectanglex = (xa + xb)/2
    rectangley = (ya + yb)/2
    print("Center of rectangle: ({}, {})".format(rectanglex, rectangley))
    disty = abs(rectangley - centery)
    distx = abs(rectanglex - centerx)
    return distx

def calcangle(xa, ya, xb, yb):
    rectanglex = (xa + xb)/2
    rectangley = (ya + yb)/2
    angleofpedestrian = math.atan2((rectangley - centery),(rectanglex - centerx))
    return angleofpedestrian


while True:
    (grabbed, frame) = camera.read()


    width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)


    centerx = width/2
    centery = height/2

    print("Center: ({}, {})".format(centerx, centery))
        
    if args.get("video") and not grabbed:
        break
    
    frame = imutils.resize(frame, width = 300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#loop over the image paths
    # load the image and resize it to (1) reduce detection time
    # and (2) improve detection accuracy
    
    orig = frame.copy()

    # detect people in the image
    (rects, weights) = hog.detectMultiScale(orig, winStride=(4, 4),
        padding=(8, 8), scale=1.05)

    # draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # apply non-maxima suppression to the bounding boxes using a
    # fairly large overlap threshold to try to maintain overlapping
    # boxes that are still people
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    #if numframe >= 8:


  
            # draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
        boxes.append((xA, yA, xB, yB))
        while len(boxes) > 8: 
            boxes.pop(0)
        if len(boxes) < 8:
            cv2.rectangle(orig, (xA, yA), (xB, yB), (0, 255, 0), 2)
            distancex = calcdist(xA, yA, xB, yB)
            print("The pedestrian is {} pixels away.".format(distancex))
            #angle = math.atan2((recy - centery),(recx - centerx))
            angle = calcangle(xA, yA, xB, yB)
            print("Angle: {}".format(angle))
            #numframe = numframe + 1
        if len(boxes) >= 8:
            avga= int(np.mean( [a for (a,_,_,_) in boxes] ))
            avgb= int(np.mean( [b for (_,b,_,_) in boxes] ))
            avgc= int(np.mean( [c for (_,_,c,_) in boxes] ))
            avgd= int(np.mean( [d for (_,_,_,d) in boxes] ))
            print("Averages: {}, {}, {}, {}".format(avga, avgb, avgc, avgd))
            distancex = calcdist(avga, avgb, avgc, avgd)
            print("The pedestrian is {} pixels away.".format(distancex))
            angle = calcangle(avga, avgb, avgc, avgd)
            print("Angle: {}".format(angle))
            cv2.rectangle(orig, (avga, avgb), (avgc, avgd), (0, 255, 0), 2)

        break



        
    
    # show some information on the number of bounding boxes
    #filename = imagePath[imagePath.rfind("/") + 1:]
    filename = "one"
    print("[INFO] {}: {} original boxes, {} after suppression".format(
        filename, len(rects), len(pick)))

    # width = camera.get(3)
    # height = camera.get(4)


    

    

    # show the output images
    #cv2.imshow("Before NMS", frame)
    cv2.imshow("After NMS", orig)
    
    cv2.waitKey(1)
 

    
    
camera.release()
cv2.destroyAllWindows()
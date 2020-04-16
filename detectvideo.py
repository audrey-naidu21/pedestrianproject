# import necessary packages
from imutils.object_detection import non_max_suppression
from imutils import paths
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

#initialize person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    (grabbed, frame) = camera.read()
        
    if args.get("video") and not grabbed:
        break
    
    frame = imutils.resize(frame, width = 300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#loop over the image paths
    # load the image and resize it to (1) reduce detection time
    # and (2) improve detection accuracy
    
    orig = frame.copy()

    # detect people in the image
#    (rects, weights) = hog.detectMultiScale(orig, winStride=(4, 4),
#        padding=(8, 8), scale=1.05)

    # draw the original bounding boxes
 #   for (x, y, w, h) in rects:
 #       cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # apply non-maxima suppression to the bounding boxes using a
    # fairly large overlap threshold to try to maintain overlapping
    # boxes that are still people
#    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
#    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    # draw the final bounding boxes
 #   for (xA, yA, xB, yB) in pick:
 #       cv2.rectangle(orig, (xA, yA), (xB, yB), (0, 255, 0), 2)
        
    
    # show some information on the number of bounding boxes
    #filename = imagePath[imagePath.rfind("/") + 1:]
    #print("[INFO] {}: {} original boxes, {} after suppression".format(
       # filename, len(rects), len(pick)))

    # show the output images
#    cv2.imshow("Before NMS", orig)
    cv2.imshow("After NMS", orig)
 

    
    
camera.release()
cv2.destroyAllWindows()


      
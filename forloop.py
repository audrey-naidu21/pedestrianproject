    i = 1
            # draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
    
        if i > 1:
            cv2.rectangle(orig, (xA, yA), (xB, yB), (0, 255, 0), 2)
            centeronex = (xA + xB)/2
            distancex = calcdist(xA, yA, xB, yB)
            print("The pedestrian is {} pixels away.".format(distancex))
            #angle = math.atan2((recy - centery),(recx - centerx))
            angle = calcangle(xA, yA, xB, yB)
            print("Angle: {}".format(angle))
            previous = boxes[i-2]
            previousdist = calcdist(previous)


        else:
            boxes.append((xA, yA, xB, yB))
            centeronex = (xA + xB)/2
            centerboxeslist.append((centeronex))
            numtotal = numtotal + 1
            if numtotal > 1:
                prev = centerboxeslist[numtotal-2] 
                now = centerboxeslist [numtotal -1]
                distancebetweenboxes= abs(prev - centeronex)
                print("The distance between the two  boxes in the same list is {}.".format(distancebetweenboxes))


            centeroney = (yA + yB)/2
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
                reconex = distancex
                print("The pedestrian is {} pixels away.".format(distancex))
                angle = calcangle(avga, avgb, avgc, avgd)
                print("Angle: {}".format(angle))
                cv2.rectangle(orig, (avga, avgb), (avgc, avgd), (0, 255, 0), 2)
            i= i+1
            break

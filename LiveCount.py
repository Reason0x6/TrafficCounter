
import time
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import urllib.request
from datetime import datetime
from PIL import Image
import os

def RunCount(loc, imgName):

    # Image from traffic camera is updated every 60 seconds
    urllib.request.urlretrieve("https://roads-waterways.transport.nsw.gov.au/trafficreports/cameras/camera_images/" + imgName, loc + ".jpg")

    im = cv2.imread(loc + '.jpg')

    bbox, label, conf = cv.detect_common_objects(im) 
    output_image = draw_bbox(im, bbox, label, conf)

    # Save to file
    Image.fromarray(output_image).save(os.getcwd()+"\\" + loc +"\\" + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg")
    # Count traffic based on cars, buses, trucks
    countH = label.count('car') + label.count('bus') + label.count('truck')

    # return the count
    return countH


# Example Data
location = "hexham"
imageOfCam = "newenglandhwy_hexham.jpg"


# Printing
print('Time\t\t\t|\tLocation\t|\tCount')

while True:
       
    print(datetime.now().strftime("%Y/%m/%d, %H:%M:%S") + \
    '\t|\t' + location + '\t\t|\t' + \
    str(RunCount(location, imageOfCam)))

    for i in range(38):
        stri = "Updating: "
        for x in range (i):
            stri += "#"
        for y in range (38-i):
            stri += "-"    
        print(stri, end="|\r")
        time.sleep(1.7)
    print("                                                ", end="\r")

# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:15:11 2019

@author: Shubham
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import imutils

#img = cv2.imread('coin1.jpg', 0)
##img1 = cv2.pyrMeanShiftFiltering(img, 21, 51)
##img_gray = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
##img_gray = cv2.bitwise_not(img_gray)
#img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)
#ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#th1 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                            cv2.THRESH_BINARY, 11, 2)
#
#kernel = np.ones((5, 5))
#edged = cv2.Canny(th1,100,200)
#edged = cv2.dilate(edged, kernel, iterations=2)
#edged = cv2.erode(edged, kernel, iterations=2)
#plt.imshow(edged)

#clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#img1 = clahe.apply(img_gray)
#
#plt.imshow(img1)

#def calcHistogram(img):
#    # create mask
#    m = np.zeros(img.shape[:2], dtype="uint8")
#    (w, h) = (int(img.shape[1] / 2), int(img.shape[0] / 2))
#    cv2.circle(m, (w, h), 60, 255, -1)
#
#    # calcHist expects a list of images, color channels, mask, bins, ranges
#    h = cv2.calcHist([img], [0, 1, 2], m, [8, 8, 8], [0, 256, 0, 256, 0, 256])
#
#    # return normalized "flattened" histogram
#    return cv2.normalize(h, h).flatten()
#
#cnts = cv2.findContours(edges, cv2.RETR_EXTERNAL,
#	cv2.CHAIN_APPROX_SIMPLE)
#cnts = imutils.grab_contours(cnts)
#for (i, c) in enumerate(cnts):
#	# draw the contour
#	((x, y), _) = cv2.minEnclosingCircle(c)
#	cv2.putText(img_gray, "#{}".format(i + 1), (int(x) - 10, int(y)),
#		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
#	cv2.drawContours(img_gray, [c], -1, (0, 255, 0), 3)

#contours = cnts
#contour_list = []
#for contour in contours:
#    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
#    area = cv2.contourArea(contour)
#    if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
#        contour_list.append(contour)
#        
#cv2.drawContours(img, contour_list,  -1, (0,255,124), 2)
#plt.imshow(img)

#plt.imshow(img_gray)

#def edges(img, t):
#    @adapt_rgb(each_channel)
#    def filter_rgb(image):
#        sigma = 1
#        return feature.canny(image, sigma=sigma,
#                             low_threshold=t/sigma/2, high_threshold=t/sigma)
#
#    edges = color.rgb2hsv(filter_rgb(img))
#    edges = edges[..., 2]
#    return edges
#
#
#img = cv2.imread('coin1.jpg', 0)
#img = cv2.GaussianBlur(img, (5, 5), 0)
##img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#img1 = clahe.apply(img_gray)
#
#circles = cv2.HoughCircles(img1, cv2.HOUGH_GRADIENT, 1, 20,
#                           param1=200, param2=100, minRadius=0, maxRadius=0)
#circles = np.uint16(np.around(circles))
#
#for i in circles[0,:]:
#    # draw the outer circle
#    cv2.circle(img_gray,(i[0],i[1]),i[2],(0,255,0),2)
#    # draw the center of the circle
#    cv2.circle(img_gray,(i[0],i[1]),2,(0,0,255),3)
#    
#plt.imshow(img_gray)

import cv2
import numpy as np;

# Read image
frame = cv2.imread('coin1.jpg')
#img1 = cv2.pyrMeanShiftFiltering(img, 21, 51)
#img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#img_gray = cv2.bitwise_not(img_gray)
img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
purpleMin = (115,50,10)
purpleMax = (160, 255, 255)

# Sets pixels to white if in purple range, else will be set to black
mask = cv2.inRange(hsv, purpleMin, purpleMax)
    
# Bitwise-AND of mask and purple only image - only used for display
res = cv2.bitwise_and(frame, frame, mask= mask)
 
#    mask = cv2.erode(mask, None, iterations=1)
# commented out erode call, detection more accurate without it
 
# dilate makes the in range areas larger
mask = cv2.dilate(mask, None, iterations=1)
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


# Set up the detector with default parameters.
im=cv2.bitwise_not(img_gray)

params = cv2.SimpleBlobDetector_Params()
params.minThreshold = 0;    # the graylevel of images
params.maxThreshold = 20000;

params.filterByColor = False
params.blobColor = 0

params.filterByCircularity = True
params.minCircularity = 0

params.filterByConvexity = True
params.minConvexity = 0
 
# Filter by Inertia
params.filterByInertia =True
params.minInertiaRatio = 0

# Filter by Area
params.filterByArea = True
params.minArea = 300
detector = cv2.SimpleBlobDetector_create(params)

reversemask=255-mask
keypoints = detector.detect(hsv)

# Detect blobs.
#keypoints = detector.detect(img_gray)
#im=cv2.bitwise_not(im)
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

plt.imshow(im_with_keypoints)
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 15:06:20 2019

@author: Shubham
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('coin2.jpg')

def detectCoin(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    
    #gray_img = cv2.medianBlur(gray_img, 5)
    
    rows = gray_img.shape[0]
    circles = cv2.HoughCircles(gray_img, 3, 1,
                               rows/8,param1=100, param2=30,
                                   minRadius=10, maxRadius=30)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(img, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(img, center, radius, (255, 0, 255), 3)
            
    plt.imshow(img)
    
def segmentObject(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    ret, markers = cv2.connectedComponents(sure_fg)
#    markers = markers + 1
#    markers[unknown==255] = 0
#    markers = cv2.watershed(img, markers)
#    img[markers==-1] = [255, 0, 0]
    plt.imshow(markers)    
    
def segmentObject2(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    gray_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    ret, thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,
                               kernel, iterations=2)
    bg = cv2.dilate(closing, kernel, iterations=1)
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
    ret, fg = cv2.threshold(dist_transform, 0.02*dist_transform.max(), 255, 0)
    
    height, width = img.shape[:2]

    #Create a mask holder
    mask = fg
    
    #Grab Cut the object
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    
    #Hard Coding the Rect… The object must lie within this rect.
    rect = (10,10,width-200,height-200)
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img1 = img*mask[:,:,np.newaxis]
    
    #Get the background
    background = img - img1
    
    #Change all pixels in the background that are not black to white
    background[np.where((background > [0,0,0]).all(axis = 2))] =[255,255,255]
    
    #Add the background and the image
    final = background + img1
    plt.imshow(final)
    return fg, final

def segmentObject3(img):
#    blur1 = cv2.GaussianBlur(img,(5,5),0)
#    gray1=cv2.cvtColor(blur1,cv2.COLOR_BGR2GRAY)
#    ret,thresh1 = cv2.threshold(gray1,65,255,cv2.THRESH_BINARY_INV)
    
#    img2=cv2.imread("front.jpeg")
    blur2 = cv2.GaussianBlur(img,(5,5),0)
    gray2=cv2.cvtColor(blur2,cv2.COLOR_BGR2GRAY)
    ret,thresh2 = cv2.threshold(gray2,65,255,cv2.THRESH_BINARY_INV)
    
#    diff=cv2.absdiff(thresh2,thresh1)
    diff=cv2.bitwise_xor(thresh2)
    
    kernel = np.ones((2,2),np.uint8)
    diff=cv2.erode(diff,kernel,iterations = 1)
    diff=cv2.dilate(diff,kernel,iterations = 8)
    
    _, contours, _= cv2.findContours(diff,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    c=max(contours,key=cv2.contourArea)
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(diff,(x,y),(x+w,y+h),(125,125,125),2)
    plt.imshow(img)
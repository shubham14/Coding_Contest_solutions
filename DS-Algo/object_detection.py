# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:53:38 2019

@author: Shubham
"""

import numpy as np
import cv2

def resize_img(img, width=-1, height=-1):
    if height == -1 or width == -1:
        raise TypeError("Invalid arguments")
    h = img.shape[0]
    w = img.shape[1]
    if height == -1:
        aspect_ratio = float(w) / h
        new_height = int(width / aspect_ratio)
        return cv2.resize(img, (width, new_height))
    elif width == -1:
        aspect_ratio = h / float(w)
        new_width = int(height / aspect_ratio)
        return cv2.resize(img, (new_width, height))
    
def pyramid(img, scale=1.5, min_size=(30, 30)):
    # yield the original image
    yield img

    # keep looping over the pyramid
    while True:
        # compute the new dimensions of the image and resize it
        w = int(img.shape[1] / scale)
        img = resize_img(img, width=w)

        # if the resized image does not meet the supplied minimum
        # size, then stop constructing the pyramid
        if img.shape[0] < min_size[1] or img.shape[1] < min_size[0]:
            break

        # yield the next image in the pyramid
        yield img
        
def sliding_window(img, window_size, step_size=8):
    for y in range(0, img.shape[0], step_size):
        for x in range(0, img.shape[1], step_size):
            window = img[x: x + window_size[1], y: y + window_size[0]]
            if not (window.shape[0] != window_size[1] or window.shape[1] != window_size[0]):
                yield (x, y, window) 
                
def hogDes(img):
    hog = cv2.HOGDescriptor()
    h = hog.compute(img)
    return h
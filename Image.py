#importing the opencv module
import cv2
import numpy as np
# using imread('path') and 1 denotes read as  color image
img = cv2.imread("dog.jpg", 1)
#Access pixel values and modify them
px = img[100, 100]
#print(px)
# accessing only blue pixel
blue = img[100, 100, 0]
#print(blue)
#This is using for display the image
#cv2.imshow('image',img)
#It will run continuously until the key press.
#cv2.destroyAllWindows()
# save image
status = cv2.imwrite('dog.jpg', img)
print("Image written sucess? : ", status)
#access access image properties
print(img.shape)
print(img.size)
print(img.dtype)
#splitting and merging image
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
#resize the image
img_resized = cv2.resize(img, (780, 540),
               interpolation = cv2.INTER_NEAREST)
#cv2.imshow("Resized",img_resized)
image = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
#cv2.imshow("Rotated",image)
# draw
cv2.circle(img,(80,80), 55, (23,0,0), -1)
#cv2.imshow('image',img)
cv2.rectangle(img,(15,25),(200,150),(0,255,255),15)
#cv2.imshow('image',img)
#defining points for polylines
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
# pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)
#cv2.imshow('image',img)
edges = cv2.Canny(img,200,300,True)
#cv2.imshow("Edge Detected Image", edges)
#blur images
#cv2.imshow("Original Image", img)
#cv2.imshow('cv2.blur output', cv2.blur(img, (3,3)))
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold = 160
ret, thresh1 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, threshold, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO_INV)
#cv2.imshow('Original',image)
#cv2.imshow('Binary Threshold', thresh1)
#cv2.imshow('Binary Threshold Inverted', thresh2)
#cv2.imshow('Truncated Threshold', thresh3)
#cv2.imshow('Zero Threshold', thresh4)
#cv2.imshow('Zero Inverted', thresh5)
ret, th1 = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 11, 2)

#cv2.imshow('Original', image)
#cv2.imshow('Binary Threshold', th1)
#cv2.imshow('Adaptive Threshold', th2)
#cv2.imshow('Gaussain Adaptive Threshold', th3)
# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
# Find Canny edges
edged = cv2.Canny(image, 30, 200)
cv2.waitKey(0)
contours, hierarchy = cv2.findContours(edged,
                                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#cv2.imshow('Original', image)
cv2.imshow('Canny Edges After Contouring', edged)

cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
mouse_events = [j for j in dir(cv2) if 'EVENT' in j]
print(mouse_events)
# image doesn't close immediately.
cv2.waitKey(0)


#Convert to gray-scale and detect edges using Canny edge detection method


import cv2
image= cv2.imread('Laugh.jpeg')
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged= cv2.Canny(gray,30,49)
cv2.imwrite('Canny_Edges.jpeg', edged)
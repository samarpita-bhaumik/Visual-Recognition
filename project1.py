#Draw a bounding box around the foreground object
import cv2
import pytesseract

img = cv2.imread('Laugh.jpeg', 1)

# Convert the color image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blurring the grayscale image
blur = cv2.GaussianBlur(gray_img, (7, 7), 0)

# Apply threshold using Otsu's method
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through the contours and draw bounding boxes
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    x -= 10
    y -= 230
    w += 19
    h += 230
    if h> 300 and w>20:
     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Save the image with bounding boxes
cv2.imwrite('bounding_box_doll.jpg', img)


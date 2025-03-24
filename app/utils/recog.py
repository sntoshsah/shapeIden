import pytesseract
import cv2 as cv


print(pytesseract.image_to_boxes(cv.imread("output/labeled_image.jpg")))
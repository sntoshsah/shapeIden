import cv2
import numpy as np
import pytesseract


def detect_text(roi: np.ndarray):
    # Convert ROI to grayscale
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    # Apply Thresholding to make text more readable
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Use pytesseract to extract text
    custom_config = "--oem 3 --psm 6"
    extracted_text = pytesseract.image_to_string(binary, config=custom_config)
    extracted_text.replace("\n", " ")
    
    return extracted_text.strip()

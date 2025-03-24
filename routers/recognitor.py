from fastapi import APIRouter, File, UploadFile
import cv2
import numpy as np
import pytesseract

router = APIRouter()




@router.post("/extract-text/")
async def extract_text(image: UploadFile = File(...)):
    # Read image file into a numpy array
    contents = await image.read()
    np_array = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    # Convert to grayscale for better OCR accuracy
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to enhance text visibility
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Extract text using pytesseract
    extracted_text = pytesseract.image_to_string(thresh)

    return {"text": extracted_text}

# Run with: uvicorn script_name:app --reload

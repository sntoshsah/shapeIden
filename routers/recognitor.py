from fastapi import APIRouter, File, UploadFile
import cv2
import numpy as np
import pytesseract
from utils.recog import detect_text

router = APIRouter()




@router.post("/extract-text/")
async def extract_text(image: UploadFile = File(...)):
    contents = await image.read()
    np_arr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    extracted_text = detect_text(img)


    return {"text": extracted_text}


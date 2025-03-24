import cv2
from fastapi import FastAPI, File, UploadFile, APIRouter
import numpy as np
from utils.detect import detect_shapes

router = APIRouter()

@router.post("/detect_shapes")
async def detect_shapes_api(file: UploadFile = File(...)):
    contents = await file.read()
    np_arr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    shapes, labeled_image = detect_shapes(image)
    cv2.imwrite("output/labeled_image.jpg", labeled_image)
    
    return shapes
    
    # # Encode labeled image to return
    # _, img_encoded = cv2.imencode('.jpg', labeled_image)
    # return {"shapes": shapes, "labeled_image": img_encoded.tobytes()}

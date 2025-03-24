from fastapi import FastAPI, File, UploadFile
from typing import List
from utils.detect import detect_shapes
from routers import detector, recognitor

app = FastAPI()

app.include_router(detector.router)
app.include_router(recognitor.router)



@app.get("/")
async def root():
    return {"message": "Hello World"}
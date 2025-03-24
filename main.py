from fastapi import FastAPI, File, UploadFile
from typing import List
from utils.detect import detect_shapes
from routers import detector

app = FastAPI()

app.include_router(detector.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
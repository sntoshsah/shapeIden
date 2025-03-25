##  Shape Detector and Text Recognition Tool

This tool is a simple tool that can detect shapes and recognize text from an image. The tool is built using OpenCV and Tesseract OCR. The tool can detect shapes such as rectangles, circles, and triangles. The tool can also recognize text from an image using Tesseract OCR.

### Requirements
- Python
- OpenCV
- pytesseract
- FastAPI


### Installation
1. Clone the repository
```bash
git clone https://github.com/sntoshsah/shapeIden.git
```
2. Change the directory
```bash
cd shapeIden
```

3. Create Virtual Environment
```bash
python3 -m venv env
```
4. Activate the virtual environment
```bash
source env/bin/activate
```
5. Install the required packages
```bash 
pip install -r requirements.txt
```
6. Run the tool
```bash
fastapi run main.py
```

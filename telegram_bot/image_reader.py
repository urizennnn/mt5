from PIL import Image
import pytesseract
import os

# Set TESSDATA_PREFIX based on the operating system
if os.name == "nt":  # Windows
    env = r"C:\Program Files\Tesseract-OCR\tessdata"
    os.environ['TESSDATA_PREFIX'] = env
else:  # Unix-like systems (Linux/MacOS)
    os.environ['TESSDATA_PREFIX'] = '/usr/share/tessdata'

def read_image(image):
    return pytesseract.image_to_string(Image.open(image))


from PIL import Image
import pytesseract

import os
os.environ['TESSDATA_PREFIX'] = '/usr/share/tessdata'
def read_image(image):
    return pytesseract.image_to_string(Image.open(image))

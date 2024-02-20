
from PIL import Image
from io import BytesIO
import pytesseract

def extract_text_from_image(image_data):
    image = Image.open(BytesIO(image_data))
    text = pytesseract.image_to_string(image)
    return text

     
        
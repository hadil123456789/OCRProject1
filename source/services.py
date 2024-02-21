# services.py
from PIL import Image
from io import BytesIO
import pytesseract
from source.preprocessing_utils import Preprocessing  # Import the Preprocessing class

class TextExtractionService:
    @staticmethod
    def extract_text_from_image(image_data):
        try:
            image = Image.open(BytesIO(image_data))
            
            # Apply preprocessing steps
            preprocessed_image = Preprocessing.preprocess_image(image)
            
            # Extract text using Tesseract
            text = pytesseract.image_to_string(preprocessed_image)
            return text
        except Exception as e:
            return f"Error: {str(e)}"

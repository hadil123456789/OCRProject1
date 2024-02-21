# preprocessing_utils.py
from PIL import Image
import cv2
from io import BytesIO
import numpy as np

class Preprocessing:
    @staticmethod
    def preprocess_image(image: Image):
        # Convert the PIL Image to a NumPy array
        img_array = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Resize the image
        img_resized = cv2.resize(img_array, (500, 500))

        # Convert the image to grayscale
        img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

        # Apply adaptive thresholding
        _, img_threshold = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY)

        # Convert NumPy array back to PIL Image
        preprocessed_image = Image.fromarray(cv2.cvtColor(img_threshold, cv2.COLOR_BGR2RGB))

        return preprocessed_image

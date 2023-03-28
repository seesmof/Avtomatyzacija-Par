# import the necessary packages
import pytesseract
from textblob import TextBlob
from PIL import Image

# load the input image and convert it to grayscale
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image = Image.open("input.jpg")

# Provide the tesseract executable location to the pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Pass the image object to the image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(image)

# Display the extracted text
print(text)

import pytesseract
from PIL import Image

img = Image.open('X00016469670.jpg')
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, config=custom_config)

print(text)

with open('X00016469670.txt', 'w') as text_file:
    text_file.write(text)
   
#оригинал: https://www.youtube.com/watch?v=UPjTYorn59g

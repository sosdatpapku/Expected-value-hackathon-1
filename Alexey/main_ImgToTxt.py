# видеооснова:
# https://www.youtube.com/watch?v=UPjTYorn59g
# описание: решается задача по распознаванию текста с картинки
# из файла XXX.jpg получаем файл XXX.txt
# (нужно для чек-поинт 2)
# проблема: точность распознавания хромает

import pytesseract
from PIL import Image

img = Image.open('X51005230621.jpg')
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, config=custom_config)
print(text)

with open('X51005230621.txt', 'w') as text_file:
    text_file.write(text)

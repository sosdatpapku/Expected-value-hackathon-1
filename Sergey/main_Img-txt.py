# текстовая оновова: 
# Обнаружение и извлечение текста из изображения с помощью Python _ by Roman _ NOP__Nuances of Programming _ Medium
# Задача: Выгрузка текста с IMG в TXT
# Не достаточная точность выгрузки

from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

img = Image.open('X00016469670.jpg')

file_name = img.filename

text = pytesseract.image_to_string(img)
#печать текста построчно
print(text[:-1])

with open(f'{file_name}.txt', 'w') as text_file:
   text_file.write(text)

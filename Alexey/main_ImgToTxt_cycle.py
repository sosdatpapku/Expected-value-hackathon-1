import pytesseract
from PIL import Image
import os

#требуется библиотека pytesseract (работал на windows)
#описание скрипта:
#в папке проекта находится две папки Folder_img и Folder_txt
#в папке Folder_img куча картинок
#скрипт берет из папки Folder_img названия файлов (без 4-х последних символов)
#работает pytesseract
#скрипт записывает в папку Folder_txt названия файлов + .txt
#файлы txt содержат соответственный распознанный текст
#проблема1: работает не быстро (10 файлов за ~10 секунд)
#проблема2: очень долго боролся с тем, что иногда все работает,
#а иногда не работает, победил, когда добавил "encoding='utf-8'",
#но возможно теряются какие-то хитрые символы

custom_config = r'--oem 3 --psm 6'
list1 = os.listdir("Folder_img")

for i in list1:
    str0 = 'Folder_img\\' + i
    img = Image.open(str0)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

    text = pytesseract.image_to_string(img, config=custom_config)

    str1 = i
    str2 = str1[-50:-4]
    str3 = 'Folder_txt\\' + str2 + '.txt'

    #print(str3)
    with open(str3, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

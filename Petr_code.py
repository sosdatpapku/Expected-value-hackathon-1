import re
import cv2
import numpy as np
import pytesseract
from pytesseract import Output
from matplotlib import pyplot as plt
import os
from PIL import Image

def replace_marks(inp_str):
# функция, удаляющая знаки препинания
# возвращает полученную на вход строку без них

    marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_''' # строка с удаляемыми символами
 
    for x in marks:  
        inp_str = inp_str.replace(x, "") # удаление символов

    return(inp_str)



def recognation(filename):  
# функция, распознающая изображение

    image = cv2.imread(path+'\\'+filename) # открытие файла изображения

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # очистка серого
    image = cv2.medianBlur(image,5) # избавление от шумов

    #pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

    text = pytesseract.image_to_string(image) # распознование текста

    # определение и отрисовка координат рамок
    h, w, c = image.shape
    boxes = pytesseract.image_to_boxes(image) 
    for b in boxes.splitlines():
        b = b.split(' ')
        image = cv2.rectangle(image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

    b,g,r = cv2.split(image)
    rgb_img = cv2.merge([r,g,b])

    cv2.imwrite(path2+'\\'+filename, img2) # сохранение файла с рамками в отдельную папку

    return text


### ПАКЕТНОЕ ОТКРЫТИЕ ФАЙЛОВ (поочерёдное)

#path = '\\path\\img'   # задаём путь к папке
path = os.getcwd() + '\\img'  # определяем корневую папку и вложенную в неё папку с изображениями выложена папка с изображениями
path2 = os.getcwd() + '\\img2'  # определяем корневую папку, если в неё выложена папка с изображениями

for filename in os.listdir(path):
    print(filename) # временная печать для проверки кода
    text_check = recognation(filename) # запуск функции преобразования изображения





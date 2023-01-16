# видеооснова:
# https://www.youtube.com/watch?v=6DjFscX4I_c
# описание: решается задача по распознаванию текста с картинки
# используется библиотека OpenCV
# (нужно для чек-поинт 2)
# проблема: точность распознавания хромает
# результат распознования main_ImgToTxt и main_OpenCV_Start отличается

import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
custom_config = r'--oem 3 --psm 6'
img = cv2.imread('X51005230621.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img, config=custom_config))
#print(pytesseract.image_to_boxes(img))
cv2.imshow("Result", img)
cv2.waitKey(0)


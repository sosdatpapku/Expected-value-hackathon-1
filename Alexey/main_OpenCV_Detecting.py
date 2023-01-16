# видеооснова:
# https://www.youtube.com/watch?v=6DjFscX4I_c
# описание: решается задача по сегментации картинки
# используется библиотека OpenCV
# (нужно для чек-поинт 1)
# проблема текущая: распознавание/сегментация выделяет не все
# проблема будущего: есть лишнии колонки, нет требуемых колонок

# важная небольшая задачка: хорошо бы картинку с сегментами сохранять (result)

import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
img = cv2.imread('X51005230605.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))

"""
### Detecting_Characters - сегментация знаков
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    print(b)
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 225), 1)
    #cv2.putText(img, b[0], (x,hImg-y), cv2.FONT_HERSHEY_COMPLEX, 0.1, (50,50,255),2)
"""

### Detecting_Words - сегментация слов
hImg, wImg, _ = img.shape
#cong = r'--oem 3 --psm 6 outputbase digits'
#, config=cong
boxes = pytesseract.image_to_data(img)
print(boxes)
for x, b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        print(b)
        if len(b)==12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 225), 1)
            #cv2.putText(img, b[0], (x,hImg-y), cv2.FONT_HERSHEY_COMPLEX, 0.1, (50,50,255),2)

cv2.imshow("Result", img)
cv2.waitKey(0)

###Создание файла с распознанным текстом
"""text = pytesseract.image_to_string(img, config=cong)
with open('X00016469670.txt', 'w') as text_file:
    text_file.write(text)"""

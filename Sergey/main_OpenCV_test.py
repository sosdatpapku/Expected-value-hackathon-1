# текстовая основова:
# Обнаружение и извлечение текста из изображения с помощью Python _ by Roman _ NOP__Nuances of Programming _ Medium# описание: решается задача по сегментации картинки
# используется библиотека OpenCV
# чек-поинт 1
# цель - обработка/распознавание/сегментация
# результат = релизована автоматическая выгрузка файлов предварительно обработанных файлов:
# 1. rectanglebox.jng - сегментированный файл
# 2. .txt - текстовое содержание сегментов
# 3. threshold_image.jng - результат перевода в бинароное изображение
# 4. dilation_image.jng - результат применение метода расширения двоичного
# изображения для получения границ текста
# проблемы, варианты доработки:
# 1. отладка механизмов сегментирования (границы) и распознавания текста
# 2. проверка на избыточность способов обработки
# 3. проверка работоспособности на расширенной выборке

import cv2
from pytesseract import pytesseract

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

img = cv2.imread("X51005230605.jpg")

# Преобразование "цветного" изображения в полутоновое для лучшей обработки текста
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# преобразование полутонового изображения в бинарное, чтобы повысить вероятность извлечения текста
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU |
                                          cv2.THRESH_BINARY_INV)
cv2.imwrite('threshold_image.jpg',thresh1)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (12, 12))

# применение метода расширения двоичного изображения для получения границ текста
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
cv2.imwrite('dilation_image.jpg',dilation)

contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_NONE)

im2 = img.copy()

#формирование ограничительной рамки и сохранение файлов
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped = im2[y:y + h, x:x + w]
    cv2.imwrite('rectanglebox.jpg', rect)

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped = im2[y:y + h, x:x + w]
    cv2.imwrite('rectanglebox.jpg', rect)
    
    file = open("text_output2.txt", "a")
    text = pytesseract.image_to_string(cropped)

    file.write(text)
    file.write("\n")
    file.close

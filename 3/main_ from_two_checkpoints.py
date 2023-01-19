import cv2
import numpy as np
from pytesseract import pytesseract
from flair.data import Sentence
from flair.models import SequenceTagger

# path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

# # скачиваем модель
tagger = SequenceTagger.load("flair/ner-english-ontonotes-large")

img = cv2.imread("D://Second_tower//Hakaton//SROIE//SROIE2019//test//img//X00016469670.jpg")

# Преобразование "цветного" изображения в полутоновое для лучшей обработки текста
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# преобразование полутонового изображения в бинарное, чтобы повысить вероятность извлечения текста
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU |
                             cv2.THRESH_BINARY_INV)
cv2.imwrite('threshold_image.jpg', thresh1)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (12, 12))

# применение метода расширения двоичного изображения для получения границ текста
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
cv2.imwrite('dilation_image.jpg', dilation)

contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)

im2 = img.copy()

# удаление шума
def noise_removal(image):
        kernel = np.ones((1, 1), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        kernel = np.ones((1, 1), np.uint8)
        image = cv2.erode(image, kernel, iterations=1)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        image = cv2.medianBlur(image, 3)
        return (image)

no_noise = noise_removal(im2)
cv2.imwrite("no_noise.jpg", no_noise)

# формирование ограничительной рамки и сохранение файлов
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped = im2[y:y + h, x:x + w]
    cv2.imwrite('rectanglebox.jpg', rect)

    file1 = open("text1_output1.txt", "a")
    text1 = pytesseract.image_to_string(cropped)

    file1.write(text1)
    file1.write("\n")
    file1.close

# считываем txt-файл
file_1 = open('text1_output1.txt','r')
content = file_1.read()

# используем распознанные текстовые сущности чека как входные данные
sentence = Sentence(content)

# пробуем предсказать теги для наших данных
tagger.predict(sentence)

# выводим полное содержимое файла
print(sentence)

# выводим предсказанные теги для отдельных сущностей
print('The following NER tags are found:')
for entity in sentence.get_spans('ner'):
    print(entity)

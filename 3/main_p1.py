#https://itproger.com/news/raspoznavanie-teksta-s-kartinki-python-tesseract-orc-opencv

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Подключение фото
img = cv2.imread('D://Second_tower//Hakaton//SROIE//SROIE2019//test//img//X00016469670.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#print(pytesseract.image_to_string(img))

config = r'--oem 3 --psm 6'
#print(pytesseract.image_to_string(img, config=config))

data = pytesseract.image_to_data(img, config=config)
for i, el in enumerate(data.splitlines()):
	if i == 0:
		continue

	el = el.split()
	try:
		# Создаем подписи на картинке
		x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
		cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
		cv2.putText(img, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
	except IndexError:
		print("Операция была пропущена")

# Отображаем фото
cv2.imshow('Result', img)
cv2.waitKey(0)

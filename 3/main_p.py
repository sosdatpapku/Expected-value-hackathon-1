#https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/doc/doc_i18n/README_%D0%A0%D1%83%CC%81%D1%81%D1%81%D0%BA%D0%B8%D0%B9_%D1%8F%D0%B7%D1%8B%CC%81%D0%BA.md
#pip3 install paddlepaddle ######### for gpu user please install paddlepaddle-gpu
#pip3 install paddleocr

#понижаем в версии numpy
#python -m pip uninstall numpy
#python -m pip install numpy==1.23.1

#сам код
from paddleocr import PaddleOCR, draw_ocr

ocr = PaddleOCR(use_angle_cls=True, lang='en') #выбираем язык, указыва что определяем угол

img_path = 'img/X00016469612.jpg' #задаём адрес изображения/ий

file_1 = open('txt/write.txt', 'a') #открываем файл для добавления нового содержимого

result = ocr.ocr(img_path,cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)
        file_1.write(str(line)) #записываем числе массива х
        file_1.write('\n')#следующая запись будет с новой строки
file_1.close()

#print(type(line))
#line = str(line)
#z = list(map(lambda x: x.upper(), line))
#print(z)

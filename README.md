# Описание
Данное приложение извлекает текст из изображений, содержащихся в папке.
По результатам поиска по ключевому слову выводится ФИО
лица, на кого была выдана доверенность и название файла.
# Запуск приложения
```console
python main.py --keyword='ключевое слово' -d='папка'
```
# Пример запуска
```console
python main.py --dir=доверенности --keyword=рф
```
# Зависимости
Требуется скачать и установить бинарник [tesseract](https://github.com/tesseract-ocr/tesseract/wiki/Downloads)(программа для извлечения текста из изображения) и установить расширения для русского языка.
# Установка через pip
```console
pip install -r requirments.txt
```
# Установка через pipenv
```console
pipenv install
```
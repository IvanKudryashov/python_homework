'''
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''

import os

f_path = r'C:\Users\1\Desktop\python_homework\homework_1_1.py'


def path_elem(text):
    path, filename = os.path.split(text)
    name, extension = os.path.splitext(filename)
    return path, name, extension


print(path_elem(f_path))

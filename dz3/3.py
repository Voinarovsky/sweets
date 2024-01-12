import pickle
import os
from pympler import asizeof

book = [
    ("Евгений Онегин", "Пушкин А.С.", 200),
    ("Муму", "Тургенев И.с.", 250),
    ("Мастер и Маргарита", "Булгаков М.А.", 500)
]

file = open("out.bin", "wb") #открываем файл в бинарном режиме для записи
pickle.dump(book, file)  #записывает туда объект
file.close()

file_name = "out.bin"
file_size = os.path.getsize(file_name) #модуль с инета что бы посчитать байты
print(f'Файл в байтах весит {file_size}')
print(f'Объект в байтах весит {asizeof.asizeof(book)}')

file = open("out.bin", "rb") #открываем файл для чтения
bs = pickle.load(file) #читаем объект из файла
file.close()
print(bs)
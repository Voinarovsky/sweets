import pickle
import os
from pympler import asizeof

book = [
    ("Евгений Онегин", "Пушкин А.С.", 200),
    ("Муму", "Тургенев И.с.", 250),
    ("Мастер и Маргарита", "Булгаков М.А.", 500)
]

file = open("out.bin", "wb")
pickle.dump(book, file)
file.close()

file_name = "out.bin"
file_size = os.path.getsize(file_name)
print(f'Файл в байтах весит {file_size}')
print(f'Объект в байтах весит {asizeof.asizeof(book)}')

file = open("out.bin", "rb")
bs = pickle.load(file)
file.close()
print(bs)
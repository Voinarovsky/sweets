import pickle
#import os
#from pympler import asizeof

book = [
    ("Евгений Онегин", "Пушкин А.С.", 200),
    ("Муму", "Тургенев И.с.", 250),
    ("Мастер и Маргарита", "Булгаков М.А.", 500)
]
def compress():
    import pickle
    def encode(obj: dict | list, file):
        file = open(file, "wb") #открываем файл в бинарном режиме для записи
        pickle.dump(obj, file)  #записывает туда объект
        file.close()

    def decode(file):
        file = open(file, "rb") #открываем файл для чтения
        bs = pickle.load(file) #читаем объект из файла
        file.close()
        return bs

    return encode, decode

print
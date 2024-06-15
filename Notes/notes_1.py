from notes_4 import TradingBotApp

# Создание экземпляра класса TradingBotApp
my_object = TradingBotApp()

def test():
    # Вызов метода win_tkinter и получение значения b_value
    b_value = my_object.win_tkinter()

    # Печать значения b_value
    print(b_value)

# Вызов функции test
test()



import tkinter as tk

class TradingBotApp:
    def __init__(self):
        self.b_value = None
        self.win = None  # Ссылка на окно

    def win_tkinter(self):
        if self.win is None:  # Проверяем, что окно еще не создано
            self.win = tk.Tk()
            self.win.config(bg='#e7e7de')
            self.win.title('Трейдинг бот')
            self.win.geometry('500x600+100+200')
            self.win.resizable(False, False)

            def get_entry_b():
                b_value = b.get()
                if b_value:
                    self.b_value = b_value
                    self.win.destroy()  # Закрываем окно после получения значения
                else:
                    self.b_value = 2

            tk.Label(self.win, text='Плечо').grid(row=2, column=0, sticky='e')
            b = tk.Entry(self.win)
            b.grid(row=2, column=1)
            tk.Button(self.win, text='Отправить', command=get_entry_b).grid(row=3, column=0)

            self.win.mainloop()  # Запускаем главный цикл окна

        return self.b_value

    def get_b_value(self):
        return self.b_value


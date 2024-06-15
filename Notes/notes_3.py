import tkinter as tk
from tkinter import ttk

class TradingBotApp:
    def __init__(self):
        self.leverage_value = None
        self.Fastsma_value = None
        self.slow_smm_value = None
        self.inst_value = None
        self.risk_value = None
        self.trade_type_value = None
        self.selection_value = None
        self.win = None  # Ссылка на окно

    def win_tkinter(self):
        if self.win is None:  # Проверяем, что окно еще не создано
            # организационные и кастомные моменты
            self.win = tk.Tk()
            self.win.config(bg='#2D384A')
            self.win.title('Трейдинг бот')
            self.win.geometry('552x450')
            self.win.resizable(False, False)

            def get_entry():  # фиксирование введеных значений с помощью метода get
                self.Fastsma_value = Fastsma.get()
                self.leverage_value = leverage.get()
                self.slow_smm_value = slow_smm.get()
                self.inst_value = inst.get()
                self.risk_value = risk.get()
                self.trade_type_value = trade_type.get()
                self.selection_value = combobox.get()
                self.win.destroy()  # Закрываем окно после получения значения

            # поля для ввода (опционально красиво их убрать в класс или функцию хз)
            tk.Label(self.win, text='Трейдинг бот', font="Sans 20", bg="#485b7a", fg="#160150").grid(row=0, column=0, columnspan=5, sticky='we')

            tk.Label(self.win, text='Плечо:', bg="#485b7a", fg="#160150").grid(row=1, column=0, sticky='e')
            leverage = tk.Entry(self.win)
            leverage.grid(row=1, column=1, padx=20, pady=30)

            tk.Label(self.win, text='Fastsma:', bg="#485b7a", fg="#160150").grid(row=1, column=2, sticky='e')
            Fastsma = tk.Entry(self.win)
            Fastsma.grid(row=1, column=3, padx=20, pady=30)

            tk.Label(self.win, text='Slow smm:', bg="#485b7a", fg="#160150").grid(row=2, column=0, sticky='e')
            slow_smm = tk.Entry(self.win)  # Используем уникальное имя переменной
            slow_smm.grid(row=2, column=1, padx=20, pady=30)

            tk.Label(self.win, text='Inst:', bg="#485b7a", fg="#160150").grid(row=2, column=2, sticky='e')
            inst = tk.Entry(self.win)  # Используем уникальное имя переменной
            inst.grid(row=2, column=3, padx=20, pady=30)

            tk.Label(self.win, text='Риск:', bg="#485b7a", fg="#160150").grid(row=3, column=0, sticky='e')
            risk = tk.Entry(self.win)  # Используем уникальное имя переменной
            risk.grid(row=3, column=1, padx=20, pady=30)

            choice_list = ['1s', '1m', '3m', '5m', '15m', '30m', '1H', '4H']
            tk.Label(self.win, text='Таймфрейм:', bg="#485b7a", fg="#160150").grid(row=3, column=2, sticky='e')
            combobox = ttk.Combobox(self.win, values=choice_list)
            combobox.grid(row=3, column=3, padx=20, pady=30)

            tk.Label(self.win, text='Тип контракта:', font="Sans 13", bg="#2D384A", fg="#160150").grid(row=4, column=0, columnspan=4, sticky='we')

            trade_type = tk.StringVar(value="Спот")
            spot = tk.Radiobutton(self.win, text="Спот", variable=trade_type, value="Спот", bg="#485b7a", fg="#160150")
            spot.grid(row=5, column=1, sticky='e', padx=15, pady=10)
            future = tk.Radiobutton(self.win, text="Фьючер", variable=trade_type, value="Фьючер", bg="#485b7a", fg="#160150")
            future.grid(row=5, column=2, sticky='w', padx=15, pady=10)

            # кнопка по которой все значения отправляются
            tk.Button(self.win, text='Отправить', command=get_entry, font="Sans 11", relief='flat', overrelief='raise', bg="#344756", fg="#160150").grid(row=6, column=0, columnspan=4, sticky='we', padx=40, pady=40, ipadx=10, ipady=10)

            self.win.grid_columnconfigure(0, minsize=100)

            self.win.mainloop()  # Запускаем главный цикл окна

        return [self.leverage_value, self.Fastsma_value, self.slow_smm_value, self.inst_value, self.risk_value, self.trade_type_value, self.selection_value]

    def get_b_value(self):
        return [self.leverage_value, self.Fastsma_value, self.slow_smm_value, self.inst_value, self.risk_value, self.trade_type_value, self.selection_value]

# для отладки и вывода в финальной версии убрать
if __name__ == '__main__':
    app = TradingBotApp()
    answer = app.win_tkinter()
    print(answer)

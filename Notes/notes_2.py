import tkinter as tk

def win_tkinter():
    win = tk.Tk()
    win.config(bg='#e7e7de')
    win.title('Трейдинг бот')
    win.geometry('500x600+100+200')
    win.resizable(False, False)

    def get_entry_b():
        b_value = b.get()
        if b_value:
            return b_value
        else:
            b_value = 2
            return b_value


    b = tk.Label(win, text='Плечо').grid(row=2,column=0,sticky='e')
    b = tk.Entry(win)
    b.grid(row=2,column=1)
    tk.Button(win, text='Отправить', command=get_entry_b).grid(row=3,column=0)


    win.mainloop()



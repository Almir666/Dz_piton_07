import tkinter as tk                        # from tkinter import * Можно еще так

root = tk.Tk()  # .Tk создает окно

frame = tk.Frame(master=root, width=500, height=300)

border_effects = {"Frame style": tk.SUNKEN}
for relief_name, relief in border_effects.items():
    frame = tk.Frame(master = root, relief = relief, borderwidth = 5)
    frame.pack(side = tk.LEFT)
    label = tk.Label(master = frame, text = relief_name)
    

title = tk.Label(text='Python рулит!',  # .Label(text= '') отображает текст на окне
                 fg="yellow",                # цвет текста foreground
                 bg="#34A2FE",               # цвет фона   background
                 width=100,                  # ширина окна
                 height=10)                  # высота окна

button = tk.Button(text="Нажми на меня, сенпай!",   # кнопка
                   width=25,
                   height=5,
                   bg="#34A2FE",
                   fg="yellow",)


entry = tk.Entry(fg="yellow", bg="#34A2FE", width=50)  # текстовое поле # методы: .get() .delete() .inseet()
text = entry.get()

# текстовый виджет, на вид такой же как Entry
text_box = tk.Text(width=37, height=1)


label.pack()
frame.pack()
text_box.pack()
entry.pack()
button.pack()
title.pack()  # .pack() что бы окно работало
tk.mainloop()  # .mainloop() что бы все работало в общем так же можно input()

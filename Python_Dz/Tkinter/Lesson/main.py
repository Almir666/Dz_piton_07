from tkinter import *
 
root = Tk()
root.geometry('1000x600')
root.title("Сотрудники предприятия")
 
# frm_form = Frame(master= root, relief= SUNKEN, borderwidth= 3, width=1000, height=100)
# frm_form.pack()
 
lbl_first_name = Label( text="Имя")
lbl_first_name.grid(row=0, column=0, sticky="n")

# lbl_last_name = Label( text="Фамилия                 ")
# lbl_last_name.grid(row=0, column=1, sticky="n")

# lbl_last_name = Label( text="Телефон                                ")
# lbl_last_name.grid(row=0, column=2, sticky="n")


# lbl_last_name = Label( text="Пол    ")
# lbl_last_name.grid(row=0, column=3, sticky="n")

# lbl_last_name = Label( text="Должность                  ")
# lbl_last_name.grid(row=0, column=4, sticky="n")

# lbl_last_name = Label( text="Зарплата          ")
# lbl_last_name.grid(row=0, column=5, sticky="n")

# frm_data = Frame()
# frm_data.pack(fill=X, ipadx=5, ipady=250)

# entry = Entry(master=frm_data, width=100)
# entry.grid(row=0, column=6, sticky="s")


mainloop()
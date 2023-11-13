import random
import string

from tkinter import *

letters = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)

all_chars = letters + digits + symbols

generator = Tk()

generator.title("Неограниченный генератор пароля")
generator.geometry('250x350')

msymbols_text = Label(generator, text="Максимальный размер")
msymbols_text.grid(column=0, row=0)
msymbols_text.place(relx=0.5, rely=0.2, anchor="center")

max_symbols = Entry(generator, width=10)
max_symbols.grid(column=1, row=0)
max_symbols.place(relx=0.5, rely=0.3, anchor="center")

lpassword = Label(generator, text="Пароль:")
lpassword.grid(column=0, row=0)
lpassword.place(relx=0.15, rely=0.5, anchor="center")


fpassword = Entry(generator, width=20)
fpassword.grid(column=1, row=2)
fpassword.place(relx=0.5, rely=0.5, anchor="center")

def generate():
    if max_symbols.get().isdigit() == True:
        max = int(max_symbols.get())
        password = ""
        for i in range(max):
            password += random.choice(all_chars)
        fpassword.delete(0, 'end')
        fpassword.insert(0, password)
    else:
        fpassword.delete(0, 'end')
        fpassword.insert(0, "Неверный ввод")

generatebtn = Button(generator, text="Сгенерировать пароль", command=generate)
generatebtn.grid(column=2, row=1)
generatebtn.place(relx=0.5, rely=0.4, anchor="center")


generator.mainloop()

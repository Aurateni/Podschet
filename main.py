import tkinter
from tkinter import *
from tkinter import Menu
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """Открывает файл для редактирования"""
    filepath = askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tkinter.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        words = text.split()
        txt_edit.insert(tkinter.END, text, print(len(words)))
        txt_edit.insert(tkinter.END, '   В этом файле: ' + str(len(words)) + ' слова')
    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    """Сохраняем текущий файл как новый файл."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tkinter.END)
        output_file.write(text)
    window.title(f"Подсчёт слов - {filepath}")


window = Tk()
window.title("Подсчёт слов")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tkinter.Text(window)
fr_buttons = tkinter.Frame(window)
btn_open = tkinter.Button(fr_buttons, text='Открыть', command=open_file)
btn_save = tkinter.Button(fr_buttons, text='Сохранить как...', command=save_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Новый', command=open_file)
new_item.add_command(label='Сохранить как...', command=save_file)
menu.add_cascade(label='Файл', menu=new_item)

window.config(menu=menu)
window.mainloop()

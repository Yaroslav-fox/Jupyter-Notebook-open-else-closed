# Библиотеки
import tkinter as tk
import os
import subprocess

# Функция для запуска Jupyter Notebook
def open_jupyter():
    os.system("start cmd /k jupyter notebook")  # Запускаем Jupyter Notebook через командную строку
    root.destroy()  # Закрываем диалоговое окно

# Функция для закрытия Jupyter Notebook
def close_jupyter():
    os.system("taskkill /f /im cmd.exe")  # Закрываем командную строку
    os.system("taskkill /f /im jupyter-notebook.exe")  # Закрываем Jupyter Notebook
    root.destroy()  # Закрываем диалоговое окно

# Экземпляр Tkinter
root = tk.Tk()
root.title("Jupyter Notebook")  # Заголовок окна
root.geometry("300x200")  # Размер окна
root.eval('tk::PlaceWindow . center')  # Размещения окна в центре экрана

# Создаем фрейм в окне
frame = tk.Frame(root)
frame.pack(expand=True)  # Фрейм в центре окна

# Создаем кнопку "Открыть"
button = tk.Button(frame, 
                   text="Открыть", 
                   fg="green",
                   command=open_jupyter)  # При нажатии на кнопку вызывается функция open_jupyter
button.pack(side=tk.LEFT, expand=True)  # Кнопка в центре фрейма

# Создаем кнопку "Закрыть"
slogan = tk.Button(frame,
                   text="Закрыть",
                   fg="red",
                   command=close_jupyter)  # При нажатии на кнопку вызывается функция close_jupyter
slogan.pack(side=tk.LEFT, expand=True)  # Кнопка в центре фрейма

# Запуск цикла Tkinter
root.mainloop()

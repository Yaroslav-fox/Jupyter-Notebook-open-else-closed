import tkinter as tk
import os
import subprocess

def open_jupyter():
    os.system("start cmd /k jupyter notebook")
    root.destroy()

def close_jupyter():
    os.system("taskkill /f /im cmd.exe")
    os.system("taskkill /f /im jupyter-notebook.exe")
    root.destroy()  

root = tk.Tk()
root.title("Jupyter Notebook")
root.geometry("300x200")
root.eval('tk::PlaceWindow . center')

frame = tk.Frame(root)
frame.pack(expand=True)

button = tk.Button(frame, 
                   text="Открыть", 
                   fg="green",
                   command=open_jupyter)
button.pack(side=tk.LEFT, expand=True)

slogan = tk.Button(frame,
                   text="Закрыть",
                   fg="red",
                   command=close_jupyter)
slogan.pack(side=tk.LEFT, expand=True)

root.mainloop()

from Presentation import Presentation
from tkinter import messagebox

presentation = Presentation()
try:
    presentation.createWindow()
except Exception as ex:
    messagebox.showerror('Error', ex.args)
    
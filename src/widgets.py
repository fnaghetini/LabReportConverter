from tkinter import *


def create_title_label(root, text=""):
    font = ('Tahoma', '12', 'bold')
    return Label(root, text=text, width=47, height=2, bg='#c80021', fg='white', font=font)


def create_app_version_label(root, text=""):
    font = ('Tahoma', '9')
    return Label(root, text=text, font=font, bg='white', fg='#6F787B', justify=RIGHT, anchor='e')

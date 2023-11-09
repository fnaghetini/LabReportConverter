from tkinter import *


def create_title_label(root, text=None):
    return Label(root, text=text, width=47, height=2, bg='#c80021', fg='white', font=('Tahoma', '12', 'bold'))


def create_parameter_label(root, text=None):
    return Label(root, text=text, width=30, bg='white', fg='black', justify=LEFT, anchor='w', padx=10)


def create_parameter_picklist(root, pkl_var, pkl_options):
    pkl_report_type = OptionMenu(root, pkl_var, *pkl_options)
    pkl_report_type.config(height=1, width=34, bg='white', highlightcolor='white', highlightbackground='white')
    return pkl_report_type


def create_button(root, btn_function, text=None):
    return Button(root, text=text, width=20, height=2, justify=CENTER, cursor='hand2', font=('Tahoma', '9', 'bold'),
                  bg='#f4f4f4', fg='black', command=btn_function)


def create_app_version_label(root, text=None):
    return Label(root, text=text, font=('Tahoma', '9'), bg='white', fg='#6F787B', justify=RIGHT, anchor='e')

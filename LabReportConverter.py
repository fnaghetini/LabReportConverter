from src.constants import *
from src.widgets import *
from src.button import generate_lab_report_template
import warnings

warnings.filterwarnings("ignore")

root = Tk()
root.title("Lundin Mining - Geologia")
root.geometry("488x270")
root.configure(background='white')

######################################################################################
# ------------------------------ Definição dos Widgets ----------------------------- #
######################################################################################

txt_title = create_title_label(root, text="Conversor de Laudos de Laboratório")

txt_report_type = Label(root, text="Tipo do(s) Laudo(s):", width=30, bg='white', fg='black', justify=LEFT, anchor='w',
                        padx=10)
report_type_var = StringVar(root)
report_type_var.set("Químico")
pkl_report_type = OptionMenu(root, report_type_var, *LAB_REPORT_TYPES)
pkl_report_type.config(height=1, width=34, bg='white', highlightcolor='white', highlightbackground='white')

btn_generate_lab_report_template = Button(root, text="Converter Laudo(s)", width=20, height=2, justify=CENTER,
                                          cursor='hand2', font=('Tahoma', '9', 'bold'), bg='#f4f4f4', fg='black',
                                          command=lambda: generate_lab_report_template(report_type_var)
                                          )

txt_version = create_app_version_label(root, text="@Datamine Software v0.0.1")

######################################################################################
# ------------------------------- Posição dos Widgets ------------------------------ #
######################################################################################

txt_title.grid(row=0, column=0, columnspan=2, pady=30)
txt_report_type.grid(row=1, column=0, pady=10, sticky=W)
pkl_report_type.grid(row=1, column=1)
btn_generate_lab_report_template.grid(row=2, column=0, columnspan=2, pady=30)
txt_version.grid(row=3, column=1, sticky=E)

root.mainloop()

from src.constants import *
from src.widgets import *
from src.button import generate_lab_report
import warnings

warnings.filterwarnings("ignore")

root = Tk()
root.title("Lundin Mining - Geologia")
root.geometry("488x250")
root.configure(background='white')

######################################################################################
# ----------------------------------- Set Widgets ---------------------------------- #
######################################################################################

txt_title = create_title_label(root, text="Conversor de Laudos de Laboratório")

txt_report_type = create_parameter_label(root, text="Tipo de Laudo:")
report_type_var = StringVar(root)
report_type_var.set("Químico")
pkl_report_type = create_parameter_picklist(root, report_type_var, LAB_REPORT_TYPES)

btn_generate_lab_report = create_button(root, lambda: generate_lab_report(report_type_var), text="Converter Laudo(s)")

txt_version = create_app_version_label(root, text="@Datamine Software v0.0.1")

######################################################################################
# -------------------------------- Widget Positions -------------------------------- #
######################################################################################

txt_title.grid(row=0, column=0, columnspan=2, pady=30)
txt_report_type.grid(row=1, column=0, pady=10, sticky=W)
pkl_report_type.grid(row=1, column=1)
btn_generate_lab_report.grid(row=2, column=0, columnspan=2, pady=20)
txt_version.grid(row=3, column=1, sticky=E)

root.mainloop()

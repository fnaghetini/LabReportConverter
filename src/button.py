from tkinter import messagebox
import pandas as pd
from src.constants import *
from src.file_io import __select_directory, __get_input_files_list, __read_xls, __save_as_csv
from src.table_builder import __build_report_header, __build_method_unit_table, __build_table_values


def generate_lab_report(report_type):
    folder_path = __select_directory()
    xls_input_files = __get_input_files_list(folder_path)

    if len(xls_input_files) == 0:
        messagebox.showerror('Erro', f"Não há nenhum arquivo .xls na pasta {folder_path}.")
        return

    for file in xls_input_files:
        raw_report = __read_xls(file)
        df_report_header = __build_report_header(raw_report, report_type.get())
        df_method_unit_table = __build_method_unit_table(report_type.get())
        df_table_values = __build_table_values(raw_report, report_type.get())
        final_template = pd.concat([df_report_header, df_method_unit_table, df_table_values])
        __save_as_csv(final_template, file[:-4] + OUTPUT_SUFFIX)

    messagebox.showinfo('Processo Concluído', f'Template(s) Fusion gerado(s) com sucesso na pasta {folder_path}.')

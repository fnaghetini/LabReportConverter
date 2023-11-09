import ntpath
from tkinter.filedialog import askdirectory
from glob import glob
import xlrd


def __get_path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def __select_directory():
    folderpath = askdirectory(initialdir='/', title='Selecione uma pasta que tenha apenas laudos do tipo selecionado')
    return folderpath


def __get_input_files_list(folder_path):
    return [f.replace('\\', '/') for f in glob(f"{folder_path}/*.xls")]


def __read_xls(file):
    return xlrd.open_workbook(file).sheet_by_index(0)


def __save_as_csv(table, path):
    return table.to_csv(path, index=False, header=False)

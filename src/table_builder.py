import numpy as np
import pandas as pd
from src.constants import *
from src.data_gathering import __get_dispatch_number, __get_number_of_samples, __get_sample_type_values
from src.data_gathering import __get_date_received, __get_date_finalized
from src.data_gathering import __get_column_values


def __clean_values_table(table, report_type):
    table_values_without_nan = table.loc[table['SAMPLE_TYPE'] != 'DROP'].replace('*', np.nan)
    table_values_reshaped = table_values_without_nan.reset_index().T.reset_index().T.iloc[:, 1:]
    if report_type == 'Químico':
        table_values_reshaped.columns = list(range(len(CHEMISTRY_REPORT_COLUMNS)))
    elif report_type in ['Umidade', 'Densidade']:
        table_values_reshaped.columns = list(range(len(UMIDITY_REPORT_COLUMNS)))
    return table_values_reshaped


def __build_report_header(raw_report, report_type):
    report_header_values = [__get_dispatch_number(raw_report), CLIENT, __get_number_of_samples(raw_report),
                            __get_date_received(raw_report), __get_date_finalized(raw_report, report_type),
                            PROJECT, np.nan, __get_dispatch_number(raw_report)]
    return pd.DataFrame([REPORT_HEADER_KEYS, report_header_values]).transpose()


def __build_method_unit_table(report_type):
    if report_type == 'Químico':
        return pd.DataFrame([CHEMISTRY_REPORT_METHODS, CHEMISTRY_REPORT_UNITS])
    elif report_type == 'Umidade':
        return pd.DataFrame([UMIDITY_REPORT_METHODS, UMIDITY_REPORT_UNITS])
    elif report_type == 'Densidade':
        return pd.DataFrame([DENSITY_REPORT_METHODS, DENSITY_REPORT_UNITS])


def __build_table_values(raw_report, report_type):
    if report_type == 'Químico':
        raw_table = {CHEMISTRY_REPORT_COLUMNS[0]: __get_column_values(raw_report, SAMPLE_COL_IDX),
                     CHEMISTRY_REPORT_COLUMNS[1]: __get_sample_type_values(raw_report),
                     CHEMISTRY_REPORT_COLUMNS[2]: __get_column_values(raw_report, AU_COL_IDX),
                     CHEMISTRY_REPORT_COLUMNS[3]: __get_column_values(raw_report, CU_COL_IDX),
                     CHEMISTRY_REPORT_COLUMNS[4]: __get_column_values(raw_report, S_COL_IDX),
                     CHEMISTRY_REPORT_COLUMNS[5]: __get_column_values(raw_report, FE_COL_IDX),
                     CHEMISTRY_REPORT_COLUMNS[6]: __get_column_values(raw_report, PB_COL_IDX),
                     CHEMISTRY_REPORT_COLUMNS[7]: __get_column_values(raw_report, ZN_COL_IDX),
                     CHEMISTRY_REPORT_COLUMNS[8]: __get_column_values(raw_report, AG_COL_IDX),
                     CHEMISTRY_REPORT_COLUMNS[9]: __get_column_values(raw_report, WEIGHT_COL_IDX)}
    elif report_type == 'Umidade':
        raw_table = {UMIDITY_REPORT_COLUMNS[0]: __get_column_values(raw_report, SAMPLE_COL_IDX),
                     UMIDITY_REPORT_COLUMNS[1]: __get_sample_type_values(raw_report),
                     UMIDITY_REPORT_COLUMNS[2]: __get_column_values(raw_report, UMIDITY_COL_IDX)}
    elif report_type == 'Densidade':
        raw_table = {DENSITY_REPORT_COLUMNS[0]: __get_column_values(raw_report, SAMPLE_COL_IDX),
                     DENSITY_REPORT_COLUMNS[1]: __get_sample_type_values(raw_report),
                     DENSITY_REPORT_COLUMNS[2]: __get_column_values(raw_report, DENSITY_COL_IDX)}
    df_table_values = pd.DataFrame.from_dict(raw_table)
    return __clean_values_table(df_table_values, report_type)

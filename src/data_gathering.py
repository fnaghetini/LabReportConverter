from datetime import datetime
import xlrd
from src.constants import *


def __clean_date_value(value, workbook):
    if type(value) == float:
        date_value = datetime(*xlrd.xldate_as_tuple(value, workbook.datemode))
        return date_value.strftime('%d/%m/%Y')
    else:
        return value


def __replace_blank_by_star(values):
    if '' in values:
        return list(map(lambda x: x.replace('', '*'), values))
    if ' ' in values:
        return list(map(lambda x: x.replace(' ', '*'), values))
    else:
        return values


def __is_a_template_sample(sample):
    if sample in ('*', '', ' '):
        return False
    elif 'MR' in sample or 'CHKCAL' in sample:
        return False
    elif 'BRANCO' in sample:
        return False
    else:
        return True


def __get_last_sample_row_idx(report_sheet):
    all_samples = report_sheet.col_values(FIRST_VALUE_LOC[1], start_rowx=FIRST_VALUE_LOC[0],
                                          end_rowx=MAX_LAST_VALUE_LOC[0])
    all_samples = __replace_blank_by_star(all_samples)
    if '*' in all_samples:
        return int(all_samples.index('*') + FIRST_VALUE_LOC[0])
    else:
        return MAX_LAST_VALUE_LOC[0]


def __get_number_of_samples(report_sheet):
    all_samples = report_sheet.col_values(FIRST_VALUE_LOC[1], start_rowx=FIRST_VALUE_LOC[0],
                                          end_rowx=MAX_LAST_VALUE_LOC[0])
    all_samples = __replace_blank_by_star(all_samples)
    final_samples = [sample for sample in all_samples if __is_a_template_sample(sample)]
    return str(len(final_samples))


def __get_dispatch_number(report_sheet):
    dispatch_number = report_sheet.cell(*DISPATCH_NUMBER_LOC).value
    if type(dispatch_number) == float:
        return str(int(dispatch_number))
    else:
        return str(dispatch_number)


def __get_date_received(report_workbook, report_sheet):
    date_received = report_sheet.cell_value(*DATE_RECEIVED_LOC)
    return __clean_date_value(date_received, report_workbook)


def __get_date_finalized(report_workbook, report_sheet, report_type):
    if report_type == 'Químico':
        date_finalized = report_sheet.cell_value(*CHEMISTRY_DATE_FINALIZED_LOC)
        return __clean_date_value(date_finalized, report_workbook)
    elif report_type == 'Umidade':
        date_finalized = report_sheet.cell_value(*UMIDITY_DATE_FINALIZED_LOC)
        return __clean_date_value(date_finalized, report_workbook)
    elif report_type == 'Densidade':
        date_finalized = report_sheet.cell_value(*DENSITY_DATE_FINALIZED_LOC)
        return __clean_date_value(date_finalized, report_workbook)


def __get_column_values(report_sheet, col_idx):
    last_row_idx = __get_last_sample_row_idx(report_sheet)
    raw_values = report_sheet.col_values(col_idx, start_rowx=FIRST_VALUE_LOC[0], end_rowx=last_row_idx)
    return raw_values


def __get_sample_type_values(report_sheet):
    sample_types = []
    samples = __get_column_values(report_sheet, SAMPLE_COL_IDX)
    for sample in samples:
        if sample in ('*', '', ' '):
            sample_types.append('DROP')
        elif 'DF' in sample:
            sample_types.append('P')
        elif 'DQ' in sample:
            sample_types.append('D')
        elif 'UMID' in sample:
            sample_types.append('H')
        elif 'DENS' in sample:
            sample_types.append('DE')
        elif 'CHKCAL' in sample or 'MR' in sample or 'BRANCO' in sample:
            sample_types.append('DROP')
        else:
            sample_types.append('A')
    return sample_types


def __get_sample_number_values(report_sheet):
    sample_numbers = []
    samples = __get_column_values(report_sheet, SAMPLE_COL_IDX)
    for sample in samples:
        if 'DF' in sample:
            sample_numbers.append(sample[:-6])
        elif 'DQ' in sample:
            sample_numbers.append(sample[:-4])
        else:
            sample_numbers.append(sample)
    return sample_numbers

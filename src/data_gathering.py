from src.constants import *


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


def __get_last_sample_row_idx(raw_report):
    all_samples = raw_report.col_values(FIRST_VALUE_LOC[1], start_rowx=FIRST_VALUE_LOC[0],
                                        end_rowx=MAX_LAST_VALUE_LOC[0])
    all_samples = __replace_blank_by_star(all_samples)
    if '*' in all_samples:
        return int(all_samples.index('*') + FIRST_VALUE_LOC[0])
    else:
        return MAX_LAST_VALUE_LOC[0]


def __get_number_of_samples(raw_report):
    all_samples = raw_report.col_values(FIRST_VALUE_LOC[1], start_rowx=FIRST_VALUE_LOC[0],
                                        end_rowx=MAX_LAST_VALUE_LOC[0])
    all_samples = __replace_blank_by_star(all_samples)
    final_samples = [sample for sample in all_samples if __is_a_template_sample(sample)]
    return str(len(final_samples))


def __get_dispatch_number(raw_report):
    dispatch_number = raw_report.cell(*DISPATCH_NUMBER_LOC).value
    if type(dispatch_number) == float:
        return str(int(dispatch_number))
    else:
        return str(dispatch_number)


def __get_date_received(raw_report):
    date_received = raw_report.cell(*DATE_RECEIVED_LOC).value
    return date_received


def __get_date_finalized(raw_report, report_type):
    if report_type == 'Químico':
        return raw_report.cell(*CHEMISTRY_DATE_FINALIZED_LOC).value
    elif report_type == 'Umidade':
        return raw_report.cell(*UMIDITY_DATE_FINALIZED_LOC).value
    elif report_type == 'Densidade':
        return raw_report.cell(*DENSITY_DATE_FINALIZED_LOC).value


def __get_column_values(raw_report, col_idx):
    last_row_idx = __get_last_sample_row_idx(raw_report)
    raw_values = raw_report.col_values(col_idx, start_rowx=FIRST_VALUE_LOC[0], end_rowx=last_row_idx)
    return raw_values


def __get_sample_type_values(raw_report):
    sample_types = []
    samples = __get_column_values(raw_report, SAMPLE_COL_IDX)
    for sample in samples:
        if sample in ('*', '', ' '):
            sample_types.append('DROP')
        elif 'DF' in sample:
            sample_types.append('D')
        elif 'DQ' in sample:
            sample_types.append('P')
        elif 'UMID' in sample:
            sample_types.append('H')
        elif 'DENS' in sample:
            sample_types.append('DE')
        elif 'CHKCAL' in sample or 'MR' in sample or 'BRANCO' in sample:
            sample_types.append('DROP')
        else:
            sample_types.append('A')
    return sample_types

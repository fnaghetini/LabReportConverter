

# Lab report types
LAB_REPORT_TYPES = ['Químico', 'Umidade', 'Densidade']

# Important postions
FIRST_VALUE_LOC = (21, 0)
MAX_LAST_VALUE_LOC = (100, 0)

DISPATCH_NUMBER_LOC = (18, 8)
DATE_RECEIVED_LOC = (18, 1)
CHEMISTRY_DATE_FINALIZED_LOC = (9, 5)
UMIDITY_DATE_FINALIZED_LOC = (16, 5)
DENSITY_DATE_FINALIZED_LOC = (17, 5)

# Important indexes
SAMPLE_COL_IDX = 0
AU_COL_IDX = 1
CU_COL_IDX = 2
S_COL_IDX = 3
FE_COL_IDX = 4
PB_COL_IDX = 5
ZN_COL_IDX = 6
AG_COL_IDX = 7
UMIDITY_COL_IDX = 8
DENSITY_COL_IDX = 9
WEIGHT_COL_IDX = 10

# Report header
REPORT_HEADER_KEYS = ['LAB JOB NUMBER', 'CLIENT', 'NUMBER OF SAMPLES', 'DATE RECEIVED', 'DATE FINALIZED',
                      'PROJECT', 'CERTIFICATE COMMENTS', 'DISPATCH REPORT']
CLIENT = 'Geologia'
PROJECT = 'PROJETO CHAPADA'

# Chemistry reports
CHEMISTRY_REPORT_METHODS = ['METHOD CODE', '', 'FAAAS', 'AAS', 'LECO', 'AAS', 'AAS', 'AAS', 'AAS', 'WEIGHT']
CHEMISTRY_REPORT_UNITS = ['UNIT', '', 'g/t', '%', '%', '%', '%', '%', 'g/t', 'kg']
CHEMISTRY_REPORT_COLUMNS = ['SAMPLE', 'SAMPLE_TYPE', 'Au', 'Cu', 'S', 'Fe', 'Pb', 'Zn', 'Ag', 'Peso']

# Umidity reports
UMIDITY_REPORT_METHODS = ['METHOD CODE', '', 'LAB']
UMIDITY_REPORT_UNITS = ['UNIT', '', '%']
UMIDITY_REPORT_COLUMNS = ['SAMPLE', 'SAMPLE_TYPE', 'Umidade']

# Density reports
DENSITY_REPORT_METHODS = ['METHOD CODE', '', 'LAB']
DENSITY_REPORT_UNITS = ['UNIT', '', 'g/cm3']
DENSITY_REPORT_COLUMNS = ['SAMPLE', 'SAMPLE_TYPE', 'Densidade']

# Output suffix
OUTPUT_SUFFIX = '_Fusion_Template.csv'

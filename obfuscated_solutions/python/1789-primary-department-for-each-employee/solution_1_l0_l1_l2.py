import pandas as pd

def v1_754(v2_214: v3_125.v4_859) -> v3_125.v4_859:
    v2_214['EmployeeCount'] = v2_214.v5_381('employee_id')['employee_id'].v6_350('size')
    v7_328 = v2_214[(v2_214['EmployeeCount'] == 1) | (v2_214['primary_flag'] == 'Y')][['employee_id', 'department_id']]
    return v7_328
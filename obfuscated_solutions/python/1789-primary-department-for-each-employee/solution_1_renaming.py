import pandas as pd


def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:
    arg_ihhe['EmployeeCount'] = arg_ihhe.groupby('employee_id')['employee_id'
        ].transform('size')
    var_rcsn = arg_ihhe[(arg_ihhe['EmployeeCount'] == 1) | (arg_ihhe[
        'primary_flag'] == 'Y')][['employee_id', 'department_id']]
    return var_rcsn

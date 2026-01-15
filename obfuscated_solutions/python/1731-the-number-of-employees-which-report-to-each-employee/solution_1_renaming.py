import pandas as pd


def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:
    var_rcsn = arg_ihhe.groupby('reports_to', as_index=False).agg(reports_count
        =('employee_id', 'size'), average_age=('age', 'mean'))
    var_rcsn['average_age'] = (var_rcsn['average_age'] + 1e-12).round(0)
    var_bacg = var_rcsn.merge(arg_ihhe[['employee_id', 'name']], how='left',
        left_on='reports_to', right_on='employee_id')
    var_bacg.rename(columns={'employee_id_y': 'employee_id'}, inplace=True)
    var_hqta = var_bacg[['employee_id', 'name', 'reports_count', 'average_age']
        ]
    return var_hqta

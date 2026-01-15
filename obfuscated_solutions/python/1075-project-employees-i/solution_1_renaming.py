import pandas as pd


def func_udax(arg_ihhe: var_rcsn.DataFrame, arg_xdvx: var_rcsn.DataFrame
    ) ->var_rcsn.DataFrame:
    var_bacg = arg_ihhe.merge(arg_xdvx, on='employee_id')
    var_bacg = var_bacg.groupby('project_id', as_index=False)[
        'experience_years'].mean()
    return var_bacg.rename(columns={'experience_years': 'average_years'}
        ).round(2)

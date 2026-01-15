import pandas as pd


def func_udax(arg_ihhe: var_rcsn.DataFrame, arg_xdvx: var_rcsn.DataFrame
    ) ->var_rcsn.DataFrame:
    var_bacg = var_rcsn.merge(arg_ihhe, arg_xdvx, on='employee_id', how='outer'
        )
    var_hqta = var_bacg[var_bacg.isna().any(axis=1)]
    var_rgwu = var_hqta[['employee_id']].sort_values(by='employee_id')
    return var_rgwu

import pandas as pd


def func_udax(arg_ihhe: var_rcsn.DataFrame, arg_xdvx: var_rcsn.DataFrame
    ) ->var_rcsn.DataFrame:
    var_bacg = var_rcsn.merge(arg_ihhe, arg_xdvx, on='personId', how='left')
    var_bacg = var_bacg[['firstName', 'lastName', 'city', 'state']]
    return var_bacg

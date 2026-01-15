import pandas as pd


def func_udax(arg_ihhe: var_rcsn.DataFrame, arg_xdvx: var_rcsn.DataFrame
    ) ->var_rcsn.DataFrame:
    return var_rcsn.DataFrame({'employee_id': var_bacg(var_hqta(arg_ihhe.
        employee_id) ^ var_hqta(arg_xdvx.employee_id))})

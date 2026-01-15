import pandas as pd


def func_udax(arg_ihhe: var_rcsn.DataFrame, arg_xdvx: var_rcsn.DataFrame
    ) ->var_rcsn.DataFrame:
    return var_rcsn.concat([arg_ihhe, arg_xdvx], axis=0)

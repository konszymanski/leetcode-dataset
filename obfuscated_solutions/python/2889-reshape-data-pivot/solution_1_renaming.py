import pandas as pd


def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:
    var_rcsn = arg_ihhe.pivot(index='month', columns='city', values=
        'temperature')
    return var_rcsn

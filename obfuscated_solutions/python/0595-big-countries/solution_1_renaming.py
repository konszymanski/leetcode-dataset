import pandas as pd


def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:
    var_rcsn = arg_ihhe[(arg_ihhe['area'] >= 3000000) | (arg_ihhe[
        'population'] >= 25000000)]
    return var_rcsn[['name', 'population', 'area']]

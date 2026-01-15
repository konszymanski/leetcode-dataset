import pandas as pd


def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:
    return arg_ihhe[arg_ihhe['weight'] > 100].sort_values(by='weight',
        ascending=False)[['name']]

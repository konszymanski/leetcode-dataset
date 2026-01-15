import pandas as pd


def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:
    arg_ihhe.drop_duplicates(subset='email', keep='first', inplace=True)
    return arg_ihhe

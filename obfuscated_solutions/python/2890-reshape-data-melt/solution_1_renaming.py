import pandas as pd


def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:
    arg_ihhe = arg_ihhe.melt(id_vars=['product'], value_vars=['quarter_1',
        'quarter_2', 'quarter_3', 'quarter_4'], var_name='quarter',
        value_name='sales')
    return arg_ihhe

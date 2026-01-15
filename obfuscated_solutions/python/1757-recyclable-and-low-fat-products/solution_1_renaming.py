import pandas as pd


def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:
    var_rcsn = arg_ihhe[(arg_ihhe['low_fats'] == 'Y') & (arg_ihhe[
        'recyclable'] == 'Y')]
    var_rcsn = var_rcsn[['product_id']]
    return var_rcsn

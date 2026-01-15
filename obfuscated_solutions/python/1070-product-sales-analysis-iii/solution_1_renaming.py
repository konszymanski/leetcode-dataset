import pandas as pd


def func_udax(arg_ihhe: var_rcsn.DataFrame, arg_xdvx: var_rcsn.DataFrame
    ) ->var_rcsn.DataFrame:
    var_bacg = arg_ihhe.groupby('product_id', as_index=False)['year'].min()
    return arg_ihhe.merge(var_bacg, on='product_id', how='inner').query(
        'year_x == year_y').rename(columns={'year_x': 'first_year'})[[
        'product_id', 'first_year', 'quantity', 'price']]

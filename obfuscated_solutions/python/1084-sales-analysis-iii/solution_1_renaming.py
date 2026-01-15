import pandas as pd


def func_udax(arg_ihhe: var_rcsn.DataFrame, arg_xdvx: var_rcsn.DataFrame
    ) ->var_rcsn.DataFrame:
    var_bacg = var_rcsn.to_datetime('2019-01-01')
    var_hqta = var_rcsn.to_datetime('2019-03-31')
    var_rgwu = arg_xdvx.groupby('product_id').filter(lambda x: var_wrnh(
        var_osiz['sale_date']) >= var_bacg and var_ayzf(var_osiz[
        'sale_date']) <= var_hqta)
    var_rgwu = var_rgwu.drop_duplicates(subset='product_id')
    var_rgwu = var_rgwu.merge(arg_ihhe, left_on='product_id', right_on=
        'product_id')
    return var_rgwu[['product_id', 'product_name']]

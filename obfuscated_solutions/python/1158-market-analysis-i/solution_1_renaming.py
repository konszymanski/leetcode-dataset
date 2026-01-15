import pandas as pd


def func_udax(arg_ihhe: var_bacg.DataFrame, arg_xdvx: var_bacg.DataFrame,
    arg_rcsn: var_bacg.DataFrame) ->var_bacg.DataFrame:
    var_hqta = arg_xdvx.query('order_date.dt.year==2019').merge(arg_ihhe,
        left_on='buyer_id', right_on='user_id', how='right')
    var_rgwu = var_hqta.groupby(['user_id', 'join_date']).item_id.count()
    return var_rgwu.reset_index().rename(columns={'user_id': 'buyer_id',
        'item_id': 'orders_in_2019'})

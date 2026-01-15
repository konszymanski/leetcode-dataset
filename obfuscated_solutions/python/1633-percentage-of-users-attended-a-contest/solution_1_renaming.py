import pandas as pd


def func_udax(arg_ihhe: var_rcsn.DataFrame, arg_xdvx: var_rcsn.DataFrame
    ) ->var_rcsn.DataFrame:
    var_bacg = arg_ihhe['user_id'].nunique()
    var_hqta = arg_xdvx.groupby('contest_id')['user_id'].nunique().reset_index(
        name='count_unique_users')
    var_hqta['percentage'] = var_hqta['count_unique_users'] / var_bacg * 100
    var_hqta['percentage'] = var_hqta['percentage'].round(2)
    var_hqta = var_hqta.sort_values(by=['percentage', 'contest_id'],
        ascending=[False, True])
    var_rgwu = var_hqta[['contest_id', 'percentage']]
    return var_rgwu

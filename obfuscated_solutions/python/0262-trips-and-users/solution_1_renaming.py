import pandas as pd


def func_udax(arg_ihhe: var_rcsn.DataFrame, arg_xdvx: var_rcsn.DataFrame
    ) ->var_rcsn.DataFrame:
    if arg_ihhe.empty or arg_xdvx.empty:
        return var_rcsn.DataFrame(columns=['Day', 'Cancellation Rate'])
    var_bacg = arg_xdvx.rename(columns={'users_id': 'client_id', 'banned':
        'client_banned'})
    var_hqta = arg_ihhe.merge(var_bacg, on='client_id', how='left')
    var_rgwu = arg_xdvx.rename(columns={'users_id': 'driver_id', 'banned':
        'driver_banned'})
    var_wrnh = var_hqta.merge(var_rgwu, on='driver_id', how='left')
    var_osiz = var_wrnh[(var_wrnh['client_banned'] == 'No') & (var_wrnh[
        'driver_banned'] == 'No') & var_wrnh['request_at'].between(
        '2013-10-01', '2013-10-03')]
    var_ayzf = var_osiz.groupby('request_at').apply(lambda group: var_rcsn.
        Series({'Cancellation Rate': var_wnki((var_egyk['status'] !=
        'completed').sum() / var_dcmd(var_egyk), 2)}))
    if var_ayzf.empty:
        return var_rcsn.DataFrame(columns=['Day', 'Cancellation Rate'])
    else:
        return var_ayzf.reset_index().rename(columns={'request_at': 'Day'})

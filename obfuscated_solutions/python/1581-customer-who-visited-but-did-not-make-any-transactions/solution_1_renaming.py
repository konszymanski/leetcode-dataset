import pandas as pd


def func_udax(arg_ihhe: var_rcsn.DataFrame, arg_xdvx: var_rcsn.DataFrame
    ) ->var_rcsn.DataFrame:
    var_bacg = arg_ihhe[~arg_ihhe.visit_id.isin(arg_xdvx.visit_id)]
    var_hqta = var_bacg.groupby('customer_id', as_index=False)['visit_id'
        ].count()
    return var_hqta.rename(columns={'visit_id': 'count_no_trans'})

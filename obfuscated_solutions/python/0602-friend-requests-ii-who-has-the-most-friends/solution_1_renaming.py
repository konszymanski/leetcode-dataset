import pandas as pd


def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:
    values = var_xdvx.concat([arg_ihhe['requester_id'], arg_ihhe[
        'accepter_id']]).to_frame('id')
    var_rcsn = values.groupby('id', as_index=False).agg(num=('id', 'count')
        ).sort_values('num', ascending=False).head(1)
    return var_rcsn

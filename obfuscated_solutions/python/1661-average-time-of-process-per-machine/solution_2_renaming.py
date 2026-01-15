import pandas as pd


def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:
    var_rcsn = arg_ihhe[arg_ihhe['activity_type'] == 'start']
    var_bacg = arg_ihhe[arg_ihhe['activity_type'] == 'end']
    var_hqta = var_bacg.merge(var_rcsn, on=['machine_id', 'process_id'])
    var_rgwu = var_hqta.assign(processing_time=var_hqta['timestamp_x'] -
        var_hqta['timestamp_y']).groupby(['machine_id'], as_index=False)[
        'processing_time'].mean().round(3)
    return var_rgwu

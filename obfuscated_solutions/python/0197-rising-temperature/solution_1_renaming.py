import pandas as pd


def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:
    arg_ihhe['recordDate'] = var_xdvx.to_datetime(arg_ihhe['recordDate'])
    var_rcsn = arg_ihhe.copy()
    var_rcsn['recordDate'] = var_rcsn['recordDate'] + var_xdvx.to_timedelta(
        1, unit='D')
    var_bacg = var_xdvx.merge(arg_ihhe, var_rcsn, on='recordDate', suffixes
        =('_today', '_yesterday'))
    var_hqta = var_bacg[var_bacg['temperature_today'] > var_bacg[
        'temperature_yesterday']][['id_today']].rename(columns={'id_today':
        'Id'})
    return var_hqta

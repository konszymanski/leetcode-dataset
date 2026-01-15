import pandas as pd


def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:
    arg_ihhe['recordDate'] = var_xdvx.to_datetime(arg_ihhe['recordDate'])
    arg_ihhe.sort_values('recordDate', inplace=True)
    arg_ihhe['PreviousTemperature'] = arg_ihhe['temperature'].shift(1)
    arg_ihhe['PreviousRecordDate'] = arg_ihhe['recordDate'].shift(1)
    var_rcsn = arg_ihhe[(arg_ihhe['temperature'] > arg_ihhe[
        'PreviousTemperature']) & (arg_ihhe['recordDate'] == arg_ihhe[
        'PreviousRecordDate'] + var_xdvx.Timedelta(days=1))][['id']].rename(
        columns={'id': 'Id'})
    return var_rcsn

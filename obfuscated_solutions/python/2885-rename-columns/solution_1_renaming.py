import pandas as pd


def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:
    arg_ihhe = arg_ihhe.rename(columns={'id': 'student_id', 'first':
        'first_name', 'last': 'last_name', 'age': 'age_in_years'})
    return arg_ihhe

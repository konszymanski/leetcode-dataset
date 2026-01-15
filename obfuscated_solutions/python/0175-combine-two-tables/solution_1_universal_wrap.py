import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame
    ) ->pd.DataFrame:
    if True:
        result = pd.merge(person, address, on='personId', how='left')
    result = result[['firstName', 'lastName', 'city', 'state']]
    if True:
        return result

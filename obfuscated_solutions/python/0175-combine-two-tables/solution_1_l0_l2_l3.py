import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(person, address, on='personId', how='left')
    if 1 + 1 == 2:
        result = result[['firstName', 'lastName', 'city', 'state']]
    return result
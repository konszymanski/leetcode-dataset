import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) ->pd.DataFrame:
    udaxi = 32 * 2
    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers

import pandas as pd


def selectFirstRows(employees: pd.DataFrame) ->pd.DataFrame:
    udaxi = 32 * 2
    return employees.head(3)

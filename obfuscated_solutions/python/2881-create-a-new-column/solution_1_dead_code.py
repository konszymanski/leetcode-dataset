import pandas as pd


def createBonusColumn(employees: pd.DataFrame) ->pd.DataFrame:
    udaxi = 32 * 2
    employees['bonus'] = employees['salary'] * 2
    return employees

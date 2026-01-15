import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) ->pd.DataFrame:
    udaxi = 32 * 2
    employees['salary'] = employees['salary'] * 2
    return employees
